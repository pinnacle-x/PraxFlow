#!/usr/bin/env python3
"""Validate the canonical PraxFlow Agent Skills core.

The core must remain portable across the three supported runtimes:
Codex, Claude Code, and DeepSeek Harness.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RUNTIME_MARKERS = {
    "${CLAUDE_SKILL_DIR}": "Claude-specific skill directory variable",
    ".claude/skills": "Claude-specific install path",
    ".codex/skills": "Codex-specific install path",
    ".dsh/skills": "DeepSeek Harness-specific install path",
    "ctx.skills": "DeepSeek Harness service API",
    "ctx.tools": "DeepSeek Harness service API",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def main() -> int:
    skills_root = repo_root() / "skills"
    errors: list[str] = []
    warnings: list[str] = []

    if not skills_root.is_dir():
        print(f"ERROR: skills directory not found: {skills_root}")
        return 1

    skills = sorted(p for p in skills_root.iterdir() if p.is_dir())
    if not skills:
        errors.append("No skill directories found")

    for skill_dir in skills:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_dir.name}: missing SKILL.md")
            continue

        text = skill_file.read_text(encoding="utf-8")
        meta = frontmatter(text)
        name = meta.get("name", "")
        description = meta.get("description", "")

        if not name:
            errors.append(f"{skill_dir.name}: missing frontmatter name")
        elif name != skill_dir.name:
            errors.append(
                f"{skill_dir.name}: frontmatter name '{name}' must match directory"
            )
        elif not NAME_RE.fullmatch(name):
            errors.append(f"{skill_dir.name}: name is not portable kebab-case")
        elif len(name) > 64:
            errors.append(f"{skill_dir.name}: name exceeds 64 characters")

        if not description:
            errors.append(f"{skill_dir.name}: missing frontmatter description")
        elif len(description) > 1024:
            errors.append(f"{skill_dir.name}: description exceeds 1024 characters")

        for marker, reason in RUNTIME_MARKERS.items():
            if marker in text:
                warnings.append(
                    f"{skill_dir.name}: canonical SKILL.md contains {reason}: {marker}"
                )

    print(f"Validated {len(skills)} PraxFlow skill directories")
    print("Supported runtimes: Codex, Claude Code, DeepSeek Harness")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        return 1
    print("Three-runtime core validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
