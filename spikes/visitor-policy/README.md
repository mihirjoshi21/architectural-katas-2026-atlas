# Visitor activity policy experiment

This small Python experiment checks a narrow architectural boundary: a model-shaped candidate selects activity IDs, but current authoritative data and explicit visitor constraints determine what may be displayed. It makes no provider calls and does not measure language understanding, retrieval, translation, semantic groundedness or user benefit.

Run from the repository root:

```bash
python -m unittest discover -s validation/tests -p 'test_visitor_policy.py' -v
```

The eighteen tests challenge closed and inaccessible activities, old/future status, expired or unrelated citations, source versions, missing authority data, time/height constraints, extra generated fields, unknown budget/provider state and malicious document text. Input candidates are hand-authored synthetic fixtures, not observed LLM responses. The injection test establishes only that this deterministic function does not interpret document prose as authority.

The candidate contract accepts `activity_ids` and `source_refs` only. Facts displayed to visitors are copied from the approved structured records. Multiple returned activities are independent alternatives; this experiment does not solve routing or add their durations into an itinerary. In production, visitor-confirmed accessibility, time and party constraints must enter independently of the model. Source authentication, strict API input validation, retrieval and actual atomic budget reservations are outside this experiment.

[Worked example](../../design/visitor-assistant-contract.md) · [Synthetic fixtures](../../validation/datasets/visitor-fixture.json) · [Recorded output](../../validation/results/visitor-policy-tests.txt)
