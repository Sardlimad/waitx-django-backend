from rest_framework import viewsets
from .models import Cliente, Localidad, Ruta, Salida, Inscripcion, DetallesPriorizacion, Fallo
from .serializers import ClienteSerializer, LocalidadSerializer, RutaSerializer, SalidaSerializer, InscripcionSerializer, DetallesPriorizacionSerializer, FalloSerializer

# 📌 Vista para Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# 📌 Vista para Localidad
class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer

# 📌 Vista para Ruta
class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    serializer_class = RutaSerializer

# 📌 Vista para Salida
class SalidaViewSet(viewsets.ModelViewSet):
    queryset = Salida.objects.all()
    serializer_class = SalidaSerializer

# 📌 Vista para Inscripción
class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

# 📌 Vista para Detalles Priorización
class DetallesPriorizacionViewSet(viewsets.ModelViewSet):
    queryset = DetallesPriorizacion.objects.all()
    serializer_class = DetallesPriorizacionSerializer

# 📌 Vista para Fallo
class FalloViewSet(viewsets.ModelViewSet):
    queryset = Fallo.objects.all()
    serializer_class = FalloSerializer
