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

#(to be continued come back at 1:30)
