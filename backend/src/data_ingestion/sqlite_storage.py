import sqlite3
import os
from datetime import datetime

def get_db_path():
    return os.getenv("SQLITE_DB_PATH", "price_estimator.db")

def init_db():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vendor_id TEXT NOT NULL,
        code TEXT NOT NULL,
        description TEXT,
        msrp_price REAL,
        internal_cost REAL,
        last_updated TEXT,
        UNIQUE(vendor_id, code)
    );
    """)
    c.execute("CREATE INDEX IF NOT EXISTS idx_vendor_code ON items (vendor_id, code);")
    conn.commit()
    conn.close()

def upsert_item(item):
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        INSERT INTO items (vendor_id, code, description, msrp_price, internal_cost, last_updated)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(vendor_id, code) DO UPDATE SET
            description=excluded.description,
            msrp_price=excluded.msrp_price,
            internal_cost=excluded.internal_cost,
            last_updated=excluded.last_updated
    """, (
        item['vendor_id'],
        item['code'],
        item['description'],
        item['msrp_price'],
        item['internal_cost'],
        item.get('last_updated', datetime.utcnow().isoformat())
    ))
    conn.commit()
    conn.close()

def get_all_vendors():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT DISTINCT vendor_id FROM items")
    vendors = [row[0] for row in c.fetchall()]
    conn.close()
    return vendors

def get_items_by_vendor(vendor_id):
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT code, description, msrp_price FROM items WHERE vendor_id=?", (vendor_id,))
    items = [{"code": row[0], "description": row[1], "msrp_price": row[2]} for row in c.fetchall()]
    conn.close()
    return items
