# Architecture decisions

The original IDs 001–006 are preserved. All records are accepted as the architecture for this submission; this is distinct from deployment approval and implementation/evaluation status. 

| ID | Decision | Status |
|---|---|---|
| [ADR-001](adr-001-mqtt-vs-wifi-edge-strategy.md) | Local MQTT messaging with explicit connectivity | Accepted; deployment gates apply |
| [ADR-002](adr-002-store-and-forward-edge-storage.md) | Durable outbox, final receipts and bounded replay | Accepted; deployment gates apply |
| [ADR-003](adr-003-exclusion-of-genai-from-pricing-and-safety.md) | Separate AI advice from consequential execution | Accepted; deployment gates apply |
| [ADR-004](adr-004-vendor-agnostic-ai-gateway.md) | Versioned AI adapter with evaluated fallback and spend limits | Accepted; deployment gates apply |
| [ADR-005](adr-005-predictive-maintenance-traditional-ml.md) | Conditional tabular ML for advisory maintenance | Accepted; deployment gates apply |
| [ADR-006](adr-006-human-in-the-loop-animal-care.md) | Task-specific human authority for animal-care actions | Accepted; deployment gates apply |
| [ADR-007](adr-007-system-boundaries-and-build-buy.md) | Modular estate core and bought commodity capabilities | Accepted; deployment gates apply |
| [ADR-008](adr-008-offline-ticketing-and-reconciliation.md) | Signed entitlements and local redemption authority | Accepted; deployment gates apply |
| [ADR-009](adr-009-operational-data-and-event-contracts.md) | Operational stores with transactional events and derived analytics | Accepted; deployment gates apply |
| [ADR-010](adr-010-grounded-assistant-and-evaluation.md) | Grounded visitor help with evaluated changes | Accepted; deployment gates apply |
| [ADR-011](adr-011-population-and-feeding-monitoring.md) | Keeper-confirmed records with conditional animal-monitoring AI | Accepted; deployment gates apply |

Shared context is in [architecture](../ARCHITECTURE.md); verification status is in [evidence](../validation/evidence-index.md). Future revisions should record supersession and the evidence that changed the decision. 
