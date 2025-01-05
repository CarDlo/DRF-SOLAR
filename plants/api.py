from plants.models import Plant
from rest_framework import viewsets, permissions
from .serializers import PlantSerializer
class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.AllowAny]