# 📘 FastAPI – Pydantic Nested Body Models

## 🔹 Why Nested Models?
In real-world APIs, data is often **hierarchical**.  
For example:
- A **Product** belongs to a **Category**.
- A **User** may have multiple **Addresses**.
- An **Order** contains a list of **Items**.

Instead of flattening everything, FastAPI + Pydantic allows **nested models** to keep data structured and validated.

---

## 📌 Example 1: Product with a Category (One-to-One)
```python
class Category(BaseModel):
    name: str = Field(
        title="Category Name",
        description="The name of the product category",
        min_length=1,
        max_length=50
    )
    description: str | None = Field(
        default=None,
        title="Category Description",
        description="A brief description of the category",
        max_length=200
    )

class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        description="The name of the product",
        min_length=1,
        max_length=100
    )
    price: float = Field(
        gt=0,
        title="Product Price",
        description="The price in USD, must be greater than zero"
    )
    stock: int | None = Field(
        default=None,
        ge=0,
        title="Stock Quantity",
        description="Number of items in stock, must be non-negative"
    )
    category: Category | None = Field(
        default=None,
        title="Product Category",
        description="The category to which the product belongs"
    )

@app.post("/products")
async def create_product(product: Product):
    return product
```

### Valid Request
```Json
{
  "name": "Laptop",
  "price": 1500,
  "stock": 20,
  "category": {
    "name": "Electronics",
    "description": "Devices like laptops, phones, and accessories"
  }
}
```
### Invalid Request (missing required category field)
```json
{
  "name": "Laptop",
  "price": 1500,
  "stock": 20,
  "category": {
    "description": "Devices like laptops, phones, and accessories"
  }
}
```

**Error: "Category Name" is required.**

## Example 2: Product with Multiple Categories (One-to-Many)

Sometimes a product can belong to **multiple categories.**
You can make the category field a list of submodels:
```python
class Product(BaseModel):
    name: str = Field(
        title="Product Name",
        description="The name of the product",
        max_length=100,
        min_length=1
    )
    price: float = Field(
        gt=0,
        title="Product Price",
        description="The price in USD, must be greater than zero"
    )
    stock: int | None = Field(
        default=None,
        ge=0,
        title="Stock Quantity",
        description="Number of items in stock, must be non-negative"
    )
    category: list[Category] | None = Field(
       default=None,
       title="Product Category",
       description="The category to which the product belongs"
    )
```
### Valid Request
```json
{
  "name": "Smartphone",
  "price": 800,
  "stock": 50,
  "category": [
    {"name": "Electronics", "description": "Electronic devices"},
    {"name": "Mobile", "description": "Smartphones and accessories"}
  ]
}
```

## Key Concepts Learned

Nested models represent hierarchical data.

Submodels `(Category)` can be embedded inside parent models `(Product)`.

Nested fields can be:

Single object → Category

List of objects → list[Category]

All nested fields are automatically validated by `Pydantic`.