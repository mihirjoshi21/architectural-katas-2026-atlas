import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPIKE = ROOT / 'spikes/edge-replay'
sys.path.insert(0, str(SPIKE))
from replay import Edge, Destination, CapacityError, IdentityConflict, replay

class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.edge_path = Path(self.tmp.name)/'edge.db'
        self.dest_path = Path(self.tmp.name)/'dest.db'
        self.edge=Edge(self.edge_path); self.dest=Destination(self.dest_path)
    def tearDown(self):
        self.edge.close(); self.dest.close(); self.tmp.cleanup()
    def test_lost_final_receipt_retries_without_second_effect(self):
        self.edge.accept('e1', {'value': 8})
        replay(self.edge,self.dest,lose_receipts_for={'e1'})
        self.assertEqual(self.edge.count(),1)
        self.assertEqual(self.dest.counts(),{'inbox':1,'effects':1})
        replay(self.edge,self.dest)
        self.assertEqual(self.edge.count(),0)
        self.assertEqual(self.dest.counts(),{'inbox':1,'effects':1})
    def test_committed_record_survives_abrupt_process_exit(self):
        self.edge.close()
        code="import sys,os;sys.path.insert(0,sys.argv[1]);from replay import Edge;e=Edge(sys.argv[2]);e.accept('committed',{'v':42});os._exit(23)"
        r=subprocess.run([sys.executable,'-c',code,str(SPIKE),str(self.edge_path)],capture_output=True,text=True)
        self.assertEqual(r.returncode,23,r.stderr)
        self.edge=Edge(self.edge_path)
        self.assertEqual(self.edge.pending()[0]['event_id'],'committed')
        replay(self.edge,self.dest)
        self.assertEqual(self.dest.counts()['effects'],1)
    def test_destination_transaction_rolls_back_inbox_and_effect(self):
        self.edge.accept('e1', {'value': 8})
        event=self.edge.pending()[0]
        with self.assertRaises(RuntimeError):self.dest.receive(event,fail_before_effect=True)
        self.assertEqual(self.dest.counts(),{'inbox':0,'effects':0})
        self.assertEqual(self.edge.count(),1)
        replay(self.edge,self.dest)
        self.assertEqual(self.dest.counts(),{'inbox':1,'effects':1})
    def test_same_identity_different_content_is_rejected_at_both_ends(self):
        self.edge.accept('e1',{'value':8})
        with self.assertRaises(IdentityConflict):self.edge.accept('e1',{'value':9})
        self.dest.receive(self.edge.pending()[0])
        with self.assertRaises(IdentityConflict):self.dest.receive({'event_id':'e1','payload':{'value':9},'priority':2})
        self.assertEqual(self.dest.counts()['effects'],1)
    def test_priority_then_insertion_order_without_global_clock_claim(self):
        self.edge.accept('low',{'v':1},3);self.edge.accept('high-a',{'v':2},1)
        self.edge.accept('middle',{'v':3},2);self.edge.accept('high-b',{'v':4},1)
        self.assertEqual(replay(self.edge,self.dest),['high-a','high-b','middle','low'])
    def test_full_quota_rejects_without_false_acceptance(self):
        self.edge.max_records=1;self.edge.accept('e1',{'v':1})
        with self.assertRaises(CapacityError):self.edge.accept('e2',{'v':2})
        self.assertEqual(self.edge.count(),1)
        self.assertFalse(self.edge.accept('e1',{'v':1}))
    def test_oversize_event_is_not_accepted(self):
        with self.assertRaises(ValueError):self.edge.accept('huge',{'value':'x'*1100})
        self.assertEqual(self.edge.count(),0)
    def test_carrier_receipt_cannot_delete_source(self):
        self.edge.accept('e1',{'v':1})
        with self.assertRaises(ValueError):self.edge.acknowledge({'kind':'carrier-custody','event_id':'e1','digest':'x'})
        self.assertEqual(self.edge.count(),1)
    def test_wrong_content_receipt_cannot_delete_source(self):
        self.edge.accept('e1',{'v':1})
        with self.assertRaises(IdentityConflict):self.edge.acknowledge({'kind':'destination-committed','event_id':'e1','digest':'wrong'})
        self.assertEqual(self.edge.count(),1)
    def test_repeated_receipt_is_idempotent(self):
        self.edge.accept('e1',{'v':1});receipt=self.dest.receive(self.edge.pending()[0])
        self.assertTrue(self.edge.acknowledge(receipt));self.assertFalse(self.edge.acknowledge(receipt))
    def test_destination_dedupe_survives_reopen(self):
        self.edge.accept('e1',{'v':1});event=self.edge.pending()[0]
        self.dest.receive(event);self.dest.close();self.dest=Destination(self.dest_path)
        self.dest.receive(event)
        self.assertEqual(self.dest.counts(),{'inbox':1,'effects':1})
    def test_limited_batch_leaves_other_records_pending(self):
        for i in range(3):self.edge.accept(str(i),{'v':i})
        replay(self.edge,self.dest,limit=2)
        self.assertEqual(self.edge.count(),1);self.assertEqual(self.dest.counts()['effects'],2)

if __name__=='__main__':unittest.main()
