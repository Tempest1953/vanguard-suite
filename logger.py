# logger.py
from typing import List, Dict
from datetime import datetime

# in-memory log store
_logs: List[Dict] = []

def add_log(service: str, message: str):
    """Add a new log entry with timestamp, service name, and message."""
    _logs.append({
        "timestamp": datetime.utcnow().isoformat(),
        "service": service,
        "message": message
    })

def get_logs() -> List[Dict]:
    """Return all stored logs."""
    return _logs
