# ADR-001: Local MQTT messaging with explicit connectivity

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R09, R10, R11 |
| Related visual | D03; [diagram index](../diagrams/README.md) |

## Context

Patchy estate Wi-Fi and a budget for MQTT-capable devices are brief constraints. MQTT is application messaging; wired Ethernet, Wi-Fi and backhaul are connectivity choices. An offline gateway helps only if readings can reach a powered gateway in the first place.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| MQTT over a provisioned local IP link | Local publish/subscribe, topic ACLs and low-rate telemetry fan-out | Broker lifecycle and persistent sessions must be operated. Selected for suitable devices. |
| HTTPS batching over the same link | Familiar request/response, easy batch receipts and also supports store-and-forward | Less natural local fan-out; selected for gateway-to-cloud batches, not rejected as incapable of resilience. |
| Direct cellular on each device | Independent radio path where coverage exists | Per-device subscriptions/power and sensor capability; not initial default. |
| Low-rate non-IP radio plus adapter | Can suit remote small readings | Survey, protocol bridge, duty cycle and payload limits; feasibility option, not a raw-video/MQTT assumption. |

## Decision

Use local MQTT for IP-capable sensors and a named adapter for other interfaces. QoS 1 is the default for operational summaries; deduplication is an application responsibility. QoS 0 is acceptable only for explicitly best-effort observations with measured gaps. Safety reporting does not rely on QoS 2 as a guarantee of physical execution. Send authenticated HTTPS batches from the durable edge outbox to cloud ingestion. Survey each site, including local power and staff access, before expanding.

## Consequences

This separates broker acknowledgements from durable application receipts. It preserves messaging usefulness without promising connectivity that is absent. It requires operating device identities, topic permissions, broker persistence and an edge ingestion consumer. Sensor retries/device persistence must be validated: the guaranteed acceptance boundary begins only after the edge outbox commit.

## Verification and revisit trigger

Check device/topic authorization, payload limit A06, ingest-before-acceptance, sensor-link loss and WAN loss separately. The included replay experiment does not test MQTT itself. A field protocol/power trial is required before a production claim. Revisit if local coverage, volume or hardware capability fails the pilot.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)
