# Capacity and cost envelope

[![Investment worksheet](../diagrams/rendered/v07-investment-scorecard.png)](../diagrams/rendered/v07-investment-scorecard.png)

Every amount and load below is a **planning assumption**, not a quote, benchmark or business forecast. The brief gives attendance goals but no event rates, staffing budget or return per visitor. [Inputs](cost-inputs.json) are canonical; `python validation/scripts/calculate_costs.py` writes the [calculated result](../validation/results/cost-model.json). Amounts are EUR; tax, financing, existing estate operating costs and physical ride/enclosure construction are excluded. The model includes hardware, delivery and operations.

## Load and field constraints

| Calculation | Result | Design implication |
|---|---|---|
| 350 sensors, one 500-byte observation every 10 seconds | 35 events/s | Modest average ingestion; capacity must include concurrent backlog replay. |
| Above load × 72 hours disconnected | 4.536 GB across the estate | 181.44 MB per gateway on an even 25-gateway split; 362.88 MB with 2× headroom. This is not the worst gateway's storage bound. |
| 15,000 visits × 20 API calls / 10 opening hours | 8.33 requests/s average; 83.33 at assumed 10× burst | Load-test realistic endpoint mixes and upstream limits; do not infer safe admission throughput. |
| 15,000 arrivals in one hour | 4.167 people/s | 12 lanes taking five seconds each process only 2.4 people/s: redesign staffing/arrival distribution before claiming target capacity. |
| 40 vibration sensors × 3 axes × 2 bytes × 1 kHz | 20.736 GB raw data/day | Compute validated features locally and retain bounded diagnostic windows; do not stream everything by default. |

The telemetry calculation excludes camera/video, indexes, SQLite WAL, filesystem reserve, retransmission overhead and prolonged backlogs. The chosen 1 KiB application-event maximum is not the assumed 500-byte average. Allocate each gateway by its actual sensor count, observed encoding and outage requirement; measure disk write amplification and worst-case backlog. Reserve disk independently for critical observations, protect the database from filling the OS volume, and alarm before the limit. On overload reject explicitly and escalate loss visibility. No design can retain unbounded data in finite storage.

Cameras are a provisional 60-device survey assumption, not continuous cloud-video upload. Begin with consented/authorized diagnostic samples appropriate to the animal task, local capture quality checks, and bounded retention. Network feasibility needs a radio/power/site survey; protocol choice is not coverage evidence.

## Base cost model

| One-off item | Assumption | EUR |
|---|---|---:|
| Hardware, gateways, networking, spares | Provisional installation envelope | 34,750 |
| Software delivery | 180 person-days × 650 | 117,000 |
| Installation | 30 person-days × 450 | 13,500 |
| Training | 12 person-days × 450 | 5,400 |
| Data preparation | 30 person-days × 350 | 10,500 |
| Specialist review | 10 person-days × 800 | 8,000 |
| Subtotal | | 189,150 |
| Contingency | 20% of one-off subtotal | 37,830 |
| One-off total | | **226,980** |

| Monthly item | EUR |
|---|---:|
| Application, database and backups | 1,200 |
| Event ingestion and storage | 450 |
| AI usage allowance | 650 |
| Cellular backhaul | 350 |
| Support/operations allocation | 4,500 |
| Replacement reserve | 300 |
| Service licenses | 250 |
| **Total per month** | **7,700** |

At 36 months the full-capacity sensitivity total is **EUR 504,180**. Uniform 0.8× and 1.4× sensitivity gives EUR 403,344 and EUR 705,852. These are arithmetic stress cases, not confidence bounds; correlated salary, vendor, scope and data costs need separate estimates. The monthly AI allowance is an expected planning allocation, not the USD 50/day hard spend ceiling. A planning conversion of USD 1 = EUR 0.90 would put a fully used 30-day ceiling at EUR 1,350, exceeding the allowance; alerts must track both forecast allocation and hard cap. No live exchange-rate claim is made.

## Recovery archive

Seven days of acknowledged summary events adds 10.584 GB estate-wide. With the pending 72-hour envelope, total is 15.12 GB before headroom. An even 25-gateway split with 2× headroom is 1,209.6 MB/gateway before indexes/WAL, OS reserve, skew and large evidence. Archive expiry never evicts accepted pending records.

### Staged investment and independent stop decisions

The immediate proposal is an **eight-week pilot capped at EUR 37,800**, allocated within the overall program. All amounts are planning estimates, not supplier quotes or approved spending. The pilot includes discovery, one admission domain, four active gateways plus one spare, 24 sensors, capture-only care drafts, a visitor-assistant sandbox and two experimental camera positions.

| Pilot package | One-off including 20% contingency | Two-month operation | Ceiling | What remains if stopped |
|---|---:|---:|---:|---|
| Operational foundation | 25,200 | 3,240 | **28,440** | Local admissions, structured observations, replay and search remain the primary deliverable |
| Visitor assistant experiment | 6,000 | 240 | **6,240** | Approved search, filters and static information remain available |
| Camera feasibility experiment | 3,000 | 120 | **3,120** | Keeper records and manual observation remain available |
| **Pilot total** | **34,200** | **3,600** | **37,800** | Stop either experiment independently |

The foundation allocation comprises EUR 4,750 hardware/networking, 18 delivery days, four installation days, two training days, three data-preparation days and one specialist day. The assistant uses six delivery days, two data days and half a specialist day. The camera trial uses EUR 1,000 hardware, one delivery day, one installation day and half a specialist day. These reconcile to the original 25/5/2/5/2 pilot person-day totals. Shared delivery tools and existing staff availability are assumptions; if supplier integration cannot fit, narrow the pilot before approval rather than silently increase scope.

| Stage | Months | One-off allocation | Monthly operating estimate | Release condition |
|---|---:|---:|---:|---|
| Pilot | 1–2 | 34,200 | 1,800 | Fund only the bounded scope above |
| Foundation | 3–4 | 50,000 | 3,000 | Useful local admission and records; recovery and workload acceptable |
| Insight | 5–8 | 60,000 | 4,500 | Measurable capture quality and manager use; replace installation assumptions with estimates |
| AI release gates | 9–12 | 50,000 | 6,000 | Promote useful evaluated capabilities; exclude failed experiments from subsequent scope |
| Conditional expansion | 13–36 | 32,780 | 7,700 | Finance-reviewed contribution case and sustainable staffing/support |

The one-off allocations sum to EUR 226,980 and include the pilot; do not add it again. Staged operation totals EUR 236,400, producing **EUR 463,380 over 36 months** if every stage is funded. The all-months-at-full-capacity calculation provides a conservative sensitivity case: **EUR 504,180**, EUR 40,800 above the staged case. Neither is an unconditional commitment or a confidence interval.

Under the explicitly assumed month-13 benefit start, 24 months of contribution at EUR 5,000 / 12,000 / 18,000 yields EUR 120,000 / 288,000 / 432,000. Against staged costs, net differences are **−343,380 / −175,380 / −31,380**. Staged break-even requires approximately **EUR 19,307.50 incremental contribution per benefit month**. The full-capacity sensitivity case requires EUR 21,007.50. These scenarios do not establish payback; earlier operational benefits are deliberately not monetized without a basis.

The pilot purchases information needed for the next decision: whether reliable capture reduces rework, whether usable local admissions can be supported, whether visitors complete tasks more easily than with search, and whether cameras can observe a meaningful quantity. The operations lead evaluates foundation value separately from model results. Finance must replace cost and contribution assumptions with supplier/support estimates, margins, adoption and seasonality before expansion. Welfare and continuity benefits may justify some spending, but are not assigned invented monetary values.

### Selected admission demand policy

Retain twelve lanes as a **planning assumption** and use timed entry capped at **1,500 people per fifteen-minute slot**, including walk-ups. At the simplified five-second service time, theoretical slot capacity is 2,160 people; the selected cap leaves approximately 31% headroom. Scheduling 15,000 people at that cap takes at least 2.5 hours, rather than promising to admit them all in one hour. Tickets count people/party allowance, not just QR scans. Preserve accessible lanes and a separate exception desk; do not route long exception handling through ordinary lanes.

The entrance supervisor owns the release cap. Before launch, measure full passage times and bursts, confirm safe queue space and check party/re-entry behavior. Proposed acceptance: under the agreed arrival profile, p95 queue wait below ten minutes, no overflow of domain-approved queue capacity, and sustainable staffing. These are unmeasured operating targets. When lanes fail, reduce future slot releases according to remaining effective capacity, communicate delays for already booked arrivals and use the staffed queue plan. API latency alone cannot satisfy this gate. Timed-entry controls are a ticket-supplier selection requirement; a supplier that cannot enforce the cap needs a scoped integration or a revised decision.
