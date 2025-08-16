from fastapi import FastAPI

app = FastAPI(title="Vanguard Sales Agent Suite")

@app.get("/")
def root():
    return {"ok": True, "service": "Vanguard Sales Agent Suite"}
