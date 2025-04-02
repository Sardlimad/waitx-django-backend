from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from .models import Cliente, Localidad, Ruta, Salida, Inscripcion, DetallesPriorizacion, Fallo
from .serializers import (
    ClienteSerializer,
    LocalidadSerializer,
    RutaSerializer,
    SalidaSerializer,
    InscripcionSerializer,
    DetallesPriorizacionSerializer,
    FalloSerializer,
    UserRegistrationSerializer,
    ChangePasswordSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
)

User = get_user_model()

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

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if not user.check_password(serializer.data.get('old_password')):
                return Response(
                    {"old_password": "Contraseña incorrecta"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response(
                {"message": "Contraseña actualizada correctamente"},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                # Generar token
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                
                # Crear URL de reset
                reset_url = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}/"
                
                # Enviar email
                send_mail(
                    'Restablecer Contraseña',
                    f'Para restablecer tu contraseña, haz clic en el siguiente enlace: {reset_url}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                
                return Response(
                    {"message": "Se ha enviado un enlace para restablecer tu contraseña"},
                    status=status.HTTP_200_OK
                )
            except User.DoesNotExist:
                return Response(
                    {"email": "No existe un usuario con este email"},
                    status=status.HTTP_404_NOT_FOUND
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = ResetPasswordSerializer

    def post(self, request, uidb64, token):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                uid = force_str(urlsafe_base64_decode(uidb64))
                user = User.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                user = None

            if user is not None and default_token_generator.check_token(user, token):
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response(
                    {"message": "Contraseña restablecida correctamente"},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "El enlace de restablecimiento de contraseña es inválido"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
