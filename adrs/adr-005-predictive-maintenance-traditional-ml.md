# ADR-005: Conditional tabular ML for advisory maintenance

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R02, R07, R12 |
| Related visual | D09; [diagram index](../diagrams/README.md) |

## Context

Historic rides create inspection and downtime concerns, but no representative labeled failure dataset was supplied. A predictive model must earn its place against inspections and simple trend/threshold methods. Sensor rates and feature extraction costs differ from model inference time.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Inspections and approved thresholds | Available before labels; understandable baseline | Limited multi-signal patterns; selected initially. |
| LightGBM on engineered features | Candidate for tabular summaries and resource-limited inference | Needs labels/features and representative evaluation; conditional preferred trial. |
| Alternative tabular/statistical models | Useful accuracy/resource baseline | Must compare on the same task/data; not pre-rejected. |
| Deep time-series model | Potentially learns richer patterns | Greater data/tuning/operation needs; no evidence of necessity yet. |

## Decision

Keep manual inspection and threshold baseline initially. Inventory/digitize maintenance outcomes and define the prediction event/horizon. Use calibrated time windows to derive vibration/thermal/usage features. Evaluate LightGBM against the baseline and other simple candidates using time- and asset-separated data. Deploy a signed/versioned artifact in shadow mode before advisory use. Keep inspection and return-to-service decisions with authorized mechanics.

## Consequences

No numerical recall, useful lead time or inference budget is claimed as achieved. Resource measurement must include acquisition, feature extraction, model and explanations. Feature attribution is not causal root cause. Poor data readiness means deferring the model, not fabricating labels or a successful metric.

## Verification and revisit trigger

Specify precision/recall at an operating threshold, false alerts per ride/day, lead time, missing/drifting sensors, unseen asset slices, model/feature parity and rollback. Report sample sizes and uncertainty. No real maintenance dataset/model is included, so this ADR remains conditional. Revisit when reviewed data and shadow evidence justify promotion.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)
