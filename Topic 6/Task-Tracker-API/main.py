#main.py
from fastapi import FastAPI, HTTPException
from models import users_db, tasks_db
from schemas import UserCreate,UserRead,TaskCreate,Task

app = FastAPI()

#Root Endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the world of Task Tracker API!"}

#User Endpoints
#Create User
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    new_user = UserRead (id=len(users_db)+1 , ** user.dict())
    users_db.append(new_user)
    return new_user

#GEt Users
@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

#TASK ENDPOINTS
#Create Task
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(id=len(tasks_db)+1, **task.dict())
    tasks_db.append(new_task)
    return new_task

#GET Task
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

#Update Task Status
@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status: str):
    allowed_statuses = {"pending", "in_progress", "completed"}
    if status not in allowed_statuses:
        raise HTTPException(status_code=400, detail=f"Status must be one of: {allowed_statuses}")
    
    for task in tasks_db:
        if task.id == task_id:
            task.status = status
            return task

    raise HTTPException(status_code=404, detail="Task not found")


#Get User Tasks
@app.get("/users/{user_id}/tasks", response_model=list[Task])
def get_user_tasks(user_id: int):
    return [task for task in tasks_db if task.user_id == user_id]

