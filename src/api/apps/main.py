from fastapi import APIRouter
from .colors.routers.ColorRouter import ColorRouter


RunRouter = APIRouter(prefix='/api')

RunRouter.include_router(ColorRouter)
