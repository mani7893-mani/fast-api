from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(50))
    product_cost = Column(Integer)
    quantity=Column(Integer)