import os
from app.config import DATA_DIR
from app.utils.file_utils import write_file_safe

def run() -> str:
    """
    Get first line of the 10 most recent .log files in /data/logs/ and write them to /data/logs-recent.txt.
    """
    logs_path = os.path.join(DATA_DIR, "logs")
    log_files = [f for f in os.listdir(logs_path) if f.endswith(".log")]
    log_files.sort(key=lambda f: os.path.getmtime(os.path.join(logs_path, f)), reverse=True)
    recent_logs = log_files[:10]
    first_lines = []
    for logfile in recent_logs:
        with open(os.path.join(logs_path, logfile), "r", encoding="utf-8") as f:
            first_lines.append(f.readline().strip())
    output = "\n".join(first_lines)
    write_file_safe("logs-recent.txt", output)
    return "Extracted first lines from 10 most recent log files."