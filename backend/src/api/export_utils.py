import pandas as pd
import sqlite3
import os

def export_items_to_excel(filepath):
    db_path = os.getenv("SQLITE_DB_PATH", "price_estimator.db")
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT code as 'Item Code', description as 'Description', msrp_price as 'Price' FROM items", conn)
    df.to_excel(filepath, index=False)
    conn.close()
    return filepath
