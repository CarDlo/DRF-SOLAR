# registros/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BayuncaViewSet, LaVillaViewSet, OldtViewSet, SolchacrasViewSet, SolsantonioViewSet, SolhuaquiViewSet, SanpedroViewSet, GonzaenergyViewSet, ProdulestiViewSet, GeneralViewSet
from django.urls import path
from .views import (
    start_client_api,
    stop_client_api,
    restart_client_api,
    get_status_api,
    start_all_clients_api,
    stop_all_clients_api,
    restart_all_clients_api
)
router = DefaultRouter()
router.register(r'bayunca', BayuncaViewSet, basename='bayunca')
router.register(r'lavilla', LaVillaViewSet, basename='lavilla')
router.register(r'oldt', OldtViewSet, basename='oldt')
router.register(r'solchacras', SolchacrasViewSet, basename='solchacras')
router.register(r'solsantonio', SolsantonioViewSet, basename='solsantonio')
router.register(r'solhuaqui', SolhuaquiViewSet, basename='solhuaqui')
router.register(r'sanpedro', SanpedroViewSet, basename='sanpedro')
router.register(r'gonzaenergy', GonzaenergyViewSet, basename='gonzaenergy')
router.register(r'produlesti', ProdulestiViewSet, basename='produlesti')
router.register(r'general', GeneralViewSet, basename='general')

urlpatterns = [
    path('', include(router.urls)),
    #Manejo de rutas para el manejo de los clientes
    path('client/start/<str:plant_name>/', start_client_api, name="start_client"),
    path('client/stop/<str:plant_name>/', stop_client_api, name="stop_client"),
    path('client/restart/<str:plant_name>/', restart_client_api, name="restart_client"),
    path('client/status/', get_status_api, name="get_status"),
    path('client/start-all/', start_all_clients_api, name="start_all_clients"),
    path('client/stop-all/', stop_all_clients_api, name="stop_all_clients"),
    path('client/restart-all/', restart_all_clients_api, name="restart_all_clients"),
]
