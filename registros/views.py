from rest_framework import viewsets
import asyncio
from .mixins import LimitPaginationMixin
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General
from .serializers import (
    LaVillaPromedioSerializer, 
    BayuncaPromedioSerializer,
    OldtPromedioSerializer,
    SolchacrasPromedioSerializer,
    SolsantonioPromedioSerializer,
    SolhuaquiPromedioSerializer,
    SanpedroPromedioSerializer,
    GonzaenergyPromedioSerializer,
    ProdulestiPromedioSerializer,
    GeneralPromedioSerializer, 
    BayuncaSerializer, 
    LaVillaSerializer, 
    OldtSerializer, 
    SolchacrasSerializer, 
    SolsantonioSerializer, 
    SolhuaquiSerializer, 
    SanpedroSerializer, 
    GonzaenergySerializer, 
    ProdulestiSerializer, 
    GeneralSerializer,
    ClientControlSerializer
)
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

@extend_schema(tags=["Modelo Bayunca"])
class BayuncaViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = Bayunca.objects.all().order_by('id')
    serializer_class = BayuncaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = BayuncaFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return BayuncaPromedioSerializer
        return BayuncaSerializer

@extend_schema(tags=["Modelo La villa"])
class LaVillaViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = LaVilla.objects.all().order_by('id')
    serializer_class = LaVillaSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = LaVillaFilter
    ordering_fields = '__all__'
    #pagination_class = None
    #ordering = ['-created_at']


    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return LaVillaPromedioSerializer
        return LaVillaSerializer
    
    
@extend_schema(tags=["Modelo Oldt"])
class OldtViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = Oldt.objects.all().order_by('id')
    serializer_class = OldtSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = OldtFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return OldtPromedioSerializer
        return OldtSerializer

@extend_schema(tags=["Modelo Solchacras"])
class SolchacrasViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = Solchacras.objects.all().order_by('id')
    serializer_class = SolchacrasSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SolchacrasFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return SolchacrasPromedioSerializer
        return SolchacrasSerializer

@extend_schema(tags=["Modelo Solsantonio"])
class SolsantonioViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = Solsantonio.objects.all().order_by('id')
    serializer_class = SolsantonioSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SolsantonioFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return SolsantonioPromedioSerializer
        return SolsantonioSerializer

@extend_schema(tags=["Modelo Solhuaqui"])
class SolhuaquiViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = Solhuaqui.objects.all().order_by('id')
    serializer_class = SolhuaquiSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SolhuaquiFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self): 
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return SolhuaquiPromedioSerializer
        return SolhuaquiSerializer

@extend_schema(tags=["Modelo Sanpedro"])
class SanpedroViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = Sanpedro.objects.all().order_by('id')
    serializer_class = SanpedroSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = SanpedroFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return SanpedroPromedioSerializer
        return SanpedroSerializer

@extend_schema(tags=["Modelo Gonzaenergy"])
class GonzaenergyViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = Gonzaenergy.objects.all().order_by('id')
    serializer_class = GonzaenergySerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = GonzaenergyFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return GonzaenergyPromedioSerializer
        return GonzaenergySerializer

@extend_schema(tags=["Modelo Produlesti"])
class ProdulestiViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = Produlesti.objects.all().order_by('id')
    serializer_class = ProdulestiSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProdulestiFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return ProdulestiPromedioSerializer
        return ProdulestiSerializer

@extend_schema(tags=["Modelo General"])
class GeneralViewSet(LimitPaginationMixin, viewsets.ModelViewSet):
    queryset = General.objects.all().order_by('id')
    serializer_class = GeneralSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = GeneralFilter
    ordering_fields = '__all__'
    #ordering = ['created_at']  # Orden predeterminado
    def get_serializer_class(self):
        if getattr(self, 'request', None) and self.request.query_params.get('promedio_diario') == 'True':
            return GeneralPromedioSerializer
        return GeneralSerializer


#Manejo de rutas para el manejo de los clientes
@extend_schema(
     tags=["Control del cliente SCADA"],
     responses={200: ClientControlSerializer}
 )
@api_view(['GET'])
def start_client_api(request, plant_name):
    """
    Inicia un cliente para una planta específica.
    """
    result = start_client(plant_name)
    return Response({"message": result, "success": True})


@extend_schema(
    tags=["Control del cliente SCADA"],
    responses={200: ClientControlSerializer}
)
@api_view(['GET'])
def stop_client_api(request, plant_name):
    """
    Detiene un cliente activo para una planta específica.
    """
    result = stop_client(plant_name)
    return Response({"message": result, "success": True})


@extend_schema(
    tags=["Control del cliente SCADA"],
    responses={200: ClientControlSerializer}
)
@api_view(['GET'])
def restart_client_api(request, plant_name):
    """
    Reinicia un cliente activo para una planta específica.
    """
    result = restart_client(plant_name)
    return Response({"message": result, "success": True})


@extend_schema(
    tags=["Control del cliente SCADA"],
    responses={200: ClientControlSerializer}
)
@api_view(['GET'])
def get_status_api(request):
    """
    Obtiene el estado actual de los clientes activos.
    """
    result = get_status()
    return Response({"message": result, "success": True})


@extend_schema(
    tags=["Control del cliente SCADA"],
    responses={200: ClientControlSerializer}
)
@api_view(['GET'])
def start_all_clients_api(request):
    """
    Inicia todos los clientes disponibles basándose en la configuración.
    """
    result = start_all_clients()
    return Response({"message": result, "success": True})


@extend_schema(
    tags=["Control del cliente SCADA"],
    responses={200: ClientControlSerializer}
)
@api_view(['GET'])
def stop_all_clients_api(request):
    """
    Detiene todos los clientes actualmente activos.
    """
    result = stop_all_clients()
    return Response({"message": result, "success": True})


@extend_schema(
    tags=["Control del cliente SCADA"],
    responses={200: ClientControlSerializer}
)
@api_view(['GET'])
def restart_all_clients_api(request):
    """
    Reinicia todos los clientes actualmente activos.
    """
    result = restart_all_clients()
    return Response({"message": result, "success": True})