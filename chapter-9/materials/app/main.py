from fastapi import Depends, Header, HTTPException, status, Query
from fastapi import FastAPI
from typing import Any, List
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class User(BaseModel):
    user_id: int
    first_name: str
    second_name: str
    phone: str
    password: str


class Task(BaseModel):
    task_id: int
    user_id: int
    text: str
    status: str

tasks_db = {}
users_db = {}

@app.get("/task/get")
def get_task(user_id: int) -> List[Task]:
    if user_id in tasks_db:
        return tasks_db[user_id]
    return []

@app.post("/task/add", tags=["Task"])
def add_task(task: Task):
    if task.user_id in users_db:
        if task.user_id not in tasks_db:
            tasks_db[task.user_id] = [task]
        else:
            tasks_db[task.user_id].append(task)
            
        return "{'message': 'Task added'}"

    return "{'message': 'User not found'}"

@app.post("/user/add", tags=["User"])
def add_user(user: User):
    if user.user_id not in users_db:
        users_db[user.user_id] = user

if __name__ == "__main__":
    uvicorn.run(app, port=5173)
