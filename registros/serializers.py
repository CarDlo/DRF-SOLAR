# registros/serializers.py
from rest_framework import serializers
from .models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class BayuncaSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Bayunca
        fields = '__all__'

class BayuncaPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = Bayunca
        fields = '__all__'

class LaVillaSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = LaVilla
        fields = '__all__'

class LaVillaPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = LaVilla
        fields = '__all__'

class OldtSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Oldt
        fields = '__all__'

class OldtPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = Oldt
        fields = '__all__'

class SolchacrasSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Solchacras
        fields = '__all__'

class SolchacrasPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = Solchacras
        fields = '__all__'

class SolsantonioSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Solsantonio
        fields = '__all__'

class SolsantonioPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = Solsantonio
        fields = '__all__'

class SolhuaquiSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Solhuaqui
        fields = '__all__'

class SolhuaquiPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = Solhuaqui
        fields = '__all__'

class SanpedroSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Sanpedro
        fields = '__all__'

class SanpedroPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = Sanpedro
        fields = '__all__'

class GonzaenergySerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Gonzaenergy
        fields = '__all__'

class GonzaenergyPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = Gonzaenergy
        fields = '__all__'

class ProdulestiSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Produlesti
        fields = '__all__'

class ProdulestiPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = Produlesti
        fields = '__all__'

class GeneralSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = General
        fields = '__all__'

class GeneralPromedioSerializer(serializers.Serializer):
    fecha_dia = serializers.DateField()
    promedio_valor = serializers.FloatField()
    class Meta(RegistroSerializer.Meta):
        model = General
        fields = '__all__'

class ClientControlSerializer(serializers.Serializer):
    message = serializers.CharField(help_text="Mensaje informativo sobre el resultado de la operación.")
    success = serializers.BooleanField(help_text="Indica si la operación fue exitosa.")