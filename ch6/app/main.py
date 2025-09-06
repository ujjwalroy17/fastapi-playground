from fastapi import FastAPI

app = FastAPI()

##Order matters

@app.get("/product/roe_nt_usb")
async def single_product_static():
    return {"response": "Single Data Fetched"}

@app.get("/product/{product_title}")
async def single_product_static(product_title:str):
    return {"response": "Single Data Fetched","product_title" : product_title}