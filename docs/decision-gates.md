# PraxFlow Decision Gates

PraxFlow uses human gates where an agent should not silently choose product behavior.

## Gate 1 — High-impact open decision

Created by `praxflow-system-discovery`.

| Severity | Default action |
|---|---|
| LOW | continue; record if useful |
| MEDIUM | agent may recommend; document architectural outcomes |
| HIGH | present to user; recommend interactive deep design review |
| CRITICAL | stop and require explicit human approval |

Typical `HIGH`/`CRITICAL` topics include safety ownership, real-time control ownership, disconnect behavior, public protocol compatibility, and difficult-to-reverse cross-repository boundaries.

A deep-design tool such as `/grill-with-docs` is optional. PraxFlow decides that a decision needs review; a human decides whether to enter an interactive Grill session.

## Gate 2 — Specification readiness

Before production code, `praxflow-spec-validate` must not be `BLOCKED`.

For protocol repositories, `praxflow-protocol-validate` must also be acceptable.

## Gate 3 — Human spec approval

The team must explicitly approve the implementation source. The approval may be represented by issue labels/status plus `SPEC_SOURCE.json` status.

The agent must not interpret silence as approval.

## Gate 4 — Manual/hardware verification

Automated tests cannot mark a physical verification step as passed unless evidence exists. Use `MANUAL_PENDING` until a human records the result.

## Gate 5 — Product release

`praxflow-manifest-release` requires a referenced system verification report with overall `PASS`. Release manifests pin immutable tested revisions.
