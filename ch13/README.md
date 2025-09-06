
# 📘 FastAPI – Path Parameters

* Path parameters allow us to capture values from the URL directly.  
* They are commonly used to fetch specific resources like products, users, or orders.  

---

## 🔹 1. Basic Path Parameter
```
@app.get("/products/{product_id}") 
async def get_product(product_id: int): 
    for product in PRODUCTS: 
        if product["id"] == product_id: 
            return product 
    return {"error": "Product not found"}
```
* {product_id} in the URL is captured.

* FastAPI automatically converts it to an int.

* Example → `/products/2`

## 🔹 2. Numeric Validation with Path
```
@app.get("/products/{product_id}") 
async def get_product(product_id: Annotated[int, Path(ge=1, le=3)]): 
    for product in PRODUCTS: 
        if product["id"] == product_id: 
            return product 
    return {"error": "Product not found"}
```
* ge=1 → product_id must be greater than or equal to 1.

* le=3 → product_id must be less than or equal to 3.

* Example → `/products/5` ❌ Invalid

## 🔹 3. Adding Metadata with Path
```
@app.get("/products/{product_id}")
async def get_product(
    product_id: Annotated[
        int,
        Path(
            title="The ID of the product",
            description="This is the product id"
        )
    ]
):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}
```
* Adds title and description in Swagger UI (/docs).

* Helpful for documentation and API readability.

## 🔹 4. Combining Path and Query Parameters
```
@app.get("/products/{product_id}")
async def get_product(
    product_id: Annotated[int, Path(gt=0, le=100)],
    search: Annotated[str | None, Query(max_length=20)] = None
):
    for product in PRODUCTS:
        if product["id"] == product_id:
            if search and search.lower() not in product["title"].lower():
                return {"error": "Product does not match search term"}
            return product
    return {"error": "Product not found"}
```
* product_id → comes from path.

* search → comes from query parameter.

* Example → `/products/2?search=shirt`

| Feature                | Path Parameter                          | Query Parameter                              |
|-------------------------|-----------------------------------------|---------------------------------------------|
| **Position**            | Part of the URL (`/products/{id}`)      | After `?` in the URL (`/products?search=bag`) |
| **Mandatory/Optional**  | Always **required**                     | Can be **optional or required**              |
| **Usage**               | Identify a specific resource            | Filter, search, or customize results         |
| **Validation**          | Done using `Path()`                     | Done using `Query()`                         |
| **Docs Metadata**       | Supports `title`, `description`         | Supports `title`, `description`, `alias`     |

## Tips & Best Practices

✅ Use Path Parameters when identifying a specific resource.

Example: `/users/10, /orders/1234`

✅ Use Query Parameters when filtering or searching.

Example: `/products?category=shoes&sort=price`

✅ Always add validation (gt, ge, lt, le, max_length, pattern) for cleaner APIs.

✅ Add metadata → improves auto-generated documentation.

✅ Combine Path + Query for flexibility.