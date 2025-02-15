import markdown
from app.utils.file_utils import read_file_safe, write_file_safe

def run() -> str:
    """
    B9: Convert /data/markdown.md (a Markdown file) to HTML and save as /data/markdown.html.
    """
    md_content = read_file_safe("markdown.md")
    html_content = markdown.markdown(md_content)
    write_file_safe("markdown.html", html_content)
    return "Markdown converted to HTML successfully."
