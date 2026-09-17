# Visitor evaluation fixtures

`visitor-fixture.json` is an invented, versioned estate information set: opening hours, family-pass rules, facilities, accessibility, food, transport, language policy and timestamped activity status. It is not actual estate information.

`visitor-scenario-specifications.json` contains 48 cases with a base-fixture reference, exact overrides, required facts/sources, forbidden claims and expected decision classes. No model results are populated. Cases cover ordinary, unknown, stale/closed, adversarial, multilingual and accessibility behavior. Initial public language support is English; multilingual cases also define separately gated trial variants.

Run `python validation/scripts/check_visitor_fixtures.py` from the repository root to resolve references and overrides. This checks specification integrity, not model answers. `python -m unittest discover -s validation/tests -p 'test_visitor_policy.py' -v` exercises a separate narrow deterministic policy with hand-authored candidates.

[Execution and scoring](../evaluation-plan.md) · [Worked journey](../../design/visitor-assistant-contract.md). All values, people and activity records in fixtures are synthetic. No animal training data, field labels or visitor experiments are represented by these files.
