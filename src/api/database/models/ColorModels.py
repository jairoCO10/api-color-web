from enum import unique
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float
import datetime
from ..connection.connection import Base
from sqlalchemy.ext.mutable import MutableList

class Colors(Base):
    __tablename__ ="colores"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=True)
    state = Column(Integer, nullable=True, default=1) 
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

