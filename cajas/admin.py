from django.contrib import admin
from .models import Cajas,Cierre_Cajas,Apertura_cajas,Movimiento_Cajas

# Register your models here.
class CajasAdmin(admin.ModelAdmin):
    list_display = ("id","estado")

class Apertura_CajasAdmin(admin.ModelAdmin):
    list_display = ("fecha_apertura","monto_inicial","observaciones")

    
class Cierre_CajasAdmin(admin.ModelAdmin):
    list_display = ("fecha_cierre","monto_cierre_sistema","monto_fisico","observaciones")
    
class Movimientos_CajasAdmin(admin.ModelAdmin):
    list_display = ("fecha_hora","tipo_movimiento","categoria","concepto","monto","metodo_pago")
    
admin.site.register(Cajas, CajasAdmin)
admin.site.register(Cierre_Cajas, Cierre_CajasAdmin)
admin.site.register(Apertura_cajas, Apertura_CajasAdmin)
admin.site.register(Movimiento_Cajas, Movimientos_CajasAdmin)