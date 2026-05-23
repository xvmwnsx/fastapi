"""
Задача 3: Маршрут путешествия (Несколько параметров)
Описание:
URL может содержать несколько переменных.

Создайте эндпоинт /flights/{from_code}/{to_code}.

Принимает два параметра: код аэропорта вылета и прилета (строки).

Ответ: {"from": from_code, "to": to_code}.

Пример: /flights/SOO/JFK -> {"from": "SOO", "to": "JFK"}.

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/flights/{from_code}/{to_code}")
async def get_flights_code(from_code, to_code: str):
    return {"from": from_code, "to": to_code}