# Accepted records and idempotent replay

This deliberately small experiment supports ADR-002 and ADR-009. It uses two local SQLite databases with WAL/FULL synchronous commits, one edge outbox and one destination inbox/effect transaction. No packages beyond Python's standard library are required.

From the repository root:

```bash
python spikes/edge-replay/demo.py
python -m unittest discover -s validation/tests -v
```

The demo accepts 20 synthetic records, delivers all, loses two receipts, and retries. The destination still has 20 effects and the edge has zero pending records after final receipts. Tests also inject failure between destination inbox/effect writes, terminate a writer process after commit, reopen databases, attempt conflicting event identity, exercise priority/batching, reject oversized/full-quota input and reject carrier/wrong-hash receipts.

This proves only the observed local software behavior. `max_records` is a logical acceptance quota, not a real free-disk or disk-wear manager. Priority is stable insertion order within a class, not global causal order. Authenticated receipts, device source identity, broker persistence, networking, concurrency load, physical power-loss durability and cloud deployment are **not implemented**. A receipt's kind/hash check is not cryptographic authentication. Never expose this example as a production ingestion endpoint.

[Actual results and evidence status](../../validation/evidence-index.md)
