# End-to-end workflows

## 1. Buy and use a family pass

A visitor chooses a published pass product and party entitlement. A payment provider handles card data; the ticketing adapter reconciles payment using an idempotency reference before issuing an entitlement. The signed payload includes issuer, ticket ID, entitlement/version, validity, party limit and key ID. A visitor can use printed paper or staff assistance as well as a phone.

At the entrance, the validator checks signature, issuer, validity, current locally known revocations and policy. It asks the local admission authority to atomically redeem the correct party allowance. Successful entry—not purchase—updates occupancy. Repeat redemption is rejected or routed to staff under the pass's explicit re-entry rules. Payment success, ticket issuance and admission are separate states.

![Offline admission](../diagrams/rendered/d04-offline-admission.svg)

If a gate cannot contact the local authority, it does not create an independent automatic single-use decision. A gate agent records an exception under the approved procedure. When WAN returns, redemptions and exceptions reconcile with cloud. Recently revoked tickets may remain admissible under stale revocation knowledge; expose that residual risk and choose a freshness limit. Do not advertise offline payment authorization unless the selected provider explicitly supports it.

## 2. Observe feeding and health, review and act

The keeper records animal/group, feed type, offered amount/unit, remaining amount or estimated consumption, time and observation quality. Environmental sensor data complements these records; it does not diagnose by itself. Manual policy or an advisory anomaly model can suggest a review task with evidence. Poor sensor quality produces a measurement-quality issue rather than a false clinical certainty.

![Care workflow](../diagrams/rendered/d06-care-workflow.svg)

A reviewer sees the underlying observations, age, trend, model version if present, suggested action and role requirements. Approve/reject/escalate commits against the current task version. Treatment needs appropriate authority; calling for help or escalating a critical notification does not wait for treatment authorization. Staff report completed, failed or unknown physical outcomes separately against an action attempt ID. Deduplicate digital reports; never automatically repeat an unknown physical action. Changed observations invalidate pending stale approvals.

When local staff access is available but WAN is down, authorized observation capture and assigned local workflows remain available within their offline role/expiry policy. Otherwise staff use the documented non-digital process and later record provenance. Clinical response thresholds and emergency procedures require domain validation, not guessed minutes from this proposal.

## 3. Reconcile piranha population

Start with a keeper-maintained population ledger and periodically reconciled observations. A camera trial may produce an estimate with occlusion/quality indicators. Repeated frame detections are not automatically distinct animals. Store candidate count and uncertainty separately from a confirmed population; compare with known births/deaths/transfers and manual checks. Poor footage routes to manual review. Model adoption requires representative footage and useful error/review-effort results.

## 4. Ask the visitor assistant

Retrieve approved, versioned park information; use authorized read tools for live operational facts with timestamps. The activity model selects IDs and source references. Ordinary code validates current status and visitor-confirmed constraints; templates render approved facts. General-information mode uses full-text search and approved excerpts. There is no unrestricted model explanation in the initial public product. If information is stale or absent, state that plainly and offer approved static options or staff help. Booking and payment happen through ordinary authorized workflows, not assistant write tools.

![Visitor assistance](../diagrams/rendered/d08-visitor-assistant.svg)

## 5. Decide where to deploy staff

Aggregate anonymous zone counts, queue samples and ride availability with coverage/quality. Define popularity as a specified metric over a time window, not interchangeable with crowd density or queue length. A manager compares periods, sees missing coverage, records a staffing/investment decision and later measures outcomes. Forecasting is deferred until simple descriptive reporting proves useful and sufficient history exists.

Offline care access is capture-only: new digital approval and execution authorization require current cloud authority. Emergency response follows established local procedures.

## Detailed authority contract

See [authority recovery and care outcomes](authority-recovery.md) for fencing and validator enrollment, twelve-hour capture grants, revoked draft quarantine, and completed/failed/unknown physical outcomes. The 72-hour telemetry buffer is separate from authenticated staff access.

Visible camera counts cover a defined region/window and are not enclosure totals. A total requires an independent keeper-led confirmation method; otherwise show its unverified status and last confirmation date.

### Visitor growth and return-visit journey

The commercial design addresses three distinct levers: attract a first visit, complete a suitable purchase, and make a return visit worthwhile. Visitor & Admissions owns the journey; it does not depend on identifying people through popularity sensors.

| Step | Selected behavior | Owner and measure |
|---|---|---|
| Discover | Publish accessible, shareable pages for approved attractions, seasonal events and pass products. Estate staff select campaign/referral links; no model invents events, prices or availability. | Visitor product owner: qualified landing sessions and attributed completed purchases, with attribution limits shown |
| Buy | Present clear party eligibility, published prices, accessible assistance and available timed-entry slots through the normal checkout. Abandoned checkout is distinct from failed payment. | Ticketing owner: completed purchases / initiated checkouts; supplier reconciliation; no card data in ATLAS chat |
| Visit | Help the visitor select appropriate activities from current authoritative information. Record admissions separately from sales. | Operations: actual attendance, exceptions and task completion |
| Save a reason to return | After a visit, offer an optional saved plan based on interests the visitor explicitly chooses and approved attractions/events. A visitor may save a plan without consenting to reminders. | Visitor product owner: voluntarily saved plans and declared interest categories |
| Re-engage | With a separate opt-in, send at most one requested reminder in a 30-day window through the ticketing supplier's existing notification capability, if available. Without that capability, retain the saved plan on the account page; no new messaging platform is assumed. Recheck permission and suppression immediately before sending. | Visitor product owner: delivery/opt-out/complaint rates, reminder-to-purchase conversion; stop reminders on withdrawal |
| Return and learn | Normal checkout and admission establish a subsequent visit. Compare repeat attendance and incremental contribution with a declared baseline/holdout. Renewing a pass, opening a message or saving a plan is not a return visit. | Operations/finance: 90-day observed return rate and contribution, accounting for support/offer costs |

A returning visitor can reopen the same bounded discovery assistant. It selects approved activity IDs using visitor-confirmed preferences; saving is a separate authenticated application command initiated by the visitor. A future plan is a saved interest, not a reservation, access guarantee or assertion of future opening. Revalidate date-specific status, access and capacity when the visitor books or arrives. A curated seasonal list is the non-AI baseline. There is no autonomous marketing agent, automatic discount or additional AI authority.

**Measurement contract:** propose a 90-day return window. The denominator is consenting, linkable adult account holders with a recorded initial admission and a complete 90-day follow-up window; the numerator is those with at least one later admission on a different date within that window. Report unlinked visits separately; a purchaser account or family party is not an individually identified child or every visitor. Do not generalize this cohort to the whole estate. Compare a randomized reminder offer against ordinary account access where feasible; record allocation, sample size, seasonality and uncertainty. A small pilot establishes instrumentation and usability, not a statistically powered retention uplift. Finance attributes contribution once and includes reminder, offer and support costs.

**Scope and data:** Visitor & Admissions owns `SavedReturnPlan`, declared interests and separate reminder preference/version/withdrawal. The notification adapter checks the latest preference and keeps a delivery/suppression audit. No facial recognition, device tracking or inferred animal-health interests are needed. Proposed expiry is 180 days of inactivity for saved plans, or earlier on deletion; retain only minimal suppression/audit information under the records policy. Public/model inputs exclude contact details and booking history. Saved plans and reporting fit the foundation backlog; automated reminders are conditional on supplier capability and are removed from scope if their cost cannot fit the service-license/support allocation.

The product owner reviews the 90-day cohorts after sufficient follow-up. Continue a reminder or discovery feature only with acceptable user feedback, no unresolved permission failures, and a finance-reviewed contribution case. Stop the experiment if it merely shifts already-planned visits or increases workload without benefit. The architecture supports the 15,000/day ambition; marketing effectiveness and physical estate demand remain business hypotheses.

### Popularity measurement and a staffing decision

The pilot allocates **four bidirectional, non-identifying entrance counters within its existing 24-sensor allowance**, at four selected attraction entry boundaries. The other twenty sensors cover selected ride/environment observations. Counter hardware, adapters and calibration must fit the existing hardware/install allocation; replace unsuitable sites with scheduled manual tallying instead of adding an uncosted camera analytics fleet. Count every access point included in a reported boundary; an uncovered bypass makes that zone partial coverage. Staff take manual samples to detect groups, staff crossings, direction errors and resets. Open spaces without a controlled count boundary use sampled observation and are labelled separately.

**Selected metric:** popularity is visitor entry observations per **covered operating hour** for the same attraction and comparable time band. A covered hour requires usable counter data for at least 90% of the hour; show valid minutes, open minutes and excluded intervals beside the metric. Missing intervals are not zeros and are not extrapolated into precise totals. Repeat entries count as visits, not unique people. Queue wait, dwell time, occupancy and safe capacity remain separate measures. Raw count events contain zone/device/time/sequence/direction/quality, not a visitor identity.

At the start of each pilot shift, compare a 15-minute manual sample with counter entries, excluding separately annotated staff movements. A proposed pilot tolerance is absolute count error no greater than the larger of two entries or 10% of the manual tally; failed samples flag the interval and require investigation before ranking that zone. This is an unmeasured measurement-quality gate, not a sensor specification. Site layout and manual reference quality may require tighter or different limits before deployment.

For a **synthetic example**, Zone A records 240 entries over two covered operating hours and Zone B 120 over the same duration: 120 versus 60 entries/hour. A sampled queue of eight minutes at A and two at B may justify moving a flexible visitor-assistance role, provided minimum staffing and qualifications remain satisfied. High popularity does not itself justify reducing animal-care, inspection or physical-protection staffing. The manager records the reason, weather/event context and follow-up comparison of queue experience, throughput and complaints; counting an intervention is not evidence it worked. Historical popularity directs review and investment hypotheses, while live missingness/status governs how much confidence to place in the display.
