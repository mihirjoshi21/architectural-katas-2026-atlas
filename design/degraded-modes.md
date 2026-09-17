# Degraded operation and recovery

| Failure | What remains available | Honest limitation / recovery |
|---|---|---|
| WAN unavailable, local power/LAN available | Local admission authority; capture-only observation drafts under expiring roles; buffered telemetry; approved static information | Cloud views stale. Replay and reconcile after destination recovery. No live cloud facts or implicit payment authorization. |
| Sensor link lost | Other sensors/gateway; manual observation route | Missing readings cannot be reconstructed as measured values. Investigate device power, wiring/radio and sampling. |
| Staff Wi-Fi unavailable | Only explicitly provisioned wired/local terminals and manual procedures | Hosting a local dashboard does not make it reachable. Staff communications and capture fallback must be exercised. |
| Gateway power/disk fails | Independent protection and manual procedures | A destroyed sole disk loses unsent records. Replace/re-enroll device, restore configuration and document lost interval. |
| Cloud application/ingestion fails | Local bounded operation; outbox accumulation | Alert on backlog age and storage locally if cloud unreachable. Restore service, validate receipts, pace backlog replay. |
| Local storage approaches quota | Retain prioritized records within provisioned limit; local alarm and collection schedule | At hard limit reject new acceptance explicitly; do not promise unlimited retention. Low-priority aggregation/drop rules must be visible and counted. |
| Collection vehicle unavailable | Retention headroom, routine local checks | Schedule a staffed response; a fully disconnected gateway cannot magically send PagerDuty. |
| LLM timeout/budget exhausted | Approved information/search, validated static routes, staff handoff | No automatic local model assumption. Stop retries at the request/budget deadline. |
| Model drift/unknown conditions | Manual/threshold baseline; data collection | Abstain or shadow mode; roll back evaluated model version. |
| Reviewer unavailable | Notification, escalation, observation capture | Treatment stays pending until appropriate authority; existing emergency response remains available. |
| Local admission authority unavailable | Staffed exception process | Isolated validators do not pretend to provide globally unique automatic redemption. |

## Recovery runbook outline

Identify affected boundary and protect existing operations; communicate stale/unavailable status; assign owner; restore verified configuration/credentials; check local and destination record counts/receipts; replay idempotently; reconcile exceptions; record data gaps and incident outcome. Restore exercises must measure recovery time and validate actual usable records, not merely successful backup commands.

![Durable replay](../diagrams/rendered/d05-store-forward.svg)

The included replay spike proves a narrow software mechanism. It does not simulate radio behavior, device corruption, upstream broker durability or the full recovery runbook. [Evidence](../validation/evidence-index.md)

Offline care access is capture-only: new digital approval and execution authorization require current cloud authority. Emergency response follows established local procedures.

## Detailed authority contract

See [authority recovery and care outcomes](authority-recovery.md) for fencing and validator enrollment, twelve-hour capture grants, revoked draft quarantine, and completed/failed/unknown physical outcomes. The 72-hour telemetry buffer is separate from authenticated staff access.
