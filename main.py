from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Список пользователей (вместо базы данных)
users = [
    User(id=1, username="UrbanUser", age=24),
    User(id=2, username="UrbanTest", age=22),
    User(id=3, username="Capybara", age=60),
]

# Главная страница, отображающая список пользователей
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# Страница пользователя по ID
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        return templates.TemplateResponse("404.html", {"request": request})
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

# Удаление пользователя
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    global users
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    users = [user for user in users if user.id != user_id]
    return {"message": "User deleted", "user_id": user_id}

# Обновление пользователя
@app.put("/user/{user_id}")
async def update_user(user_id: int, user: User):
    for index, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[index] = user
            return {"message": "User updated", "user": user}
    raise HTTPException(status_code=404, detail="User not found")

# Создание пользователя
@app.post("/user/")
async def create_user(user: User):
    users.append(user)
    return user

