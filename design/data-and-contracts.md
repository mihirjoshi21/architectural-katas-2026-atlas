# Data ownership and contracts

## Operational entities

| Entity | Owner / essential fields |
|---|---|
| Entitlement | Visitor module: ticket ID, product/version, party allowance, validity, issuer/key ID, status |
| Redemption | Admission authority: redemption ID, ticket ID, party count, gate, local sequence, decision, exception reason |
| AnimalOrGroup | Animal Care: profile/group ID, species reference, enclosure, confirmed population and record provenance |
| FeedingObservation | Animal Care: subject, feed, offered/remaining/estimated consumed, units, timestamp, keeper, quality |
| HealthObservation | Animal Care: subject, measurement/behavior, units, occurrence/receipt time, evidence, data quality |
| PopulationObservation | Animal Care: estimate, method, quality/uncertainty, image reference if permitted, reviewer and reconciliation |
| CareTask | Animal Care: version, evidence, requested action, required role, state, expiry, approval/action/outcome IDs |
| RideStatus/WorkOrder | Park Operations: asset, status/inspection, authority, evidence, timestamps and maintenance outcome |
| ZoneObservation | Park Operations: zone, method, count/metric, coverage, time window and freshness |
| AuditEntry | Owning module: actor/device/service, command, version, reason, occurrence/receipt, outcome, correlation |

Operational records live in module-owned relational schemas; analytics are derived copies. A reporting job may lag without blocking admissions or urgent workflows. Knowledge documents, permitted evidence images, model artifacts and evaluation sets use versioned object storage with access/retention policies.

## Event envelope

```json
{
  "event_id": "gateway-07:epoch-4:00003152",
  "event_type": "FeedingObservationRecorded",
  "schema_version": 1,
  "source_id": "gateway-07",
  "aggregate_id": "animal-group-12",
  "source_epoch": "epoch-4",
  "sequence": 3152,
  "occurred_at": "2026-09-16T10:00:00Z",
  "received_at": "2026-09-16T10:02:00Z",
  "priority": 2,
  "correlation_id": "care-round-18",
  "payload": {"observation_id": "obs-3152", "quality": "keeper-confirmed"}
}
```

Identifiers are examples. The production identity mechanism must allocate and persist an epoch and sequence safely, or persist a random ID before first delivery. Clock time is not uniqueness. Retries reuse exactly the same ID and payload. Event identity collisions with differing content are quarantined and investigated.

## Delivery contract

1. Edge validates bounded payload and commits the event before application-level acceptance.
2. Upload carries stable IDs and payload hashes over an authenticated channel.
3. Destination checks source permission and schema; in one transaction it records inbox identity/hash and permitted business effect.
4. Same ID and same hash returns the existing receipt; same ID and a different hash fails. A durable unique key is authoritative.
5. Destination acknowledges after commit. If acknowledgement is lost, edge retries. Edge removes its pending record only after a final receipt matching the submitted ID/hash.
6. Physical carrier receipts establish custody, not final destination commit. Do not delete the sole source copy on a drive-by acknowledgement.

Priority favors urgent operational records but is not a safety control loop. Per-aggregate ordering uses sequence/epoch and gap handling. Consumers can receive duplicates and out-of-order unrelated events. Invalid/unsupported versions go to quarantine with visibility, not silent discard.

## Versioning and retention

Additive optional fields are backward compatible within a schema version; breaking semantics require a new version and parallel acceptance/migration plan. Pin data, feature, model and prompt versions for evaluation. Retain only necessary raw imagery; prefer aggregate counts and controlled review samples. Proposed retention defaults and unresolved legal/records questions are in [assumptions](../requirements/assumptions-and-targets.md).

Care authorization is not merely any signed staff token. It must express the intended action against a particular task version, with role and expiry checked at execution. Financial, care and admission commands need their own idempotency semantics; telemetry deduplication alone does not prevent duplicate external side effects.

## Receipt versus disaster recovery

A final receipt confirms the destination transaction, not indefinite survival of every disaster. T05 separately permits up to 15 minutes of cloud record loss on disaster restore. Before deployment, reconcile that exposure with required record retention and test recoverable logs/backups and critical-record reconciliation. Do not present the replay experiment as zero-loss disaster recovery.

Acknowledged observations remain in a separate seven-day edge archive to support replay after cloud restore. Removal from the pending queue is not immediate physical erasure. The small spike covers receipt/deduplication only; archive expiry and restore-range replay require integration validation.

## Return plans and popularity records

Visitor & Admissions owns SavedReturnPlan (account, approved activity IDs, selected interests, planned date if supplied, expiry), ReminderPreference (purpose/channel, version, grant/withdrawal time), and ReminderDelivery (request ID, latest permission version, outcome/suppression). Saving a plan does not authorize messaging. An ordinary visitor command creates a plan; the model has no write permission. Refund/payment and subsequent admission retain their original authorities.

Park Operations owns ZoneEntryObservation (zone, counter, direction, occurred/received times, epoch/sequence, quality) and ZonePeriodMetric (covered/open minutes, counted entries, excluded intervals, calibration result, entries per covered operating hour). Re-entry is another observation, not a new identified person. No visitor identity is joined from these counter events. Reporting derives the 90-day return cohort from voluntarily linked adult accounts and actual admissions, separately from anonymous popularity.

Published contracts include ReturnPlanSaved, ReminderPreferenceChanged and ReminderSuppressed. Delivery rechecks current preference; a delayed event cannot resurrect withdrawn permission. Import mappings retain source identifiers and provenance as described in the [coexistence contract](coexistence-and-migration.md).
