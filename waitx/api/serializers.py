from rest_framework import serializers
from .models import Cliente, Localidad, Ruta, Salida, Inscripcion, DetallesPriorizacion, Fallo
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

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

# 📌 Serializador Ruta Básico (para relaciones anidadas)
class RutaBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = '__all__'

# 📌 Serializador Ruta Detallado
class RutaSerializer(serializers.ModelSerializer):
    # Incluir el nombre de la localidad de origen
    origen_nombre = serializers.CharField(source='origen.nombre', read_only=True)
    
    # Incluir el nombre de la localidad de destino
    destino_nombre = serializers.CharField(source='destino.nombre', read_only=True)
    
    class Meta:
        model = Ruta
        fields = ['id', 'codigo', 'origen', 'destino', 'origen_nombre', 'destino_nombre']

# 📌 Serializador Ruta con Datos Completos (opcional, para vistas detalladas)
class RutaDetailSerializer(serializers.ModelSerializer):
    origen = LocalidadSerializer(read_only=True)
    destino = LocalidadSerializer(read_only=True)
    
    class Meta:
        model = Ruta
        fields = '__all__'

# 📌 Serializador Salida
class SalidaSerializer(serializers.ModelSerializer):
    # Opcionalmente, incluir detalles de la ruta
    ruta_codigo = serializers.CharField(source='ruta.codigo', read_only=True)
    origen_nombre = serializers.CharField(source='ruta.origen.nombre', read_only=True)
    destino_nombre = serializers.CharField(source='ruta.destino.nombre', read_only=True)
    
    class Meta:
        model = Salida
        fields = ['id', 'ruta', 'fecha_hora', 'ruta_codigo', 'origen_nombre', 'destino_nombre']

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

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'email': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({"new_password": "Las contraseñas no coinciden"})
        return attrs

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password2 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError({"new_password": "Las contraseñas no coinciden"})
        return attrs