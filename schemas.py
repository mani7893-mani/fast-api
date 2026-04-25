from pydantic import BaseModel

class UserCreate(BaseModel):
    product_name: str
    product_cost: int
    quantity:int

class UserResponse(UserCreate):
    product_id: int

    class Config:
        from_attributes = True
