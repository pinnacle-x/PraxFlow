# Integration with General Engineering Skills

PraxFlow is intentionally narrow. It owns product-level workflow concerns that are not well covered by generic coding skills.

## Division of responsibility

### General engineering skills

Use general-purpose skills for:
- repository agent setup
- writing/refining `AGENTS.md`
- deep design grilling
- specification drafting
- ticket decomposition
- TDD
- implementation
- diagnosis/debugging
- code review
- architecture review
- handoff between sessions

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

## Conditional Grill

PraxFlow does not invoke Grill automatically.

`praxflow-system-discovery` classifies open decisions. If one or more decisions are `HIGH` or `CRITICAL`, it recommends a deep design review such as `/grill-with-docs` and presents the decision summary. A human decides whether to enter that interactive design process.

Do not Grill routine facts that are already explicit in source documents or approved specs.

## Specification flow

Recommended flow:

```text
evidence/raw
  ↓
system discovery
  ↓
conditional Grill
  ↓
general /to-spec (canonical spec source)
  ↓
praxflow-spec-materialize (repo-local structured artifacts)
  ↓
praxflow-spec-validate
```

The purpose of `praxflow-spec-materialize` is not to replace `/to-spec`; it transforms the approved/draft spec source into structured files owned by the repository.

## Implementation flow

For a large approved feature:

```text
/to-tickets
  ↓
create feature branch
  ↓
/implement #ticket
  ↓
TDD/build/test/review/commit
```

For a small, already-specified behavior:

```text
/tdd
```

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

Use architecture-review skills after meaningful code exists. PraxFlow does not duplicate architecture-analysis methodology.
