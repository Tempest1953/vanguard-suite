from utils.email_sender import send_email
from fastapi import APIRouter
from datetime import datetime

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
    return {
        "ok": True,
        "message": "Recruitment campaign endpoint ready",
        "product": "LexiPlex",
        "log_id": len(logs)
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
    from fastapi import APIRouter
from app.logs import add_log, get_logs  # 👈 import log functions

router = APIRouter()

@router.get("/recruitment")
def recruitment():
    add_log("recruitment")
    return {"ok": True, "message": "Recruitment campaign endpoint ready", "product": "LexiPlex"}

@router.get("/strategic")
def strategic():
    add_log("strategic")
    return {"ok": True, "message": "Strategic buyer campaign endpoint ready", "product": "CFOCore"}

@router.get("/logs")
def logs():
    return {"count": len(get_logs()), "entries": get_logs()}
