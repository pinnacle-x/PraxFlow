---
name: praxflow-spec-validate
description: Validate repository-local specification artifacts for completeness, traceability, conflicts, unresolved uncertainty, and implementation readiness.
---

# PraxFlow Spec Validate

Validate `docs/spec/` before implementation. This is a gate, not a design session.

## Read first

- `AGENTS.md`
- `CONTEXT.md` if present
- relevant `CONTEXT-MAP.md`
- `docs/adr/*`
- `docs/spec/*`
- relevant `docs/raw/*`

## Checks

At minimum check:
- required role-specific spec files exist
- source-of-truth ownership is correct
- spec does not duplicate or redefine external owner interfaces
- no unresolved `TODO_VERIFY` is hidden
- all externally derived facts have traceability when available
- no direct conflict with ADRs or context definitions
- test/verification expectations are present for implementable behavior
- acceptance criteria are observable
- dependencies on other repositories are explicit
- safety-related requirements are clearly marked and not inferred

## Result levels

Return exactly one overall result:
- `PASS`
- `PASS_WITH_WARNINGS`
- `BLOCKED`

`BLOCKED` is mandatory when unresolved uncertainty could lead to incorrect or unsafe implementation.

## Output

Create/update:
- `docs/spec/VALIDATION_REPORT.md`

The report must include:
- repository role
- checked files
- overall result
- blocking findings
- warnings
- traceability gaps
- cross-repository ownership issues
- unresolved decisions/TODOs
- recommended next action

## Rules

Do not fix product decisions by guessing. Do not generate production code. Minor mechanical spec formatting fixes may be proposed, but semantic fixes require the owner or human decision.
