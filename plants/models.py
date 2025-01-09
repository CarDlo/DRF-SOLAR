from django.db import models
from django.utils import timezone
# Create your models here.
class Plant(models.Model):
    """
    Modelo que representa la configuración de una planta fotovoltaica. Almacena información básica como nombre, ubicación y potencia, así como la configuración del protocolo de comunicación utilizado para la captura de datos (MODBUS o IEC104). Incluye parámetros de conexión y autenticación, además de opciones avanzadas de configuración en el campo `metadata`.
    """

    PROTOCOLO_CHOICES = [
        ('IEC104', 'IEC104'),
        ('MODBUS', 'MODBUS'),
        ('MODBUS-REV', 'MODBUS-REV'),
    ]

    PLANT_CHOICES = [
        ('Bayunca1', 'Bayunca1'),
        ('LaVilla', 'LaVilla'),
        ('Oldt', 'Oldt'),
        ('Solchacras', 'Solchacras'),
        ('Solsantonio', 'Solsantonio'),
        ('Solhuaqui', 'Solhuaqui'),
        ('Sanpedro', 'Sanpedro'),
        ('Gonzaenergy', 'Gonzaenergy'),
        ('Produlesti', 'Produlesti'),
        ('General', 'General'),
    ]


    name = models.CharField(unique=True, max_length=15, help_text="Nombre descriptivo de la planta fotovoltaica.")
    province = models.CharField(max_length=255, help_text="Provincia o región donde está ubicada la planta.")
    country = models.CharField(max_length=255, help_text="País donde se encuentra la planta.")
    potencia_dc = models.FloatField(help_text="Potencia en corriente directa (DC) de la planta, expresada en MW.")
    scada = models.CharField(max_length=255, null=True, blank=True, help_text="Sistema SCADA utilizado para supervisión.")
    protocolo_comunicacion = models.CharField(
        max_length=10, choices=PROTOCOLO_CHOICES, help_text="Protocolo de comunicación utilizado (MODBUS o IEC104)."
    )
    ip = models.GenericIPAddressField(null=True, blank=True, help_text="Dirección IP del sistema de control o SCADA de la planta.")
    puerto = models.PositiveIntegerField(help_text="Puerto de comunicación asociado al protocolo.")
    modelo = models.CharField(max_length=11, choices=PLANT_CHOICES, default="General", help_text="Modelo dentro del backend que se usa para almacenar los registros.")
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
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")
    class Meta:
        verbose_name = "Planta registrada"
        verbose_name_plural = "Plantas registradas"

    def __str__(self):
        return self.name

class Signs(models.Model):
    PROTOCOLO_CHOICES = [
        ('IEC104', 'IEC104'),
        ('MODBUS', 'MODBUS'),
    ]

    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="signs", null=True, blank=True, help_text="Planta asociada a la señal registrada.")
    reg_ca = models.CharField(max_length=255, null=True, blank=True, help_text="Número de registro utilizado para identificar la variable medida. En Modbus es la dirección de inicio (Start Address) y en IEC104 es la dirección común del objeto (Common Address).")
    direccion = models.CharField(max_length=255, null=True, blank=True, help_text="Dirección asociada a la medición o registro, utilizada como identificador del punto de origen de los datos. En IEC104 es el Information Object Address (IOA). Puede ser nulo.")
    meta = models.CharField(max_length=255, null=True, blank=True, help_text="Etiqueta o nombre descriptivo del estado del dispositivo o variable monitoreada.")
    description = models.TextField(null=True, blank=True, help_text="Descripción textual del estado o variable monitoreada.")
    object_type = models.CharField(max_length=255, null=True, blank=True, help_text="Tipo de objeto o registro utilizado. En IEC104 puede ser valores como 'M_ME_NC_1'. No aplica para Modbus.")
    data_type = models.CharField(max_length=255, null=True, blank=True, help_text="Tipo de dato registrado, como 'Single' o 'Double'.")
    scaler = models.FloatField(null=True, blank=True, help_text="Factor de escala o conversión aplicado al valor medido.")
    units = models.CharField(max_length=255, null=True, blank=True, help_text="Unidades de medida del valor registrado.")
    inversor = models.CharField(max_length=255, null=True, blank=True, help_text="Identificación del inversor asociado al registro.")
    panel = models.CharField(max_length=255, null=True, blank=True, help_text="Nombre del panel o subgrupo de equipos al que está asociado el registro.")
    equip_sist = models.CharField(max_length=255, null=True, blank=True, help_text="Equipo o sistema específico relacionado con el registro de medición.")
    min_value = models.FloatField(null=True, blank=True, help_text="Valor mínimo permitido para la variable monitoreada.")
    max_value = models.FloatField(null=True, blank=True, help_text="Valor máximo permitido para la variable monitoreada.")
    protocolo = models.CharField(max_length=10, choices=PROTOCOLO_CHOICES, null=True, blank=True, help_text="Protocolo de comunicación utilizado para la transmisión de datos. Puede ser MODBUS o IEC104.")
    metadata = models.JSONField(null=True, blank=True, help_text="Metadatos adicionales del registro, utilizados para almacenar información extra sobre la medición. Aplica para Modbus e IEC104.")
    active = models.BooleanField(default=True, help_text="Indica si la señal está activa o inactiva, es decir si se registra en la base de datos o se ignora.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")
    class Meta:
        verbose_name = "Señal registrada"
        verbose_name_plural = "Señales registradas"

    def __str__(self):
        return f"{self.meta} ({self.protocolo})"
