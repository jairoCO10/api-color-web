from enum import unique
from typing import TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, DateTime, Float
import datetime
from ..connection.connection import Base
from sqlalchemy.ext.mutable import MutableList

class DateColors(Base):
    __tablename__ = "tipo_color"
    id          = Column(Integer, primary_key=True, index=True)
    id_text     = Column(Integer, nullable=True, comment="Este campo hace alucion a los campos de colorModels")
    main        = Column(String(50), nullable=True)
    date_50     = Column(String(50), nullable=True)
    date_100    = Column(String(50), nullable=True)
    date_200    = Column(String(50), nullable=True)
    date_300    = Column(String(50), nullable=True)
    date_400    = Column(String(50), nullable=True)
    date_500    = Column(String(50), nullable=True)
    date_600    = Column(String(50), nullable=True)
    date_700    = Column(String(50), nullable=True)
    date_800    = Column(String(50), nullable=True)
    date_900    = Column(String(50), nullable=True)
    created_at  = Column(DateTime, default=datetime.datetime.now)
    updated_at  = Column(DateTime, onupdate=datetime.datetime.now)
    default     = Column(String(50), nullable=True)
    paper       = Column(String(50), nullable=True)
    primary     = Column(String(50), nullable=True)
    secondary   = Column(String(50), nullable=True)


