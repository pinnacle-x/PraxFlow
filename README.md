# PraxFlow

PraxFlow is a **portable Agent Skills workflow library** for repeatable product engineering across system, protocol, PC, controller, module, hardware, and manifest repositories.

The canonical implementation lives in `skills/` and follows the open `SKILL.md` Agent Skills model. PraxFlow is not tied to one model vendor or one agent runtime. Agent-specific plugin manifests and install paths are adapters around the same core skills.

## Target agents

PraxFlow is designed to work with Agent Skills-capable tools including:

- OpenAI Codex
- Claude Code
- Cursor
- Gemini CLI
- GitHub Copilot
- OpenCode
- Cline
- Roo Code
- Windsurf (adapter target; verify against the version used in your environment)

Where an agent supports the shared `.agents/skills` path, PraxFlow prefers it to reduce duplicated installations.

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

Clone once and install all skills into a compatible user-level Agent Skills directory:

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent generic --scope user
```

Or choose an agent-specific target:

```bash
python scripts/install.py --agent claude --scope user
python scripts/install.py --agent cursor --scope user
python scripts/install.py --agent gemini --scope user
python scripts/install.py --agent copilot --scope user
python scripts/install.py --agent opencode --scope user
```

See `docs/installation.md` for project-scope installs, selected skills, link mode, and agent-native alternatives.

## Packaging model

```text
skills/                         <- canonical, agent-neutral workflow logic
.codex-plugin/plugin.json       <- Codex packaging adapter
.claude-plugin/plugin.json      <- Claude Code packaging adapter
scripts/install.py              <- filesystem installer for multiple agents
docs/portability.md             <- rules that keep core skills vendor-neutral
```

Agent-specific features must not fork the workflow semantics in `skills/`.

## Workflow

See:

- `docs/workflow.md` — end-to-end product workflow
- `docs/source-of-truth.md` — repository ownership rules
- `docs/repository-roles.md` — system/protocol/PC/controller/module/manifest responsibilities
- `docs/installation.md` — cross-agent installation
- `docs/portability.md` — compatibility contract
- `docs/integration-with-general-skills.md` — optional integration with TDD, grilling, planning, review, and similar general engineering skills

## Status

Initial implementation. PraxFlow is intentionally conservative: it preserves source traceability, surfaces uncertainty instead of guessing, and requires explicit human approval for high-impact design and release gates.
