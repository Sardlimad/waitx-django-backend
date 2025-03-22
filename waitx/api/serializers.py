from rest_framework import serializers
from .models import Cliente, Localidad, Ruta, Salida, Inscripcion, DetallesPriorizacion, Fallo

# 📌 Serializador Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

# 📌 Serializador Localidad
class LocalidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidad
        fields = '__all__'

# 📌 Serializador Ruta
class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

# 📌 Serializador Salida
class SalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salida
        fields = '__all__'

# 📌 Serializador Inscripción
class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = '__all__'

# 📌 Serializador Detalles Priorización
class DetallesPriorizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallesPriorizacion
        fields = '__all__'

# 📌 Serializador Fallo
class FalloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fallo
        fields = '__all__'