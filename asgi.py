"""
ASGI config for waitx project.
"""

import os
import sys

# Añadir el directorio del proyecto al PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Añadir el directorio waitx al PYTHONPATH para encontrar api
waitx_dir = os.path.join(current_dir, 'waitx')
sys.path.insert(0, waitx_dir)

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_asgi_application() 