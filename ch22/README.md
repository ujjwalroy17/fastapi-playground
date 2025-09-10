# 📘 FastAPI – Header Parameters with Pydantic Model

## ✅ What are Headers in FastAPI?
- **Headers** are extra information sent by the client (browser, app, or API client) with each HTTP request.  
- Examples:  
  - `Authorization: Bearer token123`  
  - `Accept-Language: en-US`  
  - `User-Agent: Mozilla/5.0`  

Headers are often used for:
- Authentication & Authorization (`Authorization`)
- Localization (`Accept-Language`)
- Tracking requests (`X-Tracking-Id`)

---

##  Using Pydantic Models for Headers
Instead of defining each header separately, you can group them into a **Pydantic model**.  

### Example:
```python
class ProductHeaders(BaseModel):
    authorization: str
    accept_language: str | None = None
    x_tracking_id: list[str] = []

@app.get("/products")
async def get_product(headers: Annotated[ProductHeaders, Header()]):
    return {"headers": headers}
```
#### Test with curl:
```bash
curl -H "Authorization: Bearer token123" \
     -H "Accept-Language: en-US" \
     -H "X-Tracking-Id: track1" \
     -H "X-Tracking-Id: track2" \
     http://127.0.0.1:8000/products
```
## 🚫 Forbidding Extra Headers
By default, FastAPI accepts extra headers. If you want to strictly validate only specific headers, use extra="forbid" in your Pydantic model.
```
python
class ProductHeaders(BaseModel):
    model_config = {"extra": "forbid"}
    authorization: str
    accept_language: str | None = None
    x_tracking_id: list[str] = []
```
If the client sends an **extra header**, FastAPI will return a **validation error**.

Example request with extra header:
```bash
curl -H "Authorization: Bearer token123" \
     -H "Accept-Language: en-US" \
     -H "X-Tracking-Id: track1" \
     -H "extra-header: h123" \
     http://127.0.0.1:8000/products
```
👉 This will fail because extra-header is not defined in the model.

## Combining Cookies, Headers, and Body
You can also use Cookies, Headers, and Body together in one request.

Example Code:
```
python
class ProductCookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str
    preferred_category: str | None = None

class PriceFilter(BaseModel):
    min_price: float
    max_price: float | None = None

class ProductHeaders(BaseModel):
    model_config = {"extra": "allow"}  # allow automatic headers like Host, User-Agent
    authorization: str
    accept_language: str | None = None
    x_tracking_id: list[str] = []

@app.post("/products/recomendations")
async def get_recomendations(
    cookies: Annotated[ProductCookies, Cookie()],
    headers: Annotated[ProductHeaders, Header()],
    price_filter: Annotated[PriceFilter, Body(embed=True)]
):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        response["category"] = cookies.preferred_category
    if headers.authorization:
        response["authorization"] = headers.authorization
    response["price_range"] = {
        "min_price": price_filter.min_price,
        "max_price": price_filter.max_price
    }
    response["message"] = (
        f"Recommendations for session {cookies.session_id} "
        f"with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'} "
        f"with {headers.authorization}"
    )
    return response
```
Example Request
```
bash
curl -X POST "http://127.0.0.1:8000/products/recomendations" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer mysecrettoken" \
     -H "Accept-Language: en-US" \
     -H "X-Tracking-Id: track123" \
     -H "X-Tracking-Id: track456" \
     -b "session_id=abc123; preferred_category=electronics" \
     -d "{\"price_filter\": {\"min_price\": 100, \"max_price\": 500}}"
```
✅ Example Response:
```json
{
  "session_id": "abc123",
  "category": "electronics",
  "authorization": "Bearer mysecrettoken",
  "price_range": {
    "min_price": 100.0,
    "max_price": 500.0
  },
  "message": "Recommendations for session abc123 with price range 100.0 to 500.0 with Bearer mysecrettoken"
}
```
### Key Takeaways
* Use Header() dependency to access headers.

* Group headers into a Pydantic model for better structure.

* Use extra="forbid" to reject unexpected headers.

* You can combine Headers + Cookies + Body in a single endpoint for complex APIs.