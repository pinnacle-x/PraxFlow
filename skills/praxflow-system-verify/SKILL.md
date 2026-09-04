---
name: praxflow-system-verify
description: Verify an integrated multi-repository product change against system test requirements and record exact repository revisions and manual checkpoints.
---

# PraxFlow System Verify

Run or coordinate product-level verification after affected repositories have implemented and reviewed a change.

## Inputs

Accept a change ID, release candidate identifier, or explicit verification goal.

## Read first

- `system/AGENTS.md`
- `system/docs/spec/SYSTEM_TEST_PLAN.md`
- related `system/docs/changes/IC-*.md`
- affected repository `AGENTS.md`
- affected repository test/build instructions
- `manifest/default.xml` when available

## Actions

1. Record current branch/tag/commit SHA for every affected repository.
2. Run repository-local automated build/test commands when available.
3. Run integration tests defined by the system test plan.
4. Check public interface/spec versions match the verified revisions.
5. List hardware/manual tests that cannot be performed automatically.
6. Never mark a manual/hardware test `PASS` without explicit evidence supplied by a human or test system.

## Status values

For each check use:
- `PASS`
- `FAIL`
- `BLOCKED`
- `MANUAL_PENDING`
- `NOT_APPLICABLE`

Overall verification is `PASS` only when all required automatic and manual checks are `PASS` or `NOT_APPLICABLE`.

## Output

Create in the system repository:
- `docs/verification/VER-<id>.md`

Include:
- verification goal/change ID
- exact repository revisions
- spec/interface revisions
- commands executed
- automatic test results
- integration results
- hardware/manual results
- failures/blockers
- overall result
- evidence references

Do not create a release manifest when overall result is not `PASS`.
