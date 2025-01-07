from plants.models import Plant, Signs
from rest_framework import viewsets
from .serializers import PlantSerializer, SignalSerializer

class PlantViewSet(viewsets.ModelViewSet):

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class SignalViewSet(viewsets.ModelViewSet):

    queryset = Signs.objects.all()
    serializer_class = SignalSerializer