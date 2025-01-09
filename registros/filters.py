import django_filters
from django.db.models import Avg
from .models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General

class RegistroFilter(django_filters.FilterSet):
    startDate = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte', help_text="Formato: AAAA-MM-DD")
    endDate = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte', help_text="Formato: AAAA-MM-DD")
    REG_CA = django_filters.NumberFilter(field_name='REG_CA', help_text="Código de Registro MODBUS o Dirección Común IEC104")
    direccion = django_filters.NumberFilter(field_name='direccion', help_text="Dirección IOA de IEC104 o no aplica para MODBUS")
    promedio_diario = django_filters.BooleanFilter(method='filtrar_promedio_diario', help_text="True para calcular el promedio diario")
    muestreo = django_filters.NumberFilter(method='filtrar_muestreo', help_text="Especifica el intervalo de muestreo (e.g., 100 para 1 de cada 100 registros)")

    def filtrar_promedio_diario(self, queryset, name, value):
        if value:
            return queryset.values('created_at__date').annotate(promedio_valor=Avg('REG_CA'))
        return queryset

    def filtrar_muestreo(self, queryset, name, value):
        if value > 0:
            # Seleccionar 1 de cada 'value' registros
            return queryset.filter(id__mod=value == 0)
        return queryset

    class Meta:
        fields = ['startDate', 'endDate', 'REG_CA', 'direccion', 'promedio_diario', 'muestreo']


# Subclases para cada modelo
class BayuncaFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Bayunca

class LaVillaFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = LaVilla

class OldtFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Oldt

class SolchacrasFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Solchacras

class SolsantonioFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Solsantonio

class SolhuaquiFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Solhuaqui

class SanpedroFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Sanpedro

class GonzaenergyFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Gonzaenergy

class ProdulestiFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Produlesti

class GeneralFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = General
