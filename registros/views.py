from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bayunca, LaVilla
from .serializers import BayuncaSerializer, LaVillaSerializer
from .filters import BayuncaFilter, LaVillaFilter
from registros.services.client_manager import (
    start_client,
    stop_client,
    restart_client,
    get_status,
    start_all_clients,
    stop_all_clients,
    restart_all_clients
)


class BayuncaViewSet(viewsets.ModelViewSet):
    queryset = Bayunca.objects.all()
    serializer_class = BayuncaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BayuncaFilter

class LaVillaViewSet(viewsets.ModelViewSet):
    queryset = LaVilla.objects.all()
    serializer_class = LaVillaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LaVillaFilter


#Manejo de rutas para el manejo de los clientes
@api_view(['GET'])
def start_client_api(request, plant_name):
    """
    Inicia un cliente para una planta específica.
    """
    result = start_client(plant_name)
    return Response(result)


@api_view(['GET'])
def stop_client_api(request, plant_name):
    """
    Detiene un cliente activo para una planta específica.
    """
    result = stop_client(plant_name)
    return Response(result)


@api_view(['GET'])
def restart_client_api(request, plant_name):
    """
    Reinicia un cliente activo para una planta específica.
    """
    result = restart_client(plant_name)
    return Response(result)


@api_view(['GET'])
def get_status_api(request):
    """
    Obtiene el estado actual de los clientes activos.
    """
    result = get_status()
    return Response(result)


@api_view(['GET'])
def start_all_clients_api(request):
    """
    Inicia todos los clientes disponibles basándose en la configuración.
    """
    result = start_all_clients()
    return Response(result)


@api_view(['GET'])
def stop_all_clients_api(request):
    """
    Detiene todos los clientes actualmente activos.
    """
    result = stop_all_clients()
    return Response(result)


@api_view(['GET'])
def restart_all_clients_api(request):
    """
    Reinicia todos los clientes actualmente activos.
    """
    result = restart_all_clients()
    return Response(result)