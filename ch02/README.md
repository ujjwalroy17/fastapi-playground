
# 📘 FastAPI – Chapter 2: First API

## 1. Overview

In this chapter, we will create our **first API** using FastAPI. An API (Application Programming Interface) allows clients to communicate with your application through endpoints (URLs). FastAPI makes this process simple, fast, and intuitive.

---

## 2. Writing Your First API

### Step 1: Create `main.py`
Create a new file named `main.py` in your project folder and add the following code:

```python
from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Define a GET endpoint at '/api'
@app.get("/api")
def home():
    return {"message": "Hello FastAPI"}
```
### Explanation:

FastAPI(): Creates a new FastAPI application instance.

@app.get("/api"): Defines a GET endpoint at the path /api.

home(): Function that runs when /api is accessed. Returns a JSON response.

---
## 3. Running Your FastAPI App (Development Mode)

#### Step 1: Open Terminal & Navigate
Go to your project folder:

```
cd path\to\your\project
```
#### Step 2: Activate Virtual Environment

```
venv\Scripts\activate.bat
```
After activation, your terminal prompt will show (venv).

#### Step 3: Run with fastapi
```
fastapi dev main.py
```


#### Step 4: Test Your API

Open your browser or Postman and visit:
```
http://127.0.0.1:8000/api
```

Expected JSON response:
```
json
Copy code
{
  "message": "Hello FastAPI"
}
```
For interactive API documentation:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

