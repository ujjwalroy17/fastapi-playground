from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()

PRODUCTS = [
    {"id": 1, "title": "Ravan Backpack", "price": 109.95, "description": "Perfect for everyday use and forest walks."},
    {"id": 2, "title": "Slim Fit T-Shirts", "price": 22.3, "description": "Comfortable, slim-fitting casual shirts."},
    {"id": 3, "title": "Cotton Jacket", "price": 55.99, "description": "Great for outdoor activities and gifting."},
]


# # basic query parameter
# @app.get("/products")
# async def get_product(search:str | None = None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# # validation without Annotated
# @app.get("/products")
# async def get_products(search : str| None = Query(default= None,max_length=8)):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower(): 
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# # validation with Annotated
# @app.get("/products")
# async def get_products(
#     search:
#         Annotated[
#             str | None,
#             Query(max_length=5)
#             ] = None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower(): 
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# # Required Parameter
# @app.get("/products/")
# async def get_products(search: Annotated[str, Query(min_length=3)]):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS


# # Add regular expressions
# @app.get("/products/")
# async def get_products(search: Annotated[str | None, Query(min_length=3, pattern="^[a-z]+$")] = None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#             if filtered_products:
#                 return filtered_products
#     return PRODUCTS


# # Multiple Search Terms (list)
# @app.get("/products")
# async def get_products(search: Annotated[list[str] | None, Query()] = None):
#     if search:
#         filtered_products = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product['title'].lower():
#                     filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

## Alias parameters
# @app.get("/products/")
# async def get_products(search: Annotated[str | None, Query(alias="q")] = None):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS

# # Adding Metadata
# @app.get("/products/")
# async def get_products(search: Annotated[
#         str | None,
#         Query(alias="q", title="Search Products", description="Search by product title")
#     ] = None
#     ):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS




## Custom Validation
# def check_valid_id(id: str):
#   if not id.startswith("prod-"):
#     raise ValueError("ID must start with 'prod-'")
#   return id

# @app.get("/products/")
# async def get_products(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
#     if id:
#         return {"id": id, "message": "Valid product ID"}
#     return {"message": "No ID provided"}