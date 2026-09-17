# ADR-010: Grounded visitor help with evaluated changes

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R08, R12 |
| Related visual | D08; [diagram index](../diagrams/README.md) |

## Context

A conversational interface may help multilingual visitors navigate information and choices. Fluency does not prove current ride status, source support or accessibility. A useful FAQ/search baseline exists without generative AI.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| FAQ/search and static routes | Cheap, predictable and useful offline | Less conversational; retained as baseline/fallback. |
| Grounded assistant with scoped reads and deterministic constraints | More flexible help | Requires corpus, evaluation and operations; selected for trial. |
| Autonomous booking/pricing agent | Rich demo behavior | More authority and failure scope than required; deferred/excluded from initial trial. |

## Decision

Retrieve approved versioned content and permitted freshness-aware live facts. Keep closures, accessibility and activity validity checks outside the model. Render approved activity facts and source excerpts, distinguish stale/unknown facts and hand off when appropriate. No booking, treatment or price writes. Compare the assistant with search on human-reviewed tasks before rollout; evaluate provider, prompt, corpus and tool-contract changes.

## Consequences

Maintaining good knowledge and a held-out evaluation set is continuing work. Static fallback may be less personalized but remains useful. Not all questions require a model call; cache only non-sensitive approved responses under freshness/version rules.

## Verification and revisit trigger

Specified evaluation includes ordinary, unknown, stale, adversarial, multilingual and accessibility cases; human-supported groundedness, task completion, constraint errors, latency and cost. No live LLM experiment is included. Promote only after a human owner reviews results and residual errors; otherwise retain the baseline.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)

## Selected initial product contract

Use PostgreSQL full-text retrieval over approved versioned content and read-only authoritative status. The model returns candidate activity IDs and source references. Independently confirmed visitor constraints and ordinary code determine allowed options; templates render consequential facts. General answers use approved excerpts. Free-form explanation and additional languages require separate semantic/translation evaluation. This ADR accepts a bounded trial and release criteria, not a particular untested model. [Worked contract](../design/visitor-assistant-contract.md) defines concrete data, output and fallback behavior.

## Return journey and operational quality

The same bounded discovery capability can suggest approved options for a visitor-saved return plan. Future interest is not a reservation or future-open assertion; status and capacity are checked again for booking/arrival. Saving and reminder permission are separate visitor actions handled outside the model. Compare with curated lists and measure actual repeat admissions, not message opens. [Growth contract](../design/visitor-growth-and-popularity.md). Daily sampled task review, deterministic rejection monitoring, incident disablement and weekly outcome review follow the [AI operations contract](../design/ai-operations.md).
