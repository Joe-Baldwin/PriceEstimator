import os
import sys
import json
import sqlite3

def handle_query(sql, params=None):
    db_path = os.getenv("SQLITE_DB_PATH", "backend/price_estimator.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(sql, params or [])
    if sql.strip().lower().startswith("select"):
        columns = [desc[0] for desc in c.description]
        rows = c.fetchall()
        result = [dict(zip(columns, row)) for row in rows]
        conn.close()
        return result
    else:
        conn.commit()
        conn.close()
        return {'status': 'success'}

def main():
    print("SQLite MCP server started")
    sys.stdout.flush()
    for line in sys.stdin:
        try:
            request = json.loads(line)
            action = request.get('action')
            if action == 'query':
                sql = request['sql']
                params = request.get('params', [])
                result = handle_query(sql, params)
                print(json.dumps({'result': result}))
            else:
                print(json.dumps({'error': 'Unknown action'}))
        except Exception as e:
            print(json.dumps({'error': str(e)}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
