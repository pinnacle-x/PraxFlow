# Open Decisions — Demo Temperature System

## OD-001 — Closed-loop control ownership

- Status: OPEN
- Severity: HIGH
- Affected: controller, module-temperature, system
- Why unresolved: source requirements require closed-loop temperature control but do not define whether PID executes in the main controller or temperature module.
- Candidate options:
  1. Controller owns PID.
  2. Temperature module owns PID.
- Impact: real-time behavior, disconnect behavior, protocol bandwidth, safety allocation.
- Recommended action: interactive deep design review with human decision.

## OD-002 — PC chart refresh interval

- Status: OPEN
- Severity: LOW
- Affected: pc
- Why unresolved: no explicit user-facing refresh requirement.
- Recommended action: resolve during PC specification; no product-level Grill required.
