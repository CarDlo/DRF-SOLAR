from rest_framework import serializers
from .models import Plant, Signs

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', ]

class SignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signs
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', ]