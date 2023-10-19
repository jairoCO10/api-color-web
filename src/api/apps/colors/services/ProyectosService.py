from ....database.models.ProyectosModel import Proyectos 
from sqlalchemy import text, not_
from sqlalchemy.orm import Session, aliased
from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError

class ProyectoService:
    def get_proyectos_all(self, db:Session):
        colores = db.query(Proyectos).filter(Proyectos.estado==1).all()
        return colores
    
    def get_proyectos_by_id(self, id:int, db:Session):
        color = db.query(Proyectos).filter(Proyectos.id== id).first()
        return color
    
    def agg_proyectos(self, data, db:Session):
        try:
            data_guardar=Proyectos(
                nombre_proyecto= data.nombre_proyecto,
                descripcion_proyecto= data.descripcion_proyecto,
                desarrollador_back= data.desarrollador_back,
                desaarrollador_front= data.desaarrollador_front,
                version= data.version
            )
            db.add(data_guardar)
            db.commit()
            db.refresh(data_guardar)

            return "registro Guardado con exito"
        
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail={
                    'message': "error",
                    'information': "Error creando los modulos",
                }  
            )

    


