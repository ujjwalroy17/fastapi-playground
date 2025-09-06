# 📘 FastAPI – Pydantic Body Example Values

## 🔹 Why Use Example Values?
When testing APIs, it helps to see **sample request bodies** in Swagger UI or ReDoc.  
Example values:
- Make the API **self-explanatory**.  
- Help developers **understand request formats**.  
- Provide **default test data** for quick API testing.  

---

## 📌 Method 1: Field-Level `examples`
You can set examples directly on each field using `Field(examples=[...])`.

```python
class Product(BaseModel):
    name: str = Field(examples=["iPhone 15"])
    price: float = Field(examples=[799.00])
    stock: int | None = Field(default=None, examples=[25])

@app.post("/products")
async def create_products(product: Product):
    return product
```
### Swagger UI Example Payload
```python
{
  "name": "iPhone 15",
  "price": 799.0,
  "stock": 25
}
```
## Method 2: Model-Level json_schema_extra

Instead of field-level, you can define one complete example for the whole model.
```python
class Product(BaseModel):
    name: str
    price: float
    stock: int | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "iPhone 15",
                    "price": 799.00,
                    "stock": 45
                }
            ]
        }
    }

@app.post("/products")
async def create_products(product: Product):
    return product
```

### Swagger UI Example Payload
```json
{
  "name": "iPhone 15",
  "price": 799.0,
  "stock": 45
}
```

## Key Concepts Learned

* Field-level examples → good for showing multiple possible values.

* Model-level examples (json_schema_extra) → good for showing a complete request payload.

* Both appear automatically in Swagger UI (/docs) and ReDoc (/redoc).