from django.db import models

from django.db import models

class InscripcionPriorizada(models.Model):
    ci_cliente = models.CharField(max_length=11, unique=True)  # Carnet de identidad
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ruta = models.CharField(max_length=50)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.ruta}"

