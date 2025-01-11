import logging
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import time
from registros.models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General
from plants.models import Signs
from django.db import connection

# Configuración del logging
LOG_FILE = "modbus_client.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def start_modbus_client_rev(plant_id, plant_name, ip, port, start_address, max_registers, interval, total_registers, modelo):
    print(f"Iniciando cliente Modbus para la planta: {plant_name}")
    print(f"Configuración: IP={ip}, Puerto={port}, Start Address={start_address}, Max Registers={max_registers}, Interval={interval}")
    try:
        def verification_data(reg_address):
            try:
                connection.ensure_connection()  # Asegura la conexión
                print(f"Verificando si el registro {reg_address} está activo.")
                record = Signs.objects.filter(reg_ca=reg_address).first()
                print(f"Registro encontrado: {record.reg_ca} - Activo: {record.active} - Plant ID: {record.plant_id}")
                if record and record.active:
                    print(f"Registro {reg_address} activo.")
                    return True
                print(f"Registro {reg_address} no activo o no encontrado.")
                return False
            except Exception as e:
                print(f"Error al verificar el registro {reg_address}: {e}")
                return False

        def send_data_to_api(value, reg_address):
            try:
                connection.ensure_connection()  # Asegura la conexión
                if verification_data(reg_address):
                    print(f"Guardando en {modelo}: REG_CA={reg_address}, Valor={value}")
                    if modelo == "Bayunca1":
                        Bayunca.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "LaVilla":
                        LaVilla.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "Oldt":
                        Oldt.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "Solchacras":
                        Solchacras.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "Solsantonio":
                        Solsantonio.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "Solhuaqui":
                        Solhuaqui.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "Sanpedro":
                        Sanpedro.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "Gonzaenergy":
                        Gonzaenergy.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "Produlesti":
                        Produlesti.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    elif modelo == "General":
                        General.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                    print(f"Datos guardados exitosamente en {modelo} para REG_CA: {reg_address}")
                    return True
                else:
                    print(f"El registro {reg_address} no está activo, no se guardaron datos.")
                    return False
            except Exception as e:
                print(f"Error al guardar en la base de datos: {e}")
                return False

        def read_modbus_registers(client, start_address, max_registers):
            print(f"Leyendo registros desde la dirección {start_address} con un máximo de {max_registers} registros.")
            try:
                result = client.read_holding_registers(address=start_address, count=max_registers)
                if result.isError():
                    print(f"Error al leer registros: {result}")
                elif hasattr(result, 'registers'):
                    print(f"Registros leídos correctamente.")
                    for i, value in enumerate(result.registers):
                        reg_address = start_address + i
                        print(f"Registro {reg_address} leído con valor {value}")
                        if send_data_to_api(value, reg_address):
                            print(f"Datos guardados correctamente para REG_CA: {reg_address}")
                        else:
                            print(f"Error al guardar el registro {reg_address}")
                else:
                    print("La respuesta no contiene registros válidos.")
            except ModbusException as e:
                print(f"Excepción de Modbus: {e}")
            except Exception as e:
                print(f"Error inesperado al leer registros: {e}")

        def main_loop(plant_name, host, port, start_address, max_registers, interval, total_registers):
            client = ModbusTcpClient(host=host, port=port)
            try:
                print(f"Intentando conectar al dispositivo Modbus en {host}:{port}")
                if not client.connect():
                    print(f"No se pudo conectar a {host}:{port}")
                    return

                print(f"Conexión exitosa a {host}:{port}")

                while True:
                    if not client.is_socket_open():
                        print("Conexión perdida. Intentando reconectar...")
                        if not client.connect():
                            print("Reintento fallido. Finalizando bucle.")
                            break

                    current_address = start_address
                    while current_address < start_address + total_registers:
                        count = min(max_registers, (start_address + total_registers) - current_address)
                        read_modbus_registers(client, current_address, count)
                        current_address += count

                    print(f"Esperando {interval} segundos para la próxima lectura.")
                    time.sleep(interval)

            except KeyboardInterrupt:
                print("Bucle detenido manualmente por el usuario.")
            except Exception as e:
                print(f"Error inesperado en el bucle principal: {e}")
            finally:
                print("Cerrando conexión al dispositivo Modbus.")
                client.close()

        main_loop(plant_name, ip, port, start_address, max_registers, interval, total_registers)
    except Exception as e:
        print(f"Error general al iniciar el cliente Modbus: {e}")
