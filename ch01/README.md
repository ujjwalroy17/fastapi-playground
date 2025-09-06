# 📘 FastAPI – Chapter 1: Introduction & Setup

## 1. What is FastAPI?

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use, highly efficient, and robust.

### Key Features
- **High Performance:** Go thanks to asynchronous support using **ASGI**.
- **Fast to Code:** Reduces developer errors and speeds up development.
- **Automatic Interactive Docs:** Provides **Swagger UI** and **ReDoc** documentation automatically.
- **Type Safety:** Uses Python type hints for data validation and editor support.
- **Dependency Injection:** Simplifies modular code design and request handling.

### How It Works
- Built on **Starlette** (web framework) and **Pydantic** (data validation).
- ASGI (Asynchronous Server Gateway Interface) allows handling multiple requests concurrently.
- Supports both **synchronous** and **asynchronous** route handlers.

---

## 2. Setting Up FastAPI

### Step 1: Create a Virtual Environment
It is recommended to create a virtual environment to isolate project dependencies.

```bash
# Navigate to your project folder
cd path\to\your\project

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment

# Windows CMD
venv\Scripts\activate.bat

```

### Step 2: Install FastAPI with standard dependencies
```
pip install "fastapi[standard]" 
```
