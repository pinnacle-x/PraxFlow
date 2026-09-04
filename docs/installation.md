# Installing PraxFlow

PraxFlow is **Agent Skills first**. The canonical, vendor-neutral skills live in `skills/` and follow the `SKILL.md` Agent Skills format. Agent-specific plugin manifests are adapters, not the source of truth.

## Recommended installation model

Clone PraxFlow once, then install or link the canonical `skills/` directories into the skill directory used by your agent.

```bash
git clone https://github.com/pinnacle-x/PraxFlow.git
cd PraxFlow
python scripts/install.py --agent generic --scope user
```

The generic target installs into `~/.agents/skills`, which is a shared compatibility location supported by several modern agents.

Use project scope when the skills should travel with one repository:

```bash
python scripts/install.py --agent generic --scope project --project /path/to/project
```

Use `--mode link` while developing PraxFlow so edits are visible without reinstalling:

```bash
python scripts/install.py --agent cursor --scope user --mode link
```

On Windows, creating symbolic links may require Developer Mode or elevated privileges. Use the default `copy` mode if linking is unavailable.

## Supported targets

| Target | User scope | Project scope | Notes |
|---|---|---|---|
| `generic` | `~/.agents/skills` | `.agents/skills` | Preferred portable target when the agent supports the shared Agent Skills path. |
| `codex` | `~/.agents/skills` | `.agents/skills` | Direct skill install. PraxFlow also ships `.codex-plugin/plugin.json` as a Codex plugin adapter. |
| `claude` | `~/.claude/skills` | `.claude/skills` | Claude Code Agent Skills. PraxFlow also ships `.claude-plugin/plugin.json`. |
| `cursor` | `~/.agents/skills` | `.agents/skills` | Cursor officially supports the shared `.agents/skills` path. |
| `gemini` | `~/.agents/skills` | `.agents/skills` | Gemini CLI supports `.agents/skills` as an interoperable alias. |
| `copilot` | `~/.agents/skills` | `.agents/skills` | GitHub Copilot supports the shared Agent Skills path. |
| `opencode` | `~/.agents/skills` | `.agents/skills` | OpenCode supports `.agents/skills` as a compatibility source. |
| `cline` | `~/.agents/skills` | `.agents/skills` | Cline supports Agent Skills and the shared project layout. |
| `roo` | `~/.agents/skills` | `.agents/skills` | Roo Code supports the shared cross-agent path. |
| `windsurf` | `~/.codeium/windsurf/skills` | `.windsurf/skills` | Adapter target; verify behavior against the Windsurf version used in your environment. |

The installer intentionally copies the same canonical skill directories for every target. PraxFlow does not maintain separate skill logic per agent.

## Agent-native alternatives

Some agents have their own native installer or plugin system. Use those when convenient, while keeping `skills/` as the canonical content.

### Claude Code

Claude Code can load project skills from `.claude/skills/` and user skills from `~/.claude/skills/`. Its plugin system also discovers `skills/` in a plugin root. PraxFlow includes a Claude plugin manifest so a future Claude marketplace/install flow can use the same core skills.

### Cursor

Cursor automatically discovers Agent Skills from `.agents/skills/` and `.cursor/skills/`. Installing PraxFlow with the shared `.agents` target avoids a Cursor-only copy.

### Gemini CLI

Gemini CLI supports `~/.agents/skills/` and `.agents/skills/` aliases in addition to Gemini-specific paths. It also provides `gemini skills install` and `gemini skills link` commands.

### GitHub Copilot

GitHub Copilot supports project skills in `.agents/skills/` (as well as GitHub- and Claude-specific skill directories) and personal skills in `~/.agents/skills/`.

### OpenCode

OpenCode discovers `.agents/skills/` directly, or can be configured with an explicit `skills` source pointing to the PraxFlow `skills/` directory.

## Installing only selected skills

Repeat `--skill` to select a subset:

```bash
python scripts/install.py --agent generic --scope user \
  --skill praxflow-pdf-ingest \
  --skill praxflow-system-discovery
```

## Updating

For copy-mode installs:

```bash
git pull
python scripts/install.py --agent generic --scope user --force
```

For link-mode installs, `git pull` is sufficient because the installed paths point back to the checkout.

## Portability policy

Before adding an agent-specific feature to a canonical skill, read `docs/portability.md`. Agent-specific metadata, hooks, commands, or UI integration belong in an adapter layer; workflow semantics belong in `skills/`.
