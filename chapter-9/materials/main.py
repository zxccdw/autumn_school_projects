from fastapi import Depends, Header, HTTPException, status, Query
from fastapi import FastAPI
from typing import Any
from pydantic import BaseModel
from fastapi.testclient import TestClient # pip install httpx
from curlify2 import Curlify # pip install curlify2
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

DB = {}
dbUsers = {}

@app.get("/get_task")
def get_task(user_id: int):
    if user_id in DB:
        return f"{DB[user_id]}"
    return []

@app.post("/add_task")
def add_task(task: Task):
    if task.user_id in dbUsers:
        DB[task.user_id] = task

@app.post("/user/add", tags=["User"])
def add_user(user: User):
    if user.user_id not in dbUsers:
        dbUsers[user.user_id] = user


client = TestClient(app)

task = Task(task_id=1, user_id=1, text="SomeText", status="Wait")

if __name__ == "__main__":
    uvicorn.run(app, port=80)
