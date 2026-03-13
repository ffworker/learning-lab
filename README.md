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

When done, send your reasoning + the line you changed.
