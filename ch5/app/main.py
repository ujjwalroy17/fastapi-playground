from fastapi import FastAPI

app = FastAPI()

## Parameter without Type

# @app.get("/product/{product_id}")
# async def single_product(product_id):
#     return {"response":"Single Data Fetched","product_id":product_id}

## Parameter with Type

@app.get("/product/{product_id}")
async def single_product(product_id:int):
    return {"response":"Single Data Fetched","product_id":product_id}