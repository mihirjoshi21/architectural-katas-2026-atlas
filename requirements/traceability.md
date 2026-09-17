# Requirement traceability

Every row links an explicit brief need to behavior, a decision, visual and verification. Verification IDs refer to the [evaluation plan](../validation/evaluation-plan.md). These are design coverage claims, not claims of implemented estate features.

| ID | Requirement | Design / decision | Diagram | Verification | Phase |
|---|---|---|---|---|---|
| R01 | Ticket purchase and family passes | [Workflow](../design/workflows.md), ADR-007/008 | D04 | V02 | Foundation |
| R02 | Popularity for staff and investment decisions | [Popularity measurement](../design/visitor-growth-and-popularity.md), ADR-009 | D11 | V07 | Foundation / insight |
| R03 | Animal health observations and response | [Care design](../design/ai-use-cases.md), ADR-006/011 | D06/D07 | V03/V06 | Foundation; conditional AI trial |
| R04 | How much/well animals eat | [Data model](../design/data-and-contracts.md), ADR-006/011 | D06/D07 | V03/V06 | Foundation; conditional AI trial |
| R05 | Piranha population levels | [Population workflow](../design/workflows.md), ADR-011 | D07 | V06 | Manual baseline then feasibility trial |
| R06 | Average attendance 5,000 toward 15,000 in three years | [Capacity](../design/capacity-and-costs.md), ADR-008 | D04/D12 | V08 | Three-year business horizon |
| R07 | Profitability | [Costs](../design/capacity-and-costs.md), [phases](../PHASED_IMPLEMENTATION.md), ADR-007 | D12 | V08 plus business baseline | All phases |
| R08 | Returning visitors | [Return-visit journey](../design/visitor-growth-and-popularity.md), ADR-010 | D08 | V05 plus cohort comparison | Foundation / AI trial |
| R09 | Patchy Wi-Fi | [Degraded modes](../design/degraded-modes.md), ADR-001/002/008 | D03/D04/D05 | V01/V02 | Foundation |
| R10 | Cloud with estate transmission path | [Architecture](../ARCHITECTURE.md), ADR-001/002/009 | D02/D03/D05 | V01/V08 | Foundation |
| R11 | Budget for MQTT-capable devices | [Assumptions](assumptions-and-targets.md), ADR-001 | D03 | Field protocol/power trial | Pilot |
| R12 | Comprehensive appropriate AI-assisted architecture | [Architecture](../ARCHITECTURE.md), ADR-003–007/010/011 | D01/D02/D07–D09 | V04/V05/V06 | Evidence-gated |

## Quality scenarios

| ID | Stimulus / environment | Expected response and measure |
|---|---|---|
| Q01 | WAN unavailable, local sensor links/power available | Retain accepted events to the chosen bounded capacity; V01 accounts for accepted IDs and effects. |
| Q02 | Local gate isolated from redemption authority | Automatic single-use redemption unavailable; staffed exceptions and later reconciliation visible. |
| Q03 | Changed care evidence after approval | Reject stale task/action version; re-review and audit; V03. |
| Q04 | Budget unavailable/exhausted or model request exceeds deadline | Stop cloud calls/retries and return approved fallback; V04/V05. |
| Q05 | Stale ride/queue fact beyond T04 | Mark age; no assertion of current availability or route based on unverified openness. |
| Q06 | Cloud recovery under simultaneous fresh and backlog traffic | Restore and replay without lost accepted identities or repeated effects within ratified load/recovery targets. |
| Q07 | Model sees unknown asset/poor footage | Quality gate/abstention and manual baseline; no confident invented estimate. |

[Diagram index](../diagrams/README.md) · [ADR index](../adrs/README.md) · [Actual evidence](../validation/evidence-index.md)
