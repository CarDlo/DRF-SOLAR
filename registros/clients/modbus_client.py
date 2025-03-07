import logging
import time
from collections import defaultdict
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
from registros.models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General

# Configuración del logging
LOG_FILE = "modbus_client.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Diccionario para almacenar los datos en lotes
bulk_data = defaultdict(list)
BATCH_SIZE = 125  # Cantidad de registros antes de hacer un insert en batch

def send_data_to_api(value, reg_address, modelo, plant_id):
    """
    Acumula datos y los inserta en la base de datos en lotes para optimizar el rendimiento.

    :param value: Valor del registro.
    :param reg_address: Dirección del registro Modbus.
    :param modelo: Modelo que se usa para almacenar los registros.
    :param plant_id: ID de la planta.
    """
    try:
        # Crear el objeto sin guardarlo en la base de datos
        record = None
        match modelo:
            case "Bayunca1":
                record = Bayunca(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "LaVilla":
                record = LaVilla(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "Oldt":
                record = Oldt(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "Solchacras":
                record = Solchacras(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "Solsantonio":
                record = Solsantonio(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "Solhuaqui":
                record = Solhuaqui(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "Sanpedro":
                record = Sanpedro(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "Gonzaenergy":
                record = Gonzaenergy(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "Produlesti":
                record = Produlesti(REG_CA=reg_address, value=value, plant_id=plant_id)
            case "General":
                record = General(REG_CA=reg_address, value=value, plant_id=plant_id)

        # Acumular el registro en la lista
        if record:
            bulk_data[modelo].append(record)

        # Si se alcanzó el tamaño del batch, hacer un insert masivo
        if len(bulk_data[modelo]) >= BATCH_SIZE:
            modelo_class = eval(modelo)  # Convertir string a la clase del modelo
            modelo_class.objects.bulk_create(bulk_data[modelo])  # Insertar en batch
            bulk_data[modelo] = []  # Vaciar la lista después de la inserción

    except Exception as e:
        logging.error(f"Error al guardar los datos en la base de datos: {e}")

def read_modbus_registers(client, start_address, max_registers, modelo, plant_id):
    """
    Lee un rango de registros Modbus desde un dispositivo Modbus TCP.

    :param client: Instancia del cliente ModbusTcpClient.
    :param start_address: Dirección inicial de los registros a leer.
    :param max_registers: Cantidad máxima de registros a leer.
    :param modelo: Modelo que se usa para almacenar los registros.
    :param plant_id: ID de la planta.
    """
    try:
        logging.info(f"Leyendo registros desde la dirección {start_address} con un máximo de {max_registers} registros...")
        result = client.read_holding_registers(address=start_address, count=max_registers)

        if result.isError():
            logging.error(f"Error al leer registros: {result}")
        elif hasattr(result, 'registers'):
            for i, value in enumerate(result.registers):
                reg_address = start_address + i
                send_data_to_api(value, reg_address, modelo, plant_id)
                #print(f"Dirección: {reg_address}, Valor: {value}")
    except ModbusException as e:
        logging.error(f"Excepción de Modbus: {e}")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")

def main_loop(plant_name, ip, port, start_address, max_registers, interval, total_registers, modelo, plant_id):
    """
    Mantiene la conexión al dispositivo Modbus y realiza lecturas periódicas.
    """
    client = ModbusTcpClient(host=ip, port=port, timeout=0.2)
    try:
        logging.info(f"Conectando a {ip}:{port}...")
        if not client.connect():
            logging.error(f"No se pudo conectar al dispositivo Modbus en {ip}:{port}")
            return

        logging.info(f"Conexión exitosa a {ip}:{port}")

        while True:
            if not client.is_socket_open():
                logging.warning("Conexión perdida, intentando reconectar...")
                if not client.connect():
                    logging.error("Reintento de conexión fallido. Saliendo del bucle.")
                    break

            current_address = start_address
            while current_address < start_address + total_registers:
                count = min(max_registers, (start_address + total_registers) - current_address)
                read_modbus_registers(client, current_address, count, modelo, plant_id)
                current_address += count

            logging.info(f"Esperando {interval} segundos para la próxima lectura...")
            time.sleep(interval)

    except KeyboardInterrupt:
        logging.info("Bucle detenido por el usuario.")
    except Exception as e:
        logging.error(f"Error inesperado en el bucle principal: {e}")
    finally:
        client.close()
        logging.info("Conexión Modbus cerrada.")

def start_modbus_client(plant_id, plant_name, ip, port, start_address, max_registers, interval, total_registers, modelo):
    print(f"Configuración MODBUS, desde el cliente: {plant_name}, ip={ip}, port={port}, start_address={start_address}, max_registers={max_registers}, interval={interval}")

    # Iniciar el bucle principal
    main_loop(plant_name, ip, port, start_address, max_registers, interval, total_registers, modelo, plant_id)
