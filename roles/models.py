from django.db import models

# Create your models here.
class Roles(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion_permisos = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"


class Usuarios(models.Model):
    rol = models.ForeignKey(Roles, on_delete= models.RESTRICT,related_name="Usuarios")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    contrasena_hash = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
