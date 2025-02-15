import os
import re
import json
from app.config import DATA_DIR
from app.utils.file_utils import write_file_safe

def run() -> str:
    """
    Find all Markdown files in /data/docs/, extract the first H1 title (line starting with "# "),
    and write an index mapping filenames to titles to /data/docs/index.json.
    """
    docs_path = os.path.join(DATA_DIR, "docs")
    index = {}
    for root, _, files in os.walk(docs_path):
        for file in files:
            if file.endswith(".md"):
                rel_path = os.path.relpath(os.path.join(root, file), docs_path)
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for line in f:
                        if re.match(r"^#\s+", line):
                            index[rel_path] = line.strip()[2:].strip()
                            break
    # Ensure the index file is written inside the docs folder under data
    write_file_safe("docs/index.json", json.dumps(index, indent=2))
    return "Documentation index created."