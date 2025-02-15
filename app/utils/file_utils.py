import os
from app.config import DATA_DIR

def sanitize_path(path: str) -> str:
    # Remove extra whitespace and ensure path is within DATA_DIR
    cleaned = path.strip()
    abs_path = os.path.abspath(os.path.join(DATA_DIR, cleaned))
    if not abs_path.startswith(DATA_DIR):
        raise ValueError("Access to this path is forbidden.")
    return abs_path

def read_file_safe(path: str) -> str:
    abs_path = sanitize_path(path)
    with open(abs_path, "r", encoding="utf-8") as f:
        return f.read()

def write_file_safe(path: str, content: str) -> None:
    abs_path = sanitize_path(path)
    os.makedirs(os.path.dirname(abs_path), exist_ok=True)
    with open(abs_path, "w", encoding="utf-8") as f:
        f.write(content)

def write_log(message: str) -> None:
    log_path = sanitize_path("logs/agent.log")
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(message + "\n")