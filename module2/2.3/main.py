from fastapi import FastAPI

app = FastAPI()

fake_tasks_db = [
    {"task_name": "Task 1"},
    {"task_name": "Task 2"},
    {"task_name": "Task 3"},
    {"task_name": "Task 4"},
    {"task_name": "Task 5"},
    {"task_name": "Task 6"},
    {"task_name": "Task 7"},
    {"task_name": "Task 8"},
    {"task_name": "Task 9"},
    {"task_name": "Task 10"},
]

@app.get("/tasks")
async def get_tasks(limit: int = 10, offset: int = 0):
    return fake_tasks_db[offset : offset + limit]