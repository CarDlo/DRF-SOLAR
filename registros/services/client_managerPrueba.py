import django
django.setup()
import multiprocessing
import signal
import time
import psutil
import os
import json
from .fetch_plants_service import fetch_plants
from registros.clients.iec104_client import start_iec104_client
from registros.clients.modbus_client import start_modbus_client
from registros.clients.modbus_client_rev import start_modbus_client_rev

# Archivos de bloqueo y estado
LOCK_FILE = "plants.lock"
PROCESS_STATE_FILE = "process_state.json"

# Diccionario global para rastrear procesos
processes = {}

def load_active_plants():
    """Carga las plantas activas desde el archivo de bloqueo."""
    if os.path.exists(LOCK_FILE):
        with open(LOCK_FILE, "r") as f:
            return set(json.load(f))
    return set()

def save_active_plants(active_plants):
    """Guarda las plantas activas en el archivo de bloqueo."""
    with open(LOCK_FILE, "w") as f:
        json.dump(list(active_plants), f)

def load_process_state():
    """Carga el estado de los procesos desde el archivo."""
    if os.path.exists(PROCESS_STATE_FILE):
        with open(PROCESS_STATE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_process_state(state):
    """Guarda el estado de los procesos en el archivo."""
    with open(PROCESS_STATE_FILE, "w") as f:
        json.dump(state, f)

def handle_plant(plant):
    """
    Maneja el procesamiento de una planta según su protocolo de comunicación.
    """
    protocolo = plant.protocolo_comunicacion
    ip = plant.ip
    port = int(plant.puerto)
    modelo = plant.modelo
    plant_name = plant.name
    plant_id = plant

    metadata = plant.metadata if plant else {}
    if not isinstance(metadata, dict):
        metadata = {}

    print(f"Iniciando cliente para planta: {plant_name} con protocolo {protocolo}")

    if protocolo == "IEC104":
        tick_rate_ms = metadata.get("tick_rate_ms", 5000)
        command_timeout_ms = metadata.get("command_timeout_ms", 5000)
        time_sender_sleep_s = metadata.get("time_sender_sleep_ms", 5000) / 1000
        originator_address = metadata.get("originator_address", 123)
        time_connect_s = metadata.get("time_connect_ms", 1000) / 1000

        start_iec104_client(plant_id, plant_name,ip, port, modelo, tick_rate_ms, command_timeout_ms, time_sender_sleep_s, originator_address, time_connect_s)

    elif protocolo == "MODBUS":
        start_address = metadata.get("start_address", 0)
        max_registers = metadata.get("max_registers", 10)
        interval = metadata.get("interval", 5)
        block_registers = min(metadata.get("block_registers", 125), 125)
        start_modbus_client(plant_id, plant_name, ip, port, start_address, block_registers, interval, max_registers, modelo)

    elif protocolo == "MODBUS-REV":
        start_address = metadata.get("start_address", 0)
        max_registers = metadata.get("max_registers", 10)
        interval = metadata.get("interval", 5)
        block_registers = min(metadata.get("block_registers", 125), 125)
        start_modbus_client_rev(plant_id, plant_name, ip, port, start_address, block_registers, interval, max_registers, modelo)
    else:
        print(f"Protocolo desconocido para la planta: {plant.name} con protocolo {protocolo}")

    stop_flag = False

    def terminate_process(signal_number, frame):
        nonlocal stop_flag
        print(f"Cliente para {plant_name} recibiendo señal de terminación.")
        stop_flag = True

    signal.signal(signal.SIGTERM, terminate_process)

    try:
        while not stop_flag:
            print(f"Cliente {plant_name} trabajando...")
            time.sleep(5)
        print(f"Cliente para {plant_name} finalizado correctamente.")
    except KeyboardInterrupt:
        print(f"Cliente para {plant_name} detenido manualmente.")

def start_client(plant_name):
    """
    Inicia un cliente para una planta específica.
    """
    cleanup_orphan_processes()
    active_plants = load_active_plants()
    process_state = load_process_state()

    if plant_name in process_state:
        return {"status": "error", "message": f"La planta {plant_name} ya está en ejecución."}

    plants = fetch_plants()
    plant = next((p for p in plants if p.name == plant_name), None)

    if not plant:
        return {"status": "error", "message": f"Planta {plant_name} no encontrada."}

    process = multiprocessing.Process(target=handle_plant, args=(plant,))
    process.start()

    process_state[plant_name] = process.pid
    save_process_state(process_state)

    active_plants.add(plant_name)
    save_active_plants(active_plants)

    return {"status": "success", "message": f"Cliente iniciado para la planta: {plant_name}", "pid": process.pid}



    return {"status": "success", "data": {"stopped": stop_results, "started": start_results}}
def cleanup_orphan_processes():
    """
    Limpia los procesos huérfanos que ya no están activos usando psutil.
    """
    process_state = load_process_state()  # Diccionario con {planta: PID}
    active_plants = load_active_plants()  # Lista de plantas activas
    updated_process_state = {}

    for plant_name, pid in process_state.items():
        # Verificar si el proceso está activo con psutil
        if psutil.pid_exists(pid):
            # El proceso sigue activo, mantenerlo en el estado actualizado
            updated_process_state[plant_name] = pid
        else:
            # El proceso ya no está activo, es un proceso huérfano
            print(f"Proceso huérfano encontrado: {plant_name} con PID {pid}. Limpiando...")
            if plant_name in active_plants:
                active_plants.remove(plant_name)

    # Guardar el estado actualizado de los procesos (opcional)
    save_process_state(updated_process_state)
    save_active_plants(active_plants)

    print("Limpieza de procesos huérfanos completada.")


if __name__ == "__main__":
    import sys
    # Establecer el modo de inicio 'spawn' para evitar problemas en producción (Railway)
    multiprocessing.set_start_method("spawn")
    cleanup_orphan_processes()
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Uso: main.py [start|stop|restart|status|start-all|stop-all|restart-all] [plant_name]"}))
        sys.exit(1)

    command = sys.argv[1]
    plant_name = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        if command == "start" and plant_name:
            result = start_client(plant_name)

        else:
            result = {"status": "error", "message": "Comando desconocido o argumentos faltantes."}
    except Exception as e:
        result = {"status": "error", "message": f"Error ejecutando el comando: {e}"}

    print(json.dumps(result))
