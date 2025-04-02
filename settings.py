"""
Importador de configuración para facilitar la importación en Render.
"""

import os
import sys

# Añadir el directorio waitx al PYTHONPATH para encontrar api
waitx_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'waitx')
sys.path.insert(0, waitx_dir)

# Importar la configuración real
from waitx.waitx.settings import * 