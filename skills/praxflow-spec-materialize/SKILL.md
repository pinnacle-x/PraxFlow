---
name: praxflow-spec-materialize
description: Materialize an approved or draft tracker/spec artifact into repository-owned specification files appropriate to the repository role.
---

# PraxFlow Spec Materialize

Convert a specification source (for example a GitHub/GitLab issue, approved design artifact, or existing canonical spec) into repository-local structured specification files without changing meaning.

## Read first

- `AGENTS.md`
- repository role
- `CONTEXT.md` if present
- relevant `CONTEXT-MAP.md`
- `docs/adr/*`
- `docs/raw/*` when the spec depends on extracted evidence

## Source requirement

Require a concrete source identifier or file. Record the source; do not fabricate one.

## Role-specific outputs

### system
Create/update under `docs/spec/`:
- `SYSTEM_SPEC.md`
- `SUBSYSTEM_ALLOCATION.md`
- `INTERFACE_CATALOG.md`
- `SYSTEM_TEST_PLAN.md`
- `SPEC_SOURCE.json`

### protocol
Create/update:
- `PROTOCOL.md`
- `REGISTER_MAP.json`
- `COMMANDS.json`
- `ERROR_CODES.json`
- `TEST_VECTORS.json`
- `SPEC_SOURCE.json`

### pc
Create/update:
- `PC_SPEC.md`
- `UI_REQUIREMENTS.md`
- `DATA_MODEL.md`
- `TEST_PLAN.md`
- `SPEC_SOURCE.json`

### controller
Create/update:
- `CONTROLLER_SPEC.md`
- `STATE_MACHINE.md`
- `IO_MAP.md`
- `SAFETY_REQUIREMENTS.md`
- `TEST_PLAN.md`
- `SPEC_SOURCE.json`

### module
Create/update:
- `MODULE_SPEC.md`
- `IO_MAP.md`
- `COMMUNICATION_REQUIREMENTS.md`
- `TEST_PLAN.md`
- `SPEC_SOURCE.json`

## Traceability

Every specification item derived from source PDFs must preserve source file/page when available. Machine-readable protocol artifacts should include source metadata per item.

`SPEC_SOURCE.json` must record:
- source type
- source identifier
- repository role
- status: `draft` or `approved`
- materialized timestamp if available

## Rules

- Do not add requirements missing from the source.
- Do not resolve `TODO_VERIFY` by guessing.
- Preserve approved ADR decisions.
- Keep public interfaces in their owner repository.
- Do not generate production code.

Stop when local spec artifacts faithfully represent the source.
