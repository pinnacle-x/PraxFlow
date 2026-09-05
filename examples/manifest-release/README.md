# Manifest Release Example

Invocation:

```text
$praxflow-manifest-release
version: 1.0.0
verification: system/docs/verification/VER-RC-001.md
```

Precondition: referenced system verification result is `PASS`.

Expected output:

```text
releases/v1.0.0.xml
releases/v1.0.0.md
```

The release manifest must pin immutable tested revisions.
