# Debug Lab 01 (Container + DB)

Your mission: run this project and find/fix the injected bug.

## Goal
- `GET /` should return status ok
- `GET /health` should return status ok + db=1

## Rules (teacher mode)
1. Do **not** edit files immediately.
2. First investigate with:
   - `docker compose up --build`
   - `docker compose ps`
   - `docker compose logs -f app`
   - `docker compose logs -f db`
   - optional: `docker compose exec app sh`
3. Write down:
   - symptom
   - investigation steps
   - root cause
   - fix
4. Then patch exactly one line.

## Start
```bash
cd debug-lab-01
docker compose up --build
```

## Test endpoints
```bash
curl http://localhost:3000/
curl http://localhost:3000/health
```

## Reporting workflow (important)
After solving, do this before calling the lab "done":

1. Create your report file from template:
   ```bash
   mkdir -p reports
   cp LAB_REPORT_TEMPLATE.md reports/lab-01-report.md
   ```
2. Fill `reports/lab-01-report.md` completely.
3. Update `LAB_TRACKER.md` row for Lab 01.
4. Add a short "Lab 01 closure" summary in `LAB_TRACKER.md`.
5. Propose Lab 02 in the tracker based on your weakest point.

When done, send me:
- your root cause,
- the exact line changed,
- your reusable rule,
- and your proposed Lab 02 bug type.

---

## Quick Lesson Overview (update after each lab)

| Lab | Topic | Bug Type | Key Learning |
|---|---|---|---|
| 01 | Compose networking | Wrong DB host in `DATABASE_URL` | In Compose, use **service name** as hostname (`db`), not DB username (`postgres`). |
