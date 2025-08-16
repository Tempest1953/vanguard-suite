from fastapi import FastAPI
from typing import Dict, Any
import asyncio

app = FastAPI(title="Vanguard Sales Agent Suite")

DB: Dict[str, Any] = {"companies": {}, "contacts": {}, "metrics": {"sends": 0, "replies_total": 0}}

@app.get("/")
def root():
    return {"ok": True, "service": "Vanguard Sales Agent Suite"}

RECRUITMENT_CLIENTS = [{"id": f"lawfirm{i}", "name": f"LawFirm {i}", "domain": f"law{i}.com"} for i in range(1, 6)]
RECRUITMENT_CANDIDATES = [{"id": f"lawyer{i}", "company_id": f"lawfirm{i%5+1}", "name": f"Lawyer {i}", "email": f"lawyer{i}@mail.com"} for i in range(1, 6)]
STRATEGIC_BUYERS = [{"id": f"corp{i}", "name": f"Corp {i}", "domain": f"corp{i}.ai"} for i in range(1, 6)]
STRATEGIC_CONTACTS = [{"id": f"exec{i}", "company_id": f"corp{i%5+1}", "name": f"Exec {i}", "email": f"exec{i}@corp{i%5+1}.ai"} for i in range(1, 6)]

def seed_recruitment():
    for c in RECRUITMENT_CLIENTS: DB["companies"][c["id"]] = c
    for cand in RECRUITMENT_CANDIDATES: DB["contacts"][cand["id"]] = cand
    return {"clients": len(RECRUITMENT_CLIENTS), "candidates": len(RECRUITMENT_CANDIDATES)}

def seed_strategic():
    for c in STRATEGIC_BUYERS: DB["companies"][c["id"]] = c
    for ex in STRATEGIC_CONTACTS: DB["contacts"][ex["id"]] = ex
    return {"buyers": len(STRATEGIC_BUYERS), "contacts": len(STRATEGIC_CONTACTS)}

def dev_send(to: str, subject: str, body: str) -> None:
    print(f"[DEV SEND] → {to}: {subject}\n{body}\n", flush=True)

async def run_recruitment_sequence():
    for cand in RECRUITMENT_CANDIDATES:
        dev_send(cand["email"], "Senior legal shortlist in 72h (LexiPlex)", f"Hi {cand['name']}, quick one from LexiPlex — AI-curated legal roles. Interested?")
        DB["metrics"]["sends"] += 1
        await asyncio.sleep(0.1)

async def run_strategic_sequence():
    for ex in STRATEGIC_CONTACTS:
        dev_send(ex["email"], "Fast idea on CFOCore", f"Hi {ex['name']}, quick value thesis on CFOCore for {ex['company_id']}.")
        DB["metrics"]["sends"] += 1
        await asyncio.sleep(0.1)

@app.post("/seed/recruitment")
async def seed_and_run_recruitment():
    stats = seed_recruitment(); await run_recruitment_sequence()
    return {"ok": True, "stats": stats, "metrics": DB["metrics"]}

@app.post("/seed/strategic")
async def seed_and_run_strategic():
    stats = seed_strategic(); await run_strategic_sequence()
    return {"ok": True, "stats": stats, "metrics": DB["metrics"]}

async def scheduler_loop():
    await run_recruitment_sequence()
    await run_strategic_sequence()
    while True:
        await asyncio.sleep(24*60*60); await run_recruitment_sequence()
        await asyncio.sleep(24*60*60); await run_strategic_sequence()

@app.on_event("startup")
async def on_startup():
    asyncio.create_task(scheduler_loop())
