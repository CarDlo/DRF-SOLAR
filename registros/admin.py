from django.contrib import admin
from .models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General


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

class OldtAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Oldt, OldtAdmin)

class SolchacrasAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Solchacras, SolchacrasAdmin)

class SolsantonioAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Solsantonio, SolsantonioAdmin)

class SolhuaquiAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Solhuaqui, SolhuaquiAdmin)

class SanpedroAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Sanpedro, SanpedroAdmin)

class GonzaenergyAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Gonzaenergy, GonzaenergyAdmin)

class ProdulestiAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(Produlesti, ProdulestiAdmin)

class GeneralAdmin(admin.ModelAdmin):
    fields = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    list_display = ('REG_CA', 'direccion', 'value', 'created_at', 'updated_at')
    search_fields = ('REG_CA', 'direccion')
    list_filter = ('created_at', 'updated_at')
admin.site.register(General, GeneralAdmin)
