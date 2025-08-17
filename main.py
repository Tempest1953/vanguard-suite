from fastapi import FastAPI
from app import router  # 👈 make sure router.py is inside your app/ folder

app = FastAPI(title="Vanguard Sales Agent Suite")

# Root endpoint
@app.get("/")
def root():
    return {"ok": True, "service": "Vanguard Sales Agent Suite"}

# Include the recruitment & strategic endpoints
app.include_router(router.router)
