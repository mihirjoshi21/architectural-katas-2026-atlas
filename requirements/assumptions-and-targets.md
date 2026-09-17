# Assumptions and proposed targets

None of the values below is a measured estate SLA or organizer requirement. They are explicit planning choices to test. Targets apply to the specified boundary, not every end-to-end workflow.

| ID | Assumption / target | Owner and validation |
|---|---|---|
| A01 | One estate; existing safe physical procedures continue while digital capabilities are piloted | Architecture lead confirms with brief/operations. |
| A02 | Staff and admission local networks can be provisioned at pilot sites; WAN can fail independently | Network owner surveys links and capacity. |
| A03 | 72-hour WAN outage design envelope for buffered operational summaries; power and local sensor links available | Edge owner sizes per gateway and tests on hardware; not a guarantee for destroyed disks. |
| A04 | Full rollout 25 active gateways + 5 spares; pilot 4 + 1 | Field inventory/site survey can change counts and costs. |
| A05 | Full sensor planning case: 240 ride sensors + 110 environmental sensors; 60 cameras considered, subject to a pilot | Not counts from the brief; validate useful placement and camera processing costs. |
| A06 | Summary events ≤1,024 bytes at ingress, usually about 500 bytes; bulk/footage uses a separate object pathway | Schema and workload checks. MQTT protocol does not impose this application limit. |
| A07 | Full-plan workload: 15,000 visits/day, ten opening hours, 20 API calls/visit, 10× API burst factor | Measure arrival/API distributions; physical gate model separate. |
| T01 | Staff/visitor operational APIs p95 <300 ms server response under agreed load, excluding external payment/model delay | Load test with declared concurrency and data size. |
| T02 | Local ticket validation + redemption p95 <250 ms, excluding human passage and exceptional review | Target hardware and multi-lane workflow test. |
| T03 | Assistant final answer p95 <4 s in normal operation; request deadline 5 s followed by information fallback | Measure full chain, provider delays, retrieval and retries. |
| T04 | Current queue/status data age ≤2 min when connected; mark older data stale, never assert current availability from it | Freshness integration tests and field updates. |
| T05 | Cloud business records initial RPO ≤15 min and RTO ≤4 h through backup/restore; availability target 99.5% per calendar month | Proposed service objectives, to ratify and test; current scope does not promise zero cloud record loss. |
| T06 | Initial AI cloud budget $50/day in UTC, with atomic maximum-cost reservation and fail-closed cloud calls | Model pricing, caps and currency conversion are versioned; requires integrated test. |
| A08 | Animal and maintenance labels are unavailable until inventoried, digitized and reviewed | Model owner establishes data readiness; no predictive performance assumed. |
| A09 | Clinical, containment, emergency-response and capacity thresholds require domain authority | Keeper/vet and competent physical-system specialists approve actual procedures. |
| A10 | One entrance redemption authority; isolated gates use staffed exception procedure | Operations agrees the lost-throughput/fraud trade-off. |
| A11 | EUR is the planning currency; illustrative conversion 1 USD = EUR 0.90, not a live quote | Finance updates with dated rates and supplier estimates. |
| A12 | Proposed observation retention: summaries 90 days, aggregates 13 months, AI request diagnostics 7 days; audit/transaction retention established per obligation | Privacy/records owner confirms jurisdiction and deletes/minimizes appropriately. Do not apply defaults to required legal records. |

An estimate is not a guarantee. In particular, a 72-hour synthetic volume test is not a 72-hour real-time endurance test. The implemented experiment uses a small record count to verify state transitions, not estate-scale capacity.

A13: Retain acknowledged observation summaries for seven days in a bounded recovery archive, separate from the 72-hour pending-outage envelope. Expire archive records by policy; never evict pending records to preserve expired archive data.
A14: Propose an eight-week pilot ceiling of EUR 37,800 within the full program envelope. Validate supplier/installation/support assumptions before expenditure.

| Additional ID | Selected assumption | Validation owner |
|---|---|---|
| A15 | Twelve-hour maximum offline capture grant; no offline renewal; manual records after expiry | Care lead and security owner test expiry/revocation and usable manual capture |
| A16 | Proposed twelve lanes at five seconds/person; release at most 1,500 people per fifteen minutes, including walk-ups | Entrance operations validates actual passage, arrivals, queues and accessible provision |
| A17 | English public visitor trial; other languages separately gated; IDs/templates and approved excerpts initially | Visitor product/knowledge owner reviews task and language quality |

A15 is intentionally shorter than the A03 buffering horizon. A16 is a selected admission planning policy, not a measured throughput guarantee.

| Additional ID | Selected assumption | Validation owner |
|---|---|---|
| A18 | Four bidirectional attraction counters within the pilot's 24 sensors; manual calibration; covered hour requires at least 90% usable minutes | Field and operations owners validate count error, coverage and installation allocation |
| A19 | Return cohort: voluntarily linked adult account, distinct-date admission within 90 days, full follow-up window; saved plan expiry after 180 inactive days | Visitor product and records owners validate instrumented definitions and permission handling |
| A20 | At most one opted-in reminder per 30 days through existing supplier capability; account-page fallback | Product owner verifies supplier capability and cost before enabling reminders |
| A21 | AI daily sample of ten accepted recommendations, all reported failures; rolling fallback and provider circuit triggers | Model/platform owners tune proposed thresholds during the pilot and record changes |
