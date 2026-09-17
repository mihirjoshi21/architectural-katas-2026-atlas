# ADR-006: Task-specific human authority for animal-care actions

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R03, R04, R05 |
| Related visual | D06; [diagram index](../diagrams/README.md) |

## Context

Health and feeding observations require useful review and response. A generic signed keeper token does not prove intentional approval of one treatment against current evidence. Notification, review and execution have different urgency and authority.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Fully automatic intervention | Minimal review delay | Incorrect intervention and unclear authority; rejected. |
| Passive dashboard only | Simple and familiar | Missed review/escalation risk; not sufficient alone. |
| Versioned review workflow with independent notification | Clear accountability and current evidence | Reviewer staffing and offline role policy required; selected. |

## Decision

Record observations with subject/group, measurement units, occurrence time, evidence and quality. Create a review task when manual policy or advisory AI warrants it. Task approval binds actor, required role, task ID/version, exact action, reason and expiry; validate again before execution. Changes to evidence/version require re-review. Commit approval/audit together and deduplicate digital commands and reports. Physical outcomes are separately recorded as completed, failed or unknown; unknown outcomes require reconciliation.

Urgent notification and escalation do not wait for treatment approval. No generic barrier movement or clinical threshold is invented here. Existing emergency procedures and appropriate domain authority remain necessary. Offline staff kiosks support capture-only observation drafts under cached expiring roles. New digital care approvals and execution authorizations require the cloud authority and current evidence. Reconnection revalidates roles and drafts. Existing local emergency procedures remain independent; otherwise staff use the manual process.

## Consequences

Humans remain fallible; this is not a zero-risk claim. Alert workload and unavailable reviewers must be planned. Per-animal versus group feeding data may have uncertainty. Population estimates and keeper-confirmed records remain distinct.

## Verification and revisit trigger

Specified tests cover wrong role, missing/expired/replayed approval, stale version, concurrent review, repeated execution and unavailable reviewer escalation. The care workflow remains specified and requires an integrated test and domain walkthrough. Revisit when workflows, staffing or intervention types change.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)

## Offline grants and uncertain outcomes

Capture grants are device-bound, valid at most twelve hours, and renewable only while connected. After expiry use manual records; the 72-hour telemetry buffer does not extend staff access. Quarantine revoked/uncertain drafts for review after reconnect. Physical actions are not made idempotent by recording them: deduplicate reports by attempt ID, preserve completed/failed/unknown outcomes and reconcile unknown outcomes before repeating anything. [Operational protocol](../design/authority-recovery.md).
