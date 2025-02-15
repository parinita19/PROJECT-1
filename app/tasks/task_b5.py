import sqlite3
from app.config import DATA_DIR
from app.utils.file_utils import write_file_safe

def run() -> str:
    """
    B5: Run a SQL query on /data/ticket-sales.db to count the total number of tickets.
    Write the result to /data/ticket-count.txt.
    """
    db_path = f"{DATA_DIR}/ticket-sales.db"
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = "SELECT COUNT(*) FROM tickets;"
    cur.execute(query)
    count = cur.fetchone()[0]
    conn.close()
    write_file_safe("ticket-count.txt", str(count))
    return f"Total number of tickets: {count}"
