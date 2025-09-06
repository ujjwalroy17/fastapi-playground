# 📘 FastAPI – Pydantic `Field`

## 🔹 What is `Field`?
When defining request models in **FastAPI** using **Pydantic**, you usually declare types like `str`, `int`, or `float`.  

But often, you need **more control**:
- Enforce stricter **validation rules** (e.g., `price > 0`, `name length ≥ 3`).
- Provide **helpful metadata** (title, description).
- Supply **default values** and schema hints.
- Show clear constraints in **API docs** (`/docs`, `/redoc`).

This is where **`Field()`** comes in. It allows you to **extend the definition of a field** beyond just its type.

---

## 📌 Example: Product Model with `Field`
```python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        description="The name of the product",
        min_length=3,
        max_length=100,
        pattern="^[A-Za-z0-p]+$"   # only letters allowed
    )
    price: float = Field(
        gt=0,  # must be greater than 0
        title="Product Price",
        description="The price of the product in USD, must be greater than zero"
    )
    stock: int | None = Field(
        default=None,
        ge=0,  # must be ≥ 0 if provided
        title="Stock Quantity",
        description="The number of items in stock, must be non-negative"
    )
```
```Python
@app.post("/product")
async def create_product(product: Product):
    return {"product": product}
```
## How Validation Works
### Valid Request
```Json
{
  "name": "Laptop",
  "price": 1200.5,
  "stock": 10
}
```


### Invalid Requests

#### 1.Name too short

```Json
{"name": "PC", "price": 1200.5, "stock": 5}
```

**Error: String should have at least 3 characters.**

#### 2.Name contains numbers

```Json
{"name": "Laptop123", "price": 1200.5, "stock": 5}
```


**Error: String should match pattern "^[A-Za-z0-p]+$".**

#### 3.Negative price

```Json
{"name": "Laptop", "price": -5, "stock": 5}
```
**Error: Input should be greater than 0.**

#### 4.Negative stock

```Json
{"name": "Laptop", "price": 1200.5, "stock": -3}
```
**Error: Input should be greater than or equal to 0.**

## Key Things About Field

#### Constraints

* min_length / max_length: For strings

* gt (greater than) / ge (greater or equal): For numbers

* lt (less than) / le (less or equal): For numbers

* pattern: Regex for string validation

#### Metadata

* title: Short label (appears in docs)

* description: Longer explanation (appears in docs & OpenAPI schema)

#### Defaults

*Set default=value or default=None

#### Docs Integration

* Swagger UI (/docs) and ReDoc (/redoc) show validation rules automatically.