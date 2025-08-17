from fastapi import APIRouter

router = APIRouter()

@router.get("/recruitment")
def recruitment():
    return {"ok": True, "service": "Recruitment AI Agent", "status": "ready"}

@router.get("/strategic")
def strategic():
    return {"ok": True, "service": "Strategic Sales AI Agent", "status": "ready"}
