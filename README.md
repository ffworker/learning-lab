# Debug Lab 02 (Startup Timing / Readiness)

Lab 01 is preserved in branch `lab/01-networking`.

Your mission: diagnose and fix a startup timing issue between app and db.
(There is an intentional race condition bug in this lab.)

## Goal
- `GET /` returns status ok
- `GET /health` returns status ok + db=1 (consistently, including fresh starts)

## Rules (teacher mode)
1. Do **not** edit files for first 10 minutes.
2. Gather evidence first:
   - `docker compose down -v`
   - `docker compose up --build`
   - `docker compose ps`
   - `docker compose logs -f app`
   - `docker compose logs -f db`
3. Document symptom → timeline → root cause.
4. Implement a deterministic fix (not random retries).

## Start
```bash
cd learning-lab-01
sudo docker compose down -v
sudo docker compose up --build
```

## Endpoints
```bash
curl -s http://localhost:3000/
curl -s http://localhost:3000/health
```

## Reporting
```bash
cp LAB_REPORT_TEMPLATE.md reports/lab-02-report.md
```
Fill report + update `LAB_TRACKER.md`.

---

## Quick Lesson Overview (update after each lab)

| Lab | Topic | Bug Type | Key Learning |
|---|---|---|---|
| 01 | Compose networking | Wrong DB host in `DATABASE_URL` | In Compose, use **service name** as hostname (`db`), not DB username (`postgres`). |
| 02 | Startup readiness | App can start before DB is ready | `depends_on` order is not enough; use **healthchecks** + `service_healthy`. |
