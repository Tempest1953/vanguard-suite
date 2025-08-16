from app.models.db import DB
RECRUITMENT_CLIENTS=[{"id":f"lawfirm{i}","name":f"LawFirm {i}","domain":f"law{i}.com"} for i in range(1,13)]
RECRUITMENT_CANDIDATES=[{"id":f"lawyer{i}","company_id":f"lawfirm{i%12+1}","name":f"Lawyer {i}","email":f"lawyer{i}@mail.com"} for i in range(1,13)]
STRATEGIC_BUYERS=[{"id":f"corp{i}","name":f"Corp {i}","domain":f"corp{i}.ai"} for i in range(1,14)]
STRATEGIC_CONTACTS=[{"id":f"exec{i}","company_id":f"corp{i%13+1}","name":f"Exec {i}","email":f"exec{i}@corp{i%13+1}.ai"} for i in range(1,14)]
def seed_recruitment():
    for c in RECRUITMENT_CLIENTS: DB.companies[c["id"]]=c
    for cand in RECRUITMENT_CANDIDATES: DB.contacts[cand["id"]]=cand
    return {"clients":len(RECRUITMENT_CLIENTS),"candidates":len(RECRUITMENT_CANDIDATES)}
def seed_strategic():
    for c in STRATEGIC_BUYERS: DB.companies[c["id"]]=c
    for ex in STRATEGIC_CONTACTS: DB.contacts[ex["id"]]=ex
    return {"buyers":len(STRATEGIC_BUYERS),"contacts":len(STRATEGIC_CONTACTS)}
