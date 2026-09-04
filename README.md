# PraxFlow

PraxFlow is a Codex skill-only plugin for repeatable engineering workflows across system, protocol, PC, controller, module, and manifest repositories.

It complements general-purpose engineering skills (for example TDD, design grilling, specification and review) with product-level workflow skills for:

- repository bootstrap
- PDF ingestion with source traceability
- system discovery and open-decision classification
- specification materialization and validation
- protocol validation
- cross-repository interface changes
- system verification
- manifest-based product releases

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

## Workflow

See `docs/workflow.md` for the end-to-end workflow and `docs/source-of-truth.md` for ownership rules.

## Status

Initial implementation. The skills are intentionally conservative: they preserve source traceability, surface uncertainty instead of guessing, and require explicit human approval for high-impact design and release gates.
