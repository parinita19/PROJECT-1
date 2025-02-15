import requests
from bs4 import BeautifulSoup
from app.utils.file_utils import write_file_safe

def run() -> str:
    """
    B6: Scrape https://example.com and extract its title.
    Save the title to /data/website_title.txt.
    """
    url = "https://example.com"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch website data: {response.status_code}")
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip() if soup.title else "No title found"
    write_file_safe("website_title.txt", title)
    return f"Extracted website title: {title}"
