# PraxFlow Portability Contract

PraxFlow is an **agent-neutral Agent Skills library**. The files under `skills/` are the canonical implementation. Vendor-specific plugin formats exist only to make those skills easier to install or discover.

## Canonical skill rules

Every directory under `skills/` must:

1. Contain a `SKILL.md` entry point.
2. Use a lowercase kebab-case directory name.
3. Keep the frontmatter `name` aligned with the directory name.
4. Provide a clear `description` that explains both what the skill does and when it is relevant.
5. Use only portable frontmatter in the canonical file unless a field is known to be harmless across supported agents.
6. Reference bundled resources using paths relative to the skill directory.
7. Prefer portable Python for executable helpers when practical; scripts must fail with actionable messages when a dependency is missing.
8. Keep product facts, architecture decisions, and repository-specific configuration out of the skill package.

## Do not hard-code an agent runtime

Canonical skills must not require:

- Codex-specific tool names
- Claude-only shell interpolation or environment variables
- Cursor-only commands
- Gemini-only activation APIs
- Copilot-only tool grants
- OpenCode-only metadata
- a particular model vendor

A skill may describe an optional companion capability semantically. Example:

> If a high-impact unresolved decision remains, recommend an interactive deep-design review. If the environment provides a `grill-with-docs` skill, it is one compatible implementation.

Do not make the PraxFlow core depend on slash-command syntax that another agent may not implement.

## Adapter boundary

Agent-specific integration belongs outside the canonical workflow logic.

Current adapters:

- `.codex-plugin/plugin.json` — Codex plugin packaging
- `.claude-plugin/plugin.json` — Claude Code plugin packaging
- `scripts/install.py` — filesystem installer for several popular agents

Future adapters may live under `integrations/<agent>/` when an agent requires more than a destination path or a small manifest.

## Shared paths first

When an agent officially supports `.agents/skills`, prefer that path because it lets one project skill installation work across several agents. Use an agent-specific directory only when necessary or when the user explicitly wants agent-specific precedence.

## Human gates are semantic

PraxFlow uses human gates for high-impact decisions, specification approval, safety-sensitive validation, and product release. These gates must be expressed in the skill instructions as required behaviors, not as assumptions about one agent's approval UI.

For example:

- good: "Stop and request explicit human approval before resolving a CRITICAL open decision."
- avoid: "Call Codex approval tool X."

## Compatibility testing

A PraxFlow release should eventually validate at least:

- YAML frontmatter and naming
- relative resource links
- script portability on Windows and Linux
- discovery in one shared-path agent
- discovery in one agent-specific-path agent
- explicit invocation and automatic discovery behavior where supported

Agent-specific enhancements may be added later, but they must not fork the workflow semantics of the canonical skill.
