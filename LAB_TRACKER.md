# Lab Tracker

| Lab | Status | Main Bug Type | Time | Key Learning | Next Focus |
|---|---|---|---|---|---|
| 01 | ✅ Archived | Compose DNS host mismatch | ~30-40 min | Service name is DB host | startup readiness |
| 02 | ✅ Archived | startup timing/readiness | ~25-35 min | depends_on order != readiness; use healthcheck | persistence |
| 03 | 🚧 In Progress | wrong volume mount target |  | data durability | backups + restore drill |

## Notes
- Lab 01 branch: `lab/01-networking`
- Lab 02 branch: `lab/02-readiness`
- `main` always contains the active lab.
- Keep healthchecks as default baseline for service dependencies.
