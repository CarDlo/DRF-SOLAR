from rest_framework import routers
from .api import PlantViewSet, SignalViewSet

routers = routers.DefaultRouter()

routers.register('api/plants', PlantViewSet, 'plants')
routers.register('api/signals', SignalViewSet, 'signals')

urlpatterns = routers.urls

