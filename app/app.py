import os
import sys
from flask import Flask, jsonify
import psycopg

app = Flask(__name__)
DB_URL = os.getenv("DATABASE_URL")


def check_db():
    with psycopg.connect(DB_URL, connect_timeout=2) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            return cur.fetchone()[0]


@app.route("/")
def index():
    return jsonify({"status": "ok", "lab": 2})


@app.route("/health")
def health():
    try:
        val = check_db()
        return jsonify({"status": "ok", "db": val})
    except Exception as e:
        return jsonify({"status": "error", "reason": str(e)}), 500


if __name__ == "__main__":
    # INTENTIONAL LAB BUG:
    # Fail fast if DB is not ready exactly at app startup.
    # This makes startup ordering/timing issues visible.
    try:
        check_db()
    except Exception as e:
        print(f"Startup DB check failed: {e}", file=sys.stderr)
        sys.exit(1)

    app.run(host="0.0.0.0", port=3000)
