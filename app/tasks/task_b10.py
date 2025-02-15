import csv
import json
from app.utils.file_utils import write_file_safe

def run() -> str:
    """
    B10: Read /data/data.csv, filter rows where the 'value' column is greater than 50,
    and save the filtered rows as JSON to /data/filtered-data.json.
    """
    input_csv = "data.csv"
    output_json = "filtered-data.json"
    filtered_rows = []
    
    with open(input_csv, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                if float(row.get("value", 0)) > 50:
                    filtered_rows.append(row)
            except ValueError:
                continue
    write_file_safe(output_json, json.dumps(filtered_rows, indent=2))
    return "CSV filtered and JSON output written to filtered-data.json."