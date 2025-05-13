#schemas.py
from pydantic import BaseModel, EmailStr,constr, field_validator
from datetime import date
from typing import Optional,Annotated

class UserCreate(BaseModel):
    Username : Annotated[str, constr(min_length=3, max_length=20)]
    Email : EmailStr

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    status: str ="pending"

@field_validator('due_date')
@classmethod
def validate_due_date(cls, value):
    if value < date.today():
        raise ValueError("Due date cannot be in the past")
    return value

@field_validator('status')
@classmethod
def validate_status(cls, value):
    allowed_statuses={"pending", "in_progress", "completed"}	
    if value not in allowed_statuses:
        raise ValueError(f"Status must be one of {allowed_statuses}")
    return value

class TaskCreate(TaskBase):
    user_id:int

class Task(TaskBase):
    id: int
    user_id:int

