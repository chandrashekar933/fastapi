import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine("mysql+mysqlconnector://root:chandu%4014@localhost:3306/fastapi")

SessionLocal = sessionmaker(bind=engine, autoflush=False)