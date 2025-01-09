from django.db import models
from plants.models import Plant
# registros/models.py


class Bayunca(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="bayunca_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Bayunca 1"
        verbose_name_plural = "Bayunca 1"

    def __str__(self):
        return f"Bayunca {self.id} - {self.REG_CA}"


class LaVilla(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="lavilla_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "La Villa"
        verbose_name_plural = "La Villa"

    def __str__(self):
        return f"LaVilla {self.id} - {self.REG_CA}"


########
class Oldt(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="oldt_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Oldt"
        verbose_name_plural = "Oldt"

    def __str__(self):
        return f"Oldt {self.id} - {self.REG_CA}"


class Solchacras(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="solchacras_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Solchacras"
        verbose_name_plural = "Solchacras"

    def __str__(self):
        return f"Solchacras {self.id} - {self.REG_CA}"


class Solsantonio(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="solsantonio_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Solsantonio"
        verbose_name_plural = "Solsantonio"

    def __str__(self):
        return f"Solsantonio {self.id} - {self.REG_CA}"


class Solhuaqui(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="solhuaqui_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Solhuaqui"
        verbose_name_plural = "Solhuaqui"

    def __str__(self):
        return f"Solhuaqui {self.id} - {self.REG_CA}"


class Sanpedro(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="sanpedro_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Sanpedro"
        verbose_name_plural = "Sanpedro"

    def __str__(self):
        return f"Sanpedro {self.id} - {self.REG_CA}"


class Gonzaenergy(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="gonzaenergy_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Gonzaenergy"
        verbose_name_plural = "Gonzaenergy"

    def __str__(self):
        return f"Gonzaenergy {self.id} - {self.REG_CA}"

class Produlesti(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="produlesti_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "Produlesti"
        verbose_name_plural = "Produlesti"

    def __str__(self):
        return f"Produlesti {self.id} - {self.REG_CA}"
    
class General(models.Model):
    REG_CA = models.IntegerField(db_index=True, help_text="Código de Registro MODBUS o Dirección Común IEC104.")
    value = models.FloatField(help_text="Valor medido o capturado del registro.")
    direccion = models.IntegerField(null=True, blank=True, help_text="Dirección IOA de IEC104, no se usa en MODBUS.")
    metadata = models.JSONField(null=True, blank=True, help_text="Información adicional en formato JSON.")
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE, related_name="general_values", null=True, blank=True, help_text="Planta asociada al valor registrado.")
    created_at = models.DateTimeField(db_index=True, auto_now_add=True, help_text="Fecha y hora en que se creó el registro.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha y hora de la última actualización del registro.")

    class Meta:
        verbose_name = "General"
        verbose_name_plural = "General"

    def __str__(self):
        return f"General {self.id} - {self.REG_CA}"