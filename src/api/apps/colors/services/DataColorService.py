from ....database.models.dateColorsModel import DateColors
from sqlalchemy import text, not_
from sqlalchemy.orm import Session, aliased
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

class DataColorService:
    def get_data_color_all(self, id_text, db:Session):
        colores = db.query(DateColors).filter(DateColors.id_text==id_text).all()
        return colores
    
    def get_data_color_by_id(self, id:int, db:Session):
        color = db.query(DateColors).filter(DateColors.id_text==id).first()
        return color

    


