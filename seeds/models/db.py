from typing import Dict, Any
from collections import defaultdict
class InMemoryDB:
    def __init__(self):
        self.contacts: Dict[str, Dict[str, Any]] = {}
        self.companies: Dict[str, Dict[str, Any]] = {}
        self.metrics = defaultdict(int)
    def log_event(self, etype: str, payload: dict): self.metrics[f"events_{etype}"] += 1
    def update_contact_status(self, cid: str, status: str):
        if cid in self.contacts: self.contacts[cid]['status'] = status
    def increment(self, key: str): self.metrics[key] += 1
    def pick_contact(self, company_id: str):
        for c in self.contacts.values():
            if c['company_id']==company_id and not c.get('opt_out'): return c
        raise ValueError("No contact found")
DB = InMemoryDB()
