# ADR-011: Keeper-confirmed records with conditional animal-monitoring AI

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R03, R04, R05 |
| Related visual | D07; [diagram index](../diagrams/README.md) |

## Context

The brief explicitly asks about health, how much/well animals eat and piranha population levels. Detecting a jump is not equivalent to estimating population. Occluded aquatic animals and sparse labels can defeat a plausible-looking CV demo.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Structured keeper ledger and manual reconciliation | Immediate usable baseline and provenance | Manual effort/uncertainty; selected authority. |
| Sensor-assisted observations and simple anomaly rules | Earlier visible exceptions | Sensor quality and contextual interpretation needed; baseline extension. |
| Advisory anomaly/CV counting trials | Potentially reduces review effort or missed changes | Needs representative labels, uncertainty and workload evaluation; conditional trial. |

## Decision

Record individual/group feeding observations, offered/remaining/estimated consumption with units and quality. Keep a population ledger of confirmed changes and timestamped estimates. Candidate model estimates include method/version/quality/uncertainty and route to keeper reconciliation; they never overwrite confirmed population or authorize care. Begin trials only after measurement feasibility and a representative labeling plan. Treat ambiguous footage as insufficient evidence and use the manual process.

## Consequences

Manual work remains and models may not provide enough benefit to deploy. Frame object-detection metrics alone do not establish population accuracy. Camera placement/retention and species/group differences need review. Clinical, feeding and emergency thresholds must come from appropriate domain authorities.

## Verification and revisit trigger

Evaluate absolute count error and undercount by lighting/occlusion/turbidity, review effort and data coverage. Evaluate feeding/health anomaly precision/recall for a defined event and false alerts per shift. No real animal data or trained model is included. Defer the model if quality or staff workload fails the agreed gate.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)

## Piranha measurement contract

The first camera experiment measures **visible fish in a defined observation region during a fixed sampling window**, then flags discrepancies for keeper review. It does not infer total enclosure population from an unconstrained frame count. Store visible count, capture region/coverage, timestamp, quality and uncertainty separately from the last keeper-confirmed population and its confirmation method/date. Never add counts across frames or cameras without an established identity/coverage method.

The animal-care lead defines an observation protocol compatible with existing welfare procedures. Two reviewers independently annotate a representative set of sample frames/windows; disagreements are adjudicated and ambiguous/occluded views marked non-observable rather than assigned invented exact labels. Agreement on visible fish supplies a reference for visible-count evaluation only. An enclosure total needs an independently justified, keeper-led census/reconciliation method; if unavailable, display “total population unverified” with the last confirmation date and continue discrepancy monitoring.

The pilot uses two camera positions to test whether useful coverage can be obtained. It compares manual visible-count review with a candidate detector/counting approach under the same observation protocol. Advance only if reviewers can establish a repeatable reference, the method's count error/undercount and abstention meet a tolerance recorded by the care lead before held-out review, and workload improves. If the reference or coverage fails, stop the camera trial; the structured feeding/health ledger remains useful. A signed ledger entry is evidence of an attributed confirmation, not proof that hidden fish were observed.
