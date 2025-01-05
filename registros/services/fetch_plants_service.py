# plant/services/fetch_plants_service.py
from plants.models import Plant  # Corregido el import

def fetch_plants():
    """
    Obtiene la lista de plantas activas directamente desde el modelo Plant.
    """
    try:
        plants = Plant.objects.filter(active=True)
        return plants
    except Exception as e:
        print(f"Error al obtener las plantas desde la tabla Plant: {e}")
        return []
