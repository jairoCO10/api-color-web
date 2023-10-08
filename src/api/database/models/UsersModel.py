from enum import unique
from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float
import datetime
from ..connection.connection import Base
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer , primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=True)
    usuario= Column(String(255), nullable=True)
    password = Column('pass',String(255), nullable=True) # Especifica el nombre de la columna en la base de datos
    telefono = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    borrado = Column(Integer, nullable=True)

