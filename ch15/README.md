# 📘 FastAPI – Multiple Body Parameters

## 🔹 Why Multiple Body Parameters?
In real-world APIs, you often need to send **more than one object** or **extra values** in a request body.  
FastAPI + Pydantic makes it easy to handle multiple body parameters with **models, optional fields, single values, and embedding**.

---

## 📌 Example 1: Multiple Models in Request Body
```
@app.post("/product")
async def create_product(product: Product, seller: Seller):
    return {"product": product, "seller": seller}
```
**Example**
```
{
  "product": {
    "name": "Laptop",
    "price": 55000,
    "stock": 10
  },
  "seller": {
    "username": "ujjwal17",
    "full_name": "Ujjwal Roy"
  }
}
```
✅ FastAPI automatically separates and validates Product and Seller.

## Example 2: Optional Body Parameter
```
@app.post("/product")
async def create_product(product: Product, seller: Seller | None = None):
    return {"product": product, "seller": seller}
```

#### Valid Request (without seller):
```
{
  "product": {
    "name": "Tablet",
    "price": 15000,
    "stock": 5
  }
}
```

👉 seller becomes null if not provided.

## Example 3: Singular Values in Body

You can also accept primitive values inside the body using Body().
```
from typing import Annotated

@app.post("/product")
async def create_product(
    product: Product,
    seller: Seller,
    sec_key: Annotated[str, Body()]
):
    return {"product": product, "seller": seller, "sec_key": sec_key}
```

Request Example:
```
{
  "product": {"name": "Phone", "price": 20000, "stock": 15},
  "seller": {"username": "shop123", "full_name": "Tech Store"},
  "sec_key": "secure123"
}
```

## 📌 Example 5: Embedding a Single Body Parameter (with Pydantic model)

By default, FastAPI **does not embed** a single body model.

### Without `embed=True`
```
@app.post("/product")
async def create_product(product: Product):
    return {"product": product}
```
**Request Example:**
```
{
  "name": "Laptop",
  "price": 55000,
  "stock": 10
}
```
### With embed=True
```
from typing import Annotated
from fastapi import Body

@app.post("/product")
async def create_product(product: Annotated[Product, Body(embed=True)]):
    return {"product": product}
```
**Request Example (with embed):**
```
{
  "product": {
    "name": "Laptop",
    "price": 55000,
    "stock": 10
  }
}
```
Here, the Product model is wrapped inside a product key.