# ADR-008: Signed entitlements and local redemption authority

| Field | Value |
|---|---|
| Status | Accepted architecture decision |
| Date | 2026-09-16 |
| Authority | Team ATLAS; release owners identified below |
| Requirements | R01, R06, R09 |
| Related visual | D04; [diagram index](../diagrams/README.md) |

## Context

Visitors need useful admission when WAN is intermittent. Authenticity, current revocation knowledge, payment settlement and single-use redemption are separate properties. HMAC uses a shared secret; the earlier public-key HMAC description was incorrect.

## Alternatives

| Option | Benefit | Cost / reason |
|---|---|---|
| Cloud-only redemption | One online authority | WAN failure blocks entry; insufficient on its own. |
| Independent offline validators | High local availability | Duplicate redemption across disconnected gates; not selected for automatic single-use admission. |
| Signed tickets plus one local admission authority/domain | Offline authenticity and coordinated redemption on local LAN | Authority/LAN failures require staffed fallback; selected. |

## Decision

Use public-key signed entitlements with issuer/key ID, validity, product/version and party allowance. Use a standard signature library; proposed Ed25519 needs supplier/platform compatibility confirmation. Provision the local authority and admission LAN at the main entrance. Validators check signature, policy and known revocations, then request atomic redemption from that authority. Gate isolation moves admission to the logged staff exception process instead of inventing independent global single use.

Reconcile issuance, payment, redemption, refund/revocation and occupancy separately. Increment occupancy only on entry, decrement on exit, handle re-entry under pass policy. Offer printed/staffed alternatives. Restrict offline signing authority; scanners do not receive issuer private keys.

A warm spare may recover the authority only after the old primary is fenced, the committed journal is verified and the authority generation is changed. If journal completeness cannot be established, continue logged staff exceptions until reconciliation; do not silently reset redemption state.

## Consequences

Revocations newer than the local snapshot may be missed within the chosen freshness policy. Authority failure reduces throughput. Family party/re-entry/exception rules need operations confirmation. This design does not grant offline card authorization.

## Verification and revisit trigger

Specify tamper, expiry, key rotation, clock skew, party size, duplicate/concurrent redemption, gate isolation, stale revocation and reconciliation tests. Supplier feasibility and hardware speed are not validated here. Revisit multi-entrance authority partitioning if site topology requires it.

[Evidence status](../validation/evidence-index.md) · [Targets and assumptions](../requirements/assumptions-and-targets.md) · [ADR index](README.md)

## Recovery and demand policy

Require physical fencing, a complete reconciled redemption journal and authenticated re-enrollment at the new generation before spare activation. The new authority serves only enrolled validators. Incomplete state or uncertain fencing keeps automatic redemption disabled. Generation comparison alone is not fencing. [Recovery contract](../design/authority-recovery.md).

Plan twelve lanes at five seconds per person, with a proposed timed-entry release cap of 1,500 people per fifteen minutes. This cap leaves about 31% headroom against the simplified 2,160-person theoretical slot capacity. Walk-ups consume the same capacity. It is a throughput assumption, not an established estate layout; validate passage variability, party handling, queue space and accessible lanes before allocating slots.
