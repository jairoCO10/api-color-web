from ....database.models.ColorModels import Colors
from sqlalchemy import text, not_
from sqlalchemy.orm import Session, aliased
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

class ColorService:
    def get_colors_all(self, db:Session):
        colores = db.query(Colors).filter(Colors.state==1).all()
        return colores
    
    def get_color_by_id(self, id:int, db:Session):
        color = db.query(Colors).filter(Colors.id== id).first()
        return color

    


