#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos
python waitx/manage.py collectstatic --no-input

# Aplicar migraciones
python waitx/manage.py migrate 