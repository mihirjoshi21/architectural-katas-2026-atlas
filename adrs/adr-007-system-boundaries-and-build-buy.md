# ADR-007: Modular estate core and bought commodity capabilities

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R01, R07, R12 |
| Related visual | D02; [diagram index](../diagrams/README.md) |

## Context

The estate needs comprehensive workflows but the brief does not establish a large software operations team. Independent services in three languages plus several data platforms impose cost before independent scaling or deployment needs are known.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Custom distributed platform from day one | Independent scaling/deployment | Many operational contracts and support skills; not justified initially. |
| Entire estate on one vendor suite | Fast commodity workflows | Offline/export/domain gaps must be tested; evaluate for ticketing, not assumed complete. |
| Bought payment/ticketing where suitable + modular estate core + edge runtime | Focused custom work with clear physical separation | Integrations and module boundaries still need care; selected. |

## Decision

Use three business modules with owned schemas and interfaces in a small cloud application. Keep physical edge runtime and local admission authority separate. Isolate AI through a narrow adapter; separate deployment only where permissions/resource/fault needs justify it. Procure payment handling and evaluate ticketing suppliers against offline signed entitlements, idempotency, refunds, timed-entry people/slot caps including walk-ups, data export, accessibility and costs. If no supplier passes, record the gap and explicitly scope the minimum custom issuer integration.

## Consequences

One application deployment can couple releases; explicit module contracts and tests reduce accidental coupling. Bought services introduce commercial dependency but reduce custom commodity responsibilities. Vendor selection and field support remain open procurement work, not an invented completed purchase.

## Verification and revisit trigger

Review capability fit, team support skills, backup/export and migration path. Extract a service only with a stated independent scaling/deployment/fault-isolation need and budget. This architecture comparison is a decision proposal, not a benchmark.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)

## Existing operations and evolution

No incumbent software topology is supplied. Inventory current authorities, import with original-ID mappings and reconcile before a limited cutover. Shadow observation capture may coexist with old records; two independent ticket-redemption writers may not. [Coexistence and migration](../design/coexistence-and-migration.md). Saved plans remain in Visitor & Admissions; optional reminders use an existing supplier capability or remain an account-page feature.
