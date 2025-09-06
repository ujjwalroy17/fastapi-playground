from fastapi import FastAPI

app = FastAPI()

# #Single Query Parameter
# @app.get("/product")
# async def product(category:str):
#     return {"status":"OK","Category":category}

# #Multiple Query Parameter
# @app.get("/product")
# async def product(category:str, limit:int):
#     return {"status":"OK","Category":category,"Limit":limit}

# # Default Query Parameter
# @app.get("/product")
# async def product(category:str, limit:int=11):
#   return {"status":"OK", "category":category, "limit":limit}

# # Optional Query Parameter
# @app.get("/product")
# async def product(limit:int, category:str | None = None):
#   return {"status":"OK", "category":category, "limit":limit}


#Path and Query parameter
@app.get("/product/{year}")
async def product(year:str, category:str):
  return {"status":"OK", "year":year, "category":category}