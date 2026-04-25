from sqlalchemy import Column, Integer, String
from database import Base

class Product(Base):
    __tablename__ = "p_table"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50))
    product_cost = Column(Integer)
    quantity = Column(Integer)