# routes/workouts.py
from fastapi import APIRouter

workouts_router = APIRouter(prefix="/workouts", tags=["Workouts"])

@workouts_router.get("/{workout_id}/summary")
async def workout_summary(workout_id: int):
    workout_items = [
        {"exercise": "Push Up", "duration_min": 10, "MET": 8.0},
        {"exercise": "Squat", "duration_min": 15, "MET": 5.0}
    ]

    user_weight_kg = 70
    exercise_summaries = []
    total_calories = 0

    for item in workout_items:
        calories = item["MET"] * 3.5 * user_weight_kg / 200 * item["duration_min"]
        exercise_summaries.append({
            "exercise": item["exercise"],
            "calories": round(calories, 2)
        })
        total_calories += calories

    return {
        "workout_id": workout_id,
        "total_calories": round(total_calories, 2),
        "exercise_summaries": exercise_summaries
    }
