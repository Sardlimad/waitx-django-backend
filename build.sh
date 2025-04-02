#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Asegurando permisos de ejecución..."
chmod +x manage.py

echo "Configurando PYTHONPATH..."
export PYTHONPATH=$PYTHONPATH:$(pwd)
export DJANGO_SETTINGS_MODULE=waitx.waitx.settings

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --no-input

echo "Aplicando migraciones..."
python manage.py migrate

echo "Build completado con éxito!" 