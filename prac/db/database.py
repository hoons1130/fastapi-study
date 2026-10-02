from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABSE_URL = ""

engine = create_engine(DATABSE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

Base = declarative_base()