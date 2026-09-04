# Repository Roles

PraxFlow assumes a product may be composed from multiple independent Git repositories. Each repository should remain understandable, buildable, and reviewable on its own.

## `system`

Owns product-level structure and coordination:
- system boundary
- subsystem/context responsibilities
- cross-context relationship map
- system-level ADRs
- system requirements
- interface catalog
- system test plan
- cross-repository change records
- integrated verification records

Typical key files:

```text
AGENTS.md
CONTEXT.md                 # lazily created when system domain terms are confirmed
CONTEXT-MAP.md             # created/updated by system discovery
docs/system/SYSTEM_FACTS.md
docs/system/OPEN_DECISIONS.md
docs/adr/
docs/spec/
docs/changes/
docs/verification/
```

The system repository does not own PC/controller/module implementation or shared wire-level protocol semantics.

## `protocol`

Owns the shared communication contract:
- frame format
- messages/commands
- registers
- function/opcodes
- CRC/checksum definition
- data encoding
- public error codes
- protocol compatibility rules
- independent protocol test vectors

Typical key files:

```text
AGENTS.md
CONTEXT.md
docs/raw/
docs/adr/
docs/spec/PROTOCOL.md
docs/spec/REGISTER_MAP.json
docs/spec/COMMANDS.json
docs/spec/ERROR_CODES.json
docs/spec/TEST_VECTORS.json
```

## `pc`

Owns PC application internals:
- operator workflow
- UI/view models
- local application/data model
- device-client composition
- local persistence/reporting when assigned to PC
- PC-specific tests

It consumes public protocol/system contracts rather than redefining them.

## `controller`

Owns controller/firmware internals:
- real-time state machine
- control behavior assigned to the controller
- I/O handling
- sensor/actuator coordination
- safety behavior assigned to the controller
- firmware-specific tests

It consumes public protocol/system contracts rather than redefining them.

## `module`

Owns one independently versioned module. A module repo may be simple or complex; do not generate unnecessary documentation merely to match a template. Create `CONTEXT.md` and ADRs lazily when domain vocabulary/decisions justify them.

## `hardware`

Owns hardware design source/specification and hardware verification evidence. Keep vendor source PDFs with the hardware/module that owns the resulting facts.

## `manifest`

Owns repository composition and reproducible product versions:
- development repository list/path mapping (`default.xml`)
- immutable release combinations (`releases/*.xml`)
- release metadata (`releases/*.md`)

The manifest does not own product semantics.

## Workspace root

A workspace root containing these repositories is normally not itself a Git repository. Avoid a second top-level `AGENTS.md` unless the workspace is intentionally a managed repository. Cross-repository tasks should explicitly read the system and affected repository agent rules.
