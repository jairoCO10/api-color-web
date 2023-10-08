from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime


class ColorBase(BaseModel):
    title:str



class ColorCreate(ColorBase):
    pass


class ColorUpdate(ColorBase):
    pass


class ColorInDBBase(ColorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Color(ColorInDBBase):
    pass


class ColorInDB(ColorInDBBase):
    pass
