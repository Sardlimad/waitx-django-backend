#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Instalando dependencias..."
pip install -r requirements.txt

echo "Recolectando archivos estáticos..."
python -m waitx.manage collectstatic --no-input

echo "Aplicando migraciones..."
python -m waitx.manage migrate

echo "Build completado con éxito!" 