# 📘 FastAPI – Chapter 6: Query Parameters

## 1. What are Query Parameters?
- Query parameters are **extra values passed in the URL after a `?` symbol**.  
- They are used to **filter, search, or customize** results from an API.  
- Example:  
/products?search=shirt


Here, `search=shirt` is a query parameter.

👉 Unlike **path parameters** (which are part of the URL structure), query parameters are **optional and flexible**.

---

## 2. Declaring Query Parameters in FastAPI

### (a) Basic Query Parameter
```
@app.get("/products")
async def get_products(search: str | None = None):
  if search:
      return [p for p in PRODUCTS if search.lower() in p["title"].lower()]
  return PRODUCTS
```
* search is optional (None by default).

* If provided, it filters products by title.

### (b) Validation with Query
FastAPI provides the Query helper to add validation & constraints.

```
from fastapi import Query

@app.get("/products")
async def get_products(search: str | None = Query(default=None, max_length=8)):
    ...
```
* max_length=8 → the search term cannot exceed 8 characters.

### (c) Using Annotated for Cleaner Validation
```
from typing import Annotated

@app.get("/products")
async def get_products(
    search: Annotated[str | None, Query(max_length=5)] = None
):
    ...
```
* **Annotated** is the modern recommended way.

* Makes validation rules more readable and structured.

* **Why use Annotated?**
   * Without Annotated : The type hint (str | None) and validation (Query(max_length=5)) are inside the same parameter, making it a little messy.
   * This makes the function cleaner, especially when many parameters have validations.

## 3. Advanced Query Parameter Options
✅ Required Parameter
```
@app.get("/products")
async def get_products(search: Annotated[str, Query(min_length=3)]):
    ...
```
* search is now mandatory (no default value).

✅ Regex Validation
```
@app.get("/products")
async def get_products(
    search: Annotated[str | None, Query(min_length=3, pattern="^[a-z]+$")] = None
):
    ...
```
* Only lowercase letters allowed (pattern="^[a-z]+$").

✅ Multiple Values (List)
```
@app.get("/products")
async def get_products(search: Annotated[list[str] | None, Query()] = None):
    ...
```
* Supports queries like:

* `/products?search=shirt&search=jacket`

✅ Alias Parameters
```
@app.get("/products")
async def get_products(search: Annotated[str | None, Query(alias="q")] = None):
    ...
```
* Now `/products?q=shirt` works instead of `/products?search=shirt`.

✅ Adding Metadata
```
@app.get("/products")
async def get_products(
    search: Annotated[
        str | None,
        Query(alias="q", title="Search Products", description="Search by product title")
    ] = None
):
    ...
```
* Helpful in automatic API docs (/docs).
* Adding Metadata:
    You can attach extra information like title, description, or alias using Query inside Annotated.
    This doesn’t affect logic — it just makes your OpenAPI docs (Swagger UI) much more readable.



## 4. Custom Validation
You can add custom rules using AfterValidator.

```
from pydantic import AfterValidator

def check_valid_id(id: str):
    if not id.startswith("prod-"):
        raise ValueError("ID must start with 'prod-'")
    return id

@app.get("/products")
async def get_products(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    if id:
        return {"id": id, "message": "Valid product ID"}
    return {"message": "No ID provided"}
```
## 7. Why Query Parameters?
* ✅ Make your API flexible (search, filter, sort).
* ✅ Can be optional or required.
* ✅ Work well with automatic validation and docs.

