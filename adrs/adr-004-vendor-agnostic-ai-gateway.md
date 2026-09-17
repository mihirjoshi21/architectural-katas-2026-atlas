# ADR-004: Versioned AI adapter with evaluated fallback and spend limits

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R08, R12 |
| Related visual | D08; [diagram index](../diagrams/README.md) |

## Context

Provider APIs, model behavior and prices change. A small estate team needs a replaceable AI integration without assuming that every compatible API produces equivalent answers. Local 8B model hosting has not been costed or validated.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Provider SDKs throughout business code | Fast first call | Scattered contracts, policy and upgrade work; rejected. |
| Thin internal adapter/library, isolated deployment boundary when needed | Small initial footprint; central contract, limits and evaluation | Some adapter maintenance; selected. |
| Full multi-provider proxy platform | More routing/observability features | Additional dependency and operation; revisit with scale. |
| Self-hosted fallback model | No external model API dependency | Compute, power, security, model operation and local reachability costs; deferred. |

## Decision

Expose a versioned estate-specific request/response contract rather than leaking a vendor completion API throughout the application. Centralize scoped read tools, approved retrieval, rates, maximum output, request deadline and privacy policy. Start with one evaluated provider; promote a secondary only after the same evaluation. Reserve maximum bounded cost atomically before a call, reconcile actual usage, account for retries and fail closed for cloud calls if budget authority is unavailable. Initial cap T06 is a planning assumption.

Provider or budget failure returns approved information/search and handoff. It does not depend on a local LLM. Separate timeout detection, routing overhead and total response latency; do not claim sub-200ms failover after a 1.2s timeout.

## Consequences

A stable adapter reduces coupling, not all vendor dependence. Provider switches may need prompt/tool/response adaptations and fresh evaluation. Maximum-cost reservation requires up-to-date versioned pricing and bounded output/retries. In-flight reservations reduce available budget even before final charges are known.

## Verification and revisit trigger

Specify concurrent near-budget, timeout, 429/5xx, malformed/partial response, exhausted deadline and cost-store outage tests. Compare providers on held-out tasks and record actual token/cost/latency. These integrations are specified, not executed in this package. Revisit after usage evidence justifies a proxy platform or local inference.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)

## Operational failure contract

Unknown provider pricing prevents new calls until a bounded reservation price is configured. Provider shutdown retains search as the service baseline; any replacement repeats evaluation before promotion. Five consecutive provider failures open the proposed five-minute circuit before a controlled probe. Daily cost reconciliation, sampled output review and ownership are defined in [AI operations](../design/ai-operations.md).
