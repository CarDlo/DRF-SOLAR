from django.db import models

# Create your models here.
class Plant(models.Model):
    """
    Modelo que representa la configuración de una planta fotovoltaica. Almacena información básica como nombre, ubicación y potencia, así como la configuración del protocolo de comunicación utilizado para la captura de datos (MODBUS o IEC104). Incluye parámetros de conexión y autenticación, además de opciones avanzadas de configuración en el campo `metadata`.
    """

    PROTOCOLO_CHOICES = [
        ('IEC104', 'IEC104'),
        ('MODBUS', 'MODBUS'),
    ]

    name = models.CharField(max_length=255, help_text="Nombre descriptivo de la planta fotovoltaica.")
    province = models.CharField(max_length=255, help_text="Provincia o región donde está ubicada la planta.")
    country = models.CharField(max_length=255, help_text="País donde se encuentra la planta.")
    potencia_dc = models.FloatField(help_text="Potencia en corriente directa (DC) de la planta, expresada en MW.")
    scada = models.CharField(max_length=255, null=True, blank=True, help_text="Sistema SCADA utilizado para supervisión.")
    protocolo_comunicacion = models.CharField(
        max_length=10, choices=PROTOCOLO_CHOICES, help_text="Protocolo de comunicación utilizado (MODBUS o IEC104)."
    )
    ip = models.GenericIPAddressField(help_text="Dirección IP del sistema de control o SCADA de la planta.")
    puerto = models.PositiveIntegerField(help_text="Puerto de comunicación asociado al protocolo.")
    modelo = models.CharField(max_length=255, default="Bayunca1", help_text="Modelo dentro del backend que se usa para almacenar los registros.")
    credenciales = models.JSONField(null=True, blank=True, help_text="Credenciales para la autenticación en SCADA o API.")
    metadata = models.JSONField(
        null=True, blank=True,
        help_text=(
            "Información adicional en formato JSON. "
            "Para MODBUS: `start_address`, `max_registers`, `interval`. "
            "Para IEC104: `tick_rate_ms`, `command_timeout_ms`, `time_sender_sleep_ms`, `time_connect_ms`, `originator_address`."
        )
    )
    active = models.BooleanField(default=False, help_text="Indica si la planta está activa o inactiva.")

    class Meta:
        verbose_name = "Planta registrada"
        verbose_name_plural = "Plantas registradas"

    def __str__(self):
        return self.name
