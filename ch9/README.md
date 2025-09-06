# 📘 FastAPI – CRUD Operations (Without Database)

CRUD stands for:
- **C** → Create  
- **R** → Read  
- **U** → Update  
- **D** → Delete  

In APIs, CRUD refers to the basic operations you can perform on data.  
Here, we use a **Python list (`PRODUCTS`) as in-memory storage** instead of a database.  

---

## 🔹 1. Read (GET Request)

### ➤ Fetch All Products
```
@app.get("/product")
async def all_products():
  return PRODUCTS
```
* 📌 Example → `/product`
* ✔ Returns the list of all products.

### ➤ Fetch Single Product
```
@app.get("/product/{product_id}")
async def single_products(product_id: int):
  for product in PRODUCTS:
    if product["id"] == product_id:
      return product
```
* 📌 Example → `/product/2`
* ✔ Returns the product with ID = 2.

## 🔹 2. Create (POST Request)
```
@app.post("/product")
async def create_product(new_product: dict):
  PRODUCTS.append(new_product)
  return {"status": "created", "new_product": new_product}
```
* 📌 Important:

    * In POST, we cannot send data via the URL.

    * Instead, data must be sent in the Request Body as JSON.

    * Swagger UI (auto docs at http://127.0.0.1:8000/docs)  allows us to easily enter the input.

* 📌 Example → Send JSON body in Swagger UI:

    ```
    {
    "id": 4,
    "title": "New Jacket",
    "price": 99.99,
    "description": "Stylish and warm."
    }
    ```
    * ✔ Adds a new product to the list.

## 🔹 3. Update (PUT Request – Full Update)
```
@app.put("/product/{product_id}")
def update_product(product_id: int, new_updated_product: dict):
  for index, product in enumerate(PRODUCTS):
    if product["id"] == product_id:
      PRODUCTS[index] = new_updated_product
      return {"status": "Updated", "product_id": product_id, "new updated product": new_updated_product}
```
* 📌 Note:

    * Like POST, data is sent in the Request Body (JSON), not the URL.

    * PUT replaces the whole product with new data.

* 📌 Example JSON body in Swagger:

    ```
    {
    "id": 2,
    "title": "Updated T-Shirt",
    "price": 25.0,
    "description": "New description here"
    }
    ```
## 🔹 4. Partial Update (PATCH Request)
```
@app.patch("/product/{product_id}")
def partial_product(product_id: int, new_updated_product: dict):
    for product in PRODUCTS:
        if product["id"] == product_id:
            product.update(new_updated_product)
            return {"status": "Partial updated", "product_id": product_id, "new updated product": product}
```
* 📌 Note:

   *  Like POST & PUT, PATCH also needs input via the Request Body.

    * PATCH updates only selected fields, not the entire product.

* 📌 Example JSON body in Swagger:

```
{
  "price": 60.50
}
```
##🔹 5. Delete (DELETE Request)
```
@app.delete("/product/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            return {"status": "Deleted", "product_id": product_id}
```
* 📌 Example → `/product/1`
* ✔ Removes the product with ID = 1.

## ⚡ CRUD Quick Reference Table

| Method  | Purpose              | URL Example   | Input Location |
|---------|----------------------|---------------|----------------|
| GET     | Read all products    | `/product`    | URL            |
| GET     | Read single product  | `/product/2`  | URL            |
| POST    | Create new product   | `/product`    | Request Body   |
| PUT     | Update full product  | `/product/2`  | Request Body   |
| PATCH   | Update partial data  | `/product/3`  | Request Body   |
| DELETE  | Delete product       | `/product/1`  | URL            |
