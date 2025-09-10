# 🚀 FastAPI Learning Log — Return Type Annotation

## 📌 What is Return Type Annotation?
- In FastAPI, you can **define what your endpoint will return** using Python type hints.  
- It improves:
  - ✅ **Validation** → Ensures responses match your defined schema.  
  - ✅ **Docs** → OpenAPI/Swagger UI shows correct response models.  
  - ✅ **Clarity** → Makes your API self-documented and easier to understand.  

---

### Example Models
```python
from pydantic import BaseModel
from typing import List

class Products(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None   # optional

class ProductsOut(BaseModel):
    id: int
    name: str
```

### 🔹 Without Return Type Annotation
```python
@app.get("/products/")
async def get_products():
    return {"status": "OK"}
```
* Works, but no validation.

* Swagger docs don’t know what the response will look like.

###🔹 With Return Type Annotation
#### ✅ Single Object
```python
@app.get("/products/")
async def get_products() -> Products:
    return {"id": 1, "name": "iPhone 17", "price": 70000, "stock": 5}
```
#### ✅ Missing Optional Field
```python
@app.get("/products/")
async def get_products() -> Products:
    return {"id": 1, "name": "iPhone 17", "price": 70000}
```
* (stock is optional so this is still valid ✅)

####  Extra Field (not in schema)
```python
@app.get("/products/")
async def get_products() -> Products:
    return {"id": 1, "name": "iPhone 17", "price": 70000, "stock": 5, "description": "invalid"}
```
* FastAPI ignores extra fields not defined in the model.

#### List of Objects
```python
@app.get("/products/")
async def get_products() -> List[Products]:
    return [
        {"id": 1, "name": "iPhone 17", "price": 70000, "stock": 5},
        {"id": 2, "name": "Samsung S24", "price": 58000, "stock": 7},
        {"id": 3, "name": "Pixel 9", "price": 80000, "stock": 12}
    ]
```
### 🔹 Input vs Output Models
You may want to accept one model but **return another** (e.g., hide sensitive data).

```python
@app.post("/products/")
async def create_product(product: Products) -> ProductsOut:
    return product  # Only id & name are returned
```
#### 🔹 User Example with Inheritance
```python
class BaseUser(BaseModel):
    username: str
    full_name: str | None = None

class UserIn(BaseUser):
    password: str   # only for input

@app.post("/users/")
async def create_user(user: UserIn) -> BaseUser:
    return user     # password not returned
```
* UserIn → Input model (includes password).

* BaseUser → Output model (excludes password).

## 📊 Comparison: Without vs With Return Type

| Aspect                 | Without Return Type | With Return Type        |
|-------------------------|---------------------|--------------------------|
| **Validation**          | ❌ None            | ✅ Auto-validated        |
| **Swagger Docs**        | ❌ Only "default"  | ✅ Full schema           |
| **Security (hide fields)** | ❌ Not possible     | ✅ Possible with output models |
| **Code Readability**    | ❌ Ambiguous       | ✅ Clear & explicit      |


### ✅ Key Takeaways
* Always use return type annotations for cleaner, safer APIs.

* Use List[Model] when returning multiple items.

* Use different models for input/output to hide sensitive fields.

* Extra fields not defined in the model are ignored automatically.