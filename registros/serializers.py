# registros/serializers.py
from rest_framework import serializers
from .models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class BayuncaSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Bayunca

class LaVillaSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = LaVilla

class OldtSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Oldt

class SolchacrasSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Solchacras

class SolsantonioSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Solsantonio

class SolhuaquiSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Solhuaqui

class SanpedroSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Sanpedro

class GonzaenergySerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Gonzaenergy

class ProdulestiSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Produlesti

class GeneralSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = General
