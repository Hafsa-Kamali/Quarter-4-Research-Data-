
# 🚀 FastAPI Hello World Project

Welcome to my **first FastAPI project**, designed for beginners who want to get started with modern backend development in Python using FastAPI and `uv`.

📖 **Read the full blog post:**  
[Getting Started with FastAPI (Hello World)](https://medium.com/@hafsakamali362/getting-started-with-fastapi-hello-world-fastapi-022155d95a26)

---

## 📂 Project Structure

fastdca-p1/
│
├── main.py # Main FastAPI app with API routes
├── README.md # Project documentation (this file)
├── pyproject.toml # Project dependencies and configuration
├── .venv/ # Virtual environment (created via uv)
└── ...

yaml
Copy
Edit

---

## ✅ Features

- 🚀 FastAPI setup with modern tooling (`uv`)
- 👶 Beginner-friendly code and explanation
- 🔁 Auto-reload dev mode using `fastapi dev`
- 📦 Dependency management via `uv` and `pyproject.toml`
- 🧪 Unit testing ready with `pytest` and `pytest-asyncio`
- 🧭 Interactive API docs at `/docs`

---

## 🛠️ How to Set Up

### 1. Initialize the Project

bash
uv init fastdca-p1
cd fastdca-p1

### 2. Create and Activate Virtual Environment
###On macOS/Linux:

bash
uv venv
source .venv/bin/activate

###On Windows:
bash
uv venv
.venv\Scripts\activate

⚠️ Note: Python 3.11+ with PEP 582 might not need activation.

###3. Add Dependencies
bash
uv add "fastapi[standard]"
uv add --dev pytest pytest-asyncio


###4. Create API Routes in main.py
python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
###5. Run the Server
bash
fastapi dev main.py
Or with Uvicorn:

bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
###🔍 Test the API

###Open in your browser:

http://localhost:8000 → returns {"Hello": "World"}

http://localhost:8000/items/5?q=test` → returns item details

http://localhost:8000/docs → interactive Swagger API docs

###💡 Key Concepts Covered
FastAPI basics (routing, query/path params)

Setting up with uv

Running in dev mode with reload

Auto-generated API docs

Dependency management using pyproject.toml

📌 To-Do Next
 Add POST, PUT, DELETE methods

 Integrate a database (like SQLite or PostgreSQL)

 Add form input and validation

 Create Docker support

 Deploy on Railway, Render, or Vercel

###🙏 Thanks & Credits
This was only possible with the help of my incredible mentors — thank you for guiding me!
Built with ❤️ using FastAPI, Python, and uv.

📬 Connect With Me
📝 Read My Blog

💼 LinkedIn

🌐 Portfolio coming soon...

“Every great journey begins with a simple Hello World. This is mine — in FastAPI.”

