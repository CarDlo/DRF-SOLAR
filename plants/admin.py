from django.contrib import admin
from .models import Plant


# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    fields = ('name', 'province', 'country', 'potencia_dc', 'scada', 'protocolo_comunicacion', 'ip', 'puerto', 'modelo', 'credenciales', 'metadata', 'active')
    list_display = ('name', 'province', 'country', 'potencia_dc', 'scada', 'protocolo_comunicacion', 'ip', 'puerto', 'modelo', 'credenciales', 'metadata', 'active')

admin.site.register(Plant, PlantAdmin)