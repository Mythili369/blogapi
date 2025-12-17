# Blog API with FastAPI and SQLAlchemy

A simple RESTful API for managing **authors** and their **posts**.  
This project demonstrates **one-to-many relationships**, **foreign key constraints**, **nested endpoints**, and **cascade delete** using FastAPI and SQLAlchemy.

---

## **Features**

- Create, read, update, and delete authors.
- Create, read, update, and delete posts.
- Fetch all posts by a specific author (`/authors/{id}/posts`).
- One-to-many relationship between authors and posts.
- Foreign key constraints with cascade delete.
- Nested response: Post API includes author details.
- Proper error handling for invalid or non-existent resources.
- Efficient database queries to prevent N+1 problem.

---

## **Technology Stack**

- **Python 3.10+**
- **FastAPI** (Web Framework)
- **SQLAlchemy** (ORM)
- **SQLite** (Database)
- **Pydantic** (Request validation & response models)
- **Uvicorn** (ASGI server)

---

## **Project Structure**

```

blogapi/
│
├── app/
│   ├── **init**.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── **init**.py
│       ├── author.py
│       └── posts.py
├── blog.db
├── requirements.txt
└── README.md

````

---

## **Setup Instructions**

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd blogapi
````

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
python -m pip install --upgrade pip
python -m pip install fastapi uvicorn sqlalchemy pydantic[email]
```

* Optional: Save installed packages to `requirements.txt`:

```bash
pip freeze > requirements.txt
```

* Then others can install dependencies with:

```bash
pip install -r requirements.txt
```

5. **Run the server**

```bash
python -m uvicorn app.main:app --reload
```

6. **Open API documentation**

Go to:

```
http://127.0.0.1:8000/docs
```

7. **Optional:** Add a root endpoint to `/` in `main.py`:

```python
@app.get("/")
def read_root():
    return {"message": "Blog API is running!"}
```

---

## **Database Schema**

### **Authors Table**

| Column | Type   | Constraints      |
| ------ | ------ | ---------------- |
| id     | int    | Primary Key      |
| name   | string | Not null         |
| email  | string | Unique, Not null |

### **Posts Table**

| Column    | Type   | Constraints              |
| --------- | ------ | ------------------------ |
| id        | int    | Primary Key              |
| title     | string | Not null                 |
| content   | text   | Not null                 |
| author_id | int    | Foreign Key → authors.id |

* **Relationship:** One Author → Many Posts
* **Cascade delete:** Deleting an author deletes all associated posts automatically.

#### ER Diagram (text representation)

```
Authors
-------
id (PK)
name
email

Posts
-----
id (PK)
title
content
author_id (FK → Authors.id, on delete CASCADE)
```

---

## **API Endpoints**

### **Authors Endpoints**

| Method | Endpoint            | Description                        |
| ------ | ------------------- | ---------------------------------- |
| POST   | /authors            | Create a new author                |
| GET    | /authors            | Retrieve all authors               |
| GET    | /authors/{id}       | Retrieve author by ID              |
| PUT    | /authors/{id}       | Update author                      |
| DELETE | /authors/{id}       | Delete author (cascade delete)     |
| GET    | /authors/{id}/posts | Get all posts of a specific author |

### **Posts Endpoints**

| Method | Endpoint    | Description                                 |
| ------ | ----------- | ------------------------------------------- |
| POST   | /posts      | Create a new post                           |
| GET    | /posts      | Retrieve all posts                          |
| GET    | /posts/{id} | Retrieve a post by ID (with author details) |
| PUT    | /posts/{id} | Update a post                               |
| DELETE | /posts/{id} | Delete a post                               |

---

## **Example Requests & Responses**

### **Create Author**

```
POST /authors
Body:
{
  "name": "Alice",
  "email": "alice@example.com"
}

Response:
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}
```

### **Create Post**

```
POST /posts
Body:
{
  "title": "Hello World",
  "content": "This is my first post",
  "author_id": 1
}

Response:
{
  "id": 1,
  "title": "Hello World",
  "content": "This is my first post",
  "author": {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
}
```

### **Get All Posts by Author**

```
GET /authors/1/posts

Response:
[
  {
    "id": 1,
    "title": "Hello World",
    "content": "This is my first post",
    "author": {
      "id": 1,
      "name": "Alice",
      "email": "alice@example.com"
    }
  }
]
```

### **Cascade Delete Author**

```
DELETE /authors/1

Response:
{
  "message": "Author deleted"
}

GET /posts → []
```

---

## **Notes**

* Run the server from the **project root folder**.
* Use **Swagger UI** (`/docs`) to test endpoints interactively.
* Pydantic v2 uses `from_attributes=True` instead of `orm_mode`. Existing code still works.

---

## **License**

MIT License

```

---

This version is **ready for GitHub submission**.  

It fixes:  

- `__init__.py` formatting ✅  
- Instructions for `requirements.txt` ✅  
- Suggests a `/` root endpoint for convenience ✅  

---

