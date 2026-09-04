#!/usr/bin/env python3
"""Install PraxFlow Agent Skills for Codex, Claude Code, or DeepSeek Harness.

The canonical skills always come from ../skills. This installer only chooses a
supported runtime destination and copies or links the selected skill bundles.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path


TARGETS = {
    "codex": {"user": "~/.agents/skills", "project": ".agents/skills"},
    "claude": {"user": "~/.claude/skills", "project": ".claude/skills"},
    "deepseek": {"user": "~/.agents/skills", "project": ".agents/skills"},
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def skill_catalog() -> dict[str, Path]:
    root = repo_root() / "skills"
    catalog: dict[str, Path] = {}
    if not root.is_dir():
        raise RuntimeError(f"PraxFlow skills directory not found: {root}")
    for child in sorted(root.iterdir()):
        if child.is_dir() and (child / "SKILL.md").is_file():
            catalog[child.name] = child
    return catalog


def destination(agent: str, scope: str, project: str | None) -> Path:
    raw = TARGETS[agent][scope]
    if scope == "user":
        return Path(raw).expanduser().resolve()
    base = Path(project or os.getcwd()).expanduser().resolve()
    return (base / raw).resolve()


def install_copy(src: Path, dst: Path, force: bool) -> None:
    if dst.exists() or dst.is_symlink():
        if not force:
            raise FileExistsError(
                f"Destination already exists: {dst}. Re-run with --force to replace it."
            )
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        else:
            shutil.rmtree(dst)
    shutil.copytree(src, dst)


def install_link(src: Path, dst: Path, force: bool) -> None:
    if dst.exists() or dst.is_symlink():
        if not force:
            raise FileExistsError(
                f"Destination already exists: {dst}. Re-run with --force to replace it."
            )
        if dst.is_symlink() or dst.is_file():
            dst.unlink()
        else:
            shutil.rmtree(dst)
    try:
        dst.symlink_to(src, target_is_directory=True)
    except OSError as exc:
        raise RuntimeError(
            "Could not create a directory symlink. On Windows, enable Developer Mode "
            "or run with sufficient privileges, or use --mode copy."
        ) from exc


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install PraxFlow Agent Skills")
    parser.add_argument(
        "--agent",
        choices=sorted(TARGETS),
        required=True,
        help="Supported agent runtime: codex, claude, or deepseek.",
    )
    parser.add_argument(
        "--scope",
        choices=("user", "project"),
        default="user",
        help="Install globally for the current user or into one project.",
    )
    parser.add_argument(
        "--project",
        help="Project root for --scope project. Defaults to the current directory.",
    )
    parser.add_argument(
        "--mode",
        choices=("copy", "link"),
        default="copy",
        help="Copy skills or create directory symlinks back to this checkout.",
    )
    parser.add_argument(
        "--skill",
        action="append",
        dest="skills",
        help="Install one named skill. Repeat to install multiple skills. Default: all.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing PraxFlow skill directory at the destination.",
    )
    parser.add_argument(
        "--list-agents",
        action="store_true",
        help="Print supported target names and paths, then exit.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if args.list_agents:
        print(json.dumps(TARGETS, indent=2))
        return 0

    catalog = skill_catalog()
    selected = args.skills or list(catalog)
    unknown = [name for name in selected if name not in catalog]
    if unknown:
        print(
            "Unknown PraxFlow skill(s): " + ", ".join(sorted(unknown)),
            file=sys.stderr,
        )
        print("Available: " + ", ".join(catalog), file=sys.stderr)
        return 2

    root = destination(args.agent, args.scope, args.project)
    root.mkdir(parents=True, exist_ok=True)

    installed: list[str] = []
    for name in selected:
        src = catalog[name].resolve()
        dst = root / name
        try:
            if args.mode == "copy":
                install_copy(src, dst, args.force)
            else:
                install_link(src, dst, args.force)
        except Exception as exc:  # noqa: BLE001 - CLI needs a readable failure.
            print(f"Failed to install {name}: {exc}", file=sys.stderr)
            return 1
        installed.append(name)
        print(f"installed {name} -> {dst}")

    print()
    print(f"PraxFlow installed for target '{args.agent}' in: {root}")
    print(f"Skills installed: {len(installed)}")
    if args.agent == "deepseek":
        print(
            "DeepSeek target means DeepSeek Harness. DeepSeek API/models used behind another "
            "agent runtime do not require a separate skill installation."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
