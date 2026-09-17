# ADR-003: Separate AI advice from consequential execution

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R03, R04, R05, R12 |
| Related visual | D14; [diagram index](../diagrams/README.md) |

## Context

Visitor help, animal observations and maintenance suggestions can benefit from fallible models. Physical protection, treatment permission, ticket issuance and pricing authority need explicit domain and software controls. Repeatable traditional ML inference does not imply correctness or safety.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Autonomous model with write tools | Flexible behavior and short demos | Unacceptable authority for the proposed scope; rejected. |
| Model with prompt-only guardrails | Easy to add | Prompt compliance is not an access-control boundary; rejected as sufficient control. |
| Read/advisory AI plus external policy and authorization | Clear authority and testable boundaries | More explicit workflow/domain rules; selected. |

## Decision

No LLM, CV model or predictive model receives actuator, treatment-execution, price-write or ticket-issuance permission. Approved software rules validate prices/entitlements and care transitions; competent domain authority owns actual protection systems. AI may create a suggestion/review candidate containing evidence, never an execution authorization. Start ticket prices with approved published tiers. Exclude RL-driven pricing and automated containment commands from initial scope.

## Consequences

The team must design separate rules, permissions and human workflows. AI and human review remain fallible; review workload, missed errors and escalation require monitoring. Alerting/emergency escalation is distinct from waiting for approval of a treatment.

## Verification and revisit trigger

Specified checks include forbidden write permissions in adapter roles, tool-schema allowlists, API authorization, stale/replayed approval tests and dependency scans with known-violation fixtures. A static SDK-import check alone is insufficient and is not claimed as implemented. Revisit only through an explicit new risk/authority decision with domain evidence.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)
