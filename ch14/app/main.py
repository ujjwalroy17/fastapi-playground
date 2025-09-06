from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


# # without pydantic
# @app.post("/products")
# async def create_product(new_product:str):
#     return new_product

# with pydantic

class Product(BaseModel):
    id:int
    name:str
    price:float
    stock : int | None = None

# @app.post("/products")
# async def create_product(new_product:Product):
#     print(new_product.id)
#     print(new_product.name)
#     print(new_product.price)
#     print(new_product.stock)
#     return new_product
    

# @app.post("/products")
# async def create_product(new_product:Product):
#     product_dict = new_product.model_dump()
#     price_with_tax = new_product.price + (new_product.price * 18/100)
#     product_dict.update({"price_with_tax":price_with_tax})
#     return product_dict

# #adding path parameter
# @app.put("/products/{product_id}")
# async def update_product(product_id : int,new_updated_product:Product):
#     return {"product_id":product_id,
#             "new_updated_product": new_updated_product}
    
    
#adding query parameter
@app.put("/products/{product_id}")
async def update_product(product_id : int,new_updated_product:Product,discount:float|None=None):
    return {"product_id":product_id,
            "new_updated_product": new_updated_product,
            "discount":discount}