from enum import unique
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey,Text, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float
import datetime
from ..connection.connection import Base
from sqlalchemy.ext.mutable import MutableList

class Proyectos(Base):
    __tablename__ = "proyectos"
    id = Column(Integer, primary_key=True, index=True)
    nombre_proyecto = Column(String(100), nullable=True)
    descripcion_proyecto= Column(Text, nullable=True)
    desarrollador_back= Column(String(250), nullable=True)
    desaarrollador_front=Column(String(250), nullable=True)
    estado= Column(Integer)
    version= Column(String(200), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

