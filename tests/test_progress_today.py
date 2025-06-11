# tests/test_progress_today.py
import sys
import os
import pytest
from fastapi.testclient import TestClient

# Make sure to add the parent directory to sys.path so it finds `main`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app

client = TestClient(app)

def test_progress_today_returns_200():
    response = client.get("/progress/today")
    assert response.status_code == 200

def test_progress_today_returns_valid_data():
    response = client.get("/progress/today")
    assert response.status_code == 200
    data = response.json()
    assert "calories" in data
    assert isinstance(data["calories"], (int, float))
    assert data["calories"] >= 0

def test_workout_summary():
    response = client.get("/workouts/1/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_calories" in data
    assert isinstance(data["exercise_summaries"], list)