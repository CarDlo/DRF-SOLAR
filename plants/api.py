from plants.models import Plant, Signs
from rest_framework import viewsets
from .serializers import PlantSerializer, SignalSerializer
from drf_spectacular.utils import extend_schema
#from .filters import SignsFilter
from django_filters.rest_framework import DjangoFilterBackend
#@extend_schema(tags=["Plantas"])
class PlantViewSet(viewsets.ModelViewSet):

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

#@extend_schema(tags=["Señales"])
class SignalViewSet(viewsets.ModelViewSet):

    queryset = Signs.objects.all()
    serializer_class = SignalSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['plant_id', 'reg_ca', 'created_at']
    #filterset_class = SignsFilter