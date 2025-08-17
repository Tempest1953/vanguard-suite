from fastapi import APIRouter
from sales_logger import log_lead   # 👈 import the logger

router = APIRouter()

@router.get("/recruitment")
def recruitment():
    log_lead("Recruitment AI Agent", "LexiPlex")
    return {"ok": True, "message": "Recruitment campaign endpoint ready", "product": "LexiPlex"}

@router.get("/strategic")
def strategic():
    log_lead("Strategic Sales AI Agent", "CFOCore")
    return {"ok": True, "message": "Strategic buyer campaign endpoint ready", "product": "CFOCore"}
