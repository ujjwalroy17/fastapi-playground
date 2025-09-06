from fastapi import FastAPI,Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Product(BaseModel):
    name:str
    price : float
    stock : int |None = None

class Seller(BaseModel):
    username : str
    full_name : str | None = None
    
# @app.post("/product")
# async def create_product(product:Product,seller:Seller):
#     return {"product":product,
#             "seller" : seller}

# #Make any Body Optional
# @app.post("/product")
# async def create_product(product:Product,seller:Seller |None=None):
#     return {"product":product,
#             "seller" : seller}
    
# #Singular Vallues in Body
# @app.post("/product")
# async def create_product(product:Product,seller:Seller,
#                          sec_key:Annotated[str, Body()]):
#     return {"product":product,
#             "seller" : seller,
#             "sec_key":sec_key}
    
# #Embed a single body parameter
# # Without embed
# @app.post("/product")
# async def create_product(product:Product):
#     return {"product":product,
#             }

#with embed
@app.post("/product")
async def create_product(product:Annotated[Product, Body(embed=True)]):
    return {"product":product,
           }