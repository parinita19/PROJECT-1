def parse_task(task_description: str) -> str:
    """
    Map keywords in the task description to a task code.
    This simple implementation uses keyword matching.
    """
    desc = task_description.lower()
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
    raise ValueError("Unable to parse task description.")