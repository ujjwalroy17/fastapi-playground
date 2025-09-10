# 📘 FastAPI — Include & Exclude Specific Fields in Response Models

FastAPI allows you to **control which fields** are returned in API responses using the `response_model`, `response_model_include`, `response_model_exclude`, and `response_model_exclude_unset` parameters.

---

##  Example Setup

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

products_db = {
    "1": {"id": "1", "name": "Laptop", "price": 999.99, "stock": 10, "is_active": True},
    "2": {"id": "2", "name": "Smartphone", "price": 499.99, "stock": 50, "is_active": False}
}

class Product(BaseModel):
    id: str
    name: str
    price: float
    description: Optional[str] = None
    tax: float = 15.0
```
## 🔹 1. Exclude Unset Default Values
```python
@app.get("/products/{product_id}", response_model=Product, response_model_exclude_unset=True)
async def get_product(product_id: str):
    return products_db.get(product_id, {})
```
*  Removes fields that are not explicitly set in the DB.

* Example: If description is missing, it won’t appear in the response.

## 🔹 2. Include Specific Fields
```python
@app.get("/products/{product_id}", response_model=Product, response_model_include={"name", "price"})
async def get_product(product_id: str):
    return products_db.get(product_id, {})
```

*  Only returns name and price.

* Useful for lightweight responses (e.g., product listings).

##🔹 3. Exclude Specific Fields
```python
@app.get("/products/{product_id}", response_model=Product, response_model_exclude={"tax", "description"})
async def get_product(product_id: str):
    return products_db.get(product_id, {})
```

*  Returns all fields except tax and description.

* Useful when you want to hide sensitive fields.

## 📊 Comparison Table

| Feature                      | Example Param                          | Effect                                |
|------------------------------|----------------------------------------|---------------------------------------|
| Exclude unset default values | `response_model_exclude_unset=True`    | Hides fields with defaults if not set |
| Include only specific fields | `response_model_include={"name"}`      | Returns only chosen fields            |
| Exclude specific fields      | `response_model_exclude={"tax"}`       | Returns all fields except chosen ones |

### Key Takeaways

* Use include when you want a minimal set of fields.

* Use exclude when you want to hide specific fields.

* Use exclude_unset to avoid returning default values.

* Helps in security, performance, and clarity of API responses.