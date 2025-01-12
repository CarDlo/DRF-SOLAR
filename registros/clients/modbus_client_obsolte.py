import logging
from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import time
from registros.models import Bayunca, LaVilla, Oldt, Solchacras, Solsantonio, Solhuaqui, Sanpedro, Gonzaenergy, Produlesti, General

# Configuración del logging
LOG_FILE = "modbus_client.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def start_modbus_client(plant_id, plant_name,ip, port, start_address, max_registers, interval, modelo):
    print(f"Configuración MODBUS, desde el cliente:plant_name={plant_name}, ip={ip}, port={port}, start_address={start_address}, max_registers={max_registers}, interval={interval}")
    """
    Inicia el cliente Modbus TCP y envía datos a una API en intervalos definidos.

    :param ip: Dirección IP del dispositivo Modbus.
    :param port: Puerto TCP del dispositivo Modbus.
    :param start_address: Dirección inicial de los registros a leer.
    :param max_registers: Cantidad máxima de registros a leer.
    :param interval: Intervalo en segundos entre lecturas consecutivas.
    :param modelo: Modelo que se usa para almacenar los registros.
    """

    def send_data_to_api(value, reg_address):
        """
        Envía datos leídos del dispositivo Modbus a una API.

        :param io_address: Dirección de E/S (si aplica, aquí es "NA").
        :param value: Valor del registro.
        :param reg_address: Dirección del registro Modbus.
        """
        try:
            match modelo:
                case "Bayunca1":
                    Bayunca.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "Lavilla":
                    LaVilla.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "Oldt":
                    Oldt.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "Solchacras":
                    Solchacras.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "Solsantonio":
                    Solsantonio.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "Solhuaqui":
                    Solhuaqui.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "Sanpedro":
                    Sanpedro.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "Gonzaenergy":
                    Gonzaenergy.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "Produlesti":
                    Produlesti.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
                case "General":
                    General.objects.create(REG_CA=reg_address, value=value, plant_id=plant_id)
        except Exception as e:
            logging.error(f"Error al guardar los datos en la base de datos: {e}")



    def read_modbus_registers(client, start_address, max_registers):
        """
        Lee un rango de registros Modbus desde un dispositivo Modbus TCP.

        :param client: Instancia del cliente ModbusTcpClient.
        :param start_address: Dirección inicial de los registros a leer.
        :param max_registers: Cantidad máxima de registros a leer.
        """
        try:
            logging.info(f"Leyendo registros desde la dirección {start_address} con un máximo de {max_registers} registros...")
            result = client.read_holding_registers(address=start_address, count=max_registers)

            if result.isError():
                logging.error(f"Error al leer registros: {result}")
            elif hasattr(result, 'registers'):
                logging.info(f"Registros leídos correctamente:")
                for i, value in enumerate(result.registers):
                    reg_address = start_address + i
                    logging.info(f"Dirección: {reg_address}, Valor: {value}")
                    
                    send_data_to_api(value, reg_address)
            else:
                logging.error("La respuesta del servidor no contiene registros.")
        except ModbusException as e:
            logging.error(f"Excepción de Modbus: {e}")
        except Exception as e:
            logging.error(f"Error inesperado: {e}")

    def main_loop(plant_name, host, port, start_address, max_registers, interval):
        """
        Mantiene la conexión al dispositivo Modbus y realiza lecturas periódicas.

        :param host: Dirección IP del dispositivo Modbus.
        :param port: Puerto TCP del dispositivo Modbus.
        :param start_address: Dirección inicial de lectura.
        :param max_registers: Cantidad máxima de registros a leer.
        :param interval: Intervalo en segundos entre lecturas consecutivas.
        """
        client = ModbusTcpClient(host=host, port=port)
        try:
            logging.info(f"Conectando a {host}:{port}...")
            if not client.connect():
                logging.error(f"No se pudo conectar al dispositivo Modbus en {host}:{port}")
                return

            logging.info(f"Conexión exitosa a {host}:{port}")

            while True:
                if not client.is_socket_open():
                    logging.warning("Conexión perdida, intentando reconectar...")
                    if not client.connect():
                        logging.error("Reintento de conexión fallido. Saliendo del bucle.")
                        break
                read_modbus_registers(client, start_address, max_registers)
                logging.info(f"Esperando {interval} segundos para la próxima lectura...")
                time.sleep(interval)

        except KeyboardInterrupt:
            logging.info("Bucle detenido por el usuario.")
        except Exception as e:
            logging.error(f"Error inesperado en el bucle principal: {e}")
        finally:
            logging.info("Cerrando conexión...")
            client.close()

    # Iniciar el bucle principal
    main_loop(plant_name,ip, port, start_address, max_registers, interval)
    print(plant_name,ip, port, start_address, max_registers, interval)
    # if __name__ == "__main__":
    #     # Configuración personalizable
    #     HOST = "127.0.0.1"  # Dirección IP del dispositivo Modbus
    #     PORT = 502          # Puerto TCP del dispositivo Modbus
    #     START_ADDRESS = 0   # Dirección inicial de lectura
    #     MAX_REGISTERS = 10  # Cantidad máxima de registros a leer
    #     INTERVAL = 2       # Intervalo en segundos entre lecturas

    #     # Llamar a la función principal
    #     main_loop(HOST, PORT, START_ADDRESS, MAX_REGISTERS, INTERVAL)
