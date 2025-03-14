import logging
import time
import struct
from collections import defaultdict
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
from registros.models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General
from plants.models import Signs
# Configuración del logging
LOG_FILE = "modbus_client.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Diccionario para almacenar los datos en lotes
bulk_data = defaultdict(list)
BATCH_SIZE = 125  # Cantidad de registros antes de hacer un insert en batch


# -------------------------------------------------------------------
# Funciones para verificar el tipo de datos
# -------------------------------------------------------------------
def verification_data(reg_address):
    """
    Verifica si el valor de reg_address está activo en la tabla.

    :param reg_address: Dirección del registro Modbus.
    :return: Tipo de dato (por ejemplo, "Single", "Int32", etc.) si el registro está activo, o False en caso contrario.
    """
    try:
        # Buscar el registro en la tabla
        record = Signs.objects.filter(reg_ca=reg_address).first()
        if record:
            return record.data_type
        else:
            return False
    except Exception as e:
        logging.error(f"Error al verificar los datos: {e}")
    return False

# -------------------------------------------------------------------
# Funciones para enviar y almacenar datos en la DB
# -------------------------------------------------------------------
def send_data_to_api(value, reg_address, modelo, plant_id):
    """
    Acumula datos y los inserta en la base de datos en lotes para optimizar el rendimiento.
    """
    
    try:
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

        if record:
            bulk_data[modelo].append(record)

        if len(bulk_data[modelo]) >= BATCH_SIZE:
            modelo_class = eval(modelo)  # Convertir string a la clase del modelo
            modelo_class.objects.bulk_create(bulk_data[modelo])
            print("Enviando datos a la base de datos BULK...")
            bulk_data[modelo] = []
            




    except Exception as e:
        logging.error(f"Error al guardar los datos en la base de datos: {e}")

# -------------------------------------------------------------------
# Funciones de decodificación de datos según tipo
# -------------------------------------------------------------------
def decode_float32_mid_endian(registers):
    """
    Decodifica dos registros Modbus como Float32 usando Mid-endian CDAB.
    """
    if len(registers) < 2:
        logging.warning("Se requieren al menos 2 registros para interpretar un Float32.")
        return None
    # Reordenar los registros: CDAB (se intercambian las palabras)
    reordered_registers = [registers[1], registers[0]]
    byte_data = struct.pack(">HH", *reordered_registers)
    valor_float = struct.unpack(">f", byte_data)[0]
    logging.info(f"Valor Float32 (Mid-endian CDAB): {valor_float}")
    return valor_float

def decode_int32_mid_endian(registers):
    """
    Decodifica dos registros Modbus como Int32 usando Mid-endian CDAB.
    """
    if len(registers) < 2:
        logging.warning("Se requieren al menos 2 registros para interpretar un Int32.")
        return None
    reordered_registers = [registers[1], registers[0]]
    byte_data = struct.pack(">HH", *reordered_registers)
    valor_int = struct.unpack(">i", byte_data)[0]
    logging.info(f"Valor Int32 (Mid-endian CDAB): {valor_int}")
    return valor_int

def decode_uint32_mid_endian(registers):
    """
    Decodifica dos registros Modbus como UInt32 usando Mid-endian CDAB.
    """
    if len(registers) < 2:
        logging.warning("Se requieren al menos 2 registros para interpretar un UInt32.")
        return None
    reordered_registers = [registers[1], registers[0]]
    byte_data = struct.pack(">HH", *reordered_registers)
    valor_uint = struct.unpack(">I", byte_data)[0]
    logging.info(f"Valor UInt32 (Mid-endian CDAB): {valor_uint}")
    return valor_uint

def decode_int16(value):
    """
    Decodifica un registro Modbus como Int16.
    """
    valor_int16 = struct.unpack(">h", struct.pack(">H", value))[0]
    logging.info(f"Valor Int16: {valor_int16}")
    return valor_int16

def decode_uint16(value):
    """
    Decodifica un registro Modbus como UInt16.
    """
    logging.info(f"Valor UInt16: {value}")
    return value

def decode_value(data_type, registers):
    """
    Decodifica el valor de acuerdo al tipo de dato usando los registros necesarios.
    :param data_type: Tipo de dato (ej. "Single", "Int32", "UInt16", etc.).
    :param registers: Lista de registros necesarios para la decodificación.
    :return: Valor decodificado.
    """
    if data_type == "Single":
        return decode_float32_mid_endian(registers)
    elif data_type == "Int32":
        return decode_int32_mid_endian(registers)
    elif data_type == "UInt32":
        return decode_uint32_mid_endian(registers)
    elif data_type == "Int16":
        return decode_int16(registers[0])
    elif data_type == "UInt16":
        return decode_uint16(registers[0])
    else:
        # Por defecto, retornar el primer registro sin conversión
        return registers[0]

# -------------------------------------------------------------------
# Función para procesar los registros leídos
# -------------------------------------------------------------------
def process_registers(registers, start_address, modelo, plant_id):
    """
    Procesa los registros leídos, decodifica cada valor según su tipo 
    y los envía a la API para su almacenamiento.
    """
    i = 0
    while i < len(registers):
        reg_address = start_address + i
        # Consultar el tipo de dato para la dirección actual
        data_type = verification_data(reg_address)
        
        if data_type in ["Single", "Int32", "UInt32"]:
            # Estos tipos requieren dos registros para su decodificación
            if i + 1 < len(registers):
                reg_pair = registers[i:i+2]
                decoded_val = decode_value(data_type, reg_pair)
                # Ahora guardamos el valor decodificado en reg_address (NO en reg_address + 1)
                send_data_to_api(decoded_val, reg_address, modelo, plant_id)
                i += 2
            else:
                logging.warning(
                    f"No hay suficientes registros para decodificar el valor en la dirección {reg_address}"
                )
                i += 1
        elif data_type in ["Int16", "UInt16"]:
            # Estos tipos se decodifican con un único registro
            decoded_val = decode_value(data_type, [registers[i]])
            send_data_to_api(decoded_val, reg_address, modelo, plant_id)
            i += 1
        else:
            # Si el registro no está activo o no se ha definido el tipo, 
            # se almacena el valor sin conversión
            send_data_to_api(registers[i], reg_address, modelo, plant_id)
            i += 1

# -------------------------------------------------------------------
# Función de lectura de registros Modbus
# -------------------------------------------------------------------
def read_modbus_registers(client, start_address, max_registers, modelo, plant_id):
    """
    Lee un rango de registros Modbus desde un dispositivo Modbus TCP y procesa cada registro.
    """
    try:
        logging.info(f"Leyendo registros desde la dirección {start_address} con un máximo de {max_registers} registros...")
        result = client.read_holding_registers(address=start_address, count=max_registers)
        
        if result.isError():
            logging.error(f"Error al leer registros: {result}")
        elif hasattr(result, 'registers'):
            process_registers(result.registers, start_address, modelo, plant_id)
    except ModbusException as e:
        logging.error(f"Excepción de Modbus: {e}")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")

# -------------------------------------------------------------------
# Funciones de ciclo principal y arranque del cliente Modbus
# -------------------------------------------------------------------
def main_loop(plant_name, ip, port, start_address, max_registers, interval, total_registers, modelo, plant_id):
    """
    Mantiene la conexión al dispositivo Modbus y realiza lecturas periódicas.
    """
    client = ModbusTcpClient(host=ip, port=port, timeout=5)
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

def start_modbus_client_rev(plant_id, plant_name, ip, port, start_address, max_registers, interval, total_registers, modelo):
    print(f"Configuración MODBUS, desde el cliente: {plant_name}, ip={ip}, port={port}, start_address={start_address}, max_registers={max_registers}, interval={interval}")
    main_loop(plant_name, ip, port, start_address, max_registers, interval, total_registers, modelo, plant_id)
