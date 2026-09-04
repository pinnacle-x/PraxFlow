# Source of Truth

PraxFlow uses explicit ownership to prevent multi-repository drift.

## Principle

**One fact has one owner repository.** Other repositories consume or reference that fact instead of maintaining independent semantic copies.

## Recommended ownership

| Information | Owner repository |
|---|---|
| Product/system boundary | `system` |
| Context relationships | `system/CONTEXT-MAP.md` |
| System requirements | `system/docs/spec/` |
| Shared communication protocol | `protocol/docs/spec/` |
| PC internal design | `pc` |
| Controller internal design | `controller` |
| Module internal design | corresponding module repo |
| Repository membership/development checkout | `manifest/default.xml` |
| Product release composition | `manifest/releases/*.xml` |

## Evidence layers

PraxFlow distinguishes evidence from interpretation:

```text
input/*.pdf
    ↓
docs/raw/*
    ↓
CONTEXT / ADR / approved specification
    ↓
implementation
```

- `input/*` is immutable source evidence.
- `docs/raw/*` is faithful extraction, not design.
- `CONTEXT.md` is confirmed domain language.
- `CONTEXT-MAP.md` maps contexts and responsibilities.
- `docs/adr/*` explains significant accepted decisions.
- `docs/spec/*` is the repository-local implementation contract.
- source code implements the approved contract; it does not redefine it.

## Conflict handling

If two sources disagree:

1. record the conflict explicitly
2. preserve both source references
3. mark the dependent item unresolved
4. block implementation when the conflict could change behavior or safety
5. resolve through the owner repository/human decision

Never resolve a conflict by silently preferring whichever document is easier to implement.

## Consumer rule

A consumer repository may cache generated artifacts for build convenience only when the generation/source relationship is explicit. It must not become a second semantic owner.

For public interface changes, use `praxflow-interface-change` and update the owner first.
