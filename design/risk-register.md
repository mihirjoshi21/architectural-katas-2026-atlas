# Risk register

Likelihood/impact are qualitative planning judgments. Residual risks need named human acceptance before field deployment; the role labels below are not evidence of sign-off.

| ID | Risk / trigger | Likelihood / impact | Mitigation and evidence | Owner / residual |
|---|---|---|---|---|
| K01 | Local coverage/power unavailable | High / high | Field survey, local fallback, power design and staged installation | Field lead; unsampled/lost readings remain possible. |
| K02 | Gateway media/power failure loses unsent records | Medium / high | Durable commits, appropriate media/power, backup/custody plan, power-cut endurance trial | Edge lead; software replay test does not prove hardware durability. |
| K03 | Offline ticket reuse/revocation delay | Medium / medium | Local authority, exception process, bounded key/revocation age, reconciliation | Admissions lead; stale unseen revocations possible. |
| K04 | Incorrect treatment or stale authorization | Medium / critical | Domain authority, task/version binding, approval/effect audit, escalation distinction | Care lead; human error still exists. |
| K05 | Camera cannot count representative population | High / high | Manual baseline, quality gate, keeper labels and undercount analysis | Model/care lead; remove trial if infeasible. |
| K06 | Sparse maintenance labels make model ineffective | High / medium | Baseline first, data readiness, time/asset splits and shadow trial | Maintenance lead; do not promise predictive benefit. |
| K07 | Provider changes quality/price or becomes unavailable | Medium / medium | Evaluated adapter, bounded spend, static fallback and rollback | AI owner; graceful degradation reduces functionality. |
| K08 | Alerts overload staff | Medium / high | Measure false alerts and review time; suppress duplicates; tune under authority | Operations/care lead; staffing budget may increase. |
| K09 | Underestimated installation/support/delivery cost | High / high | Full scenario cost model, quotations and pilot stop/go | Sponsor; estimates not supplier commitments. |
| K10 | Attendance grows beyond physical service capacity | Medium / high | Arrival/lane/staff/site-capacity model, approved capacity process | Operations; software does not create safe physical capacity. |
| K11 | Privacy/retention obligations differ from assumptions | Medium / high | Jurisdiction review, aggregate sensing, minimum personal data, role separation | Records owner; obligations unresolved. |
| K12 | Contradictory documents or unproven success claims | Medium / high for submission | Single targets registry, linked decisions, actual evidence status and docs check | Architecture lead; human review still required. |
| K14 | Disaster restore loses previously acknowledged cloud records | Medium / high | T05 states an RPO; test recoverable logs/backups and reconcile critical-record obligations before deployment | Platform/records owner; final delivery receipt is not an unlimited DR guarantee. |
| K13 | Deadline/registration/access mismatch | Unknown / critical for entry | Confirm organizer messages and actual repo/form visibility | Team lead; package does not submit or register itself. |

Revisit high-impact assumptions after the pilot or any incident/model/provider change. Record accepted residual risk, date and actual human owner; do not fill these fields with invented approvals.
