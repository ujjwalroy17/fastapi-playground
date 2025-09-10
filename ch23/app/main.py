from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Products(BaseModel):
    id : int
    name : str
    price : float
    stock : int | None = None
    
class ProductsOut(BaseModel):
    id : int
    name : str
 
    
# Without Retrun Type
# @app.get("/products/")
# async def get_products():
#     return {
#         "status" : "OK"
#     }

# return type annotation
# @app.get("/products/")
# async def get_products() -> Products:
#     return {
#         "id" : 1 ,"name" : "iphone 17" , "price" : 70000, "stock" : 5
#     }

# @app.get("/products/")
# async def get_products() -> Products:
#     return {
#         "id" : 1 ,"name" : "iphone 17" , "price" : 70000
#     }

# @app.get("/products/")
# async def get_products() -> Products:
#     return {
#         "id" : 1 ,"name" : "iphone 17" , "price" : 70000, "stock" : 5,
#         "description" : "this is iphone 17"
#     }

# @app.get("/products/")
# async def get_products() -> List[Products]:
#     return [
#         {"id" : 1 ,"name" : "iphone 17" , "price" : 70000, "stock" : 5},
#         {"id" : 1 ,"name" : "samsung s24" , "price" : 58000, "stock" : 7},
#         {"id" : 1 ,"name" : "Pixel 9" , "price" : 80000, "stock" : 12}
# ]

# @app.post("/products/")
# async def create_product(product : Products) -> Products:
#     return product,{"developer": "Ujjwal"}

# @app.post("/products/")
# async def create_product(product : Products) -> ProductsOut:
#     return product,{"developer": "Ujjwal"}

# class BaseUser(BaseModel):
#     username : str
#     full_name : str | None = None
    
# class UserIn(BaseUser):
#     password : str
    
# @app.post("/products/")
# async def create_user(user : UserIn) -> BaseUser:
#     return user,{"developer": "Ujjwal"}