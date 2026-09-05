# PDF Ingest Example

Input:

```text
input/DeviceManual.pdf
```

Invocation:

```text
$praxflow-pdf-ingest input/DeviceManual.pdf
```

Expected outputs:

```text
docs/raw/DeviceManual_raw.md
docs/raw/DeviceManual_extraction_report.md
```

The raw file must preserve source pages. Ambiguous extraction is marked for verification instead of being silently corrected.
