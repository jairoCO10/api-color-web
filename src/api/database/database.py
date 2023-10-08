from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.api.database.settings.settings import Setting

class Database:
    SQLALCHEMY_DATABASE_URL = Setting.DATABASE_URL
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)