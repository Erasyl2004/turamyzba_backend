from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv('./.env')

URL_DATABASE = os.getenv('DB_URL')

engine = create_engine(URL_DATABASE)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#Dependency
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()