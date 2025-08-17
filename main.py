from fastapi import FastAPI
from app.agents_router import router   # import the new router file

app = FastAPI(title="Vanguard Sales Agent Suite")

@app.get("/")
def root():
    return {"ok": True, "service": "Vanguard Sales Agent Suite"}

# include the AI agent routes
app.include_router(router)
