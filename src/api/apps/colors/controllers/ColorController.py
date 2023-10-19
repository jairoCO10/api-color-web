from ..services.ColorService import ColorService
from ....database.connection.connection import Connection
from sqlalchemy.orm import Session
from fastapi import Depends
from ..services.DataColorService import DataColorService
from ..services.ProyectosService import ProyectoService
colores_service = ColorService()
data_color = DataColorService()
data_proyecto = ProyectoService()

class Color:
    def get_colors(self, db):
        colores = colores_service.get_colors_all(db)
        response= []
        for color in colores:
            data_color={}
            data_color = procesar_color(color)
            response.append(data_color)
        return response

    def create_color(self, data):  # Debes pasar los datos del color a crear como argumento
        # Lógica para crear un nuevo color en la base de datos
        pass

    def get_color_by_id(self, id: int, db):
        color = colores_service.get_color_by_id(id, db)

        if not color:
            return None
        data_color={}
        data_color = procesar_color(color)
        return data_color
        
     
    def update_color(self, color_id: int, data, db):  # Debes pasar los datos del color a actualizar como argumento
        # Lógica para actualizar el color en la base de datos
        pass

    def delete_color_by_id(self, color_id: int, db):
        
        return colores_service.delete_color_by_id(db, color_id)
    
    def data_resource(self, db):
        data = {}
        colores = colores_service.get_colors_all(db)
        
        for response in colores:
            if response:
                id_text = response.id
                datacolores = data_color.get_data_color_all(id_text, db)  # Supongo que esta función existe y devuelve un diccionario
                for  color in datacolores:
                    # Asigna color_data a la clave específica en el diccionario data
                    data[f"{response.title}"] = procesar_data_color(color)
                       
        return data
    

    def get_proyecto(self, id_proyecto:int, db:Session):

        data = {}
        response = data_proyecto.get_proyectos_by_id(id_proyecto, db)
        if not response:
            return None

        dat_proyecto = procesar_proyecto(response)
        data_colores = self.data_resource(db)  # Obtiene los datos de los colores usando data_resource
        dat_proyecto['colores'] = data_colores  # Asigna los datos de colores al diccionario del proyecto

        # Crea un diccionario para almacenar el resultado final
        result = {
            'proyecto': dat_proyecto,  # Puedes cambiar 'proyecto' por la clave que desees para el proyecto
        }
        return result


def data_procesada(campos, color):
    dataprocesada = {}
    for campo in campos:
        value = getattr(color, campo)
        if value is not None:
            dataprocesada[campo] = value
    return dataprocesada


def procesar_proyecto(proyecto):
    campos= ['id',"version",
                "nombre_proyecto","descripcion_proyecto", "estado",
            ]
    
    return data_procesada(campos, proyecto)




def procesar_color(color):
    campos = ['id', 'title']
    return data_procesada(campos, color)

def procesar_data_color(color):
    campos = ["main",
    "date_50","date_100", "date_200","date_300","date_400",
    "date_500","date_600","date_700","date_800","date_900",  "primary",
    "secondary", "default","paper"
    ]
    return data_procesada(campos, color)
