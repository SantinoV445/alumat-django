from django.db import models

# Create your models here.
class Cajas(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.Pointfield()