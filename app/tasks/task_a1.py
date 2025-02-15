import requests
import subprocess
import tempfile

def run_datagen(user_email: str) -> str:
    url = "https://raw.githubusercontent.com/sanand0/tools-in-data-science-public/tds-2025-01/project-1/datagen.py"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to download datagen.py")
    
    # Save the script to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
        temp_file.write(response.content)
        temp_path = temp_file.name

    try:
        # Capture output and errors
        completed_process = subprocess.run(
            ["python", temp_path, user_email],
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError as e:
        # Raise an exception with detailed output for debugging
        raise Exception(
            f"datagen.py failed with exit status {e.returncode}.\nStdout: {e.stdout}\nStderr: {e.stderr}"
        )
    
    return "Data generation completed successfully."