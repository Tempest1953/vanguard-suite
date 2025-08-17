rom fastapi import APIRouter

router = APIRouter()

@router.get("/recruitment")
async def recruitment():
    return {
        "ok": True,
        "message": "Recruitment campaign endpoint ready",
        "product": "LexiPlex"
    }

@router.get("/strategic")
async def strategic():
    return {
        "ok": True,
        "message": "Strategic buyer campaign endpoint ready",
        "product": "CFOCore"
    }
