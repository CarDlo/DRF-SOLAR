from django.db import models
# registros/models.py


class Bayunca(models.Model):
    REG_CA = models.IntegerField(help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104 o registro MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Bayunca 1"
        verbose_name_plural = "Bayunca 1"

    def __str__(self):
        return f"Bayunca {self.id} - {self.REG_CA}"


class LaVilla(models.Model):
    REG_CA = models.IntegerField(help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104 o registro MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "La Villa"
        verbose_name_plural = "La Villa"

    def __str__(self):
        return f"LaVilla {self.id} - {self.REG_CA}"
