---
name: praxflow-pdf-ingest
description: Convert repository-owned PDFs into traceable raw Markdown and an extraction report. Use before semantic interpretation, specification, or implementation.
---

# PraxFlow PDF Ingest

Transform source PDFs into faithful, traceable raw artifacts. This skill extracts evidence; it does not design the product or generate production code.

## Inputs

Accept one or more PDF paths, normally under `input/`. If no path is provided, discover PDFs in `input/`.

## Preferred execution

For text-layer extraction, use the bundled helper first:

```bash
python skills/praxflow-pdf-ingest/scripts/extract_pdf.py input/<file>.pdf --out-dir docs/raw --json
```

When installed as a plugin outside the target repo, resolve the script relative to this skill directory rather than assuming the target repository contains `skills/`.

The helper tries PyMuPDF first and then pypdf. It deliberately does not OCR pages automatically; pages with little/no extractable text are reported as OCR candidates.

## Extraction strategy

1. Classify each PDF as text, table-heavy, scanned, or mixed.
2. Prefer the existing PDF text layer.
3. Use the bundled helper or equivalent local extraction tools.
4. Inspect visually important tables/diagrams when text extraction is insufficient.
5. Use OCR only for pages that cannot be reliably extracted otherwise.
6. Preserve page boundaries and source file identity.
7. Preserve headings, numbering, tables, units, hexadecimal values, signs, decimal points, and data types.
8. Never silently normalize an ambiguous token.

## Uncertainty rule

For unclear or conflicting content, write `TODO_VERIFY` with:
- source file
- page number
- observed text/image interpretation
- candidate interpretations if useful

Do not choose a candidate without evidence.

## Outputs

For each input PDF create:
- `docs/raw/<stem>_raw.md`
- `docs/raw/<stem>_extraction_report.md`

The raw file must annotate source pages, for example:

```markdown
<!-- source_file: device.pdf -->
<!-- source_page: 18 -->
```

The extraction report must include:
- total pages
- extraction method by page/range
- detected/visually relevant tables when known
- OCR pages/candidates
- low-confidence or failed pages
- count/list of `TODO_VERIFY`
- overall result: `PASS`, `PASS_WITH_WARNINGS`, or `BLOCKED`

## Prohibited actions

- Do not create product requirements from implied meaning.
- Do not convert guesses into facts.
- Do not create ADRs.
- Do not create implementation specs.
- Do not modify source PDFs.
- Do not generate production code.

Stop after extraction, visual follow-up for flagged pages as needed, and report generation.
