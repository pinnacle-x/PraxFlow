# PraxFlow

PraxFlow is a portable Agent Skills workflow library for repeatable product engineering across system, protocol, PC, controller, module, hardware, and manifest repositories.

PraxFlow intentionally supports **three agent environments only**:

- OpenAI Codex
- Claude Code
- DeepSeek Harness

The canonical workflow logic lives in `skills/` as standard `SKILL.md` bundles. Agent-specific packaging is only an adapter around the same core skills.

## DeepSeek support: two different meanings

PraxFlow distinguishes the DeepSeek **agent runtime** from the DeepSeek **model/API**:

- **DeepSeek Harness** is a supported agent runtime and can discover PraxFlow skills from Agent Skills directories.
- **DeepSeek API / DeepSeek models** are model backends. They do not need a separate PraxFlow skill format. PraxFlow should work when Codex, Claude Code-compatible workflows, or DeepSeek Harness use DeepSeek models as the reasoning backend.

In other words, PraxFlow is runtime-portable across Codex, Claude Code, and DeepSeek Harness, and model-provider-neutral inside those runtimes.

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

## Install

Clone once:

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
```

Install for Codex:

```bash
python scripts/install.py --agent codex --scope user
```

Install for Claude Code:

```bash
python scripts/install.py --agent claude --scope user
```

Install for DeepSeek Harness:

```bash
python scripts/install.py --agent deepseek --scope user
```

See `docs/installation.md` for project-scope installs, selected skills, link mode, and runtime-specific notes.

## Packaging model

```text
skills/                         <- canonical workflow logic shared by all supported runtimes
.codex-plugin/plugin.json       <- Codex packaging adapter
.claude-plugin/plugin.json      <- Claude Code packaging adapter
scripts/install.py              <- Codex / Claude Code / DeepSeek Harness installer
docs/portability.md             <- three-runtime compatibility contract
```

DeepSeek Harness does not require a PraxFlow-specific plugin manifest when loading the shared Agent Skills format.

## Workflow

See:

- `docs/workflow.md` — end-to-end product workflow
- `docs/source-of-truth.md` — repository ownership rules
- `docs/repository-roles.md` — system/protocol/PC/controller/module/manifest responsibilities
- `docs/installation.md` — Codex / Claude Code / DeepSeek Harness installation
- `docs/portability.md` — compatibility contract
- `docs/deepseek.md` — DeepSeek Harness vs DeepSeek API/model-backend support
- `docs/integration-with-general-skills.md` — optional integration with TDD, grilling, planning, review, and similar general engineering skills

## Status

Initial implementation. PraxFlow is intentionally conservative: it preserves source traceability, surfaces uncertainty instead of guessing, and requires explicit human approval for high-impact design and release gates.
