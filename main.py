# main.py
from fastapi import FastAPI
from routers.progress import progress_router
from routes.exercises import exercises_router
from routes.workouts import workouts_router

app = FastAPI()

# Register all routers
app.include_router(progress_router)      # Handles /progress/today
app.include_router(exercises_router)     # Handles /exercises/search
app.include_router(workouts_router)      # Handles /workouts/{id}/summary and more
