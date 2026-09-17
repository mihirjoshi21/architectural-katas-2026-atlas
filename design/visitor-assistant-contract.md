# Visitor assistant contract

## Decision

**Product decision:** trial natural-language discovery of approved activities as the first AI capability. The hypothesis is that visitors can find a suitable activity with less effort than browsing search results and applying filters themselves. The interface distinguishes “Find an activity” from “Estate information.” Only activity discovery enters the model candidate contract; general-information questions use approved full-text search and excerpts. Public release starts in English. Spanish, French, German and Hindi remain separately reviewed trial languages; unsupported languages receive published English information and staff help. No translation quality is assumed.

### Retrieval and authority

Approved knowledge documents live in versioned object storage. A publishing job copies approved, unexpired text and structured facts into a PostgreSQL full-text index/read model, recording document ID, version, source URI, approver and expiry. Start with lexical retrieval over the small curated corpus; embeddings and a separate vector database are deferred until failed-query evaluation justifies them. Rank at most five eligible passages, with a bounded total input size. An empty or conflicting result uses search/help rather than an unconstrained answer. Retrieving approved content does not make embedded instructions trustworthy.

The estate application exposes read-only activity/status and approved-knowledge interfaces to the AI adapter. It also enforces a visitor-confirmed constraint object: access needs, available time and party restrictions. A model may propose an interpretation of natural language, but cannot silently relax these confirmed constraints. The initial activity product returns up to three independent options, not a claimed optimal multi-stop route. Route descriptions and individual visit durations come from approved records; route optimization is outside the pilot.

Use one hosted model through the versioned adapter, with no write tools, a five-second total deadline, a maximum 500 output tokens and no automatic retry in the initial visitor flow. Input, output and any billed reasoning allowances must have provider-enforced bounds compatible with the reservation contract; reject a provider configuration whose maximum charge cannot be bounded. Provider/model selection is an evaluation gate, not a claim that an untested model is interchangeable.

### Fully specified example

The following values are **synthetic fixture data**, not actual estate facts or an observed model response. Evaluation time is 2026-09-18 14:00 UTC. The visitor asks: “We have 30 minutes, need a step-free route, and would prefer something indoors.” The visitor confirms `wheelchair=true` and `max_minutes=30` in the interface.

| Evidence | Approved fixture | Implication |
|---|---|---|
| `doc-access`, version 1, expires 19 September | A1 Aquarium Gallery: step-free, 20 minutes including approach; A2 Conservatory: step-free, 25 minutes; R1 requires wheelchair transfer | A1 fits the confirmed access/time constraints; R1 does not |
| `doc-weather`, version 1 | A1 and A2 are indoor activities | Either matches the indoor preference if currently usable |
| Status API, observed 13:59:30 UTC | A1 open; A2 closed | A2 cannot be offered as open; the A1 observation is 30 seconds old |

A hand-authored candidate illustrating the model contract is:

```json
{"activity_ids":["A1"],"source_refs":[{"id":"doc-access","version":1},{"id":"doc-weather","version":1}]}
```

For activity recommendations, the model selects IDs and evidence references; it does not supply unrestricted final prose. The application checks the schema, approved source versions/expiry, activity membership, closure/status age and confirmed access/time/height constraints. It rejects the whole candidate on a failed check and shows approved search/help. For a valid candidate, the interface renders the option from authoritative structured fields:

> Aquarium Gallery — step-free route; allow 20 minutes including the approach. Reported open at 13:59:30 UTC. Accessibility information: doc-access v1. Check current status again before setting out.

The exact wording is an authored template. It is not a model-quality result. A candidate containing A2 is rejected because the current status is closed. A status older than 120 seconds, a future-dated status, an expired source, an unrelated citation, or an unknown activity cannot establish a current valid option. A fresh check occurs at display; a later closure can still occur and the UI does not promise continued availability.

### What output checks establish

| Check | Mechanism | Limit |
|---|---|---|
| Shape and authority | Exact schema, ID allowlists, read-only service credentials, no write capability | Schema validity alone does not establish truth |
| Current operational facts | Join returned IDs to authoritative records; reject closed/stale/future/unknown status | Incorrect upstream observations can still mislead; field quality matters |
| Constraints | Apply visitor-confirmed access/time/height rules outside the model | The model must not be the sole interpreter of a consequential constraint |
| Source relationship | Require the current approved document version mapped to the displayed fact | A source existing is not proof that arbitrary prose follows from it |
| Explanatory language | Initial activity cards use templates; general information uses approved excerpts with source/expiry | Later free-form explanation needs separate human-supported semantic evaluation; no universal hallucination detector is claimed |

This narrows the model's role deliberately: natural-language discovery and candidate selection can add convenience while the presentation of consequential facts stays controlled. The [policy experiment](../spikes/visitor-policy/README.md) exercises this boundary with hand-authored candidates. It does not measure whether an LLM selects the right IDs or whether users prefer the assistant.

### Change, cost and failure

The knowledge owner previews changed content and its structured facts, publishes a version, and invalidates affected caches. Shared caches contain public information only and key on corpus/version/locale plus relevant status freshness. Public content is the only information sent to the model. Unknown or sensitive requests use an authenticated supplier workflow or staff handoff rather than placing private booking/care data into a prompt.

Reserve a maximum charge through a PostgreSQL budget row transaction keyed by UTC day and request ID. Admission requires settled usage plus outstanding reservations plus the new maximum to remain within USD 50/day. A duplicate request cannot reserve or call twice. Do not return an uncertain in-flight reservation to the spend pool after timeout; reconcile it with provider usage or conservatively charge its reserved maximum. A budget outage starts no new call. The policy spike does not implement this concurrent reservation protocol.

Compare the same tasks against full-text search and filters using the same documents and status data. Freeze the corpus, provider/model, prompt, constraints and scoring rubric for a run. The visitor product owner owns the decision; a reviewer checks high-consequence facts and translations. If the assistant fails the release contract, keep the useful search/records foundation and stop the assistant's incremental spend.
