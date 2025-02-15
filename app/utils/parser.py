def parse_task(task_description: str) -> str:
    desc = task_description.lower()
    # A tasks
    if "datagen.py" in desc or "install uv" in desc:
        return "A1"
    if "format" in desc and "format.md" in desc:
        return "A2"
    if "wednesday" in desc and "dates.txt" in desc:
        return "A3"
    if "contacts" in desc and "sort" in desc:
        return "A4"
    if "log" in desc and "recent" in desc:
        return "A5"
    if "markdown" in desc and "index" in desc:
        return "A6"
    if "email" in desc and "extract" in desc:
        return "A7"
    if "credit card" in desc:
        return "A8"
    if "comments" in desc and "similar" in desc:
        return "A9"
    if "ticket" in desc and "gold" in desc:
        return "A10"
    
    # B tasks
    if "fetch data" in desc or ("api" in desc and "save" in desc):
        return "B3"
    if "clone a git repo" in desc or ("git" in desc and "commit" in desc):
        return "B4"
    if ("run sql query" in desc or "count tickets" in desc or "query database" in desc):
        return "B5"
    if "scrape" in desc or "extract data from website" in desc:
        return "B6"
    if "resize image" in desc or "compress image" in desc:
        return "B7"
    if "transcribe audio" in desc or ("mp3" in desc and "transcribe" in desc):
        return "B8"
    if "markdown to html" in desc:
        return "B9"
    if "filter csv" in desc or ("csv" in desc and "json" in desc):
        return "B10"
    
    raise ValueError("Unable to parse task description.")