# PraxFlow Portability Contract

PraxFlow maintains one canonical Agent Skills implementation for exactly three supported runtime environments:

- OpenAI Codex
- Claude Code
- DeepSeek Harness

The files under `skills/` are the source of truth. Runtime-specific packaging exists only to make the same workflow logic discoverable in each supported environment.

## Canonical skill rules

Every directory under `skills/` must:

1. Contain a `SKILL.md` entry point.
2. Use a lowercase kebab-case directory name.
3. Keep the frontmatter `name` aligned with the directory name.
4. Provide a clear `description` that explains both what the skill does and when it is relevant.
5. Use frontmatter accepted by the supported Agent Skills readers.
6. Reference bundled resources using paths relative to the skill directory.
7. Prefer portable Python for executable helpers when practical.
8. Fail with actionable messages when a required local dependency is missing.
9. Keep product facts, architecture decisions, and repository-specific configuration out of the skill package.

## Runtime-neutral core

Canonical skills must not require:

- Codex-specific tool names or approval APIs
- Claude-only shell interpolation, plugin hooks, or environment variables
- DeepSeek Harness-only `ctx.*` service APIs or Cordis plugin configuration
- a particular model vendor

A canonical skill may describe an optional companion capability semantically. Example:

> If a high-impact unresolved decision remains, recommend an interactive deep-design review. If the current environment provides a compatible deep-design skill, use it only after human approval.

The core must not depend on slash-command syntax or a runtime-specific tool name.

## Supported adapter boundary

Runtime-specific integration belongs outside canonical workflow semantics.

Current adapters:

- `.codex-plugin/plugin.json` — Codex packaging
- `.claude-plugin/plugin.json` — Claude Code packaging
- `scripts/install.py` — installation paths for Codex, Claude Code, and DeepSeek Harness

DeepSeek Harness can consume the shared Agent Skills format directly, so PraxFlow does not require a dedicated DeepSeek plugin manifest for ordinary skill discovery.

## DeepSeek model neutrality

DeepSeek API/models are separate from DeepSeek Harness.

PraxFlow compatibility is defined at the agent-runtime layer. A supported runtime may use OpenAI, Anthropic, DeepSeek, or another compatible model provider without changing the canonical PraxFlow skills.

Therefore:

- Codex + DeepSeek API remains a Codex PraxFlow installation.
- DeepSeek Harness + DeepSeek model remains a DeepSeek Harness PraxFlow installation.
- Model-provider configuration must not leak into `skills/*/SKILL.md` unless the workflow itself genuinely concerns model-provider setup.

## Shared paths

Codex and DeepSeek Harness can both use `.agents/skills` as a shared Agent Skills location. PraxFlow prefers this shared path for those two runtimes.

Claude Code uses its own `.claude/skills` path or plugin packaging adapter.

Do not create duplicate copies merely to satisfy branding differences between runtimes.

## Human gates are semantic

PraxFlow uses human gates for high-impact decisions, specification approval, safety-sensitive validation, and product release. Express those gates as required behavior, not assumptions about one runtime's approval UI.

Good:

> Stop and request explicit human approval before resolving a CRITICAL open decision.

Avoid:

> Call Codex approval tool X.

## Compatibility testing

A PraxFlow release should validate:

- `SKILL.md` frontmatter and naming
- relative resource links
- script portability on Windows and Linux where relevant
- discovery/install path for Codex
- discovery/install path for Claude Code
- discovery/install path for DeepSeek Harness
- at least one explicit skill invocation smoke test per supported runtime when automated testing becomes practical

PraxFlow deliberately does not claim support for Cursor, Gemini CLI, Copilot, OpenCode, Cline, Roo Code, Windsurf, or other runtimes unless support is intentionally added later.
