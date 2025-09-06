# 📘 FastAPI – Chapter 4: Path Parameters and HTTP Methods

## 1. Overview
In this chapter, we explore how to handle **path parameters** in FastAPI and implement CRUD operations using various **HTTP methods**. FastAPI provides an easy way to manage resources via RESTful APIs.

We cover:
- Path parameters for dynamic URLs.
- HTTP methods: GET, POST, PUT, PATCH, DELETE.
- Sending and receiving JSON data.

---

## 2. FastAPI Setup

```
from fastapi import FastAPI

app = FastAPI()
```
## 3. Path Parameters
### Definition:
A path parameter is a variable part of a URL that allows your API to accept dynamic values. These are defined in the URL path using curly braces {}.

#### Example:

```
@app.get("/product/{product_id}")
async def get_product(product_id: int):
    return {"product_id": product_id}
```
Here, {product_id} is a path parameter.

The API can fetch different products by passing different product_id values in the URL.

FastAPI automatically validates the type if you declare it (e.g., int).

---

## 4. HTTP Methods and Usage
### 1️⃣ GET Requests
Used to fetch/read data from the server.


#### Fetch all products

```
@app.get("/product")
async def all_products():
    return {"response": "All Products"}
```

#### Fetch a single product by ID (path parameter)

```
@app.get("/product/{product_id}")
async def single_products(product_id: int):
    return {"response": "Single Data Fetched", "product_id": product_id}
```
### 2️⃣ POST Request
Used to create/insert new data.

```
@app.post("/product")
async def create_product(new_product: dict):
    return {"response": "Product Created", "new_product": new_product}
```
### 3️⃣ PUT Request
Used to update the complete data of a resource.

```
@app.put("/product/{product_id}")
async def update_product(new_updated_product: dict, product_id: int):
    return {
        "response": "Complete Data Updated",
        "product_id": product_id,
        "new_updated_product": new_updated_product
    }
```
### 4️⃣ PATCH Request
Used to update partial data of a resource.

```
@app.patch("/product/{product_id}")
async def partial_product(new_updated_product: dict, product_id: int):
    return {
        "response": "Partial Data Updated",
        "product_id": product_id,
        "new_updated_product": new_updated_product
    }
```
### 5️⃣ DELETE Request
Used to delete a resource.

```
@app.delete("/product/{product_id}")
async def delete_product(product_id: int):
    return {"response": "Data Deleted", "product_id": product_id}
```


### 5. Auto-generated Docs
FastAPI provides interactive API documentation at:

```
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc
```
These docs allow you to test all endpoints directly from the browser.


