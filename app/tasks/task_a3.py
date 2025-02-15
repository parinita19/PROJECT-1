import datetime
from app.utils.file_utils import read_file_safe, write_file_safe

def run() -> str:
    """
    Count Wednesdays in /data/dates.txt and write count to /data/dates-wednesdays.txt.
    Expect dates in ISO format (YYYY-MM-DD).
    """
    content = read_file_safe("dates.txt")
    count = 0
    for line in content.splitlines():
        try:
            dt = datetime.datetime.strptime(line.strip(), "%Y-%m-%d")
            if dt.weekday() == 2:
                count += 1
        except Exception:
            continue
    write_file_safe("dates-wednesdays.txt", str(count))
    return f"Found {count} Wednesdays."