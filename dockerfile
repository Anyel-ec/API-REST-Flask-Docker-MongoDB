FROM python:3.8

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias especificadas en el requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que Flask se ejecuta por defecto
EXPOSE 5000

# Comando para ejecutar la aplicación cuando el contenedor se inicia
CMD ["python", "app.py"]

