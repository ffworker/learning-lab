# Debug Lab 04 (Backup & Restore Drill)

## Quick Project Snapshot
- **Current active lab:** `main` branch (right now: **Lab 04**)
- **Finished labs:** `lab/01-networking`, `lab/02-readiness`, `lab/03-persistence`
- **Flow:** finish lab on `main` → push to `lab/NN-*` branch → scaffold next lab on `main`

Your mission: validate backup + restore flow and fix one restore bug.

## Goal
1. Create backup from DB
2. Simulate data loss
3. Restore from backup successfully
4. Verify recovered row exists

## Rules (teacher mode)
1. First run scripts as-is and observe failure.
2. Do not edit app/db first; inspect scripts + logs.
3. Fix exactly one root-cause line.
4. Verify with proof query at end.

## Start
```bash
cd learning-lab-01
sudo docker compose down -v
sudo docker compose up --build -d
```

## Drill commands
```bash
# seed one row
sudo docker compose exec db psql -U postgres -d labdb -c "CREATE TABLE IF NOT EXISTS notes(id serial primary key, txt text); INSERT INTO notes(txt) VALUES ('restore-me');"

# backup
./scripts/backup.sh

# simulate loss
sudo docker compose exec db psql -U postgres -d labdb -c "DROP TABLE notes;"

# restore (currently buggy)
./scripts/restore.sh

# verify
sudo docker compose exec db psql -U postgres -d labdb -c "SELECT * FROM notes;"
```

## Reporting
```bash
cp LAB_REPORT_TEMPLATE.md reports/lab-04-report.md
```
Fill report + update `LAB_TRACKER.md`.

---

## Quick Lesson Overview (update after each lab)

| Lab | Topic | Bug Type | Key Learning |
|---|---|---|---|
| 01 | Compose networking | Wrong DB host in `DATABASE_URL` | In Compose, use **service name** as hostname (`db`), not DB username (`postgres`). |
| 02 | Startup readiness | App can start before DB is ready | `depends_on` order is not enough; use **healthchecks** + `service_healthy`. |
| 03 | Persistence/volumes | Wrong DB volume mount target | Persistent DB data only survives when volume is mounted to the **actual Postgres data dir**. |
| 04 | Backup/restore | Restore script targets wrong DB | A backup is useless unless restore is tested against the **correct target database**. |
