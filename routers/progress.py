# routers/progress.py
from fastapi import APIRouter

progress_router = APIRouter(prefix="/progress", tags=["Progress"])

@progress_router.get("/today")
def get_today_progress():
    return {"calories": 123}
