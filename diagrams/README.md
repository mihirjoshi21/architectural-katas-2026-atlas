# Architecture drawings

The fourteen technical drawings D01–D14 each have editable **draw.io XML**, a vector SVG and a PNG. Twelve also have Mermaid specifications; the wireframes and authority matrix use native drawing objects. Every export includes its own notation key.

| ID | View | Notation / purpose |
|---|---|---|
| D01 | [Context](rendered/d01-context.svg) | C4 system context: people, estate platform and external systems |
| D02 | [Containers](rendered/d02-containers.svg) | C4 container view: runtime responsibilities, stores and boundaries |
| D03 | [Deployment](rendered/d03-edge-deployment.svg) | Physical deployment and distinct failure domains |
| D04 | [Admission](rendered/d04-offline-admission.svg) | UML sequence: validation, local commit and reconciliation |
| D05 | [Replay](rendered/d05-store-forward.svg) | UML sequence: lost receipt, retry and one effect |
| D06 | [Care](rendered/d06-care-workflow.svg) | UML state model: draft, review, approval, invalidation and outcome |
| D07 | [Animal monitoring](rendered/d07-animal-monitoring.svg) | Activity swimlanes: capture, analytics and keeper ownership |
| D08 | [Visitor assistant](rendered/d08-visitor-assistant.svg) | Data-flow view with trust and policy boundaries |
| D09 | [Maintenance](rendered/d09-maintenance-ml.svg) | Offline model lifecycle and operational release gate |
| D10 | [Domain ownership](rendered/d10-context-map.svg) | Context ownership and published contracts |
| D11 | [Popularity](rendered/d11-popularity.svg) | Observation-to-decision data lineage |
| D12 | [Roadmap](rendered/d12-roadmap.svg) | Relative-month phased timeline and funding gates |
| D13 | [Operator views](rendered/d13-operator-views.svg) | Low-fidelity wireframes with synthetic examples |
| D14 | [Authority](rendered/d14-authority.svg) | Permission matrix: capabilities and role boundaries |

Open the matching file in `drawio/` with diagrams.net to edit native shapes and connectors. The supplied SVG and PNG exports are ready to display. Keep an edited source and its exports consistent. No drawing is a site survey or a working product screenshot.

## Business and decision views

The README places these seven views beside the relevant decision or workflow. Images link to their full-size exports. V01–V04 are the supplied Miro views; V05–V07 have self-contained HTML sources, vector SVG exports and high-resolution PNG exports. They complement the technical drawings above.

| ID | View | Source |
|---|---|---|
| V01 | [ATLAS at a glance](rendered/v01-atlas-overview.png) | Supplied Miro view |
| V02 | [Visitor experience](rendered/v02-visitor-experience.png) | Supplied Miro view |
| V03 | [Keeper experience](rendered/v03-keeper-experience.png) | Supplied Miro view |
| V04 | [Popularity to action](rendered/v04-popularity-decision.png) | Supplied Miro view |
| V05 | [Pilot deployment and expansion gates](rendered/v05-pilot-and-expansion.png) | [Editable HTML](html/v05-pilot-and-expansion.html) |
| V06 | [Animal Care domain events](rendered/v06-care-domain-events.png) | [Editable HTML](html/v06-care-domain-events.html) |
| V07 | [Investment worksheet](rendered/v07-investment-scorecard.png) | [Editable HTML](html/v07-investment-scorecard.html) |

Open an HTML source locally to inspect or edit it. All styles are embedded; no external scripts, fonts or network access are required. The worksheet uses the existing executable cost model; it does not represent measured returns or a live spreadsheet.
