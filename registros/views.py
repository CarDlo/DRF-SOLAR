from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General
from .serializers import BayuncaSerializer, LaVillaSerializer, OldtSerializer, SolchacrasSerializer, SolsantonioSerializer, SolhuaquiSerializer, SanpedroSerializer, GonzaenergySerializer, ProdulestiSerializer, GeneralSerializer
from .filters import BayuncaFilter, LaVillaFilter, OldtFilter, SolchacrasFilter, SolsantonioFilter, SolhuaquiFilter, SanpedroFilter, GonzaenergyFilter, ProdulestiFilter, GeneralFilter
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

class OldtViewSet(viewsets.ModelViewSet):
    queryset = Oldt.objects.all()
    serializer_class = OldtSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OldtFilter

class SolchacrasViewSet(viewsets.ModelViewSet):
    queryset = Solchacras.objects.all()
    serializer_class = SolchacrasSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SolchacrasFilter

class SolsantonioViewSet(viewsets.ModelViewSet):
    queryset = Solsantonio.objects.all()
    serializer_class = SolsantonioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SolsantonioFilter

class SolhuaquiViewSet(viewsets.ModelViewSet):
    queryset = Solhuaqui.objects.all()
    serializer_class = SolhuaquiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SolhuaquiFilter

class SanpedroViewSet(viewsets.ModelViewSet):
    queryset = Sanpedro.objects.all()
    serializer_class = SanpedroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SanpedroFilter

class GonzaenergyViewSet(viewsets.ModelViewSet):
    queryset = Gonzaenergy.objects.all()
    serializer_class = GonzaenergySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GonzaenergyFilter

class ProdulestiViewSet(viewsets.ModelViewSet):
    queryset = Produlesti.objects.all()
    serializer_class = ProdulestiSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProdulestiFilter

class GeneralViewSet(viewsets.ModelViewSet):
    queryset = General.objects.all()
    serializer_class = GeneralSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GeneralFilter


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