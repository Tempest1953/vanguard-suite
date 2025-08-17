from datetime import datetime

# simple in-memory log store for now
LOGS = []

def add_log(endpoint: str):
    LOGS.append({
        "endpoint": endpoint,
        "timestamp": datetime.utcnow().isoformat()
    })

def get_logs():
    return LOGS
