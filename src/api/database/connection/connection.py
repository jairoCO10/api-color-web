from sqlalchemy.ext.declarative import declarative_base
from ..database import Database
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status 

Base = declarative_base()

class Connection:

    def get_db():
        db = Database.sessionlocal()
        try:
            yield db
        finally:
            db.close()

   