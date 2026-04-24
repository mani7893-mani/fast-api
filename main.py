from fastapi import FastAPI, HTTPException
from database import engine, SessionLocal, Base
from models import User
from schemas import UserCreate, UserResponse

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    db = SessionLocal()

    new_user = User(name=user.name, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()
    return new_user

@app.get("/users", response_model=list[UserResponse])
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users
@app.get("/users/{id}", response_model=UserResponse)
def get_user(id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == id).first()
    db.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
@app.get("/")
def home():
    return {"message": "API is running"}
