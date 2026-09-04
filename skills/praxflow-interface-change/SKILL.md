---
name: praxflow-interface-change
description: Plan and control a cross-repository public interface change before implementation. Use when a change affects system, protocol, PC, controller, modules, or compatibility boundaries.
---

# PraxFlow Interface Change

Create an owner-first change plan for a public interface change. Do not implement production code during this skill.

## Read order

When visible, read:
1. `system/AGENTS.md`
2. `system/CONTEXT-MAP.md`
3. `system/docs/spec/*`
4. owner repository `AGENTS.md` and `docs/spec/*`
5. affected consumer repository `AGENTS.md`, `CONTEXT.md`, and relevant specs
6. `manifest/default.xml`

If running inside a single repository, use available cross-repository references declared in `AGENTS.md`.

## Actions

1. Identify the interface owner repository.
2. Identify all consumers and affected repositories.
3. Classify the change as compatible, conditionally compatible, or breaking.
4. Identify specification changes required before implementation.
5. Identify implementation order.
6. Identify migration/versioning requirements.
7. Identify automated, integration, and hardware verification needed.
8. Detect `HIGH`/`CRITICAL` unresolved design decisions and recommend a human design review/Grill when needed.

## Output

Create in the system owner repository:
- `docs/changes/IC-XXXX-<slug>.md`

Choose the next available numeric ID without rewriting existing IDs.

The change file must contain:
- goal
- owner repository
- affected repositories
- current contract
- proposed contract
- compatibility impact
- required spec updates
- required implementation order
- required tests
- manual/hardware checkpoints
- unresolved decisions
- approval status

## Owner-first rule

Public interface semantics must be updated and approved in the owner repository before consumers implement them.

## Prohibited actions

- Do not implement consumer code.
- Do not silently alter protocol semantics inside a consumer.
- Do not mark a breaking change compatible without evidence.

Stop after producing the change plan and recommended next action.
