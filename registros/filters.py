# registros/filters.py
import django_filters
from .models import Bayunca, LaVilla

class RegistroFilter(django_filters.FilterSet):
    startDate = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte', help_text="Formato: AAAA-MM-DD")
    endDate = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte', help_text="Formato: AAAA-MM-DD")
    REG_CA = django_filters.NumberFilter(field_name='REG_CA', help_text="Código de Registro MODBUS o Dirección Común IEC104")
    direccion = django_filters.NumberFilter(field_name='direccion', help_text="Dirección IOA de IEC104 o registro MODBUS")

    class Meta:
        fields = ['startDate', 'endDate', 'REG_CA', 'direccion']

class BayuncaFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = Bayunca

class LaVillaFilter(RegistroFilter):
    class Meta(RegistroFilter.Meta):
        model = LaVilla
