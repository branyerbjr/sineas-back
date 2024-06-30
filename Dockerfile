# Usa una imagen base de Python 3.10 Alpine
FROM python:3.10-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el resto de los archivos al directorio de trabajo
COPY . .

# Excluir la carpeta .venv
RUN find /app -type d -name ".venv" -exec rm -rf {} +

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8000 (ajusta según sea necesario)
EXPOSE 8000

# Comando para iniciar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]