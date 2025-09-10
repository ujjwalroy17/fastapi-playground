from fastapi import FastAPI
from pydantic import BaseModel
from typing import List,Any

app = FastAPI()

class Products(BaseModel):
    id : int
    name : str
    price : float
    stock : int | None = None
    
class ProductsOut(BaseModel):
    id : int
    name : str
    
# with Response Model parameter
# @app.get("/products/",response_model=Products)
# async def get_products():
#     return {
#         "id" : 1 ,"name" : "iphone 17" , "price" : 70000, "stock" : 5
#     }

# @app.get("/products/",response_model=List[Products])
# async def get_products():
#     return [
#          {"id" : 1 ,"name" : "iphone 17" , "price" : 70000, "stock" : 5},
#          {"id" : 1 ,"name" : "samsung s24" , "price" : 58000, "stock" : 7},
#          {"id" : 1 ,"name" : "Pixel 9" , "price" : 80000, "stock" : 12}
#     ]

@app.get("/products/",response_model=List[Products])
async def get_products():
    return [
         {"id" : 1 ,"name" : "iphone 17" , "price" : 70000, "stock" : 5,"desc" : "hello 1"},
         {"id" : 1 ,"name" : "samsung s24" , "price" : 58000, "stock" : 7,"desc" : "hello 5"},
         {"id" : 1 ,"name" : "Pixel 9" , "price" : 80000, "stock" : 12,"desc" : "hello 9"}
    ]
 
# @app.post("/products/",response_model=Products)
# async def create_product(product : Products):
#     return "hello world"
    
# @app.post("/products/",response_model=Products)
# async def create_product(product : Products):
#     return product

# class BaseUser(BaseModel):
#     username : str
#     full_name : str | None = None
    
# class UserIn(BaseUser):
#     password : str
    
# @app.post("/products/",response_model=BaseUser)
# async def create_user(user : UserIn):
#     return user,{"developer": "Ujjwal"}

@app.post("/products/",response_model=Products)
async def create_product(product : Products) -> Any:
    return product