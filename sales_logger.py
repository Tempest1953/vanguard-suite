import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("leads.csv")

def log_lead(service: str, product: str):
    """Append a lead entry with timestamp, service, and product."""
    new_file = not LOG_FILE.exists()
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "service", "product"])
        writer.writerow([datetime.utcnow().isoformat(), service, product])
