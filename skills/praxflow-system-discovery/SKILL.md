---
name: praxflow-system-discovery
description: Discover product contexts, repository ownership, established system facts, and unresolved product-level decisions from existing evidence. Use in the system repository after raw source ingestion.
---

# PraxFlow System Discovery

Analyze existing product evidence without inventing architecture. This skill separates facts from decisions and classifies unresolved decisions by impact.

## Read first

- `AGENTS.md`
- `docs/raw/*`
- existing `CONTEXT.md` if present
- existing `CONTEXT-MAP.md` if present
- `docs/adr/*`
- `docs/spec/*`
- workspace repository list when visible
- `manifest/default.xml` when available

## Actions

1. Identify product-level contexts/subsystems that are explicitly supported by evidence.
2. Identify the owner repository for each fact or interface when known.
3. Extract established responsibilities and interface directions.
4. Separate facts from assumptions.
5. Create or update a context map.
6. Create an open-decision register for unresolved design choices.
7. Classify each open decision as `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`.

## Decision severity

- `LOW`: local, cheap to reverse, little downstream impact.
- `MEDIUM`: meaningful design choice mainly contained within one repository.
- `HIGH`: cross-repository, public-interface, real-time, compatibility, or expensive-to-reverse choice.
- `CRITICAL`: safety, hazardous behavior, irreversible product behavior, or system integrity decision requiring explicit human approval.

## Grill recommendation

For each `HIGH` or `CRITICAL` item, recommend `/grill-with-docs` (or equivalent deep design review) but do not invoke it automatically.

## Outputs

Create or update:
- `CONTEXT-MAP.md`
- `docs/system/SYSTEM_FACTS.md`
- `docs/system/OPEN_DECISIONS.md`

`CONTEXT-MAP.md` records contexts, repository mapping, responsibilities, owned interfaces, and dependencies. It is a map, not a duplicate of subsystem contexts.

`SYSTEM_FACTS.md` contains only evidence-backed facts and their source references.

`OPEN_DECISIONS.md` must give every item a stable ID (`OD-001`, ...), status, severity, affected contexts/repos, why unresolved, candidate options when known, impact, and recommended next action.

## Stop conditions

Stop after discovery. Do not create production code. Do not silently resolve `HIGH` or `CRITICAL` decisions. If no major decisions remain, state that the project can proceed to specification.
