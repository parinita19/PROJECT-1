import os
import subprocess
from app.config import DATA_DIR
from app.utils.file_utils import write_file_safe

def run() -> str:
    """
    B4: Clone a git repository (to /data/git_repo) and make a commit.
    This operation is done locally and does not push to a remote.
    """
    repo_url = "https://github.com/octocat/Spoon-Knife.git"
    clone_dir = os.path.join(DATA_DIR, "git_repo")
    
    # Clone if not already cloned
    if not os.path.exists(clone_dir):
        subprocess.run(["git", "clone", repo_url, clone_dir], check=True)
    
    # Create a new file and commit the change
    new_file = os.path.join(clone_dir, "automated_commit.txt")
    write_file_safe(os.path.relpath(new_file, DATA_DIR), "This is an automated commit from the LLM agent.")
    subprocess.run(["git", "-C", clone_dir, "add", "automated_commit.txt"], check=True)
    subprocess.run(["git", "-C", clone_dir, "commit", "-m", "Automated commit from LLM agent"], check=True)
    
    return "Cloned repository and made an automated commit."