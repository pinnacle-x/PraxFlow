# PraxFlow Quick Start

This is the recommended first-run procedure after PraxFlow and your general engineering skills are already installed.

Assume a product workspace like:

```text
D:\Products\DemoDevice\
├── manifest\
├── system\
├── protocol\
├── pc\
└── controller\
```

The workspace root is not a Git repository. Each child directory is an independent Git repository.

## 1. Bootstrap every repository

Open the repository with your agent and run the normal agent setup for that repository if needed. Then run PraxFlow.

System repository:

```text
$praxflow-repo-bootstrap
role: system
```

Protocol repository:

```text
$praxflow-repo-bootstrap
role: protocol
```

PC repository:

```text
$praxflow-repo-bootstrap
role: pc
```

Controller repository:

```text
$praxflow-repo-bootstrap
role: controller
```

Expected result: `AGENTS.md` is updated and durable folders are created. Do not expect `CONTEXT.md`, ADRs, or formal specs yet.

## 2. Put source documents in the owner repository

Examples:

```text
system/input/ProductRequirements.pdf
protocol/input/CommunicationProtocol.pdf
controller/input/ControllerVendorManual.pdf
```

One fact should have one owner repository.

## 3. Ingest every owned PDF

Example:

```text
$praxflow-pdf-ingest input/ProductRequirements.pdf
```

Expected output:

```text
docs/raw/ProductRequirements_raw.md
docs/raw/ProductRequirements_extraction_report.md
```

Inspect `TODO_VERIFY`, `OCR_CANDIDATE`, missing tables, and source-page references before treating the extraction as reliable evidence.

## 4. Discover the product system

Run only in the system repository after the main source material is ingested:

```text
$praxflow-system-discovery
```

Expected output:

```text
CONTEXT-MAP.md
docs/system/SYSTEM_FACTS.md
docs/system/OPEN_DECISIONS.md
```

## 5. Review open decisions

Inspect `OPEN_DECISIONS.md`.

- `LOW`: normally continue.
- `MEDIUM`: agent may propose a recommendation, but document the decision if it becomes architectural.
- `HIGH`: present to the user; interactive deep design review is recommended.
- `CRITICAL`: stop for explicit human approval; do not silently resolve.

If you use Matt Pocock Skills and a major unresolved decision exists, one compatible command is:

```text
/grill-with-docs
```

Do not run Grill merely because a PDF contains a clear factual requirement.

## 6. Create the specification source

After important decisions are resolved, use your installed specification workflow. With Matt Pocock Skills this may be:

```text
/to-spec
```

Record the resulting concrete source identifier, for example a GitHub/GitLab issue number or reviewed specification file.

## 7. Materialize repository-local specs

Example:

```text
$praxflow-spec-materialize
source: issue #123
```

Typical protocol output:

```text
docs/spec/PROTOCOL.md
docs/spec/REGISTER_MAP.json
docs/spec/COMMANDS.json
docs/spec/ERROR_CODES.json
docs/spec/TEST_VECTORS.json
docs/spec/SPEC_SOURCE.json
```

## 8. Validate before implementation

Every implementation repository:

```text
$praxflow-spec-validate
```

Protocol repository additionally:

```text
$praxflow-protocol-validate
```

Do not implement when the validation result is `BLOCKED`.

## 9. Human approval gate

Approve the spec using the team's chosen mechanism. `SPEC_SOURCE.json` should indicate an approved source before production implementation begins.

## 10. Implement

For a large approved spec, decompose into tickets first. With Matt Pocock Skills:

```text
/to-tickets #123
```

Create a feature branch, then implement one ticket:

```text
/implement #130
```

For a small, already-approved behavior:

```text
/tdd
Implement <behavior> according to the approved spec.
```

## 11. Cross-repository contract change

Before changing a shared/public interface:

```text
$praxflow-interface-change
goal: Add StartTest command.
```

Update and approve the owner spec first, then update consumers.

## 12. Verify the product

After all affected repositories are ready:

```text
$praxflow-system-verify
change: IC-0001
```

Manual/hardware checks remain `MANUAL_PENDING` until a human provides evidence.

## 13. Release the tested repository combination

Only when system verification is `PASS`:

```text
$praxflow-manifest-release
version: 1.0.0
verification: system/docs/verification/VER-RC-001.md
```

Expected output:

```text
releases/v1.0.0.xml
releases/v1.0.0.md
```

## First-run rule

Do not redesign the workflow before trying it. Run one real project through the process, record friction points, then change the relevant `skill`, `docs`, `template`, or `example` based on observed failures.
