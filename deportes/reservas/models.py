from django.db import models

# Create your models here.
class ActividadDeportiva(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    lugar = models.CharField(max_length=150)
    cupo = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} ({self.lugar}) - Cupo: {self.cupo}"


class Horario(models.Model):
    DIAS_SEMANA = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    actividad = models.ForeignKey(
        ActividadDeportiva, 
        on_delete=models.CASCADE, 
        related_name='horarios'
    )
    dia = models.CharField(max_length=20, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.actividad.nombre} - {self.dia} ({self.hora_inicio} a {self.hora_fin})"


class Inscripcion(models.Model):
    ESTADOS = [
        ('Activa', 'Activa'),
        ('Cancelada', 'Cancelada'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='Activa')
    horario = models.ForeignKey(
        Horario, 
        on_delete=models.CASCADE, 
        related_name='inscripciones'
    )

    def __str__(self):
        return f"{self.apellido}, {self.nombre} (DNI: {self.dni}) - {self.horario} [{self.estado}]"