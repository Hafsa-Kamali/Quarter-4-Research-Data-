# 📝 FastAPI Task Management Application

![Task Tracker Banner](https://storage.googleapis.com/profit-prod/wp-content/uploads/2022/07/d4eaf149-task-management.jpg)

A beginner-friendly Task Management API built using **FastAPI**, **Pydantic**, and **in-memory storage**. This guide walks you through creating and interacting with API endpoints for users and tasks — with clean validation and auto-generated documentation using Swagger UI.

📖 **Read the Full Blog on Medium**:  
👉 [Step-by-Step FastAPI Task Tracker Guide](https://medium.com/@hafsakamali362/fastapi-task-management-api-complete-guide-for-beginners-d48eb4c7c654)

---

## 📁 Project Structure

task-tracker/
├── env/ # Virtual environment
├── main.py # Main FastAPI app
├── models.py # In-memory database (lists)
└── schemas.py # Pydantic models and validators

yaml

---

## 🚀 Features

- ✅ Create and fetch users
- ✅ Create, fetch, and update tasks
- ✅ Filter tasks by user
- ✅ Status validation (`pending`, `in_progress`, `completed`)
- ✅ Auto-generated interactive docs at `/docs`

---

## 🛠️ Getting Started

### 1. 📦 Create a Virtual Environment

```bash
# Navigate to your preferred directory
cd path/to/your/projects

# Create the project folder
mkdir task-tracker && cd task-tracker

# Set up virtual environment
python -m venv env

# Activate it
# Windows:
env\Scripts\activate
# Linux/macOS:
source env/bin/activate
````

2. 🧩 Install Dependencies
```bash
pip install fastapi uvicorn pydantic
```

🧱 Code Explanation
📄 schemas.py
Defines the shape of user and task data using Pydantic:

UserCreate: Input model for creating users

UserRead: Output model with id

TaskBase: Common fields for a task

TaskCreate: Extends TaskBase with user_id

Task: Output model with id and user_id

Validation:

```python
@field_validator('due_date')
def validate_due_date(cls, value):
    if value < date.today():
        raise ValueError("Due date cannot be in the past")
    return value
```

📄 models.py
Simulates a database using Python lists:

```python
users_db: List[UserRead] = []
tasks_db: List[Task] = []
```

📄 main.py
Core FastAPI app:

POST /users/: Create a user

GET /users/{user_id}: Get user details

POST /tasks/: Create a task (validates user existence)

GET /tasks/{task_id}: Get task

PUT /tasks/{task_id}?status=...: Update task status

GET /users/{user_id}/tasks: List user’s tasks

Example:

```python
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    new_user = UserRead(id=user_id_counter, **user.dict())
    users_db.append(new_user)
    user_id_counter += 1
    return new_user
```

▶️ Run the App
bash
uvicorn main:app --reload
Access the Swagger UI:

🧪 http://127.0.0.1:8000/docs

🧪 API Testing
Action	Endpoint	Method
Create a user	/users/	POST
Get user by ID	/users/{user_id}	GET
Create a task	/tasks/	POST
Get task by ID	/tasks/{task_id}	GET
Update task status	/tasks/{task_id}?status=...	PUT
Get user's tasks	/users/{user_id}/tasks	GET

🧠 Key Concepts
FastAPI: High-performance web framework

Pydantic: Data validation using Python type hints

In-Memory Storage: Temporary lists simulating a DB

🛡️ Best Practices
✅ Validate all input
✅ Provide clear error messages
✅ Use proper status codes
✅ In production, use PostgreSQL, MongoDB, or SQLite
✅ Add authentication (OAuth2 or JWT)
✅ Handle exceptions globally

📚 Resources
🔗 FastAPI Docs

🔗 Pydantic Docs

🔗 Uvicorn Docs

📸 Screenshots
Swagger UI	Create Task

👩‍💻 Author
[Hafsa Kamali]
Check out the full blog 👉 [Step-by-Step FastAPI Task Tracker Guide](https://medium.com/@hafsakamali362/fastapi-task-management-api-complete-guide-for-beginners-d48eb4c7c654)
