FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /code

# Copia el archivo requirements.txt al contenedor
COPY ./requirements.txt /code/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia el resto del código al contenedor
COPY . /code

# Expone el puerto en el que Gunicorn escuchará
EXPOSE 80

CMD ["python", "main.py"]
# CMD ["gunicorn", " -k", "uvicorn.workers.UvicornWorker", "-c","gunicorn.py", "main:app"]
