import django_filters
from django.db.models import Avg
from .models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General
from django.db.models import F
from django.db.models.functions import TruncDate

class RegistroFilter(django_filters.FilterSet):
    startDate = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte', help_text="Formato: AAAA-MM-DD")
    endDate = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte', help_text="Formato: AAAA-MM-DD")
    REG_CA = django_filters.NumberFilter(field_name='REG_CA', help_text="Código de Registro MODBUS o Dirección Común IEC104")
    direccion = django_filters.NumberFilter(field_name='direccion', help_text="Dirección IOA de IEC104 o no aplica para MODBUS")
    promedio_diario = django_filters.CharFilter(field_name='promedio_diario', method='filtrar_promedio_diario', help_text="True para calcular el promedio diario")
    muestreo = django_filters.NumberFilter(method='filtrar_muestreo', help_text="Especifica el intervalo de muestreo (e.g., 100 para 1 de cada 100 registros)")
    plant_id = django_filters.NumberFilter(field_name='plant_id', help_text="ID de la planta")
   # limit = django_filters.NumberFilter(method='filtrar_cantidad', help_text="Número máximo de registros a devolver")

    def filtrar_promedio_diario(self, queryset, name, value):
        if value and value.lower() == 'true':  # Asegúrate de que el valor sea 'true'
            # Aplicar el filtro REG_CA si está presente
            if 'REG_CA' in self.data:
                queryset = queryset.filter(REG_CA=self.data['REG_CA'])
            
            # Excluir registros con valor nulo y agrupar por día
            queryset = queryset.exclude(value__isnull=True).annotate(
                fecha_dia=TruncDate('created_at')
            ).values('fecha_dia').annotate(
                promedio_valor=Avg('value')
            ).order_by('fecha_dia')
            
            return queryset
        return queryset



    def filtrar_muestreo(self, queryset, name, value):
        if value > 0:
            # Utilizar annotate y filtro basado en el residuo
            return queryset.annotate(mod_result=F('id') % value).filter(mod_result=0)
        return queryset
    
    # def filtrar_cantidad(self, queryset, name, value):
    #     if value > 0:
    #         return queryset[:value]
    #     return queryset



    class Meta:
        abstract = True
        fields = ['startDate', 'endDate', 'REG_CA', 'direccion', 'promedio_diario', 'muestreo', 'plant_id']


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
