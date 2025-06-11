
# Workout API with ExerciseDB integration

## Setup

1️⃣ Clone repo or unzip files  
2️⃣ Install dependencies:

```bash
pip install fastapi uvicorn httpx python-dotenv
```

3️⃣ Create `.env` file:

```bash
cp .env.example .env
```

Insert your RapidAPI Key.

4️⃣ Run the app:

```bash
uvicorn main:app --reload
```

5️⃣ Test the endpoints:

- **Exercises search:**  
  `GET /exercises/search?muscleGroup=chest,shoulders,triceps`

- **Workout summary:**  
  `GET /workouts/{id}/summary`

## Notes

- `/exercises/search` calls RapidAPI ExerciseDB API
- `/workouts/{id}/summary` calculates calories (example logic)

Enjoy! 🚀
