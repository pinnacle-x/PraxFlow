---
name: praxflow-manifest-release
description: Create an immutable product release manifest from a successfully verified multi-repository workspace. Use only after system verification passes.
---

# PraxFlow Manifest Release

Create a reproducible product release by pinning exact repository revisions in the manifest repository.

## Preconditions

Require:
- a requested product version
- a system verification artifact with overall result `PASS`
- exact repository revisions used by that verification

If any required verification is `FAIL`, `BLOCKED`, or `MANUAL_PENDING`, stop.

## Read first

- manifest repository `AGENTS.md`
- `default.xml`
- existing `releases/*`
- referenced system verification artifact

## Actions

1. Validate that each repository revision in the release matches the successful verification record.
2. Refuse dirty/unrecorded workspace state when it would make the release non-reproducible.
3. Generate a release manifest pinning exact immutable revisions (commit SHA or approved immutable tag).
4. Generate a human-readable release record.
5. Preserve `default.xml` as the development manifest unless the user explicitly requests a development-baseline update.

## Outputs

Create:
- `releases/v<version>.xml`
- `releases/v<version>.md`

The Markdown release record must include:
- product version
- source verification artifact
- repository names, paths, and pinned revisions
- protocol/interface versions when applicable
- known limitations
- release date when available
- reproducibility instructions

## Rules

- Never point a release manifest at moving branches such as `develop` or `main` unless the user explicitly requests a non-reproducible snapshot and the file is clearly marked as such.
- Never create a release from unverified revisions.
- Never rewrite an existing released version without explicit user approval.

Stop after creating the release artifacts and reporting the exact pinned revisions.
