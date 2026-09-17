# Existing operations and controlled migration

### Fit with existing systems and controlled introduction

The brief provides existing physical operations and recently inspected rides, but **no existing software topology**. ATLAS does not assume that the estate already runs PostgreSQL, a ticketing platform or a particular cloud. Discovery inventories current ticket/pass products, payment settlement, animal ledgers, maintenance records, device interfaces, staff roles and data-export rights. Existing physical protection, inspections and emergency procedures remain independent of ATLAS.

| Step | Introduction and acceptance | Rollback boundary |
|---|---|---|
| Discover contracts | Record authoritative owners, identifiers, supported interfaces and data quality; select suppliers against offline redemption, timed entry and export requirements | Keep incumbent/manual operation if no acceptable integration exists |
| Import and reconcile | Map legacy/manual IDs explicitly; preserve original units, timestamps, author and uncertainty; compare ticket allowances, financial references and animal balances with source totals | Quarantine ambiguous records; never invent missing animal or financial facts |
| Shadow | Capture observations and produce comparison views without changing operational authority; staff review missingness, duplicate records and workflow effort | Stop capture/integration and retain existing procedures |
| Pilot cutover | Select one entrance domain and a limited care-record scope; explicitly transfer the relevant write authority after reconciliation and staff rehearsal | Do not run two independent redemption writers. On failure, stop automated redemption and reconcile its journal before returning authority |
| Expand selectively | Apply the evaluated contracts to the next site/capability; retain original-ID mappings and an export path | Roll back the failed capability rather than the whole estate; preserve accepted records and audit |

Availability, consistency and latency differ by boundary: local admission requires one writer; observations tolerate delayed cloud delivery; care approvals require current authority; reporting and AI may degrade to baseline. Integrations use versioned contracts rather than direct cross-system table writes. A legacy supplier that cannot support these semantics changes the integration decision and scope; it is not made compatible by drawing an adapter box.
