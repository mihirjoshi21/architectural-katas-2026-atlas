"""Generate observed demonstration output; no internet or third-party packages."""
from pathlib import Path
import json
import tempfile
from replay import Edge, Destination, replay

def main():
    with tempfile.TemporaryDirectory() as folder:
        edge=Edge(Path(folder)/'edge.db');dest=Destination(Path(folder)/'dest.db')
        for i in range(20):edge.accept(f'event-{i:03}',{'observation':i},1 if i%5==0 else 2)
        accepted=edge.count()
        replay(edge,dest,lose_receipts_for={'event-000','event-005'})
        pending_after_loss=edge.count();effects_first=dest.counts()['effects']
        replay(edge,dest)
        report={'accepted_events':accepted,'destination_effects_after_first_delivery':effects_first,
                'pending_after_two_lost_receipts':pending_after_loss,'pending_after_retry':edge.count(),
                'destination_final':dest.counts(),
                'scope':'Local SQLite software experiment; no network, MQTT, power-cut, model or field proof.'}
        assert accepted==20 and effects_first==20 and pending_after_loss==2 and edge.count()==0
        assert dest.counts()=={'inbox':20,'effects':20}
        edge.close();dest.close();print(json.dumps(report,indent=2))
if __name__=='__main__':main()
