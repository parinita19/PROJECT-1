import requests
from app.utils.file_utils import write_file_safe

def run() -> str:
    """
    B3: Fetch data from a public API (e.g. current Bitcoin price) and save it to /data/bitcoin.json.
    """
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    write_file_safe("bitcoin.json", response.text)
    return "Fetched Bitcoin price data and saved to bitcoin.json."