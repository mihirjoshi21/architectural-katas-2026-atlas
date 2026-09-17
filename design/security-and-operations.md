# Security, physical boundaries and operations

## Authority and trust

![Authority boundaries](../diagrams/rendered/d14-authority.svg)

Visitors can read permitted information and initiate ordinary purchase workflows. Gate staff handle admission exceptions within a defined role. Keepers record/reconcile observations; authorized reviewers approve the actions appropriate to their role. Mechanics retain inspection and return-to-service authority. Devices publish only for their declared sources/topics. The AI adapter receives scoped read tools and cannot call treatment, price-write, ticket-issuance or physical-control interfaces.

Public-key signed entitlements use a standard supported signature implementation (Ed25519 is the proposed starting algorithm), issuer/key IDs and a managed rotation policy. Validators keep public verification keys; the issuer protects the private key. Offline validators must reject unknown/expired keys and enforce an explicitly accepted revocation-staleness policy. Do not build cryptography by hand. [EdDSA specification](https://www.rfc-editor.org/rfc/rfc8032)

Use authenticated device channels and source ACLs, local encryption where sensitive data is stored, managed secrets, least privilege and audit logs. Physical segregation and logical VLAN/firewall rules are distinct; diagrams do not label routed networks “air-gapped.” Protect local admission and staff networks from guest traffic. A readable public knowledge document is still untrusted input for model instruction purposes.

## Threats and controls

| Threat | Control / residual issue |
|---|---|
| Copied/replayed QR | Local atomic redemption; isolation policy; cloud reconciliation; latest unseen revocations remain a bounded risk. |
| Stolen staff device | Device protection, expiring roles, revocation, task-specific approvals; offline expiry may reduce availability. |
| Spoofed sensor or forged batch | Device identity, source/topic ACL, schema and hash checks; compromised authenticated hardware still needs detection/replacement. |
| Replayed or stale care approval | Bind actor/task/action/version/expiry; compare-and-set transition and audit; external effects idempotent. |
| Compromised guest network | Segregated routed boundaries, default-deny access, tested exposure; no claim that a VLAN alone proves isolation. |
| Malicious retrieved text | Treat as data, allowlisted tools, data/permission checks outside model, grounded output review; prompt filtering alone is insufficient. |
| AI cost abuse | Rate limits, max output, atomic cost reservation, bounded retries, fail-closed cloud calls when budget state unavailable. |
| Lost collection unit | Authenticated enrollment, encrypted storage/transfers, manifest integrity, custody records, source retention until final receipt. |
| Poisoned/incorrect model data | Source/label provenance, held-out data, reviewer review, versioned promotion and rollback. |

## Device lifecycle

Inventory device/site/owner, identity and firmware; provision least-privilege credentials; measure baseline readings; calibrate and commission; monitor age/backlog/health; sign and stage updates with rollback; rotate credentials before expiry with an offline policy; replace failed units using spares; decommission by revoking identity and sanitizing data. Require explicit field validation before treating consumer-board endurance as sufficient.

## Operational ownership

| Role | Operating responsibility / measures |
|---|---|
| Estate operations lead | Staff escalation, local manual processes, incident owner, training and opening readiness |
| Platform support | Availability, ingestion lag, restore/RPO/RTO, cost and database capacity |
| Field/device support | Power, calibration, link quality, disk/backlog, replacement and collection |
| Animal-care owner | Review queue age, missing observations, model-error review and clinical/operational procedures |
| Model/knowledge owner | Corpus freshness, evaluations, drift, prompt/model versions, cost and rollback |
| Privacy/records owner | Jurisdiction, retention, access/deletion, camera placement and collection purpose |

On-call staffing and supplier support are costed assumptions. Escalation when fully disconnected must use a reachable local channel or routine physical check. Alerts should be actionable; sensor drift and duplicate notifications must not create unmanageable keeper workload.

Actual jurisdiction, payment scope, animal-care obligations and retention have not been established. This proposal defines review questions rather than asserting compliance. Physical protection requires competent domain engineering; these diagrams and software checks do not certify a ride, enclosure or emergency procedure. [OT security context](https://csrc.nist.gov/pubs/sp/800/82/r3/final)

Offline care access is capture-only: new digital approval and execution authorization require current cloud authority. Emergency response follows established local procedures.

## Detailed authority contract

See [authority recovery and care outcomes](authority-recovery.md) for fencing and validator enrollment, twelve-hour capture grants, revoked draft quarantine, and completed/failed/unknown physical outcomes. The 72-hour telemetry buffer is separate from authenticated staff access.

## Model and customer-data operations

[AI monitoring](ai-operations.md) defines daily sampling, response thresholds and provider shutdown handling. Saved return plans and reminder permission are separate, versioned visitor choices. Recheck permission immediately before delivery; withdrawal suppresses pending reminders. Contact details and booking history never enter the model context. A failed supplier notification capability falls back to the account page.
