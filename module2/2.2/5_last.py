"""
Задача 5: Логика на основе параметра
Описание:
Параметры пути нужны, чтобы искать данные.

У вас есть словарь users_db (в коде уже задан).

Создайте эндпоинт /users/{user_id}.

Параметр user_id — целое число.

Если пользователь с таким ID есть в словаре, верните {"name": имя_пользователя}.

Если пользователя нет, верните {"error": "User not found"} (пока без использования HTTPException, просто словарем).
"""

from fastapi import FastAPI

app = FastAPI()

users_db = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for key, name in users_db.items():
        if key == user_id:
            return {"name": name}
    else:
        return {"error": "User not found"}