from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, LocalidadViewSet, RutaViewSet, SalidaViewSet, InscripcionViewSet, DetallesPriorizacionViewSet, FalloViewSet

# 📌 Configurar el router de DRF
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'localidades', LocalidadViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'salidas', SalidaViewSet)
router.register(r'inscripciones', InscripcionViewSet)
router.register(r'detalles_priorizacion', DetallesPriorizacionViewSet)
router.register(r'fallos', FalloViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las rutas generadas por el router
]
