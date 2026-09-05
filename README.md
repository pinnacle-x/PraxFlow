# PraxFlow

PraxFlow is a portable Agent Skills workflow library for repeatable product engineering across system, protocol, PC, controller, module, hardware, and manifest repositories.

The canonical workflow logic lives in `skills/`. Agent-specific packaging is an adapter around the same core skills.

## Start here

- [Quick start](docs/quick-start.md) — exact commands for the first project run
- [Full workflow](docs/workflow.md) — canonical end-to-end process
- [Skill reference](docs/skill-reference.md) — what each PraxFlow skill reads, does, and writes
- [Decision gates](docs/decision-gates.md) — when human approval or deep design review is required
- [Cross-repository workflow](docs/cross-repo-workflow.md) — owner-first public interface changes
- [Repository roles](docs/repository-roles.md) — system/protocol/PC/controller/module/manifest ownership
- [Source of truth](docs/source-of-truth.md) — evidence, specs, ADRs, and implementation ownership
- [Examples](examples/README.md) — synthetic product examples and expected outputs
- [Templates](templates/) — reusable output formats
- [Exported documents](docs/exports/README.md) — Word/PDF-style release documents

## Skills

- `praxflow-repo-bootstrap`
- `praxflow-pdf-ingest`
- `praxflow-system-discovery`
- `praxflow-spec-materialize`
- `praxflow-spec-validate`
- `praxflow-protocol-validate`
- `praxflow-interface-change`
- `praxflow-system-verify`
- `praxflow-manifest-release`

## Repository model

```text
PraxFlow/
├── skills/       # executable workflow methods
├── docs/         # canonical process and reference documentation
├── examples/     # synthetic, reviewable examples
├── templates/    # reusable output schemas/templates
├── scripts/      # installers and validators
└── tests/        # future regression tests
```

Markdown files under `docs/` are the maintained source of truth for the process. Binary Word/PDF exports under `docs/exports/` are publication artifacts and may carry explicit version numbers.

## Installation

See [docs/installation.md](docs/installation.md).
