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
    main        = Column('main',String(50), nullable=True)
    date_50     = Column('50', String(50), nullable=True)
    date_100    = Column('100',String(50), nullable=True)
    date_200    = Column('200',String(50), nullable=True)
    date_300    = Column('300',String(50), nullable=True)
    date_400    = Column('400',String(50), nullable=True)
    date_500    = Column('500',String(50), nullable=True)
    date_600    = Column('600',String(50), nullable=True)
    date_700    = Column('700',String(50), nullable=True)
    date_800    = Column('800',String(50), nullable=True)
    date_900    = Column('900',String(50), nullable=True)
    created_at  = Column(DateTime, default=datetime.datetime.now)
    updated_at  = Column(DateTime, onupdate=datetime.datetime.now)
    default     = Column(String(50), nullable=True)
    paper       = Column(String(50), nullable=True)
    primary     = Column(String(50), nullable=True)
    secondary   = Column(String(50), nullable=True)
    # prueba = Column('900', String(50), nullable=True)

