import uuid
from django.db import models

# 📌 Modelo Cliente
class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ci = models.CharField(max_length=11, unique=True)  # Carnet de identidad único
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.ci})"

# 📌 Modelo Localidad
class Localidad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 📌 Modelo Ruta
class Ruta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=50, unique=True)  # Código único de la ruta
    origen = models.ForeignKey(Localidad, related_name="rutas_origen", on_delete=models.CASCADE)
    destino = models.ForeignKey(Localidad, related_name="rutas_destino", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo}: {self.origen} -> {self.destino}"

# 📌 Modelo Salida (Fecha y Hora de Salida de una Ruta)
class Salida(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()  # Fecha y hora de salida

    def __str__(self):
        return f"Salida {self.ruta.codigo} - {self.fecha_hora}"

# 📌 Modelo Inscripción
class Inscripcion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vigente = models.BooleanField(default=True)  # Si la inscripción sigue válida

    def __str__(self):
        estado = "Vigente" if self.vigente else "No Vigente"
        return f"Inscripción {self.id} - {self.cliente} en {self.ruta.codigo} ({estado})"

# 📌 Modelo Detalles de Priorización
class DetallesPriorizacion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    causa = models.CharField(max_length=50)
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)

    def __str__(self):
        return f"Priorización {self.inscripcion.id}: {self.causa}"

# 📌 Modelo Fallo (Asignación de un Pasaje a un Cliente)
class Fallo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salida = models.ForeignKey(Salida, on_delete=models.CASCADE)
    asignado_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vigente = models.BooleanField(default=True)  # Si el fallo sigue válido

    def __str__(self):
        estado = "Vigente" if self.vigente else "No Vigente"
        return f"Fallo {self.id} - Cliente: {self.asignado_cliente} - {estado}"

