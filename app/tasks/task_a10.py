import sqlite3
from app.config import DATA_DIR
from app.utils.file_utils import write_file_safe

def run() -> str:
    """
    Query /data/ticket-sales.db to compute the total sales of "Gold" tickets,
    then write the result to /data/ticket-sales-gold.txt.
    """
    db_path = f"{DATA_DIR}/ticket-sales.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = "SELECT SUM(units * price) FROM tickets WHERE type = 'Gold';"
    cur.execute(query)
    total = cur.fetchone()[0] or 0
    conn.close()
    write_file_safe("ticket-sales-gold.txt", str(total))
    return f"Total Gold ticket sales: {total}"