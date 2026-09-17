"""Bounded local experiment: accepted outbox records and atomic receipt/effect.
Not production transport, device authentication, physical safety, or a disk quota.
"""
from contextlib import contextmanager
import hashlib
import json
import sqlite3

class CapacityError(RuntimeError): pass
class IdentityConflict(ValueError): pass

def encode(event_id, payload, priority=2):
    if not isinstance(event_id, str) or not event_id or len(event_id) > 128:
        raise ValueError('event_id must be a nonempty string of at most 128 characters')
    if type(priority) is not int or priority not in (1, 2, 3):
        raise ValueError('priority must be 1, 2 or 3')
    if not isinstance(payload, dict):
        raise ValueError('payload must be an object')
    raw = json.dumps({'event_id': event_id, 'priority': priority, 'payload': payload},
                     sort_keys=True, separators=(',', ':'), allow_nan=False)
    if len(raw.encode('utf-8')) > 1024:
        raise ValueError('serialized event exceeds experiment limit of 1024 bytes')
    return raw, hashlib.sha256(raw.encode('utf-8')).hexdigest()

def connect(path):
    db = sqlite3.connect(path, isolation_level=None, timeout=5)
    db.execute('PRAGMA journal_mode=WAL')
    db.execute('PRAGMA synchronous=FULL')
    db.execute('PRAGMA foreign_keys=ON')
    return db

@contextmanager
def transaction(db):
    db.execute('BEGIN IMMEDIATE')
    try:
        yield
        db.execute('COMMIT')
    except BaseException:
        db.execute('ROLLBACK')
        raise

class Edge:
    def __init__(self, path, max_records=10000):
        if type(max_records) is not int or max_records < 1:
            raise ValueError('positive max_records required')
        self.max_records = max_records
        self.db = connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS outbox ('
                        'seq INTEGER PRIMARY KEY AUTOINCREMENT, event_id TEXT UNIQUE NOT NULL, '
                        'body TEXT NOT NULL, digest TEXT NOT NULL, priority INTEGER NOT NULL)')

    def accept(self, event_id, payload, priority=2):
        raw, digest = encode(event_id, payload, priority)
        with transaction(self.db):
            old = self.db.execute('SELECT digest FROM outbox WHERE event_id=?', (event_id,)).fetchone()
            if old:
                if old[0] != digest: raise IdentityConflict('same identity has different content')
                return False
            if self.count() >= self.max_records: raise CapacityError('record quota full; record NOT accepted')
            self.db.execute('INSERT INTO outbox(event_id,body,digest,priority) VALUES(?,?,?,?)',
                            (event_id, raw, digest, priority))
        # Application acceptance happens only after the transaction commits.
        return True

    def pending(self, limit=100):
        if type(limit) is not int or limit < 1: raise ValueError('positive limit required')
        return [json.loads(r[0]) for r in self.db.execute(
            'SELECT body FROM outbox ORDER BY priority,seq LIMIT ?', (limit,))]

    def acknowledge(self, receipt):
        if receipt.get('kind') != 'destination-committed':
            raise ValueError('carrier custody is not a final destination receipt')
        with transaction(self.db):
            row = self.db.execute('SELECT digest FROM outbox WHERE event_id=?', (receipt['event_id'],)).fetchone()
            if row is None: return False
            if row[0] != receipt['digest']: raise IdentityConflict('receipt does not match accepted content')
            self.db.execute('DELETE FROM outbox WHERE event_id=?', (receipt['event_id'],))
        return True

    def count(self): return self.db.execute('SELECT COUNT(*) FROM outbox').fetchone()[0]
    def close(self): self.db.close()

class Destination:
    def __init__(self, path):
        self.db = connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS inbox(event_id TEXT PRIMARY KEY,digest TEXT NOT NULL)')
        self.db.execute('CREATE TABLE IF NOT EXISTS effects(event_id TEXT PRIMARY KEY,body TEXT NOT NULL,'
                        'FOREIGN KEY(event_id) REFERENCES inbox(event_id))')

    def receive(self, event, fail_before_effect=False):
        raw, digest = encode(event['event_id'], event['payload'], event['priority'])
        with transaction(self.db):
            old = self.db.execute('SELECT digest FROM inbox WHERE event_id=?', (event['event_id'],)).fetchone()
            if old:
                if old[0] != digest: raise IdentityConflict('destination identity/content conflict')
            else:
                self.db.execute('INSERT INTO inbox VALUES(?,?)', (event['event_id'], digest))
                if fail_before_effect: raise RuntimeError('injected failure between inbox and effect')
                self.db.execute('INSERT INTO effects VALUES(?,?)', (event['event_id'], raw))
        return {'kind': 'destination-committed', 'event_id': event['event_id'], 'digest': digest}

    def counts(self):
        return {t: self.db.execute('SELECT COUNT(*) FROM '+t).fetchone()[0] for t in ('inbox','effects')}
    def close(self): self.db.close()

def replay(edge, destination, lose_receipts_for=(), limit=100):
    processed = []
    for event in edge.pending(limit):
        receipt = destination.receive(event)
        processed.append(event['event_id'])
        if event['event_id'] not in lose_receipts_for: edge.acknowledge(receipt)
    return processed
