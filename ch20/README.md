# FastAPI – Cookie Parameters with Pydantic Models

## 🔹 What are Cookies in FastAPI?
- **Cookies** are small pieces of data sent by the server and stored in the client’s browser.  
- They are automatically included in requests back to the server.  
- Useful for: **sessions, user preferences, authentication, recommendations**.

---

### 1. Cookies with a Pydantic Model
You can use **Pydantic models** to validate cookie values.

```python
class ProductCookies(BaseModel):
    session_id: str
    preferred_category: str | None = None
    tracking_id: str | None = None

@app.get("/products/recommendations")
async def get_recommendations(cookies: Annotated[ProductCookies, Cookie()]):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        response["message"] = f"Recommendations for {cookies.preferred_category} products"
    else:
        response["message"] = f"Default recommendations for session {cookies.session_id}"
    if cookies.tracking_id:
        response["tracking_id"] = cookies.tracking_id
    return response
```
✅ Example request using curl:
```cmd
curl -H "Cookie: session_id=abc123; preferred_category=Electronics; tracking_id=xyz789" \
http://127.0.0.1:8000/products/recommendations
```

### 2. Forbidding Extra Cookies

You can disallow unexpected cookie values using extra="forbid" in Pydantic’s model_config.
```python
class ProductCookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str
    preferred_category: str | None = None
    tracking_id: str | None = None
```

➡️ Now, if a client sends any extra cookie (not defined in the model), FastAPI will **reject** the request.

### 3. Combining Cookies with Body Parameters

You can use cookies together with JSON body parameters for more powerful validation.
```Python
class ProductCookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str = Field(title="Session ID", description="User session identifier")
    preferred_category: str | None = Field(default=None, title="Preferred Category", description="User's preferred product category")

class PriceFilter(BaseModel):
    min_price: float = Field(ge=0, title="Minimum Price", description="Minimum price for recommendations")
    max_price: float | None = Field(default=None, title="Maximum Price", description="Maximum price for recommendations")

@app.post("/products/recommendations")
async def get_recommendations(
    cookies: Annotated[ProductCookies, Cookie()],
    price_filter: Annotated[PriceFilter, Body(embed=True)]
):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        response["category"] = cookies.preferred_category
    response["price_range"] = {
        "min_price": price_filter.min_price,
        "max_price": price_filter.max_price
    }
    response["message"] = (
        f"Recommendations for session {cookies.session_id} "
        f"with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'}"
    )
    return response
```

✅ Example request:
```cmd
curl -X POST \
-H "Cookie: session_id=abc123; preferred_category=Electronics" \
-H "Content-Type: application/json" \
-d "{\"price_filter\":{\"min_price\":50.0,\"max_price\":1000.0}}" \
http://127.0.0.1:8000/products/recommendations
```
### Key Concepts Learned

* Cookies can be mapped directly into Pydantic models for validation.

* Use extra="forbid" to prevent unexpected cookies.

* Cookies can be combined with request body to build complex and secure endpoints.

* Field() helps add metadata like title, description, constraints for better documentation.


