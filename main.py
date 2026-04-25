from fastapi import FastAPI, HTTPException
from database import engine, SessionLocal, Base
from models import Table as Product
from schemas import UserCreate, UserResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)


# ✅ Create Product
@app.post("/product", response_model=UserResponse)
def create_product(product: UserCreate):
    db = SessionLocal()

    new_product = Product(
        product_name=product.product_name,
        product_cost=product.product_cost,
        quantity=product.quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    db.close()

    return new_product


# ✅ Get All Products
@app.get("/products", response_model=list[UserResponse])
def get_products():
    db = SessionLocal()

    products = db.query(Product).all()
    db.close()

    return products


# ✅ Get Product by ID
@app.get("/product/{id}", response_model=UserResponse)
def get_product(id: int):
    db = SessionLocal()

    db_product = db.query(Product).filter(Product.id == id).first()
    db.close()

    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    return db_product

@app.get("/")
def home():
    return {"message": "API is running"}