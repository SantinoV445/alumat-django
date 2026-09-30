from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=150)
    cuit = models.CharField(max_length=20, unique=True)
    direccion_fiscal = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.SET_NULL,
        db_column="id_empresa",
        related_name="clientes",
        null=True,
        blank=True,  # clientes particulares no tienen empresa
    )

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class OrdenVenta(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        db_column="id_cliente",
        related_name="ordenes_venta",
    )
    fecha_hora = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    saldo_pendiente = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_entrega_prometida = models.DateTimeField(null=True, blank=True)
    lugar_entrega = models.CharField(max_length=255, blank=True)
    notas_instalacion = models.TextField(blank=True)
    porcentaje_descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    porcentaje_con_descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0)


    def __str__(self):
        return f"Orden #{self.id_orden_venta} - {self.cliente}"
    
class Modelos(models.Model):
    orden_venta = models.ForeignKey(
        "OrdenVenta",
        on_delete=models.CASCADE,
        db_column="id_orden_venta",
        related_name="disenos",
    )
    tipo_apertura = models.CharField(max_length=100)
    estilo = models.CharField(max_length=100)
    vidrio = models.CharField(max_length=100)
    linea_accesorios = models.CharField(max_length=100)
    tapa_junta = models.CharField(max_length=100)
    revestimiento = models.CharField(max_length=100)
    marco = models.CharField(max_length=100)
    color_carpinteria = models.CharField(max_length=100)
    adicionales = models.CharField(max_length=255, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Diseño #{self.id_diseno} - Orden #{self.orden_venta_id}"