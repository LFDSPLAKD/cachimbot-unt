#!/bin/bash
# Instalar todas las dependencias desde requirements.txt
pip install -r requirements.txt

# Configurar Flask para que se ejecute correctamente
export FLASK_APP=app.py

# Ejecutar la aplicación Flask
flask run --host=0.0.0.0 --port=10000
