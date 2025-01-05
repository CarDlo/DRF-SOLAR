from rest_framework import routers
from .api import PlantViewSet

routers = routers.DefaultRouter()

routers.register('api/plants', PlantViewSet, 'plants')

urlpatterns = routers.urls

