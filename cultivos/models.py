from django.db import models
from django.contrib.auth.models import AbstractUser


class Requisito(models.Model):
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    humedad = models.DecimalField(max_digits=3, decimal_places=2)
    ph_suelo = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_riego = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'requisitos'


class Cuidado(models.Model):
    ESTADOS_CRECIMIENTO = [('Germinación', 'Germinación'), ('Crecimiento vegetativo', 'Crecimiento Vegetativo'), (
        'Fructificación', 'Fructificación'), ('Senescencia', 'Senescencia')]
    estado_crecimiento = models.CharField(max_length=50, choices=ESTADOS_CRECIMIENTO)
    descripcion = models.TextField()

    class Meta:
        db_table = 'cuidados'


class Cultivo(models.Model):
    nombre = models.CharField(max_length=50)
    TIPOS_ALIMENTO = [('Tubérculo', 'Tubérculo'), ('Fruta', 'Fruta'), ('Hortaliza', 'Hortaliza')]
    tipo_alimento = models.CharField(max_length=10, choices=TIPOS_ALIMENTO)
    TIPOS_PROPAGACION = [('Tallo', 'Tallo'), ('Semilla', 'Semilla')]
    tipo_propagacion = models.CharField(max_length=10, choices=TIPOS_PROPAGACION)
    requisito = models.ForeignKey(Requisito, on_delete=models.CASCADE)
    cuidado = models.ForeignKey(Cuidado, on_delete=models.CASCADE)

    class Meta:
        db_table = 'cultivos'


class Usuario(AbstractUser):
    cultivo = models.ForeignKey(Cultivo, on_delete=models.CASCADE)

    groups = models.ManyToManyField('auth.Group', related_name='usuarios', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='usuarios', blank=True)

    class Meta:
        db_table = 'usuarios'

