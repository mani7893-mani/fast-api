from sqlalchemy import Column, Integer, String
from database import Base

class Table(Base):
    __tablename__ = "p_table"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(50))
    product_cost = Column(Integer)
    quantity=Column(Integer)