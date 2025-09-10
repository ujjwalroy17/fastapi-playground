# 📘 FastAPI – Header Parameters

## 🔹 What are Headers?
- Headers are **extra information** sent by the client along with the request.  
- Example headers:
  - `User-Agent`: tells the server what browser or client is making the request.
  - `Authorization`: sends tokens for authentication.
  - `Content-Type`: type of data being sent (e.g., JSON).

👉 Think of headers as **metadata** about the request.

---

## 🔹 Using Header Parameters in FastAPI
FastAPI makes it easy to extract header values using the `Header` class.

### Example:
```python
from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()

@app.get("/products")
async def get_products(user_agent: Annotated[str | None, Header()] = None):
    return user_agent
```
* **Header() tells FastAPI to look inside the headers.**

* Here, it extracts the value of User-Agent.

* If the client doesn’t send it → it returns None.

#### Test with curl:
```bash
curl -H "User-Agent: Mozilla/5.0" http://127.0.0.1:8000/products
```
Response:
```json
"Mozilla/5.0"
```
## 🔹 Handling Duplicate Headers
Some headers can appear multiple times in a request.
In that case, FastAPI can collect them into a list.

Example:
```python
Copy code
@app.get("/products")
async def get_product(
    x_product_token: Annotated[list[str] | None, Header()] = None
):
    return {"x_product_token": x_product_token or []}
```
Test with curl:
```bash
curl -H "X-Product-Token: token1" -H "X-Product-Token: token2" http://127.0.0.1:8000/products
```
Response:
```json
{
  "x_product_token": ["token1", "token2"]
}
```
## 🔹 Key Notes
* Headers are case-insensitive

  * User-Agent, user-agent, or USER-AGENT are the same.


* Use cases of headers

    * Authentication (Authorization: Bearer <token>)

    * Content type (Content-Type: application/json)

    * Language preference (Accept-Language: en-US)

    * Custom tracking headers (X-Request-ID: 12345)