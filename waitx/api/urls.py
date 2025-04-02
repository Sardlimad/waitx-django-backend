from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    ClienteViewSet, 
    LocalidadViewSet, 
    RutaViewSet, 
    SalidaViewSet, 
    InscripcionViewSet, 
    DetallesPriorizacionViewSet, 
    FalloViewSet,
    UserRegistrationView,
    ChangePasswordView,
    ForgotPasswordView,
    ResetPasswordView,
)

# 📌 Configurar el router de DRF
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'localidades', LocalidadViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'salidas', SalidaViewSet)
router.register(r'inscripciones', InscripcionViewSet)
router.register(r'detalles_priorizacion', DetallesPriorizacionViewSet)
router.register(r'fallos', FalloViewSet)

# 📌 URLs de autenticación
auth_urls = [
    # Registro de usuario
    path('auth/register/', UserRegistrationView.as_view(), name='user-register'),
    
    # Login y gestión de tokens
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Gestión de contraseñas
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('auth/forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('auth/reset-password/<str:token>/', ResetPasswordView.as_view(), name='reset-password'),
]

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las rutas generadas por el router
    path('', include(auth_urls)),     # Incluye las rutas de autenticación
]
