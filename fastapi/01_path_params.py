from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

app = FastAPI(
    title="Product Service",
    description="An API to manage and retrieve product details",
    version="1.1.0"
)

# 1. Define a Pydantic response model for structured outputs
class ProductResponse(BaseModel):
    product_id: int = Field(..., description="Unique identifier of the product")
    name: str = Field(..., description="Name of the product")
    price: float = Field(..., description="Price of the product in USD")

# Simulated database
FAKE_DATABASE = {
    1: {"product_id": 1, "name": "Wireless Mouse", "price": 29.99},
    2: {"product_id": 2, "name": "Mechanical Keyboard", "price": 89.99},
}

@app.get(
    "/products/{product_id}",
    response_model=ProductResponse,
    summary="Get Product by ID",
    description="Retrieves a specific product using its unique ID.",
    tags=["Products"]
)
def get_product(
    product_id: int = Path(..., gt=0, description="The ID of the product to retrieve", example=1)
):
    # 2. Check if product exists and handle errors
    product = FAKE_DATABASE.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
        
    return product
