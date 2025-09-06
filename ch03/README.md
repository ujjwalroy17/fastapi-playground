# 📘 FastAPI – Chapter 3: Project Structure & Vertical Folder Layout

## 1. Overview

In this chapter, we study the **vertical (modular) folder structure** of a FastAPI project. Proper folder structure helps in maintaining large applications, making the code **clean, scalable, and maintainable**.

---

## 2. Types of Folder Structures in FastAPI

### 2.1 Flat Structure

**Example:**

```
project/
├─ main.py
├─ models.py
├─ routes.py
├─ schemas.py
├─ services.py
├─ db.py

```

**Advantages:**
- Simple and easy to start for small projects.
- Minimal files and folders to manage.
- Quick for prototypes or learning purposes.

**Disadvantages:**
- Becomes **hard to maintain** as project grows.
- Difficult to separate responsibilities.
- Can lead to **messy code** with multiple endpoints and models in one file.

---

### 2.2 Vertical (Modular) Structure

**Example (like your `ch3` folder):**

```

ch3/
├─ app/
│ ├─ db/
│ │ ├─ init.py
│ │ └─ config.py
│ ├─ product/
│ │ ├─ init.py
│ │ ├─ models.py
│ │ ├─ routes.py
│ │ ├─ schemas.py
│ │ └─ services.py
│ ├─ user/
│ │ ├─ init.py
│ │ ├─ models.py
│ │ ├─ routes.py
│ │ ├─ schemas.py
│ │ └─ services.py
│ └─ main.py
├─ tests/
│ └─ user/
│ └─ init.py
├─ venv/
├─ README.md
└─ requirements.txt

```


**Advantages:**
- **Separation of Concerns:** Each module (product, user, etc.) has its own models, routes, schemas, and services.
- **Scalable:** Easier to add new features without cluttering code.
- **Maintainable:** Easier for multiple developers to work together.
- **Testable:** Each module can be tested independently.

**Disadvantages:**
- Slightly more complex for small projects.
- Requires understanding of Python packages and imports.

---

## 3. Explanation of Files in Vertical Structure

- **`main.py`** – Entry point of the FastAPI application. Registers routes and starts the app.
- **`models.py`** – Database models for the module.
- **`schemas.py`** – Pydantic models for request/response validation.
- **`routes.py`** – API endpoints for the module.
- **`services.py`** – Business logic and interactions with models.
- **`db/config.py`** – Database connection and configuration.
- **`tests/`** – Test cases for modules.
- **`venv/`** – Virtual environment containing installed packages.

---

## 4. Auto-Generated Documentation in FastAPI

FastAPI automatically generates **interactive API documentation** using the **OpenAPI standard**. This is very helpful during development and testing.

**Swagger UI:**  
- Access by default at: `http://127.0.0.1:8000/docs`
- Provides a **UI to test endpoints**, view request/response schemas, and see parameters.

**ReDoc:**  
- Access by default at: `http://127.0.0.1:8000/redoc`
- Clean, organized view of API documentation.
- Provides detailed explanations of endpoints and data models.

**Benefits of Auto Docs:**
- No manual documentation required.
- Helps frontend developers and testers understand API structure.
- Speeds up development and debugging.

---




