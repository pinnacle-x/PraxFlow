---
name: praxflow-protocol-validate
description: Perform protocol-specific validation of machine-readable and human-readable communication specifications before consumers implement them.
---

# PraxFlow Protocol Validate

Validate protocol artifacts in the protocol owner repository. This is stricter than generic spec validation.

## Read first

- `AGENTS.md`
- `CONTEXT.md` if present
- `docs/raw/*`
- `docs/adr/*`
- `docs/spec/PROTOCOL.md`
- `docs/spec/REGISTER_MAP.json`
- `docs/spec/COMMANDS.json`
- `docs/spec/ERROR_CODES.json`
- `docs/spec/TEST_VECTORS.json`

## Required checks

Check at least:
- duplicate/overlapping addresses
- address syntax and ranges
- function/opcode uniqueness
- request/response mapping
- frame length rules
- CRC/checksum definition and known vectors
- byte order and word order
- signed vs unsigned types
- scale and offset
- units
- access mode (`R`, `W`, `RW`)
- enum completeness
- error/exception codes
- broadcast behavior
- timeout/retry semantics when protocol-owned
- reserved ranges
- version/compatibility rules when present
- source file/page traceability
- unresolved `TODO_VERIFY`
- consistency between human-readable and machine-readable forms

## Test vectors

Where the source defines enough information, ensure `TEST_VECTORS.json` includes independently checkable examples. Do not generate expected values by simply reusing the same implementation algorithm without an independent source.

## Result

Return exactly one:
- `PASS`
- `PASS_WITH_WARNINGS`
- `BLOCKED`

## Output

Create/update:
- `docs/spec/PROTOCOL_VALIDATION_REPORT.md`

The report must list every blocking ambiguity explicitly. Do not mutate consumer repositories. Do not invent missing protocol semantics.
