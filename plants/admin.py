from django.contrib import admin
from .models import Plant, Signs


# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    fields = ('name', 'province', 'country', 'potencia_dc', 'scada', 'protocolo_comunicacion', 'ip', 'puerto', 'modelo', 'credenciales', 'metadata', 'active')
    list_display = ('name', 'province', 'country', 'potencia_dc', 'scada', 'protocolo_comunicacion', 'ip', 'puerto', 'modelo', 'credenciales', 'metadata', 'active')

admin.site.register(Plant, PlantAdmin)

class SignsAdmin(admin.ModelAdmin):
    fields = (
        'plant_id',
        'reg_ca',
        'direccion',
        'meta',
        'description',
        'object_type',
        'data_type',
        'scaler',
        'units',
        'inversor',
        'panel',
        'equip_sist',
        'min_value',
        'max_value',
        'protocolo',
        'metadata',
    )
    list_display = (
        'plant_id',
        'reg_ca',
        'direccion',
        'meta',
        'description',
        'scaler',
        'units',
        'inversor',
        'min_value',
        'max_value',
        'protocolo',
        'metadata',
        'created_at',
        'updated_at'
    )
    search_fields = ('plant_id', 'protocolo')

admin.site.register(Signs, SignsAdmin)