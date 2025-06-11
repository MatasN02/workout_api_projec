# routes/exercises.py
from fastapi import APIRouter, Query
import httpx
import os
import json

exercises_router = APIRouter(prefix="/exercises", tags=["Exercises"])

@exercises_router.get("/search")
async def search_exercises(muscleGroup: str = Query(..., description="Comma-separated muscle groups")):
    muscle_groups = [m.strip() for m in muscleGroup.split(",")]

    exercises = []
    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),  # ❗ use an environment variable key name, not the actual key
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    async with httpx.AsyncClient() as client:
        for target in muscle_groups:
            response = await client.get(
                f"https://exercisedb.p.rapidapi.com/exercises/target/{target}",
                headers=headers
            )
            response.raise_for_status()
            data = response.json()
            exercises.extend(data)

    unique_exercises = {ex["id"]: ex for ex in exercises}.values()
    result = list(unique_exercises)

    with open("search_results.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    return result
