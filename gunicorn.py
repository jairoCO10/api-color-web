workers = 4  # Número de procesos de trabajo (ajústalo según la cantidad de CPU en tu servidor)
bind = "0.0.0.0:80"  # Dirección y puerto en los que Gunicorn debe escuchar
worker_class = "uvicorn.workers.UvicornWorker"  # Especifica el Worker Uvicorn
