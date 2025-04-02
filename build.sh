#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Configurando PYTHONPATH..."
export PYTHONPATH=$PYTHONPATH:$(pwd)

echo "Recolectando archivos estáticos..."
cd waitx && python manage.py collectstatic --no-input

echo "Aplicando migraciones..."
python manage.py migrate

echo "Build completado con éxito!" 