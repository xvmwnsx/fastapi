"""
Задача 1: Приветствие пользователя (Строковой параметр)
Описание:
Самый простой вариант параметра пути.

Создайте эндпоинт /hello/{name}.

Метод: GET.

Параметр name может быть любой строкой.

Функция должна возвращать JSON: {"message": "Hello, <name>!"}.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def test_greeting(name: str):
    return {"message": f"Hello, {name}!"}
