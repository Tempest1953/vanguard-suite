# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Safe, simple runtime
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app

WORKDIR /app

# Install deps
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy your whole repo (brings in the app/ folder)
COPY . .

# Expose port; Render will pass $PORT in env — we’ll honor it
EXPOSE 8000
CMD ["sh","-c","uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
