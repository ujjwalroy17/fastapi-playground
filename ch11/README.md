# 📘 FastAPI – Chapter 5: Status Codes

## 1. What are Status Codes?
Status codes are **3-digit numbers** returned with every HTTP response.  
They tell the client whether the request was successful, failed, or needs further action.

They are divided into different **categories**:

- ✅ **2xx – Success** → The request was successful.  
- ⚠️ **3xx – Redirection** → The client must take additional action.  
- ❌ **4xx – Client Error** → Something is wrong with the request.  
- 💥 **5xx – Server Error** → Something went wrong on the server.  

---

## 2. Using Status Codes in FastAPI

### (a) Directly in the decorator
```
from fastapi import FastAPI, status

app = FastAPI()

@app.post("/product", status_code=status.HTTP_201_CREATED)
async def create_product():
    return {"message": "Product created successfully"}
```
### (b) Using Response object
```
from fastapi import FastAPI, Response, status

app = FastAPI()

@app.delete("/product/{product_id}")
async def delete_product(product_id: int, response: Response):
    if product_id == 0:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}
    return {"message": "Product deleted successfully"}
```
## 3. Shortcut for Status Codes
Instead of writing raw numbers like 200, 201, etc.,
FastAPI provides shortcuts via the status module.

```
from fastapi import status

status.HTTP_200_OK          # 200
status.HTTP_201_CREATED     # 201
status.HTTP_204_NO_CONTENT  # 204
status.HTTP_400_BAD_REQUEST # 400
status.HTTP_404_NOT_FOUND   # 404
status.HTTP_500_INTERNAL_SERVER_ERROR # 500
```
**✅ These names make your code more readable and self-explanatory.**

## 4. In Short (Status Code Categories)
100 - 199 → Informational
Rarely used directly. Responses with these status codes cannot have a body.

200 - 299 → Successful responses

200 OK → Default status code, means everything is fine.

201 Created → Common after creating a new record.

204 No Content → No data to return, response must not have a body.

300 - 399 → Redirection
* Used for redirects.
* Example: 304 Not Modified (must not have a body).

400 - 499 → Client errors
* 400 Bad Request → Generic client-side error.
* 404 Not Found → Resource doesn’t exist.

500 - 599 → Server errors

You rarely set them manually.

If something goes wrong in your code or server, FastAPI will return them automatically.

