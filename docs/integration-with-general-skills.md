# Integration with General Engineering Skills

PraxFlow is intentionally narrow. It owns product-level workflow concerns that are not well covered by generic coding skills. It does **not** require a specific companion framework or agent runtime.

## Division of responsibility

### General engineering capabilities

Use any compatible general-purpose skill pack or native agent capability for:
- repository agent setup
- writing/refining `AGENTS.md`
- deep design grilling or brainstorming
- specification drafting
- ticket/task decomposition
- TDD
- implementation
- diagnosis/debugging
- code review
- architecture review
- handoff between sessions

Matt Pocock's engineering skills are one compatible option, but PraxFlow core skills must also work when those skills are absent.

### PraxFlow skills

Use PraxFlow for:
- repository role bootstrap
- PDF evidence ingestion
- system/context discovery
- local spec materialization
- spec validation
- protocol-specific validation
- cross-repository interface change control
- integrated system verification
- manifest-based releases

## Conditional deep-design review

PraxFlow does not start a deep-design review automatically.

`praxflow-system-discovery` classifies open decisions. If one or more decisions are `HIGH` or `CRITICAL`, it recommends an interactive deep-design review and presents the decision summary. A human decides whether to enter that process.

If a companion skill such as `grill-with-docs` is installed, it may be used. Otherwise use the current agent's native planning/brainstorming capability or another compatible design-review skill.

Do not run a design interview for routine facts that are already explicit in source documents or approved specs.

## Specification flow

Portable flow:

```text
evidence/raw
  ↓
praxflow-system-discovery
  ↓
conditional deep-design review
  ↓
canonical specification source
  ↓
praxflow-spec-materialize
  ↓
praxflow-spec-validate
```

A canonical specification source may be produced by a general spec skill, the agent's native planning workflow, an issue tracker artifact, or a reviewed design document.

When Matt Pocock skills are available, `/to-spec` is one compatible way to create that source. PraxFlow does not depend on that command.

## Implementation flow

For a large approved feature, use the environment's planning/task decomposition and implementation capabilities. With the Matt skill pack, one example is:

```text
/to-tickets
  ↓
create feature branch
  ↓
/implement #ticket
  ↓
TDD/build/test/review/commit
```

For a small, already-specified behavior, use a TDD capability directly where appropriate.

Do not force design/specification loops onto every atomic implementation task.

## Cross-repository changes

Before implementation when a public contract changes:

```text
praxflow-interface-change
  ↓
owner spec update + approval
  ↓
owner implementation
  ↓
consumer implementations
  ↓
praxflow-system-verify
```

## Architecture review

Use an architecture-review capability after meaningful code exists. PraxFlow does not duplicate general architecture-analysis methodology.

## Agent adapters

Agent-specific invocation syntax belongs in installation or adapter documentation, not in the canonical PraxFlow skills. See `docs/installation.md` and `docs/portability.md`.
