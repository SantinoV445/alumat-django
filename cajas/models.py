from django.db import models


# Create your models here.
class Cajas(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=50, )
    
    def __str__(self):
        return f"{self.nombre}"
            
class Apertura_cajas(models.Model):
    caja = models.ForeignKey(Cajas, on_delete= models.RESTRICT ,related_name= "Apertura_caja")
    fecha_apertura = models.DateTimeField(auto_now_add=True)
    monto_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.fecha_apertura}"
    
class Cierre_Cajas(models.Model):
    caja = models.ForeignKey(Cajas, on_delete= models.RESTRICT ,related_name= "Cierre_cajas")
    fecha_cierre = models.DateTimeField(auto_now_add=True)
    monto_cierre_sistema = models.DecimalField(max_digits=11, decimal_places=2)
    monto_fisico = models.DecimalField(max_digits=11, decimal_places=2)
    observaciones = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.caja} {self.fecha_cierre}"
    
class Movimiento_Cajas(models.Model):
    caja = models.ForeignKey(
        Cajas,
        on_delete= models.PROTECT,
        related_name="movimientos_Cajas")
    fecha_hora = models.DateTimeField(auto_now_add=True)
    tipo_movimiento = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    concepto = models.CharField(max_length=255)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)
    num_comprobante = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.tipo_movimiento}"