from django.contrib import admin
from .models import Bayunca, LaVilla


# Register your models here.
class BayuncaAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Bayunca, BayuncaAdmin)

class LaVillaAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(LaVilla, LaVillaAdmin)