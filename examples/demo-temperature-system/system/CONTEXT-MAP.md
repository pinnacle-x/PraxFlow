# Context Map — Demo Temperature System

| Context | Repository | Responsibility | Public interfaces owned |
|---|---|---|---|
| System | system | product boundaries and allocation | system-level allocation |
| PC | pc | operator UI, visualization, records | PC application interfaces |
| Controller | controller | real-time sequencing and safety coordination | controller-local control API |
| Temperature Module | module-temperature | temperature sensing and actuator interface | module-local IO behavior |
| Shared Protocol | protocol | wire-level communication contract | commands, registers, errors |

Relationships:

```text
PC -> Shared Protocol -> Controller
Controller -> Shared Protocol -> Temperature Module
System -> allocates responsibilities across all contexts
```
