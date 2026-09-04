# Installing PraxFlow

PraxFlow supports three agent environments:

- OpenAI Codex
- Claude Code
- DeepSeek Harness

The canonical skills live in `skills/` and use the portable `SKILL.md` Agent Skills format. Runtime-specific manifests and install paths are adapters only.

## Clone once

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
```

## Codex

User scope:

```bash
python scripts/install.py --agent codex --scope user
```

Project scope:

```bash
python scripts/install.py --agent codex --scope project --project /path/to/project
```

Default destinations:

- user: `~/.agents/skills`
- project: `.agents/skills`

PraxFlow also ships `.codex-plugin/plugin.json` as a Codex packaging adapter.

## Claude Code

User scope:

```bash
python scripts/install.py --agent claude --scope user
```

Project scope:

```bash
python scripts/install.py --agent claude --scope project --project /path/to/project
```

Default destinations:

- user: `~/.claude/skills`
- project: `.claude/skills`

PraxFlow also ships `.claude-plugin/plugin.json` so the same canonical `skills/` can be packaged through Claude Code's plugin mechanism.

## DeepSeek Harness

User scope:

```bash
python scripts/install.py --agent deepseek --scope user
```

Project scope:

```bash
python scripts/install.py --agent deepseek --scope project --project /path/to/project
```

Default destinations:

- user: `~/.agents/skills`
- project: `.agents/skills`

DeepSeek Harness can consume standard Agent Skills bundles directly. PraxFlow therefore does not need a separate DeepSeek plugin manifest for ordinary skill discovery.

A DeepSeek Harness deployment may also use a native `.dsh/skills` project location when that is preferable. PraxFlow's installer uses `.agents/skills` by default because it is also compatible with Codex and avoids maintaining duplicate skill copies on machines that use both runtimes.

## DeepSeek API / model backend

`--agent deepseek` means **DeepSeek Harness**, not the DeepSeek HTTP API by itself.

DeepSeek API/models are model providers, not skill-discovery runtimes. If Codex or another supported harness is configured to use DeepSeek as its model backend, install PraxFlow for that agent runtime exactly as normal. No second PraxFlow installation is required for the model provider.

Examples:

```text
Codex + DeepSeek API
  -> install PraxFlow for codex

DeepSeek Harness + DeepSeek model
  -> install PraxFlow for deepseek

Claude Code-compatible workflow + DeepSeek backend
  -> install PraxFlow for the Claude Code runtime layer
```

## Link mode for PraxFlow development

Use `--mode link` while editing PraxFlow itself:

```bash
python scripts/install.py --agent codex --scope user --mode link
```

On Windows, directory symlinks may require Developer Mode or elevated privileges. Use the default `copy` mode when linking is unavailable.

## Install selected skills only

Repeat `--skill`:

```bash
python scripts/install.py --agent codex --scope user \
  --skill praxflow-pdf-ingest \
  --skill praxflow-system-discovery
```

## Updating

For copy-mode installs:

```bash
git pull
python scripts/install.py --agent codex --scope user --force
```

For link-mode installs, `git pull` is normally sufficient.

## Supported-target policy

PraxFlow deliberately does not promise installation or compatibility for every coding agent. New runtime adapters should be added only when there is a concrete need and a maintained test path.

The supported compatibility contract is defined in `docs/portability.md`.
