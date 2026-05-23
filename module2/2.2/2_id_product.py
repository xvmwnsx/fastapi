"""
Задача 2: Идентификатор товара (Валидация Int) 
Описание:
В URL часто передают ID, которые должны быть числами.

Создайте эндпоинт /product/{product_id}.

Метод: GET.

Параметр product_id должен быть целым числом (int).

Ответ: {"product_id": product_id}.

Если передать буквы, FastAPI должен вернуть ошибку 422.

"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/product/{product_id}')
async def get_product_id(product_id: int):
    return {"product_id": product_id}