# DeepSeek Support

PraxFlow uses the word **DeepSeek** in two different technical contexts. They must not be confused.

## 1. DeepSeek Harness

DeepSeek Harness is an agent runtime. It has a Skills subsystem and can consume standard Agent Skills bundles.

PraxFlow supports DeepSeek Harness directly through the same canonical `skills/` directory used by the other supported runtimes.

Recommended install:

```bash
python scripts/install.py --agent deepseek --scope user
```

Default user destination:

```text
~/.agents/skills/
```

Recommended project destination:

```text
<project>/.agents/skills/
```

DeepSeek Harness may also use its native `.dsh/skills` project location. PraxFlow defaults to `.agents/skills` because Codex and DeepSeek Harness can share that location on the same workstation.

PraxFlow does not require a dedicated DeepSeek plugin manifest for normal skill discovery.

## 2. DeepSeek API / DeepSeek models

DeepSeek API/models are model providers. They are not, by themselves, an Agent Skills runtime.

Therefore PraxFlow installation follows the runtime that is actually executing tools and loading skills.

### Codex using DeepSeek API

```text
Codex runtime
  + DeepSeek model/API backend
  + PraxFlow installed for Codex
```

Install:

```bash
python scripts/install.py --agent codex --scope user
```

Do not install PraxFlow a second time merely because the model backend is DeepSeek.

### DeepSeek Harness using DeepSeek models

```text
DeepSeek Harness runtime
  + DeepSeek model backend
  + PraxFlow installed for DeepSeek Harness
```

Install:

```bash
python scripts/install.py --agent deepseek --scope user
```

### Claude Code-compatible execution using a DeepSeek backend

If a Claude Code-compatible runtime layer is responsible for skill discovery and tool execution while requests are routed to a DeepSeek model, install PraxFlow for the Claude runtime layer:

```bash
python scripts/install.py --agent claude --scope user
```

## Compatibility rule

PraxFlow core skills must never assume that:

- Codex always uses an OpenAI model,
- Claude Code always uses an Anthropic model,
- DeepSeek Harness always uses one particular DeepSeek model.

The agent runtime owns skill discovery and tool execution. The model provider owns inference. PraxFlow workflow semantics stay independent from the model provider.

## Supported configurations

PraxFlow currently targets these runtime configurations:

| Runtime | PraxFlow support | Model backend |
|---|---|---|
| Codex | supported | OpenAI or DeepSeek-compatible backend |
| Claude Code | supported | Anthropic or compatible routed backend |
| DeepSeek Harness | supported | DeepSeek or another configured provider |

Other agent runtimes are outside the maintained compatibility scope unless explicitly added later.
