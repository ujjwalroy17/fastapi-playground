from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

# Using Field level examples
class Product(BaseModel):
    name: str = Field(examples=["Iphone 15"])
    price: float = Field(examples=[799.00])
    stock: int |None= Field(default=None, examples=["25"])
    
@app.post("/products")
async def create_products(product: Product):
    return product

# ##Using Pydantic's json_schema_extra
# class Product(BaseModel):
#     name: str 
#     price: float 
#     stock: int |None= None
    
#     model_config = {
#         "json_schema_extra":{
#             "examples":[
#                 {   
#                 "name" : "Iphone 15",
#                 "price" : 799.00,
#                 "stock" : 45
#             }
#             ]
#         }
#     }
    
# @app.post("/products")
# async def create_products(product: Product):
#     return product