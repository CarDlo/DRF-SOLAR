# registros/filters.py
import django_filters
from .models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General

class RegistroFilter(django_filters.FilterSet):
    startDate = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte', help_text="Formato: AAAA-MM-DD")
    endDate = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte', help_text="Formato: AAAA-MM-DD")
    REG_CA = django_filters.NumberFilter(field_name='REG_CA', help_text="Código de Registro MODBUS o Dirección Común IEC104")
    direccion = django_filters.NumberFilter(field_name='direccion', help_text="Dirección IOA de IEC104 o no aplica para MODBUS")

    class Meta:
        fields = ['startDate', 'endDate', 'REG_CA', 'direccion']

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