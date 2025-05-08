# 🚀 FastAPI Hello World Project

Welcome to my **first FastAPI project**, built with the goal of helping beginners get started with modern backend development using Python. This guide walks you through setting up a FastAPI app using `uv`, running your first API, and understanding the core structure.

📖 **Read the full blog post here:**  
[Getting Started with FastAPI (Hello World)](https://medium.com/@hafsakamali362/getting-started-with-fastapi-hello-world-fastapi-022155d95a26)

---

## 📂 Project Structure

fastdca-p1/
│
├── main.py # Main FastAPI app with API routes
├── README.md # Project documentation (you are here)
├── pyproject.toml # Project dependencies and settings
├── .venv/ # Virtual environment (auto-created by uv)
└── ...

yaml
Copy
Edit

---

## ✅ Features

- 📦 Lightweight & beginner-friendly setup
- 🧪 Ready for unit testing with `pytest` and `pytest-asyncio`
- 🛠️ Uses [`uv`](https://github.com/astral-sh/uv) for faster dependency management
- ⚡ FastAPI with `dev` mode auto-reloading
- 🌐 Interactive API docs out-of-the-box (`/docs`)

---

## 🛠️ Setup Instructions

### 1. Create Project Folder and Init

```bash
uv init fastdca-p1
cd fastdca-p1
2. Create and Activate Virtual Environment
On macOS/Linux:

bash
Copy
Edit
uv venv
source .venv/bin/activate
On Windows:

bash
Copy
Edit
uv venv
.venv\Scripts\activate
🔔 For Python 3.11+ with PEP 582 support, activation may not be required.

3. Install Dependencies
bash
Copy
Edit
uv add "fastapi[standard]"
uv add --dev pytest pytest-asyncio
4. Write Your First API (main.py)
python
Copy
Edit
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
5. Run Your Server
bash
Copy
Edit
fastapi dev main.py
Or alternatively:

bash
Copy
Edit
uv run uvicorn main:app --reload
🔎 Test Your API
http://localhost:8000 → Returns {"Hello": "World"}

http://localhost:8000/items/5?q=test → Returns item details

📘 Explore interactive API docs:
http://localhost:8000/docs

🧠 Key Concepts Covered
Root path and dynamic routing

Query parameters

Uvicorn development server

API structure and documentation

pyproject.toml config with uv

📌 To-Do / Next Steps
 Add more API routes (CRUD)

 Integrate database support (e.g., SQLite or PostgreSQL)

 Add automated tests with pytest

 Containerize with Docker

 Deploy to Render / Railway / Vercel

🙌 Credits
Special thanks to my mentors for their incredible guidance 🙏
Built with 💖 using FastAPI, uv, and Python 3.11+

📬 Connect With Me
📖 Read My Blog

💼 LinkedIn

🌐 Portfolio Website

💡 "Every great journey begins with a simple 'Hello World' — this is mine with FastAPI."

yaml
Copy
Edit

---

Would you like a logo banner or badge section for GitHub too?






You said:
generate it in a readme form


ChatGPT said:
Sure! Here's your complete README.md file content ready to copy and paste into your GitHub project:

markdown
Copy
Edit
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

```bash
uv init fastdca-p1
cd fastdca-p1
2. Create and Activate Virtual Environment
On macOS/Linux:

bash
Copy
Edit
uv venv
source .venv/bin/activate
On Windows:

bash
Copy
Edit
uv venv
.venv\Scripts\activate
⚠️ Note: Python 3.11+ with PEP 582 might not need activation.

3. Add Dependencies
bash
Copy
Edit
uv add "fastapi[standard]"
uv add --dev pytest pytest-asyncio
4. Create API Routes in main.py
python
Copy
Edit
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
5. Run the Server
bash
Copy
Edit
fastapi dev main.py
Or with Uvicorn:

bash
Copy
Edit
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
🔍 Test the API
Open in your browser:

http://localhost:8000 → returns {"Hello": "World"}

http://localhost:8000/items/5?q=test` → returns item details

http://localhost:8000/docs → interactive Swagger API docs

💡 Key Concepts Covered
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

🙏 Thanks & Credits
This was only possible with the help of my incredible mentors — thank you for guiding me!
Built with ❤️ using FastAPI, Python, and uv.

📬 Connect With Me
📝 Read My Blog

💼 LinkedIn

🌐 Portfolio coming soon...

“Every great journey begins with a simple Hello World. This is mine — in FastAPI.”
