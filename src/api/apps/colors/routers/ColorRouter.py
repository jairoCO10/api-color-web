from fastapi import APIRouter,status, Request, UploadFile, Form, File
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi.responses import JSONResponse
from ....utils.logger import CustomLogger
from ..controllers.ColorController import Color
from ....database.connection.connection import Connection
from sqlalchemy.orm import Session


ColorRouter = APIRouter(tags=['Colors'])
logger = CustomLogger('src/api/apps/Colors/logs/color.log')
message_log= "Se hizo una solicitud a la ruta"

@ColorRouter.get('/color')
async def get_color_all(db:Session=Depends(Connection.get_db)):
    data_color = Color()
    data = f"{message_log} /color. Data enviada: "
    colores =data_color.get_colors(db)
    logger.log(data)

    return colores


@ColorRouter.get('/color/{id}')
async def get_color_all(id:int, db:Session=Depends(Connection.get_db)):
    data_color = Color()
    data = f"{message_log} /color. Data enviada: {id}"
    color =data_color.get_color_by_id(id, db)
    logger.log(data)
    return color



@ColorRouter.get('/data-resoucer/')
async def get_color_all( db:Session=Depends(Connection.get_db)):
    data_color = Color()
    # data = f"{message_log} /color. Data enviada: "
    response =data_color.data_resource(db)
    # logger.log(data)
    return response


