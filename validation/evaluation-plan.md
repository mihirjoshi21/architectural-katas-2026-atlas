# Evaluation plan

## Evidence discipline

**Specified** means a method is documented. **Implemented** means runnable code exists. **Executed** means an actual run is recorded. **Field validated** requires representative site/hardware/domain evidence. A simulator cannot establish field validation. Current results are in [the evidence index](evidence-index.md).

| ID | Method and challenge | Evidence / decision | Current status |
|---|---|---|---|
| V01 | WAN-style delivery interruption, process exit after commit, lost receipt, retry/duplicate, identity conflict, transaction failure, priority, quota and oversize | Account for accepted IDs; atomic inbox/effect; no false acceptance. Physical power/free-disk/concurrency tests later | Narrow local replay experiment implemented/executed; field/network behavior specified. |
| V02 | Ticket tamper/expiry, unknown keys, party size, re-entry, concurrent local redemption, isolated gate, stale revocation and refund reconciliation | Correct policy, clear exceptions and residual partition risk; measure target-hardware latency | Specified; ticket integration not implemented. |
| V03 | Missing/wrong-role/expired/replayed care approval, changed task version, two reviewers, duplicate execution, reviewer unavailable | Role/action/version checked; one permitted effect; urgent escalation independent | Specified; needs integrated workflow and domain review. |
| V04 | Concurrent near-budget calls, deadline, 429/5xx, partial/malformed response, failed budget authority, changed provider | Atomic reservations, bounded retries and useful fallback; price/model/contract versions recorded | Specified; no live provider calls measured. |
| V05 | Assistant versus FAQ/search on ordinary, unknown, stale, adversarial, multilingual and accessibility tasks | Human-supported source/constraint/task quality, cost and latency; evaluate updates before promotion | 48 concrete synthetic cases and source fixtures specified; 18 narrow deterministic policy tests executed; no model score reported. |
| V06 | Animal count/anomaly and maintenance models on representative held-out data; poor sensor/footage/unknown-asset slices | Separate per-use metrics, error uncertainty and review workload; shadow then human promotion | Specified; no real training/evaluation dataset supplied. |
| V07 | Sample zone observations against manual counts, missing coverage, freshness and manager walkthrough | Coverage and error visible; measure usefulness of a real staff decision | Specified; field measurement required. |
| V08 | Visitor/API arrival profiles, physical gate throughput, telemetry/replay capacity, backup/restore and business scenarios | Measured load/resources/recovery; cost sensitivity; separate physical capacity from API speed | Arithmetic executed; deployment/load/restore/business outcomes not measured. |

## AI acceptance specification

### Release decisions and proposed acceptance rules

These are selected **pilot decision rules**, not measured performance or domain certification. Owners may tighten them before evaluation, recording the reason; they must not relax them after seeing failures merely to pass a candidate.

| Gate | Accountable role | Measure and proposed acceptance rule | Failure decision |
|---|---|---|---|
| G1 Foundation continuity | Operations lead + platform owner | Account for every accepted ID in outage/replay and restore exercises; duplicate delivery creates no second digital effect; incomplete admission recovery stays in exception mode; capture expiry routes to usable manual records | Fix foundation before adding operational scope |
| G2 Assistant policy and quality | Visitor product owner + independent knowledge reviewer | Freeze 48 cases and materialized fixtures; run each three times per candidate configuration. No high-consequence constraint, privacy or authority violation; at least 90% task-pass rate overall and report each category separately | Retain search; correct failures and evaluate a fresh held-out set |
| G3 Assistant usefulness | Visitor product owner | Eight representative adult participants, six counterbalanced activity-discovery tasks each, using assistant and search on matched task variants with identical information. At least 90% task completion; no lower completion than search; median successful-task time at least 20% lower than search. Record mistakes, confidence and accessibility feedback | Stop incremental assistant release if it offers no useful improvement |
| G4 Assistant resources | Platform/model owner | T03 p95 under four seconds, five-second end-to-end deadline; provider maximum charge can be reserved; measured average daily spend fits the planned allowance and USD 50/day ceiling under the declared workload | Reduce usage/scope or keep search; do not bypass the cap |
| G5 Additional language | Knowledge owner + fluent reviewer | Repeat relevant tasks with the candidate locale; preserve facts, restrictions and meaningful handoff; no critical mistranslation on the reviewed set | Keep that language disabled; English/help fallback remains |
| G6 Animal observation feasibility | Animal-care lead | Two-reviewer visible-count reference can be established; pre-record count/undercount tolerance, coverage and review-time limit before held-out scoring; no claim of enclosure total without independent reference | Stop camera/model trial independently; retain structured records |
| G7 Maintenance readiness | Maintenance lead | Defined event and useful warning horizon, reviewed time/asset-separated labels, pre-recorded false-alert/lead-time limits and benefit against inspection/threshold baseline | Continue inspections and data collection; no predictive deployment |
| G8 Admission demand | Entrance operations lead | Under validated timed-entry arrivals, p95 queue wait below ten minutes, no overflow of domain-approved queue space, sustainable accessible-lane/staff provision | Reduce slot allocation and remediate passage/queue design |
| G9 Expansion investment | Finance + operations | Replace illustrative supplier/support assumptions; fund only capabilities with justified incremental contribution or explicitly accepted nonfinancial value | Stop or narrow expansion; do not assume the full envelope is approved |

G2's 48 cases are a small development/release contract, not a statistically representative population sample. Three repetitions expose some variability but do not establish a failure-rate bound. G3 is a directional usability pilot, not a statistically powered causal study. Counterbalance order and task variants; do not show the same answer twice and count recall as product benefit. A participant may stop a task; count failure/abandonment in completion, rather than excluding it to improve results. The time measure uses successful matched pairs, with excluded pairs and task-completion rates reported alongside it.

### Case execution and scoring

Each case references `visitor-fixture.json`, a frozen evaluation time, exact per-case overrides and an oracle containing required facts, source IDs, forbidden claims and the expected decision class. Materialize dot-path overrides before execution; document arrays are addressed by document ID. The fixture checker resolves every reference/override and checks that no model result has been populated. Multilingual cases contain separate public-fallback and trial-locale expectations. Synthetic fixtures are not field ground truth.

For each model run, record case ID, fixture hash, provider/model and prompt version, retrieved IDs/versions, confirmed constraints, candidate, final rendered output, latency, billed/reserved cost and the reviewer decision. Task pass requires the expected decision class, all applicable required facts, no forbidden claims and correct sources. Score source support, constraint respect and appropriate abstention separately; no single model-judge score substitutes for this rubric. Evaluate retrieval selection and language interpretation separately from the deterministic output checks. A fluent reviewer evaluates enabled translations.

Freeze a held-out set before prompt tuning. The included 48 cases are an initial public contract; create additional held-out variants for release so optimizing to published cases cannot masquerade as generalization. Any high-consequence failure blocks promotion even when aggregate task completion passes. Investigate, add a regression, and repeat affected plus critical cases after changes. Source/corpus changes rerun retrieval and grounding checks; schema/tool/provider changes rerun the full relevant contract.

## Model and knowledge lifecycle

Version input schema, label source, split, feature pipeline, model, prompt, tools and approved corpus. Review evaluation and operational cost; shadow or canary a candidate; monitor drift, missed/false alerts, unsupported answers and workload; roll back to the last evaluated version or baseline. Model-provider replacements repeat relevant evaluations. A changed price can reduce the permissible use rate and must update the reservation model.

## Proposed field experiments

One surveyed gate domain, four active pilot gateways plus one spare, a small representative ride/enclosure sample chosen with staff. Obtain baseline feeding/population/maintenance and popularity measurements before claiming benefit. Exercise local network, WAN, power and storage failure as different scenarios; document participants, procedure, observed outcomes and limits. Domain-led physical/clinical approval is required before consequential deployment.

Recovery integration exercises must additionally cover seven-day archive expiry/range replay after cloud restore, capture-only offline roles, stale drafts on reconnect and fenced admission recovery with an incomplete journal. These are specified, not covered by the current replay spike.

## Business, migration and production acceptance scenarios

| Scenario | Observable acceptance condition | Evidence status |
|---|---|---|
| Save plan without reminder permission; withdraw while delivery queued | Plan persists if requested; no message without a current grant; queued delivery suppressed after withdrawal; repeated request does not send twice | Specified; supplier/account integration required |
| Future plan reopened after an activity closure | Saved interest remains labelled as a plan; current closure/access and dated checkout capacity are revalidated | Specified; visitor workflow integration required |
| Return cohort with partial follow-up, refunds and same-day re-entry | Count only eligible linked accounts with full follow-up and actual later-date admission; report exclusions and unlinked visits separately | Specified; no retention uplift measured |
| Counter misses groups, resets or loses data | Compare shift sample with manual reference; at most max(2 entries, 10% error) under proposed gate; preserve reset identity; exclude low-coverage hours rather than enter zeros | Specified; field count calibration required |
| Import with mismatched allowances or ambiguous animal balances | Quarantine mismatch, preserve source record and mapping; no authority cutover until reconciliation | Specified; incumbent discovery required |
| Production model remains structurally valid but produces irrelevant options | Daily human task sample detects the failure; incident owner can pause canary and restore search; affected regression cases added | Specified; no model/user result claimed |
| Provider price unknown or supplier shuts down | No new unbounded-cost call; search remains usable; replacement cannot bypass evaluation | Specified; controlled provider integration exercise required |

Foundation field gates include calibrated popularity and usable records; AI go-live additionally requires reviewed production monitoring. Return-plan and reminder effectiveness are measured after sufficient cohort follow-up, independently of the initial policy test results.
