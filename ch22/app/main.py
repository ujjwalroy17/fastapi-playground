from typing import Annotated
from fastapi import FastAPI, Header, Body, Cookie
from pydantic import BaseModel, Field
app = FastAPI()

# ## Headers with a Pydantic Model

# class ProductHeaders(BaseModel):
#   authorization: str
#   accept_language: str | None = None
#   x_tracking_id: list[str] = []

# @app.get("/products")
# async def get_product(headers: Annotated[ProductHeaders, Header()]):
#     return {
#         "headers": headers
#     }

# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" http://127.0.0.1:8000/products

# Forbidding Extra Headers
# class ProductHeaders(BaseModel):
#   model_config = {"extra":"forbid"}
#   authorization: str
#   accept_language: str | None = None
#   x_tracking_id: list[str] = []

# @app.get("/products")
# async def get_product(headers: Annotated[ProductHeaders, Header()]):
#     return {
#         "headers": headers
#     }

# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-US" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" -H "extra-header: h123" http://127.0.0.1:8000/products

# Combining Cookie, Header and Nody parameters

class ProductCookies(BaseModel):
  model_config = {"extra": "forbid"}
  session_id: str = Field(title="Session ID", description="User session identifier")
  preferred_category: str | None = Field(default=None, title="Preferred Category", description="User's preferred product category")

class PriceFilter(BaseModel):
    min_price: float = Field(ge=0, title="Minimum Price", description="Minimum price for recommendations")
    max_price: float | None = Field(default=None, title="Maximum Price", description="Maximum price for recommendations")
    
class ProductHeaders(BaseModel):
  model_config = {"extra":"allow"}
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
        response["authorization"] =  headers.authorization
    response["price_range"] = {
        "min_price": price_filter.min_price,
        "max_price": price_filter.max_price
    }
    response["message"] = f"Recommendations for session {cookies.session_id} with price range {price_filter.min_price} to {price_filter.max_price or 'unlimited'} with {headers.authorization}"
    return response
# curl -X POST "http://127.0.0.1:8000/products/recomendations" -H "Content-Type: application/json" -H "Authorization: Bearer mysecrettoken" -H "Accept-Language: en-US" -H "X-Tracking-Id: track123" -H "X-Tracking-Id: track456" -b "session_id=abc123; preferred_category=electronics" -d "{\"price_filter\": {\"min_price\": 100, \"max_price\": 500}}"


