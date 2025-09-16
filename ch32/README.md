# 📘 FastAPI Notes – Custom Exceptions

## 🔹 What I Learned Today
- In FastAPI, apart from `HTTPException`, we can also create **Custom Exceptions**.
- Custom exceptions allow us to handle **application-specific errors** in a clean and reusable way.
- We can also define **custom exception handlers** to decide how errors are returned (JSON, HTML, etc.).

---

## 🔹 Example Code
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

Fruits = {
    "apple": "a juicy fruit",
    "banana": "a yellow delight"
}

# Step 1: Create a Custom Exception
class FruitException(Exception):
    def __init__(self, fruit_name: str):
        self.fruit_name = fruit_name

# Step 2: Create a Custom Exception Handler
@app.exception_handler(FruitException)
async def fruit_exception_handler(request: Request, exc: FruitException):
    return JSONResponse(
        status_code=418,  # HTTP "I'm a teapot" for fun
        content={"message": f"{exc.fruit_name} is not valid"}
    )

# Step 3: Use the Exception in an Endpoint
@app.get("/Fruits/{fruit_name}")
async def read_fruit(fruit_name: str):
    if fruit_name not in Fruits:
        raise FruitException(fruit_name=fruit_name)
    return Fruits[fruit_name]
```
## 🔹 How It Works
1.Custom Exception Class → Define your own error type (e.., FruitException).

2.Exception Handler → Decide what happens when the custom exception is raised.
  * Return custom JSON, HTML, or any response.

 * Choose your own status_code.

3.Raising the Exception → Inside endpoints, raise your custom exception when a condition is not met.

## 🔹 Example Usage
* Request: GET /Fruits/apple

  Response:

```json
"a juicy fruit"
```
* Request: GET /Fruits/mango

  Response (custom error):

```json
{
  "message": "mango is not valid"
}
```
## 🔹 Comparison: HTTPException vs Custom Exception

| Feature        | HTTPException                                  | Custom Exception (`FruitException`)          |
|----------------|-----------------------------------------------|----------------------------------------------|
| **Purpose**    | For standard HTTP-related errors (404, 400, etc.) | For app-specific or domain-specific errors   |
| **Built-in support** | Yes, provided by FastAPI                 | No, you create your own class                 |
| **Flexibility**| Limited to `status_code`, `detail`, and `headers` | Full control over response structure         |
| **Use Case**   | Resource not found, unauthorized, bad request  | Invalid business logic (e.g., invalid fruit) |
| **Error Format** | JSON with `status_code`, `detail`, `headers` | Fully customizable (JSON, HTML, etc.)        |


##🔹 Why Use Custom Exceptions?
* Makes your API errors clearer and more readable.

* Keeps your code organized by separating normal logic and error handling.

* Helps in large projects where multiple types of errors need different responses.