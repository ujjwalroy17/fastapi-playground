# 📘 FastAPI – Validating Request Body with Pydantic Models

## 🔹 Why Validation?
When building APIs, client data may be:
- Incomplete ❌  
- Wrong type ❌  
- Extra or unexpected fields ❌  

**Example of invalid data:**
```json
{
  "id": "abc",   
  "name": 123,   
  "price": "free"
}
```
Without validation, your backend may crash.
FastAPI + Pydantic provides automatic validation for request bodies.

## 📝 Approach 1: Without Pydantic

```python
@app.post("/products")
async def create_product(new_product: str):
    return new_product
```
**Problems:**

*  No type validation

*  Cannot enforce structure
*  Input is just a string

## 📝 Approach 2: With Pydantic

### Define a Pydantic model:

```python
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None  # optional field
```
**Benefits:**
* Automatic data validation

* Invalid input returns 422 Unprocessable Entity

* Model schema visible in API docs

## 📌 Example 1: Basic Validation

```python
@app.post("/products")
async def create_product(new_product: Product):
    return new_product
```
**Valid Request Body**
```
{
  "id": 1,
  "name": "Laptop",
  "price": 55000.0,
  "stock": 10
}
```
**Invalid Request Body**
```
{
  "id": "abc",
  "name": "Laptop",
  "price": "expensive"
}
```
**Response Example (422 Unprocessable Entity)**
```
{
  "detail": [
    {
      "loc": ["body", "id"],
      "msg": "Input should be a valid integer",
      "type": "int_parsing"
    },
    {
      "loc": ["body", "price"],
      "msg": "Input should be a valid number",
      "type": "float_parsing"
    }
  ]
}
```
## Example 2: Business Logic (Price with Tax)
```
@app.post("/products")
async def create_product(new_product: Product):
    product_dict = new_product.model_dump()
    price_with_tax = new_product.price + (new_product.price * 18 / 100)
    product_dict.update({"price_with_tax": price_with_tax})
    return product_dict
```
Response Example:
```
{
  "id": 1,
  "name": "Laptop",
  "price": 55000.0,
  "stock": 10,
  "price_with_tax": 64900.0
}
```
## 📌 Example 3: Path Parameter + Body

You can use **path parameters** + **request body** together.

```python
@app.put("/products/{product_id}")
async def update_product(product_id: int, new_updated_product: Product):
    return {
        "product_id": product_id,
        "new_updated_product": new_updated_product
    }
```
#### PUT Request
```
/products/101
```

#### Request Body
```
{
  "id": 101,
  "name": "Tablet",
  "price": 15000.0,
  "stock": 5
}
```
### You can even add query parameters with request body.
```
@app.put("/products/{product_id}")
async def update_product(
    product_id: int,
    new_updated_product: Product,
    discount: float | None = None
):
    return {
        "product_id": product_id,
        "new_updated_product": new_updated_product,
        "discount": discount
    }
```

#### Request Example
```
PUT /products/101?discount=10
```
#### Request Body
```
{
  "id": 101,
  "name": "Tablet",
  "price": 15000.0,
  "stock": 5
}
```
#### Response Example
```
{
  "product_id": 101,
  "new_updated_product": {
    "id": 101,
    "name": "Tablet",
    "price": 15000.0,
    "stock": 5
  },
  "discount": 10
}
```

##  Auto Docs in Action

FastAPI auto-generates interactive documentation:

Swagger UI 👉 http://127.0.0.1:8000/docs

ReDoc 👉 http://127.0.0.1:8000/redoc

Both will show your Product model schema automatically.

## Key Concepts Learned

✅ Pydantic Models enforce data validation

✅ Fields are automatically type-checked

✅ Optional fields use | None or Optional[type]

✅ .model_dump() converts a model into a dictionary

✅ Path + Query + Body can all be combined in one route

✅ FastAPI auto-generates documentation for models