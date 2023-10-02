from django.db import models


# Create your models here.

class Requisito(models.Model):
    temperatura = models.DecimalField(max_digits=5, decimal_places=2)
    humedad = models.DecimalField(max_digits=3, decimal_places=2)
    MAGNITUDES_TERRENO = [('extenso', 'Extenso'), ('casero', 'Casero')]
    magnitud_terreno = models.CharField(max_length=10, choices=MAGNITUDES_TERRENO)
    ph_suelo = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad_riego = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'requisitos'

# TODO: Modelos dependientes por definir
