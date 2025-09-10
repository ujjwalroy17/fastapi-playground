# 🚀 FastAPI Learning Log — Response Models

## 📌 What is a Response Model?
- A **response model** in FastAPI defines the **shape of the data** returned from your API.  
- Declared using the `response_model` parameter in route decorators.  
- Benefits:
  - ✅ **Validation** → Response must match schema.  
  - ✅ **Documentation** → Swagger/OpenAPI shows exact response schema.  
  - ✅ **Security** → Automatically remove/ignore extra fields.  
  - ✅ **Data Control** → Hide sensitive fields (e.g., passwords).  

---

## Example Models
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
## 🔹 Using Response Model
### Single Object

```python
@app.get("/products/", response_model=Products)
async def get_products():
    return {"id": 1, "name": "iPhone 17", "price": 70000, "stock": 5}
```
### List of Objects
```python
@app.get("/products/", response_model=List[Products])
async def get_products():
    return [
        {"id": 1, "name": "iPhone 17", "price": 70000, "stock": 5},
        {"id": 2, "name": "Samsung S24", "price": 58000, "stock": 7},
        {"id": 3, "name": "Pixel 9", "price": 80000, "stock": 12},
    ]
```
## 🔹 Extra Fields are Automatically Removed
Even if the function returns extra fields, FastAPI strips them out (keeps response clean).

```python
@app.get("/products/", response_model=List[Products])
async def get_products():
    return [
        {"id": 1, "name": "iPhone 17", "price": 70000, "stock": 5, "desc": "hello"},
        {"id": 2, "name": "Samsung S24", "price": 58000, "stock": 7, "desc": "hidden"},
    ]
```
* ✅ Returned response will exclude desc, since it’s not in the model.

### 🔹 POST Example with Response Model
```python
@app.post("/products/", response_model=Products)
async def create_product(product: Products):
    return product
```
 *  Input and output both validated.

*  If you return a string ("hello world"), FastAPI throws a validation error.

### 🔹 Hiding Sensitive Fields
You can define different input and output models.

```python
class BaseUser(BaseModel):
    username: str
    full_name: str | None = None

class UserIn(BaseUser):
    password: str   # only for input

@app.post("/users/", response_model=BaseUser)
async def create_user(user: UserIn):
    return user
```
* UserIn includes password (for request).
*  BaseUser excludes password (for response).

## 📊 Response Model vs Return Type Annotation

| Aspect                     | Return Type Annotation (`-> Model`) | Response Model (`response_model`) |
|-----------------------------|--------------------------------------|-----------------------------------|
| **Validation**              | ✅ Validates response               | ✅ Validates response              |
| **Swagger Docs**            | ✅ Shown in docs                    | ✅ Shown in docs                   |
| **Extra Fields Removal**    | ❌ Not enforced                     | ✅ Auto-strips unknown fields      |
| **Input vs Output Separation** | ⚠️ Harder to manage                 | ✅ Clean & easy with different models |
| **Preferred for APIs**      | Good for typing/hints               | Best practice for real-world APIs  |


✅ Key Takeaways
* Use response_model when you want to control what is returned.

* It auto-removes unknown/extra fields → response is always clean.

* Combine with separate input/output models to hide sensitive data.

* Use return type annotations for type hints + docs, but response_model is stronger for data validation & control.