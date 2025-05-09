# 🚀 FastAPI + Pydantic Chatbot API

![Pydantic Logo](https://miro.medium.com/v2/resize:fit:1024/1*HVgtWxguKGQbvXhPSCfDLw.png)

Welcome to a simple and powerful **FastAPI + Pydantic chatbot API** built with clean structure and full validation support. This project is perfect for beginners who want to learn:

- ✅ Data validation using Pydantic
- ✅ Nested models
- ✅ Custom validators
- ✅ FastAPI routing and response handling

---

## 📖 Medium Blog

Check out the full step-by-step tutorial with easy explanations in English + Roman Urdu:

👉 [Read the Blog on Medium](https://medium.com/ai-agent-insider/pydantic-ai-agent-framework-02b138e8db71)

---

## 📁 Project Structure
fastdca_p1/
├── main.py # FastAPI app entry point
├── models.py # Pydantic models (User, Message, Response)
├── requirements.txt # Dependencies
├── assets/
│ └── pydantic-logo.png # Pydantic image used in README
└── README.md # This file


---

## 🧪 Features

- 🔹 **Pydantic Models**: Validates `User`, `Message`, `Response`
- 🔹 **Nested Metadata**: Auto timestamps and session IDs
- 🔹 **Custom Validators**: Ensure name is at least 2 characters
- 🔹 **API Endpoints**:
  - `/` – Welcome route
  - `/users/{user_id}` – Get user info with optional role
  - `/chat/` – Accepts message and returns a response

---

## ⚙️ How to Run

```bash
# Setup project
uv init fastdca_p1
cd fastdca_p1

# Create virtual environment
uv venv
source .venv/bin/activate

# Add FastAPI
uv add "fastapi[standard]"

# Run server
fastapi dev main.py
````

Then open in browser:
http://localhost:8000

🧠 Concepts Covered
Concept       	Description
BaseModel	    Validates data structure
Field	Sets    defaults like timestamps, UUIDs
validator	    Custom logic for fields
EmailStr	    Email validation
list[Model]	   Handles arrays of nested models
Optional	    Supports nullable/optional values


📄 License
MIT License

💡 Author
Made with ❤️ by Hafsa kamali | Fullstack developer
Feel free to connect or contribute!



