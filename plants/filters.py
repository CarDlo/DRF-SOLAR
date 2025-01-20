import django_filters
from .models import Signs

class SignsFilter(django_filters.FilterSet):
    plant_id = django_filters.NumberFilter(field_name='plant_id', help_text="ID de la planta")
    reg_ca = django_filters.CharFilter(field_name='reg_ca', help_text="Número de registro utilizado para identificar la variable medida. En Modbus es la dirección de inicio (Start Address) y en IEC104 es la dirección común del objeto (Common Address).")
    class Meta:
        model = Signs
        fields = ['plant_id', 'reg_ca']

