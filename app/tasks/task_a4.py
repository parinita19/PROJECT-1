import json
from app.utils.file_utils import read_file_safe, write_file_safe

def run() -> str:
    """
    Sort contacts in /data/contacts.json by last_name then first_name.
    Write sorted contacts to /data/contacts-sorted.json.
    """
    contacts = json.loads(read_file_safe("contacts.json"))
    sorted_contacts = sorted(contacts, key=lambda x: (x.get("last_name", "").lower(), x.get("first_name", "").lower()))
    write_file_safe("contacts-sorted.json", json.dumps(sorted_contacts, indent=2))
    return "Contacts sorted successfully."
