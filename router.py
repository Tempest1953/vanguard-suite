from fastapi import APIRouter
from app.models.db import DB
from app.hub import SwarmHub
from app.memory.vector import MEM
from app.agents.dealstrike import DealStrikeBot
from app.agents.investorlens import InvestorLensBot
from app.agents.evalintel import EvalIntelBot
from app.agents.orchestrator import Orchestrator
from app.seeds import campaigns
router = APIRouter()
HUB = SwarmHub(DB, MEM)
HUB.register(Orchestrator(HUB))
HUB.register(InvestorLensBot(HUB))
HUB.register(DealStrikeBot(HUB))
HUB.register(EvalIntelBot(HUB))
@router.post("/seed/recruitment")
async def seed_recruitment():
    stats = campaigns.seed_recruitment()
    for comp in campaigns.RECRUITMENT_CLIENTS:
        await HUB.emit({"type":"NEW_ACCOUNT","payload":{"company":comp,"product":"LexiPlex"}})
    return {"ok": True, "stats": stats}
@router.post("/seed/strategic")
async def seed_strategic():
    stats = campaigns.seed_strategic()
    for comp in campaigns.STRATEGIC_BUYERS:
        await HUB.emit({"type":"NEW_ACCOUNT","payload":{"company":comp,"product":"CFOCore"}})
    return {"ok": True, "stats": stats}
@router.post("/seed")
async def seed_one():
    DB.companies["acme"]={"id":"acme","name":"Acme Capital","domain":"acmecap.com"}
    DB.contacts["jane"]={"id":"jane","company_id":"acme","name":"Jane Doe","email":"jane@acmecap.com"}
    await HUB.emit({"type":"NEW_ACCOUNT","payload":{"company":DB.companies["acme"],"product":"CFOCore"}})
    return {"ok": True, "metrics": dict(DB.metrics)}
