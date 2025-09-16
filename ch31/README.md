# 📘 FastAPI Notes – Handling Errors with `HTTPException`

## 🔹 What I Learned Today
- In FastAPI, errors can be handled gracefully using **`HTTPException`**.
- Instead of crashing or showing unclear messages, we can raise structured error responses with:
  - **status codes**
  - **detail messages**
  - **custom headers**

---

## 🔹 Basic Example
```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {
    "apple": "a juicy fruit",
    "banana": "a yellow delight"
}

@app.get("/items/{item_id}")
async def read_items(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    return items[item_id]
```
* If the item exists → return its description
* If not → return a structured 404 error

## 🔹 Adding Custom Headers
We can attach extra information in headers when raising exceptions.

```python
@app.get("/items/{item_id}")
async def read_items(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"x-error-type": "itemmissing"}
        )
    return items[item_id]
```
* This adds custom metadata in the response, useful for debugging or API clients.

##🔹 Common Use Cases of HTTPException
* 404 Not Found → resource missing

* 400 Bad Request → invalid input

* 401 Unauthorized → user not logged in

* 403 Forbidden → no permission

* 500 Internal Server Error → unexpected issue

## 🔹 Why Use HTTPException?
* Returns proper HTTP responses instead of raw errors.

* Helps clients (frontend/mobile apps) understand what went wrong.

* Improves debugging and user experience.

