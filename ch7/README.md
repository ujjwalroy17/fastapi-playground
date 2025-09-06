# 📘 FastAPI – Path Parameters with Predefined Values

## 1. What are Path Parameters with Predefined Values?
- Sometimes, we don’t want users to pass **any random value** in the path.
- Instead, we **restrict the input** to a set of predefined values (like product categories).
- This can be achieved using **Python Enums** with FastAPI.

---

## 2. Using Enum in FastAPI
We define an **Enum class** and use it as the type for our path parameter.

```
from enum import Enum
from fastapi import FastAPI

app = FastAPI()

# Define Enum with fixed categories
class ProductCategory(str, Enum):
    books = "books"
    clothing = "clothing"
    electronics = "electronics"

@app.get("/product/{category}")
async def get_products(category: ProductCategory):
    return {"response": "Products fetched", "category": category}
```
## 3. How it works:

The URL `/product/{category}` will only accept:

- `/product/books`
- `/product/clothing`
- `/product/electronics`

❌ If you try `/product/food`, FastAPI will automatically return a **422 validation error**.

## 4. Working with Python Enums in Path

You can also add **custom logic** inside the endpoint:

```
@app.get("/product/{category}")
async def get_products(category: ProductCategory):
    if category == ProductCategory.books:
        return {"category": category, "message": "Books are awesome!"}
    elif category.value == "clothing":
        return {"category": category, "message": "Fashion trends here!"}
    elif category == ProductCategory.electronics.value:
        return {"category": category, "message": "Latest gadgets available!"}
    else:
        return {"category": category, "message": "Unknown category"}
```
## 5. Why use predefined values?

- ✅ Prevents invalid inputs  
- ✅ Makes APIs self-documented (**Swagger UI shows valid options**)  
- ✅ Improves **data consistency & validation**  

---

## 🎯 Quick Summary

- Use **Enums** to restrict path parameters.  
- Users can only enter values defined in the Enum.  
- Swagger UI automatically displays a **dropdown** with valid choices
