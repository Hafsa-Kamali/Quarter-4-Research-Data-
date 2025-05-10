# 🚀 {{🚀 FastAPI Parameters Made Easy: A Beginner-Friendly Guide with Real-Life Examples}}

![Banner Image]({{https://gpttutorpro.com/wp-content/uploads/2024/02/a-professor-robot-is-teaching-a-tutorial-with-the-title-fastapi-basics-path-parameters-query-parameters-and-request-body-in-a-boardroom.jpeg}})

> 📖 {{Short Description}}

🔗 **Read the full blog post on [Medium]({{https://medium.com/@hafsakamali362/fastapi-parameters-made-easy-a-beginner-friendly-guide-with-real-life-examples-9016d782d523}})**  
📁 Built for developers, learners, and API architects looking to master FastAPI's request-handling mechanisms.

---

## 📚 Table of Contents

1. [Path Parameters](#-1-path-parameters)
2. [Query Parameters](#-2-query-parameters)
3. [Body Parameters](#-3-body-parameters)
4. [Header Parameters](#-4-header-parameters)
5. [Cookie Parameters](#-5-cookie-parameters)
6. [Form Parameters](#-6-form-parameters)
7. [File Uploads](#-7-file-uploads)

---

## 🔹 1. Path Parameters

**What it is**:  
Path parameters are required parts of the URL path.

**Use Case**:  
Used to identify specific resources like `/items/{item_id}`.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
````

## 🔹 2. Query Parameters
**What it is**:
Optional values appended to the URL with ?, great for filtering and pagination.

**Use Case**:
Filtering search results like /items/?q=sofa&limit=10.

````python
@app.get("/items/")
def search_items(q: str = None, limit: int = 10):
    return {"query": q, "limit": limit}

````
## 🔹 3. Body Parameters
**What it is**:
Data sent in the request body, often in JSON format.

Use Case:
Sending data for creating or updating a resource.

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return item
    
## 🔹 4. Header Parameters
**What it is**:
Passed in the HTTP headers, often used for tokens or content type info.

Use Case:
Authentication via headers.

from fastapi import Header

@app.get("/secure-data/")
def get_data(authorization: str = Header()):
    return {"Authorization": authorization}
## 🔹 5. Cookie Parameters
**What it is**:
Stored in the browser and sent with each request.

Use Case:
Session handling.

python
from fastapi import Cookie

@app.get("/me/")
def read_me(user_id: str = Cookie(None)):
    return {"user_id": user_id}
## 🔹 6. Form Parameters
**What it is**:
Used for traditional HTML form submissions.

Use Case:
Form submissions for login or feedback.

from fastapi import Form

@app.post("/login/")
def login(username: str = Form(), password: str = Form()):
    return {"username": username}

    
## 🔹 7. File Uploads
**What it is**:
Handles file uploads such as images or PDFs.

Use Case:
Uploading profile pictures or documents.

from fastapi import File, UploadFile

@app.post("/upload/")
def upload_file(file: UploadFile = File()):
    return {"filename": file.filename}
✨ Features
✅ Covers all parameter types supported by FastAPI.

🧠 Easy-to-understand examples for beginners and pros.

📘 Linked Medium blog for full walkthrough.

🧪 Includes testable endpoints.

## 📎 License
MIT © {{Hafsa Kamali}}
Fork this repo, star it, and feel free to contribute! 
