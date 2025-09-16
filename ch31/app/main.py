from fastapi import FastAPI,HTTPException

app = FastAPI()

items = {
    'apple' : "a juicy fruit",
    'banana' : "a yellow delight"
}

# @app.get("/items/{item_id}")
# async def read_items(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404,detail= "Item not found")
#     return items[item_id]

@app.get("/items/{item_id}")
async def read_items(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail= "Item not found",
            headers={"x-error-type" : "itemmissing"}
            )
    return items[item_id]