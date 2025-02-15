from app.utils.file_utils import read_file_safe, write_file_safe
from app.utils.llm_utils import extract_email

def run() -> str:
    """
    Extract the sender’s email address from /data/email.txt.
    """
    content = read_file_safe("email.txt")
    email = extract_email(content)
    write_file_safe("email-sender.txt", email)
    return f"Extracted email: {email}"