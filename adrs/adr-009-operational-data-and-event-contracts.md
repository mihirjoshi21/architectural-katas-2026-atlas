# ADR-009: Operational stores with transactional events and derived analytics

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R01, R03, R04, R05, R10 |
| Related visual | D05; [diagram index](../diagrams/README.md) |

## Context

Care approval, ticket redemption and payment reconciliation need authoritative transactional state. A fifteen-minute analytical cleaning pipeline cannot be the gate for urgent business decisions. Operational authority must be separate from delayed analytical processing.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Lakehouse as primary workflow store | Analytical flexibility | Poorly matched transactional authority and latency; rejected. |
| Operational relational ownership + durable events + aggregate exports | Straightforward transactions and traceability | Some projection/analytics lag; selected. |
| Full event sourcing and enterprise streaming | Flexible replay and independent consumers | More versioning/replay/operations complexity; revisit if requirements justify it. |

## Decision

Use module-owned PostgreSQL schemas in cloud and SQLite for bounded local outboxes/admission records as appropriate. Persist business changes and outbound events in one transaction; consumers use durable inbox uniqueness and idempotent effects. Identity/hash conflict is an error. Object storage holds exports and controlled artifacts; reporting reads derived views. Keep model estimates separate from authoritative observed/confirmed facts. Define retention/access by data class and unresolved jurisdiction requirements.

## Consequences

The architecture promises explicit authority, not automatic consistency across disconnected locations. Cross-boundary synchronization needs reconciliation. A Bloom filter or expiring cache is not the final authority for dropping a critical duplicate. Schema changes require compatibility policy and gap handling.

## Verification and revisit trigger

Validate atomic write/outbox behavior, replay/dedupe, conflicting IDs, schema evolution, audit provenance and restore. The replay spike covers a narrow inbox/effect transaction; cloud deployment and full module integration remain specified. Revisit streaming/lakehouse when measured data/query requirements exceed simple reporting.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)

## Popularity and return-event ownership

Use non-identifying bidirectional entry observations and manual calibration for pilot popularity, reported as entries per covered operating hour with missingness. Keep these anonymous measures separate from voluntarily linked return-visit cohorts. Visitor & Admissions owns saved plans and separately versioned reminder permission. [Business measurement contract](../design/visitor-growth-and-popularity.md).
