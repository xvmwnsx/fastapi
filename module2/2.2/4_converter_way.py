"""
Задача 4: Конвертер пути (Путь к файлу)
Описание:
Обычно FastAPI считает, что слэш / — это разделитель параметров. Но что, если нам нужно передать путь к файлу, например images/logo.png?
Для этого используется конвертер :path.

Создайте эндпоинт /files/{file_path:path}.

Функция должна возвращать: {"file": file_path}.

Обратите внимание на синтаксис в декораторе: {имя_переменной:path}.

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def file_path(file_path):
    return {"file": file_path}