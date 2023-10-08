from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware


async def custom_middleware(request: Request, call_next):
    # Código que se ejecuta antes de pasar la solicitud a las rutas
    print("Middleware se está ejecutando antes de la solicitud llegar a la ruta.")
    
    response = await call_next(request)  # Llama a la siguiente función en la cadena de middlewares
    
    # Código que se ejecuta después de que las rutas han manejado la solicitud
    print("Middleware se está ejecutando después de que las rutas han manejado la solicitud.")
    
    return response

# Middleware para Autenticación y Autorización (ejemplo básico)
async def authentication_middleware(request: Request, call_next):
    # Implementa tu lógica de autenticación aquí (por ejemplo, JWT)
    # Si la autenticación falla, puedes retornar una respuesta de error o lanzar una excepción
    # Usuario autenticado (por ejemplo, user_id) se puede almacenar en request.state para su posterior uso
    request.state.user_id = 123  # Ejemplo, reemplaza con la lógica real de autenticación
    response = await call_next(request)
    return response

async def authorization_middleware(request: Request, call_next):
    # Implementa tu lógica de autorización aquí (por ejemplo, verifica permisos basados en request.state.user_id)
    # Si la autorización falla, puedes retornar una respuesta de error o lanzar una excepción
    response = await call_next(request)
    return response

# Middleware para Logging
async def logging_middleware(request: Request, call_next):
    print(f"Solicitud recibida: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Respuesta enviada: {response.status_code}")
    return response

# Middleware para Validación de Datos (ejemplo básico)
async def validation_middleware(request: Request, call_next):
    # Implementa la lógica de validación de datos aquí (por ejemplo, verifica campos obligatorios)
    # Si la validación falla, puedes retornar una respuesta de error o lanzar una excepción
    response = await call_next(request)
    return response

# Middleware para Cache (ejemplo básico usando un diccionario como caché)
cache = {}

async def cache_middleware(request: Request, call_next):
    key = str(request.url)
    if key in cache:
        return cache[key]
    response = await call_next(request)
    cache[key] = response
    return response

# Middleware para Manipulación de Encabezados (ejemplo básico)
async def headers_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "Valor personalizado"
    return response

# Middleware para Manejo de Errores
async def error_handling_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        # Manejo de errores personalizado (por ejemplo, retornar una respuesta de error específica)
        return Response(content=f"Error: {str(e)}", status_code=500)



# Configurar la aplicación para usar el middleware CORS y Gzip
def add_middleware(app, origins):
    app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    app.add_middleware(GZipMiddleware)
    app.middleware("http")(custom_middleware)  # Agrega tu middleware personalizado
    return app
