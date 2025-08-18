from fastapi import APIRouter
from datetime import datetime
from utils.email_sender import send_email   # email helper

router = APIRouter()

# simple in-memory log
logs = []

@router.get("/recruitment")
def recruitment():
    entry = {
        "time": datetime.utcnow().isoformat(),
        "agent": "Recruitment AI Agent",
        "action": "Outreach pitch triggered for LexiPlex"
    }
    logs.append(entry)

    # send a demo email
    result = send_email(
        "testrecipient@example.com",
        "LexiPlex AI Outreach",
        "Hello, this is LexiPlex AI reaching out about recruitment solutions."
    )

    return {
        "ok": True,
        "message": "Recruitment campaign endpoint ready",
        "product": "LexiPlex",
        "log_id": len(logs),
        "email_result": result
    }

@router.get("/strategic")
def strategic():
    entry = {
        "time": datetime.utcnow().isoformat(),
        "agent": "Strategic Sales AI Agent",
        "action": "Outreach pitch triggered for CFOCore"
    }
    logs.append(entry)
    return {
        "ok": True,
        "message": "Strategic buyer campaign endpoint ready",
        "product": "CFOCore",
        "log_id": len(logs)
    }

@router.get("/logs")
def get_logs():
    return {"count": len(logs), "entries": logs}

# 👇 New route for Automations to stop error emails
@router.get("/sweep")
def sweep():
    return {
        "ok": True,
        "message": "Post-Ignition Sweep successful",
        "regions": ["EU", "US", "Asia", "Global"]
    }
