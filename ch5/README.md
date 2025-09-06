# 📘 FastAPI – Path Parameters with Types

## 1. Overview

In FastAPI, **path parameters** allow your API to accept dynamic values directly from the URL. You can optionally declare a **type** for the parameter, which helps FastAPI **validate** incoming requests automatically.

This guide covers:
- Using path parameters without types.
- Using path parameters with types.
- What happens when a type is specified.

---

## 2. FastAPI Setup

```
from fastapi import FastAPI

app = FastAPI()
```
---
## 3. Path Parameters Without Type
When you do not specify a type, FastAPI treats the parameter as a string by default.


```
@app.get("/product/{product_id}")
async def single_product(product_id):
    return {"response": "Single Data Fetched", "product_id": product_id}

```
* Here, product_id can be any value (string, number, or mixed).

* FastAPI always converts the path parameter to string if no type is given.

* No automatic validation is applied.

* If a client sends /product/abc123, it works without errors.

  - Pros: Flexible, accepts any value.
  - Cons: No type validation; can lead to unexpected behavior if numeric values are expected.
---

## 4. Path Parameters With Type
You can specify a type for the parameter, e.g., int, float, or str. FastAPI will validate the input and return an error if the type doesn’t match.


```
@app.get("/product/{product_id}")
async def single_product(product_id: int):
    return {"response": "Single Data Fetched", "product_id": product_id}

```
* Here, product_id must be an integer.

* FastAPI tries to coerce compatible types, but raises an error if it fails.

* **Cases:**
  * **Client sends an integer:**

    - ```
        GET /product/5
    - ✅ Works. product_id becomes 5 (int).

   *  **Client sends a string that cannot convert to int:**


        - ```
            GET /product/abc
            ```
        - ❌ Fails. FastAPI responds with 422 Unprocessable Entity — it does not convert "abc" to int.

   *  **Client sends a numeric string that can convert:**


        - ```
          GET /product/10
          ```
        - ✅ Works. FastAPI converts "10" (string from URL) into 10 (int).

**So FastAPI only converts if possible, otherwise it throws an error.**

---

## 5. Common Types for Path Parameters
| Type | Behavior |
| ----- | ----- |
| `str` | Default type. Accepts any string. FastAPI always converts to string if the type is not given. |
| `int` | Accepts only integers. Non-integer values cause validation errors. |
| `float` | Accepts decimal numbers. Invalid floats return validation errors. |
| `bool` | Accepts `true` or `false` (case-insensitive). |

---
## 6. Key Takeaways
Without type: Parameter is treated as string, flexible but no validation.

With type: FastAPI validates the type, improving API reliability and preventing errors.

Always declare types for numeric or boolean parameters to ensure correct data handling.