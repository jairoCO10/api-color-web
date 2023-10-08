from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from src.api.database.settings.middleware.middleware import add_middleware, authentication_middleware
import uvicorn
from src.api.apps.main import RunRouter


version = "1.2"
app = FastAPI(version=version)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)

# Configurar CORS y Gzip
origins = ["*"]  # Puedes especificar los orígenes permitidos en lugar de "*"
app = add_middleware(app, origins)  # Agregar middlewares de CORS, GZip y personalizados
# Middleware de autenticación (se ejecuta antes de cada solicitud)
app.middleware("http")(authentication_middleware)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Define tus rutas debajo de esta línea
@app.get("/")
async def read_root(request: Request):
    # Acceder a datos de usuario autenticado almacenados en request.state (si está configurado en los middlewares)
    user_id = request.state.user_id if hasattr(request.state, "user_id") else None
    return {"message": f"Hello, user {user_id}!"}

# Manejadores de excepciones personalizados
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append( 
            {
                "loc": error["loc"],
                "msg": error["msg"],
                "type": error["type"],
            }
        )
    return JSONResponse(status_code=HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": errors})

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    # Personaliza el manejo de excepciones para obtener información detallada
    return JSONResponse(status_code=500, content={"detail": "Ha ocurrido un error inesperado"})


app.include_router(RunRouter)