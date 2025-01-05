# registros/serializers.py
from rest_framework import serializers
from .models import Bayunca, LaVilla

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class BayuncaSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = Bayunca

class LaVillaSerializer(RegistroSerializer):
    class Meta(RegistroSerializer.Meta):
        model = LaVilla
