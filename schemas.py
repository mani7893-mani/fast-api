from pydantic import BaseModel

class ProductCreate(BaseModel):
    product_name: str
    product_cost: int
    quantity: int


class ProductResponse(ProductCreate):
    product_id: int

    class Config:
        from_attributes = True