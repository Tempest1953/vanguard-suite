from fastapi import FastAPI
import asyncio
import app.router as router
import app.scheduler as scheduler
from app.router import HUB
from app.seeds import campaigns
app = FastAPI(title="Vanguard Sales Agent Suite")
app.include_router(router.router)
def _register_jobs():
    scheduler.SCHED.every(24*60*60, job_recruitment_seed)
    scheduler.SCHED.every(48*60*60, job_strategic_seed)
async def job_recruitment_seed():
    campaigns.seed_recruitment()
    for comp in campaigns.RECRUITMENT_CLIENTS:
        await HUB.emit({"type":"NEW_ACCOUNT","payload":{"company":comp,"product":"LexiPlex"}})
    print("[SCHED] recruitment campaign fired")
async def job_strategic_seed():
    campaigns.seed_strategic()
    for comp in campaigns.STRATEGIC_BUYERS:
        await HUB.emit({"type":"NEW_ACCOUNT","payload":{"company":comp,"product":"CFOCore"}})
    print("[SCHED] strategic buyer campaign fired")
@app.on_event("startup")
async def startup_jobs():
    _register_jobs()
    asyncio.create_task(scheduler.SCHED.run_forever())
@app.get("/")
async def root():
    return {"ok": True, "service": "Vanguard Sales Agent Suite"}
