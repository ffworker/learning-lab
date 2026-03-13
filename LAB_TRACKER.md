# Lab Tracker

Use this to close each lab, summarize progress, and design the next one.

## Progress Board

| Lab | Status | Main Bug Type | Time | Confidence Δ | Key Learning | Next Focus |
|---|---|---|---|---|---|---|
| 01 | ✅ Closed | Compose DNS host mismatch | ~30-40 min | +3 (3→6) | Use compose service name as DB host (`db`) | Startup timing/readiness |
| 02 | Planned | startup timing / race condition |  |  |  | readiness strategies |
| 03 | Not Started |  |  |  |  |  |

---

## Lab Closure Summary (fill after each lab)

### Lab 01
- **What broke:** `DATABASE_URL` used host `postgres` while db service name is `db`.
- **How I found it:** compared `/` (200) vs `/health` (500), then inspected app logs + compose connection string.
- **Minimal fix:** changed one line in `docker-compose.yml` from `@postgres:5432` to `@db:5432`.
- **Most valuable lesson:** a running container can still fail on dependency connectivity.
- **Reusable debugging rule:** If health endpoint fails but root endpoint works, inspect dependency connection config first.

### Promote to long-term memory
- **Keep forever:** In compose networking, service name is the hostname.
- **Still shaky:** Distinguishing normal DB log noise vs real failure signal.

### Design for next lab
- **Raise difficulty by:** making failure intermittent (timing-based) instead of static config typo.
- **Constraint:** no editing for first 10 minutes; must gather evidence first.
- **Target skill:** readiness diagnosis and deterministic fix.
