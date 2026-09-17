# Evidence index

This package distinguishes documentation, a small implemented experiment and future estate validation. No AI quality score, field uptime, financial return or human approval is claimed.

| Evidence | Artifact | Interpretation |
|---|---|---|
| Replay implementation | [Source and instructions](../spikes/edge-replay/README.md) | Small SQLite model of acceptance, destination transaction and final receipt |
| Twelve focused tests | [Actual test output](results/unit-tests.txt), [run record](results/run-record.json) | Executed locally; process exit, retry, conflict, transaction rollback, priority and bounded acceptance |
| Lost-receipt scenario | [Actual demo output](results/replay-demo.json) | Twenty events, two lost receipts, twenty effects after retry; no duplicate business effect |
| Cost/capacity arithmetic | [Inputs](../design/cost-inputs.json), [results](results/cost-model.json) | Reproducible calculations from illustrative assumptions; no empirical forecast |
| Repository checks | [Actual check output](results/repository-checks.txt) | Local links, file formats, diagram/ADR presence and requirement IDs |
| Visitor policy checks | [Eighteen test results](results/visitor-policy-tests.txt), [policy source](../spikes/visitor-policy/policy.py) | Executed deterministic checks against hand-authored candidates; not a model benchmark |
| Visitor fixtures | [Integrity result](results/visitor-fixture-checks.txt), [48 cases](datasets/visitor-scenario-specifications.json), [corpus](datasets/visitor-fixture.json) | Concrete sources, overrides and oracles resolve; no model results populated |
| Model/user evaluation | [Release contract](evaluation-plan.md) | Specified only; model and user task quality remain unmeasured |
| Field behavior | [Failure modes](../design/degraded-modes.md) | Specified only; site coverage, physical power/storage endurance and integrated restore untested |

## Replay evidence boundary

The spike has no MQTT client, real WAN, ticket vendor, cloud database, provider model, authenticated transport or animal-care implementation. The local test explicitly terminates a child process after a committed insert; this is a process-failure test, not a physical power-cut experiment. Its logical row quota is not a filesystem-full simulation. The tests do not establish sustained load, concurrency behavior or durability of a particular device. Production sequencing, quarantine, security and operational policies need their own implementation and validation.

Rerun the replay and visitor-policy checks using the commands in their linked experiment instructions; the other commands are in the run record. The recorded Python/SQLite versions and source hashes identify what produced the sample results. A later source edit requires rerunning the applicable tests; the recorded run is not a certification of arbitrary future changes. CI runs checks after push but no remote CI run is claimed by this ZIP.

## Diagram review

All fourteen generated exports were reviewed together for coverage and layout, with detailed inspection of selected views. Native draw.io XML, suitable Mermaid specifications and vector/PNG exports are included. The views represent the proposed architecture, not a surveyed site or an implemented product. Automated structure checks cannot establish the correctness of a care policy or a drawing's domain meaning.

The seven-day recovery archive, care role synchronization and fenced authority recovery are design extensions beyond the bounded replay implementation; no integrated result is claimed for them. The 48 visitor cases include concrete fixtures and review oracles. The 18 deterministic policy tests are executed separately; there are no model or user-study results.
