import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

BASE_URL = os.getenv("BACKEND_BASE_URL", "http://127.0.0.1:8000/api/v1").rstrip("/")


def get_health() -> dict:
    response = requests.get(f"{BASE_URL}/health/", timeout=10)
    response.raise_for_status()
    return response.json()


def get_kpis() -> dict:
    response = requests.get(f"{BASE_URL}/kpis/", timeout=30)
    response.raise_for_status()
    return response.json()


def create_prediction(payload: dict) -> dict:
    response = requests.post(f"{BASE_URL}/predictions/", json=payload, timeout=30)
    response.raise_for_status()
    return response.json()


def upload_preview(file_name: str, file_bytes: bytes) -> dict:
    files = {"file": (file_name, file_bytes)}
    response = requests.post(f"{BASE_URL}/ingest/preview/", files=files, timeout=60)
    response.raise_for_status()
    return response.json()
