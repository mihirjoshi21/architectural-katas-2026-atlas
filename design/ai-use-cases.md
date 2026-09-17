# AI use cases and evidence gates

## Chosen scope

| Use | Initial non-AI baseline | AI trial and authority | Release condition |
|---|---|---|---|
| Visitor assistance | Approved FAQ/search, clear pass products and static accessible itineraries | Natural-language activity selection, confirmed constraints and approved fact templates; language-specific release gates | Human-reviewed task usefulness, source support, stale-data behavior and operating cost beat the baseline. |
| Animal health/feeding review | Structured keeper observations, schedules and domain-approved thresholds | Advisory anomaly ranking with evidence and uncertainty; no treatment write authority | Representative reviewed data, useful precision/recall, acceptable review burden and safe abstention. |
| Piranha population observations | Keeper ledger and reconciled manual observations | Candidate vision counting/quality estimation; keeper confirms records | Representative footage and acceptable count error/undercount, uncertainty and review effort. |
| Ride maintenance | Inspections and domain-approved threshold trends | Conditional LightGBM candidate on engineered features, advisory only | Labels and useful horizon established; time/asset-separated validation and shadow results support promotion. |

Popularity reporting initially uses descriptive aggregation, not a forecast model. Dynamic prices, reinforcement learning and a local LLM fleet are deferred. One AI capability succeeding does not validate the others.

## Visitor assistant design card

**Selected trial:** natural-language activity discovery, PostgreSQL full-text retrieval, visitor-confirmed constraints, model-selected activity IDs and source references, followed by deterministic checks and approved fact templates. General information uses approved excerpts. English is the initial public language; additional languages require separate review. No model has booking, pricing or care authority.

The [complete contract](visitor-assistant-contract.md) specifies the synthetic journey, exact candidate schema, source/version joins, stale/closed behavior, cost reservation and fallback. [Release gates](../validation/evaluation-plan.md) separate policy tests, model task quality, user usefulness and measured resources. The 48 concrete synthetic cases have no model results. Eighteen executed policy tests establish only the narrow deterministic boundary.

## Animal anomaly and population design card

**Owner:** animal-care lead with qualified reviewers. **Data:** time-stamped subject/group, feeding amounts/units, observations, environmental trends; for counts, explicitly permitted representative camera samples with keeper-reviewed ground truth. **Candidate:** simple rule/statistical baseline first; anomaly ranking or vision estimate only if data and trial justify it.

**Quality:** missing sensors, reflections, overlapping animals, turbidity, seasonality and feeding schedule shifts are explicit test slices. Confidence scores need interpretation/calibration; uncertain observations route to manual review. Keep model estimates separate from the population ledger and clinical facts. Log births, deaths, transfers and corrections to support reconciliation.

**Evaluation:** anomaly false alerts per review shift, recall/precision for a defined event and workload; population absolute count error, systematic undercount, coverage and review effort. Labels require domain review; synthetic examples cannot establish biological accuracy. **Fallback:** manual observation and established care process. **Actions:** approval is action/task/version-specific; notification and urgent escalation remain separate.

![Animal monitoring](../diagrams/rendered/d07-animal-monitoring.svg)

## Maintenance design card

**Owner:** park maintenance lead. **Data:** calibrated raw sample windows, derived RMS/spectral/thermal features, inspections, repair outcomes and operating conditions. No suitable failure dataset is assumed to exist. Start with inventory/digitization, standardized labels and the manual/threshold baseline.

**Candidate:** LightGBM for tabular features; compare with simple statistical/rule and alternative tabular models. Keep raw acquisition rate distinct from small summarized MQTT events. Feature extraction, inference and explanations have separate measured resource budgets. SHAP-style attribution is model explanation, not causal proof.

**Evaluation:** define predicted event/horizon, group/time-separated splits, false alerts per ride/day, useful lead time, precision/recall and error uncertainty; test missing sensors and unseen asset conditions. Shadow before advising live work orders. Retain human inspection/return-to-service authority. No predictive performance or runtime measurement is claimed before representative evaluation.

![Maintenance lifecycle](../diagrams/rendered/d09-maintenance-ml.svg)

## Piranha measurement contract

The first camera experiment measures **visible fish in a defined observation region during a fixed sampling window**, then flags discrepancies for keeper review. It does not infer total enclosure population from an unconstrained frame count. Store visible count, capture region/coverage, timestamp, quality and uncertainty separately from the last keeper-confirmed population and its confirmation method/date. Never add counts across frames or cameras without an established identity/coverage method.

The animal-care lead defines an observation protocol compatible with existing welfare procedures. Two reviewers independently annotate a representative set of sample frames/windows; disagreements are adjudicated and ambiguous/occluded views marked non-observable rather than assigned invented exact labels. Agreement on visible fish supplies a reference for visible-count evaluation only. An enclosure total needs an independently justified, keeper-led census/reconciliation method; if unavailable, display “total population unverified” with the last confirmation date and continue discrepancy monitoring.

The pilot uses two camera positions to test whether useful coverage can be obtained. It compares manual visible-count review with a candidate detector/counting approach under the same observation protocol. Advance only if reviewers can establish a repeatable reference, the method's count error/undercount and abstention meet a tolerance recorded by the care lead before held-out review, and workload improves. If the reference or coverage fails, stop the camera trial; the structured feeding/health ledger remains useful. A signed ledger entry is evidence of an attributed confirmation, not proof that hidden fish were observed.
