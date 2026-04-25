from sqlalchemy.orm import Session
from models import Product
from schemas import ProductCreate


def create_product(db: Session, product: ProductCreate):
    new_product = Product(
        product_name=product.product_name,
        product_cost=product.product_cost,
        quantity=product.quantity
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_products(db: Session):
    return db.query(Product).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.product_id == product_id).first()


def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = get_product(db, product_id)
    if db_product:
        db_product.product_name = product.product_name
        db_product.product_cost = product.product_cost
        db_product.quantity = product.quantity
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product