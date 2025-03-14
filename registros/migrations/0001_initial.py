# Generated by Django 5.1.4 on 2025-01-04 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bayunca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REG_CA', models.IntegerField(help_text='MOD.REG(Modbus) o Common Address (IEC104)')),
                ('value', models.FloatField()),
                ('direccion', models.IntegerField(blank=True, help_text='IEC104 IOA o Modbus', null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LaVilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REG_CA', models.IntegerField(help_text='MOD.REG(Modbus) o Common Address (IEC104)')),
                ('value', models.FloatField()),
                ('direccion', models.IntegerField(blank=True, help_text='IEC104 IOA o Modbus', null=True)),
                ('metadata', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
