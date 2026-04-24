
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

username = "root"
password = "Password1%40"
database = "d1"

engine = create_engine(f"mysql+pymysql://{username}:{password}@localhost/{database}")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
