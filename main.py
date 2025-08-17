from fastapi import FastAPI
from app.agents_router import router   # << notice agents_router, not router

app = FastAPI(title="Vanguard Sales Agent Suite")

@app.get("/")
def root():
    return {"ok": True, "service": "Vanguard Sales Agent Suite"}

# include our router
app.include_router(router)
