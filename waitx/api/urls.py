from django.urls import path
from .views import InscripcionPriorizadaListCreate

urlpatterns = [
    path('inscripciones/', InscripcionPriorizadaListCreate.as_view(), name='inscripciones'),
]