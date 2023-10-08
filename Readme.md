# API-colors

API de Colores para Sitio Web

Esta api está diseñada para usar de manera dinámica los colores para un sitio web

## Tecnologías Utilizadas

- **FastAPI**: Framework web moderno y rápido para construir APIs con Python 3.6+.
- **SQLAlchemy**: Biblioteca de SQL para Python.
- **Docker**: Plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores.
- **Alembic**: Herramienta para manejar migraciones de bases de datos SQL.

## Requisitos

- Python 3.9+
- Docker

## Configuración del Proyecto

1. **Clonar el Repositorio:**
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd api-colores-sitio-web
    ```
2. **Instalar Dependencias:**
    ## Nota
    Si no deseas ejecutar docker puedes usar el entorno de desarrollo de python el cual puedes crear de la siguiente manera
    * Si virtualenv no esta instalado

    ```sh
        pip install virtualenv
    ```

    * cuando la libreria instalada  ejecutar

    ```sh
    python -m virtualenv env
    ```
    luego entrar al entorno virtual de acuerdo al SO que tenga

    ```sh
    pip install -r requirements.txt
    ```

2.1. **Configurar la Base de Datos:**
    - Configura las credenciales y la URL de conexión a la base de datos en `src/api/database/settings/settings.py`.
    - Ejecuta las migraciones con Alembic para inicializar la base de datos:
        ```sh
        alembic revision --autogenerate -m "Adding Tables" && alembic upgrade head
        ```

3. **Ejecutar la Aplicación:**
    * Si usa el entorno virtual de python
    ```sh
    python main.py
    ```
    * Si usara docker 
    ```sh
    docker compose up
    ```



4. **Acceder a la Documentación de la API:**
    Abre un navegador y visita `http://localhost:8000/docs` para acceder a la documentación interactiva de la API generada automáticamente por FastAPI.

## Uso de la API
`http://localhost:8095/api/data-resoucer/` url para ver la respuesta

Mediante esta  peticion recibiras esta respuesta en el caso de que ya tengas los registros en la Base de datos

## Respuesta de la api 
```json
    {
        "primary": {
            "main": "#0000c6",
            "date_50": "#efe7fc",
            "date_100": "#d5c4f6",
            "date_200": "#b99cf1",
            "date_300": "#9c71ed",
            "date_400": "#8450e9",
            "date_500": "#6b2ce3",
            "date_600": "#5f27dd",
            "date_700": "#4e1ed4",
            "date_800": "#3b17ce"
        },
        "secondary": {
        ...
            "date_900": "#867300"
        },
        "text": {
            "primary": "#0000c6",
            "secondary": "#0094fa"
        },
        "error": {
        ...
        },
        "success": {
        ...
        },
        "warning": {
        ...
        },
        "info": {
            ...
        },
        "background": {
            "default": "#fbfbfb",
            "paper": "#fff"
        }
    }
```

## Contribución

Si quieres contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama con tu característica o corrección de errores: `git checkout -b mi-caracteristica`.
3. Haz commit de tus cambios: `git commit -m "Añadir nueva característica"`.
4. Sube tus cambios a tu fork: `git push origin mi-caracteristica`.
5. Crea un pull request en GitHub.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

Este es un ejemplo básico y puedes expandirlo según las necesidades específicas de tu proyecto. Asegúrate de incluir información importante como cómo configurar el entorno, cómo ejecutar pruebas, cómo contribuir y cualquier otra información relevante para los desarrolladores que quieran utilizar o colaborar en tu proyecto.