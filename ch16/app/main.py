from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated
app = FastAPI()

## Pydantic's Field
class Product(BaseModel):
    name : str = Field(
        title="Product Name",
        description="The name of the product",
        max_length=100,
        min_length=3,
        pattern="^[A-Za-z0-p]+$"
    )
    price : float = Field(
        gt=0,
        title="Product price",
        description="The price of the product in USD , must be greater than zero",
    )
    stock :int|None = Field(
        default=None,
        ge=0,
        title="Stock Quantity",
        description="The number of items in Stock,must be non-negative",
    )

@app.post("/product")
async def create_product(product:Product):
    return {"product":product}