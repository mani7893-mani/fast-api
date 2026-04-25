
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database = os.getenv("DB_NAME")

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
