# Cross-Repository Public Interface Workflow

Use this process when one product change modifies a contract consumed by more than one independent Git repository.

Example: adding a `StartTest` command affects `protocol`, `controller`, `pc`, and `system`.

## 1. Analyze before implementation

From a workspace that can see the relevant repositories:

```text
$praxflow-interface-change
goal: Add StartTest command.
```

Expected plan:

```text
system/docs/changes/IC-0001-start-test-command.md
```

The plan identifies:

- owner repository
- affected repositories
- compatibility risk
- required specification changes
- required implementation order
- required verification

## 2. Owner-first rule

If `protocol` owns the public command:

```text
protocol spec update
  -> protocol validation
  -> human approval
  -> protocol implementation (if executable code exists)
  -> controller consumer update
  -> PC consumer update
  -> integration verification
```

Consumers must not create locally divergent meanings because the current owner contract is inconvenient.

## 3. Separate Git history

Each repository keeps its own branch, commit, merge request, and review history. Do not mix unrelated repositories into one commit.

## 4. Verify exact revisions

After all affected repositories are ready:

```text
$praxflow-system-verify
change: IC-0001
```

The verification report records exact SHAs for every affected repository.

## 5. Release only the tested combination

A product release manifest must reference the exact verified combination, not merely floating `develop` branches.
