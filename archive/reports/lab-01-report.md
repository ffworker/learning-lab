# Lab 01 Report

## 0) Metadata
- **Lab:** 01
- **Date:** 2026-03-13
- **Duration:** ~30-40 min
- **Confidence before (0-10):** 3
- **Confidence after (0-10):** 6

## 1) Objective (in my own words)
Debug a containerized app + database setup by using evidence (logs/endpoints), not guesswork.

## 2) Expected behavior
- `GET /` returns status ok
- `GET /health` returns status ok and db=1

## 3) Observed symptom(s)
- `/` returned 200
- `/health` returned 500
- App process looked healthy

## 4) Hypotheses
1. DB tuning/checkpoint issue
2. Port mismatch
3. DB connection string / host mismatch
4. Startup timing issue

## 5) Investigation log (chronological)
| Step | Command / Action | Why | Result | What it means |
|---|---|---|---|---|
| 1 | `docker compose logs app` | check app runtime health | app served requests; `/health` 500 | app alive, handler failing internally |
| 2 | inspect endpoint behavior | compare `/` vs `/health` | `/` 200, `/health` 500 | failure isolated to DB check path |
| 3 | check compose env line | validate DB URL host | URL used `@postgres:5432` while service is `db` | DNS/service-name mismatch likely root cause |

## 6) Root cause
Application DB host in `DATABASE_URL` pointed to `postgres` instead of compose service name `db`.

## 7) Fix
- **File:** `docker-compose.yml`
- **Line changed:** app `DATABASE_URL`
- **Before:** `...@postgres:5432/...`
- **After:** `...@db:5432/...`
- **Why this works:** In docker compose, services resolve by service name on the internal network.

## 8) Verification
- `/health` returned success after restart
- app and db running, endpoint behavior correct

## 9) Learning extraction
### What I learned (technical)
- HTTP 500 means server-side/internal failure in handler path.
- Compose service discovery uses service names, not DB usernames.
- Healthy process does not mean healthy dependencies.

### What I learned (debugging process)
- Compare healthy endpoint vs failing endpoint to isolate subsystem.
- Treat logs as evidence and refine hypotheses quickly.

### Mistake pattern to avoid next time
- Don’t over-index on noisy DB log lines (e.g., checkpoints) before checking connection config.

## 10) Closure checklist
- [x] I can explain the bug without reading notes
- [x] I can explain why first hypothesis was wrong
- [x] I verified before and after behavior
- [x] I wrote one reusable rule for future labs

## 11) Reusable rule (one-liner)
"If one endpoint is healthy but health-check fails, inspect dependency connection settings (host/service name, auth, db name) first."

## 12) Build into Lab 02
- **Next weakness to train:** startup timing + readiness validation
- **Proposed bug type:** startup timing / race condition
- **Success criteria for Lab 02:** identify timing-related failure from logs and fix with proper readiness strategy (not blind sleep).
