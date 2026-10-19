@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: int = Body(gt=0),
    q: str | None = None,
):
    ...   


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a Pydantic model for the request body
class Item(BaseModel):
    name: str
    description: str | None = None  # Optional field with a default value
    price: float
    tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
    # FastAPI automatically parses, validates, and converts the body into the Item model
    item_dict = item.dict()
    if item.tax:
        item_dict["price_with_tax"] = item.price + item.tax
    return item_dict

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put("/items/{item_id}")
async def update_item(
    item_id: int,                  # Path parameter
    item: Item,                    # Request Body (Pydantic model)
    q: str | None = None,          # Query parameter
    published: bool = True         # Query parameter with default value
):
    results = {"item_id": item_id, **item.dict(), "published": published}
    if q:
        results["q"] = q
    return results
