#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Asegurando permisos de ejecución..."
chmod +x manage.py

echo "Configurando PYTHONPATH..."
# Añadir directorio actual al PYTHONPATH
export PYTHONPATH=$PYTHONPATH:$(pwd)
# Añadir directorio waitx al PYTHONPATH para encontrar api
export PYTHONPATH=$PYTHONPATH:$(pwd)/waitx
export DJANGO_SETTINGS_MODULE=settings

echo "Mostrando PYTHONPATH..."
echo $PYTHONPATH

echo "Recolectando archivos estáticos..."
python manage.py collectstatic --no-input

echo "Aplicando migraciones..."
python manage.py migrate

echo "Build completado con éxito!" 