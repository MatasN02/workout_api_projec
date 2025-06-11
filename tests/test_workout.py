from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_workout_summary():
    response = client.get("/workouts/1/summary")
    assert response.status_code == 200
    data = response.json()
    assert "total_calories" in data
    assert isinstance(data["exercise_summaries"], list)
