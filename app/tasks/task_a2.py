from app.utils.file_utils import read_file_safe, write_file_safe

def run() -> str:
    """
    Format the contents of /data/format.md using a simulated prettier (convert to title case).
    """
    filepath = "format.md"
    content = read_file_safe(filepath)
    formatted_content = content.title()  # A simple transformation to simulate formatting
    write_file_safe(filepath, formatted_content)
    return "File formatted using prettier simulation."