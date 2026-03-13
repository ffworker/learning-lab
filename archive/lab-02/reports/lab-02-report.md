# Lab 02 Report

## 0) Metadata
- **Lab:** 02
- **Date:** 2026-03-13
- **Duration:** ~25-35 min
- **Confidence before (0-10):** 5
- **Confidence after (0-10):** 7

## 1) Objective (in your own words)
Understand startup timing/readiness and implement a deterministic fix so app only starts when DB is truly ready.

## 2) Expected behavior
App starts reliably and `/health` returns 200 after fresh startup.

## 3) Observed symptom(s)
Initial confusion: services looked healthy in one run. Root issue identified as app can start before DB readiness.

## 4) Hypotheses
1. App starts before DB is ready
2. Need startup retries in app
3. Compose dependency only controls order, not readiness

## 5) Investigation log (chronological)
| Step | Command / Action | Why | Result | What it means |
|---|---|---|---|---|
| 1 | inspect app/db logs | confirm failure class | startup/readiness mismatch discussion validated | timing issue likely |
| 2 | inspect compose dependencies | verify orchestration behavior | plain `depends_on` used | no readiness gate |
| 3 | add healthcheck + service_healthy | deterministic readiness control | app/db healthy and `/health` 200 | root problem fixed |

## 6) Root cause
`depends_on` startup ordering was insufficient; app could start before DB accepted connections.

## 7) Fix
- **File:** `docker-compose.yml`
- **Change:** added `db.healthcheck` and app `depends_on: db: condition: service_healthy`
- **Why this works:** app waits for DB readiness signal, not just container start event.

## 8) Verification
- `docker compose ps` showed healthy state
- `/health` returned success

## 9) Learning extraction
- Healthchecks are first-class operational controls.
- Service order != service readiness.
- Deterministic readiness beats arbitrary sleep loops.

## 10) Reusable rule (one-liner)
"If service A depends on service B, gate startup on B's healthcheck, not mere start order."

## 11) Build into Lab 03
- Next weakness: persistence guarantees
- Proposed bug type: wrong volume mount target
- Success criteria: data survives `down/up` (without `-v`) consistently.
