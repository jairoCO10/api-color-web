from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os
import boto3
from .domains.mysql import MySql
from botocore.config import Config
from fastapi import Depends,HTTPException,status 


load_dotenv()

class Setting:
    
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM')
    
    SQL_DB=  MySql.SQL_DB
    SQL_USER= MySql.SQL_USER
    SQL_PASSWORD= MySql.SQL_PASSWORD
    
    SQL_SERVER= MySql.SQL_SERVER
    SQL_PORT=MySql.SQL_PORT

    SERVER_TYPE= MySql.SERVER_TYPE
    LIBRARY_SERVER= MySql.LIBRARY_SERVER
    
    SQLALCHEMY_DATABASE_URL = f"{SERVER_TYPE}+{LIBRARY_SERVER}://{SQL_USER}:{SQL_PASSWORD}@{SQL_SERVER}:{SQL_PORT}/{SQL_DB}"
  
    DATABASE_URL = SQLALCHEMY_DATABASE_URL
  

    engine = create_engine(DATABASE_URL)
 

    meta= MetaData()
    
    conn = engine.connect()
    
settings = Setting()
