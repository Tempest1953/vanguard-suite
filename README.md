# Vanguard Sales Agent Suite

Autonomous, self-learning multi-agent sales system for Braylock core + branch businesses (including Recruitment).

## Quick Start (Local)
1. Install Python 3.11
2. In a terminal:
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```
3. Open http://localhost:8000

## Docker (Local)
```
docker build -t vanguard-suite:latest .
docker run -p 8000:8000 --name vanguard vanguard-suite:latest
```

## Endpoints
- `GET /` – health
- `POST /seed/recruitment` – seed & fire recruitment campaign
- `POST /seed/strategic` – seed & fire strategic buyer campaign

## Deploy
- Use the included Dockerfile on Render / Railway / Fly.io / Cloud Run / Azure.
