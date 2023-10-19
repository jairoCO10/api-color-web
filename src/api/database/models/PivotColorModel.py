from enum import unique
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float
import datetime
from ..connection.connection import Base
from sqlalchemy.ext.mutable import MutableList

class PivotColor(Base):
    __tablename__ = "pivot_color"
    id = Column(Integer, primary_key=True, index=True)
    id_proyecto=Column(Integer)
    id_color=Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)

