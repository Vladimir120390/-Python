from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
from typing import Dict

app = FastAPI()

# Словарь для хранения пользователей
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}


# Модель для валидации данных пользователя
class User(BaseModel):
    username: constr(min_length=1)
    age: int


@app.get("/users")
async def get_users() -> Dict[str, str]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int) -> str:
    if age < 0:
        raise HTTPException(status_code=400, detail="Возраст не может быть отрицательным")

    # Находим максимальный ключ
    new_id = str(max(map(int, users.keys()), default=0) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if age < 0:
        raise HTTPException(status_code=400, detail="Возраст не может быть отрицательным")

    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    del users[user_id]
    return f"User {user_id} has been deleted"

