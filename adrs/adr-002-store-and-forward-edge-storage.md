# ADR-002: Durable outbox, final receipts and bounded replay

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R09, R10 |
| Related visual | D05; [diagram index](../diagrams/README.md) |

## Context

A WAN outage must not silently discard already accepted operational events. Finite storage, retries, process failure and collection vehicles make custody and deletion rules important. Accepted records need an explicit durable commit policy and measured storage behavior.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Memory buffer only | Simple, low writes | Lost on restart; rejected for accepted operational records. |
| SQLite WAL with FULL synchronous commits | Small operational footprint and durable transaction boundary | Storage latency/wear and hardware assumptions; selected for the outbox. |
| Replicated local log or managed edge appliance | Stronger local redundancy potential | More power, cost and operations; revisit if loss tolerance demands it. |

## Decision

Validate and persist each accepted event with a stable ID and content hash. Use WAL and FULL synchronous mode for this outbox; choose media/power based on measurement. Cloud inserts durable inbox identity/hash and its effect in one transaction. Same identity/content returns a receipt without repeating the effect; different content under the same identity is a conflict. The edge removes pending data only after matching final receipt. Prioritize operational classes while handling aggregate sequence/gaps explicitly.

Reserve storage by class and monitor both quota and physical free space. At the acceptance limit reject explicitly and alert locally; never acknowledge data that was not stored. Low-value summaries may be coalesced only under a declared policy. A carrier receipt is not a cloud receipt: keep the source copy until final acknowledgement or a separately approved redundancy policy.

After final receipt, retain acknowledged observation envelopes in a separate seven-day recovery archive, then expire them according to policy. Replay original IDs after a cloud restore. This archive is an implementation requirement beyond the small receipt/deduplication spike; it does not guarantee recovery of destroyed disks or cloud-only state.

## Consequences

WAL/FULL improves the committed-record boundary but does not survive destruction of a sole disk or guarantee every storage device honors flushes. Global chronological order is not promised. Batch acknowledgement loss creates duplicates, which are expected. Longer outage envelopes require measured capacity and an operational collection schedule.

## Verification and revisit trigger

The runnable spike tests restart recovery, lost receipts, duplicate/hash conflict handling, bounded acceptance and atomic inbox/effect behavior. It uses local SQLite at both ends; it is not a cloud, broker, concurrency-load, media endurance or physical power-cut certification. Perform hardware trials for the latter. Revisit at measured write latency/endurance, capacity or recovery failures.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)
