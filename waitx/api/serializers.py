from rest_framework import serializers
from .models import InscripcionPriorizada

class InscripcionPriorizadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscripcionPriorizada
        fields = '__all__'