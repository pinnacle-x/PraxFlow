---
name: praxflow-repo-bootstrap
description: Bootstrap a repository for PraxFlow. Use when starting or standardizing a system, protocol, PC, controller, module, hardware, or manifest repository.
---

# PraxFlow Repository Bootstrap

Create only durable repository scaffolding and agent rules. Do not invent product requirements, domain terminology, architecture decisions, or implementation details.

## Inputs

Require or infer exactly one repository role:
- `system`
- `protocol`
- `pc`
- `controller`
- `module`
- `hardware`
- `manifest`

If the role cannot be inferred safely, ask once.

## Preconditions

- The current directory is a Git repository.
- Preserve an existing `AGENTS.md`; edit it instead of replacing unrelated rules.
- Preserve metadata created by other installed engineering-skill packs or repository tooling unless it conflicts with an explicit PraxFlow requirement.

## Actions

1. Detect the repository role and current structure.
2. Ensure `AGENTS.md` contains concise PraxFlow sections for:
   - repository role and ownership
   - required reading order
   - source-of-truth references
   - cross-repository boundaries
   - PDF handling rules when applicable
   - implementation gates
   - build/test expectations when known
   - prohibited actions
3. Create only directories appropriate to the role.
4. Do not create speculative `CONTEXT.md`, `CONTEXT-MAP.md`, ADRs, or formal specs.

## Role scaffolds

### system
Create: `input/`, `docs/raw/`, `docs/system/`, `docs/adr/`, `docs/spec/`, `docs/changes/`, `docs/verification/`, `tools/`.

### protocol
Create: `input/`, `docs/raw/`, `docs/adr/`, `docs/spec/`, `tools/`, `tests/`.

### pc/controller/module
Create: `docs/adr/`, `docs/spec/`, `src/`, `tests/`, `tools/`. Add `input/` only when this repo owns source documents.

### hardware
Create: `input/`, `docs/raw/`, `docs/spec/`, `docs/verification/`.

### manifest
Create: `releases/`, `docs/`; create `default.xml` only if repository membership is already known.

## Required AGENTS.md policy

PraxFlow rules must state:
- One fact has one owner repository.
- Consumers reference owner specs instead of maintaining divergent copies.
- Unknown or conflicting facts are never guessed.
- Production implementation requires an approved implementation source.
- Cross-repository interface changes use `praxflow-interface-change`.
- Release combinations are recorded by the manifest repository.

## Output

Report:
- repository role
- files/directories created or changed
- any unresolved bootstrap assumptions
- next recommended step

Stop after bootstrap. Do not begin product design or implementation.
