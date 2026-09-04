# PraxFlow Workflow

PraxFlow coordinates product-level engineering across multiple independent Git repositories. It complements, rather than replaces, general engineering skills such as design review, specification, TDD, implementation, diagnosis, and code review.

## 1. Workstation setup

Install general engineering skills globally once. Install PraxFlow as a Codex skill-only plugin. Do not duplicate the same general skills into every product repository unless a project intentionally pins them.

## 2. Product workspace

A product workspace is normally **not** a Git repository. It contains independent repositories such as:

```text
product/
├── manifest/
├── system/
├── protocol/
├── pc/
├── controller/
├── module-temperature/
└── module-io/
```

Later, Android `repo`/manifest may populate the same directory layout. Each child remains an independent Git repository with its own branch, commits, merge requests, and tags.

## 3. Initialize each repository

For every new repository:

1. Run the general agent setup skill (for example `setup-matt-pocock-skills`) once for that repository.
2. Run `praxflow-repo-bootstrap` with the repository role.
3. Run `writing-for-agents` or equivalent to review `AGENTS.md` without adding speculative product facts.

Key output: repository-specific `AGENTS.md` plus durable directory scaffolding.

Do **not** create `CONTEXT.md`, ADRs, or formal specs merely because the repository exists.

## 4. Put source documents in the owner repository

Examples:

- product/system requirements → `system/input/`
- shared communication protocol PDF → `protocol/input/`
- controller-owned vendor/manual source → `controller/input/`
- module-specific source → that module's `input/`

A fact should have one owner repository.

## 5. Ingest PDFs

Run `praxflow-pdf-ingest` on source PDFs.

Outputs:

```text
docs/raw/<stem>_raw.md
docs/raw/<stem>_extraction_report.md
```

This stage extracts evidence only. It does not create product decisions or production code.

## 6. Discover the system

In the system repository, run `praxflow-system-discovery` after relevant source material is ingested.

Outputs:

```text
CONTEXT-MAP.md
docs/system/SYSTEM_FACTS.md
docs/system/OPEN_DECISIONS.md
```

The skill classifies unresolved decisions as LOW, MEDIUM, HIGH, or CRITICAL.

## 7. Conditionally use Grill / deep design review

Do not Grill every task.

If `OPEN_DECISIONS.md` contains HIGH or CRITICAL decisions, present them to the user and recommend `/grill-with-docs`. Human approval is required to enter that design-review mode.

Typical Grill candidates:

- ownership of a real-time control loop
- behavior after PC/controller/module disconnection
- safety-state ownership
- public protocol compatibility strategy
- cross-repository responsibility boundaries

Routine facts already defined by source documents do not require Grill.

Confirmed domain terms may create/update `CONTEXT.md`; significant hard-to-reverse decisions may create ADRs under `docs/adr/`.

## 8. Create the specification source

Use the general specification skill (for example `/to-spec`) after important decisions are resolved. The canonical upstream spec may live in a tracker issue or another configured specification surface.

Do not duplicate its semantics manually.

## 9. Materialize repository-local specs

Run `praxflow-spec-materialize` with the concrete spec source.

Outputs vary by repository role. Examples:

### System

```text
docs/spec/SYSTEM_SPEC.md
docs/spec/SUBSYSTEM_ALLOCATION.md
docs/spec/INTERFACE_CATALOG.md
docs/spec/SYSTEM_TEST_PLAN.md
docs/spec/SPEC_SOURCE.json
```

### Protocol

```text
docs/spec/PROTOCOL.md
docs/spec/REGISTER_MAP.json
docs/spec/COMMANDS.json
docs/spec/ERROR_CODES.json
docs/spec/TEST_VECTORS.json
docs/spec/SPEC_SOURCE.json
```

### PC

```text
docs/spec/PC_SPEC.md
docs/spec/UI_REQUIREMENTS.md
docs/spec/DATA_MODEL.md
docs/spec/TEST_PLAN.md
docs/spec/SPEC_SOURCE.json
```

### Controller

```text
docs/spec/CONTROLLER_SPEC.md
docs/spec/STATE_MACHINE.md
docs/spec/IO_MAP.md
docs/spec/SAFETY_REQUIREMENTS.md
docs/spec/TEST_PLAN.md
docs/spec/SPEC_SOURCE.json
```

## 10. Validate specs

Run `praxflow-spec-validate` in every implementation repository before production implementation.

Output:

```text
docs/spec/VALIDATION_REPORT.md
```

Protocol repositories additionally run `praxflow-protocol-validate`.

Output:

```text
docs/spec/PROTOCOL_VALIDATION_REPORT.md
```

A BLOCKED report prevents implementation until the blocking uncertainty is resolved.

## 11. Human approval gate

A human approves the specification using the team's chosen mechanism (for example an approved label/status in GitHub/GitLab plus `SPEC_SOURCE.json` status).

Production implementation must not begin from an unapproved spec.

## 12. Implement

For a large approved spec, use a ticket decomposition skill (for example `/to-tickets`) and create a feature branch before implementation.

Then use the general implementation skill (for example `/implement #ticket`). The implementation layer should perform TDD where appropriate, build/test, code review, and commits according to the repository's own rules.

For a small, already-clear behavior, direct `/tdd` is enough; do not re-run Grill/specification for every atomic task.

## 13. Cross-repository public interface changes

Before changing a public contract, run `praxflow-interface-change` from a workspace that can see the relevant repositories.

Output:

```text
system/docs/changes/IC-XXXX-<slug>.md
```

Implement owner-first:

1. update and approve the owner spec
2. update owner implementation if needed
3. update consumers
4. run integration/system verification

Consumers must never redefine public protocol semantics locally just because the current contract is inconvenient.

## 14. System verification

After all affected repositories are implemented/reviewed, run `praxflow-system-verify`.

Output:

```text
system/docs/verification/VER-<id>.md
```

It records exact repository SHAs and separates automatic from manual/hardware verification. Manual checks remain `MANUAL_PENDING` until explicit evidence exists.

## 15. Product release

Only when system verification is PASS, run `praxflow-manifest-release` in the manifest repository.

Outputs:

```text
releases/vX.Y.Z.xml
releases/vX.Y.Z.md
```

Release manifests pin immutable revisions so the complete product version is reproducible.

## Compact lifecycle

```text
repo setup
  ↓
praxflow-repo-bootstrap
  ↓
PDF owner/input
  ↓
praxflow-pdf-ingest
  ↓
praxflow-system-discovery (system repo)
  ↓
HIGH/CRITICAL decisions? ─ yes → human-approved Grill
  ↓ no / resolved
specification
  ↓
praxflow-spec-materialize
  ↓
praxflow-spec-validate
  ↓
protocol? → praxflow-protocol-validate
  ↓
human approval
  ↓
implementation / TDD / review
  ↓
cross-repo? → praxflow-interface-change before contract changes
  ↓
praxflow-system-verify
  ↓
manual/hardware checks complete
  ↓
praxflow-manifest-release
```
