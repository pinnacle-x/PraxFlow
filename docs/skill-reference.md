# PraxFlow Skill Reference

This file describes the maintained PraxFlow skills. The corresponding `skills/<name>/SKILL.md` remains the executable instruction source.

## `praxflow-repo-bootstrap`

**Use when:** creating or standardizing a system, protocol, PC, controller, module, hardware, or manifest repository.

**Typical invocation:**

```text
$praxflow-repo-bootstrap
role: system
```

**Reads:** current repository structure, existing `AGENTS.md`, existing agent metadata.

**Does:** establishes repository role, ownership rules, durable folders, implementation gates, source-of-truth references.

**Does not:** invent requirements, create speculative `CONTEXT.md`, ADRs, or formal specs.

## `praxflow-pdf-ingest`

**Typical invocation:**

```text
$praxflow-pdf-ingest input/DeviceManual.pdf
```

**Does:** extracts PDF evidence, preserves source file/page, identifies weak extraction/OCR candidates, marks uncertainty instead of guessing.

**Writes:**

```text
docs/raw/<stem>_raw.md
docs/raw/<stem>_extraction_report.md
```

## `praxflow-system-discovery`

**Use in:** the system repository after relevant source ingestion.

**Typical invocation:**

```text
$praxflow-system-discovery
```

**Does:** identifies evidence-backed contexts, responsibilities, interface ownership, and unresolved product decisions.

**Writes:**

```text
CONTEXT-MAP.md
docs/system/SYSTEM_FACTS.md
docs/system/OPEN_DECISIONS.md
```

**Decision policy:** classify unresolved decisions `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`. Recommend deep design review for `HIGH`/`CRITICAL`; do not invoke it automatically.

## `praxflow-spec-materialize`

**Typical invocation:**

```text
$praxflow-spec-materialize
source: issue #123
```

**Does:** converts a concrete reviewed/draft specification source into repository-owned structured files without changing meaning.

**Writes:** role-specific files under `docs/spec/` plus `SPEC_SOURCE.json`.

## `praxflow-spec-validate`

**Typical invocation:**

```text
$praxflow-spec-validate
```

**Checks:** completeness, unresolved `TODO_VERIFY`, source ownership, contradictions with ADRs, testability, implementation readiness.

**Writes:** `docs/spec/VALIDATION_REPORT.md`.

**Result:** `PASS`, `PASS_WITH_WARNINGS`, or `BLOCKED`.

## `praxflow-protocol-validate`

**Use in:** protocol repositories.

**Typical invocation:**

```text
$praxflow-protocol-validate
```

**Checks:** addresses, function/command codes, frame lengths, CRC, endianness, signedness, scale/offset, units, permissions, enumerations, error codes, source pages, unresolved verification markers.

**Writes:** `docs/spec/PROTOCOL_VALIDATION_REPORT.md`.

## `praxflow-interface-change`

**Typical invocation:**

```text
$praxflow-interface-change
goal: Add StartTest command.
```

**Does:** identifies owner repository, affected consumers, compatibility risk, required update order, verification plan.

**Writes:** `system/docs/changes/IC-XXXX-<slug>.md`.

**Rule:** owner spec first; consumers never redefine a shared contract locally.

## `praxflow-system-verify`

**Typical invocation:**

```text
$praxflow-system-verify
change: IC-0001
```

**Does:** records exact repository SHAs, runs/records repository tests, integration checks, and separates automated from manual/hardware evidence.

**Writes:** `system/docs/verification/VER-<id>.md`.

**Result:** `PASS`, `BLOCKED`, or `FAIL`.

## `praxflow-manifest-release`

**Typical invocation:**

```text
$praxflow-manifest-release
version: 1.0.0
verification: system/docs/verification/VER-RC-001.md
```

**Precondition:** system verification is `PASS`.

**Writes:**

```text
releases/vX.Y.Z.xml
releases/vX.Y.Z.md
```

The XML pins the tested repository revisions so the complete product can be reproduced.
