import os

DATA_DIR = os.path.abspath(os.path.join(os.getcwd(), "data"))
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN", "")