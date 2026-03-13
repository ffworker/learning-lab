# Debug Lab 03 (Persistence / Volumes)

Lab 01 and Lab 02 are archived under `archive/` with reports preserved.

Your mission: diagnose and fix a persistence bug while keeping healthchecks.

## Goal
After writing data to DB, it must survive:
1. `docker compose down`
2. `docker compose up -d`

(Do NOT use `-v` during verification.)

## Rules (teacher mode)
1. First verify current behavior before editing.
2. Use evidence:
   - `docker compose ps`
   - `docker compose logs -f db`
   - `docker compose exec db psql -U postgres -d ${POSTGRES_DB} -c "..."`
3. Explain *why* data disappeared.
4. Fix exactly the storage mapping issue.

## Start
```bash
cd learning-lab-01
sudo docker compose down -v
sudo docker compose up --build -d
```

## Repro persistence test
```bash
# create table + row
sudo docker compose exec db psql -U postgres -d ${POSTGRES_DB} -c "CREATE TABLE IF NOT EXISTS notes(id serial primary key, txt text); INSERT INTO notes(txt) VALUES ('hello-lab03');"

# verify row exists
sudo docker compose exec db psql -U postgres -d ${POSTGRES_DB} -c "SELECT * FROM notes;"

# recreate stack without deleting volumes
sudo docker compose down
sudo docker compose up -d

# verify again (should still exist when fixed)
sudo docker compose exec db psql -U postgres -d ${POSTGRES_DB} -c "SELECT * FROM notes;"
```

## Reporting
```bash
cp LAB_REPORT_TEMPLATE.md reports/lab-03-report.md
```
Fill report + update `LAB_TRACKER.md`.
