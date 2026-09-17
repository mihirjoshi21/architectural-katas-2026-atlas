# Domain model and event-storming synthesis

This is a document-based domain synthesis, not a claim that a facilitated event-storming workshop took place. Use it to guide a human walkthrough and record unresolved hotspots.

![Context ownership](diagrams/rendered/d10-context-map.svg)

## Bounded contexts

| Context | Owns | Published contracts |
|---|---|---|
| Visitor & Admissions | Ticket products, entitlements, admission/redemption, visitor preference choices, loyalty cohorts | TicketIssued, AdmissionRecorded, ExitRecorded, EntitlementRevoked |
| Park Operations | Ride status, inspection/work orders, zones, popularity read models and staff decisions | RideStatusChanged, InspectionRequested, ZoneObservationRecorded, StaffAllocationRecorded |
| Animal Care | Animal/group profile, feeding and health observations, population reconciliation, care tasks and outcomes | FeedingObservationRecorded, AnimalObservationRecorded, PopulationEstimateRecorded, PopulationConfirmed, CareActionApproved, CareActionCompleted, CareActionFailed, CareActionOutcomeUnknown |

Edge ingestion, identity, AI and reporting are supporting capabilities. A shared physical database can host separate schemas; ownership and interfaces prevent modules from silently changing each other's state. Cross-context business effects use transactional outboxes and idempotent consumers; raw sensor chatter is not automatically a meaningful domain event.

[![Animal Care event-storming synthesis](diagrams/rendered/v06-care-domain-events.png)](diagrams/rendered/v06-care-domain-events.png)

The outcome events branch directly from `ReportCareOutcome`; completed, failed and unknown are alternatives, never a required sequence. Unknown outcomes require qualified reconciliation before another action.

## Events, commands and policies

| Command | Resulting event | Policy / boundary |
|---|---|---|
| IssueEntitlement | TicketIssued | Only after authorized issuance/payment state; issuance does not increase occupancy. |
| RedeemEntitlement | AdmissionRecorded | Local admission authority checks party size and prior use; increase occupancy from entry. |
| RecordExit | ExitRecorded | Decrease occupancy; re-entry follows explicit pass policy. Missing exits reduce confidence. |
| RecordFeedingObservation | FeedingObservationRecorded | Preserve offered/consumed units, time, observer and quality; flagged exceptions create review tasks. |
| EstimatePopulation | PopulationEstimateRecorded | Store model/manual estimate and quality separately; no overwrite of confirmed population. |
| ConfirmPopulation | PopulationConfirmed | Keeper records independent reference method/date plus reconciliation; visible camera counts alone cannot confirm enclosure total. |
| ReviewCareAction | CareActionApproved or CareActionRejected | Approval binds task, version, action, actor and expiry; changed observation requires re-review. |
| AuthorizeActionAttempt | CareActionAttemptAuthorized | Recheck role, task version and expiry; record attempt ID. |
| ReportCareOutcome | CareActionCompleted, CareActionFailed or CareActionOutcomeUnknown | Deduplicate digital reports; reconcile unknown physical outcomes before any new action. Approval alone is not completion. |
| RequestInspection | InspectionRequested | Mechanic triages; ML advice never overrides inspection authority. |
| RecordZoneObservation | ZoneObservationRecorded | Compute aggregate popularity with coverage and freshness; do not infer identity. |
| AllocateStaff | StaffAllocationRecorded | Manager decides and records reason; later compare outcomes. |

Emergency notification is independent of treatment approval. Physical protection follows separately engineered procedures; event-driven reporting must not become a newly invented mandatory safety dependency.

## Hotspots to resolve through domain review

Family pass split-party/re-entry terms; refund/revocation latency; source of exit counts; individual versus group feeding measurements; acceptable uncertainty for population observations; who may approve each care action; response times for urgent symptoms; retention obligations; actual gate topology; local staff communications when Wi-Fi/power fails. These remain visible in [risk register](design/risk-register.md).

## Event semantics

Use past-tense events and imperative commands. Keep occurrence and receipt timestamps distinct. A priority queue can reorder unrelated events; preserve aggregate sequence semantics and explicitly handle gaps. “Global chronological replay” is not promised when clocks differ or messages are prioritized. [Data contracts](design/data-and-contracts.md)

## Return-visit and measurement events

Visitor commands SaveReturnPlan and ChangeReminderPreference produce ReturnPlanSaved and ReminderPreferenceChanged. A scheduled notification request checks current permission; withdrawal can produce ReminderSuppressed. Subsequent AdmissionRecorded establishes an observed return under the declared cohort rules. Saving a plan is not a booking and consent to one purpose does not grant another.

ZoneEntryObserved and ZoneCoverageMeasured feed Park Operations' popularity read model. They do not identify people or update visitor profiles. Clinical/physical staffing minima constrain any StaffAllocationRecorded decision. Migration preserves original identifiers and hands over each transactional authority explicitly.
