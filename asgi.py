"""
ASGI config for waitx project.
"""

import os
import sys

# Añadir el directorio raíz al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waitx.waitx.settings')

application = get_asgi_application() 