import psutil

def listar_procesos():
    print("Procesos de Python activos:")
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        if 'python' in proc.info['name'].lower():
            print(f"PID: {proc.info['pid']}, Nombre: {proc.info['name']}, Estado: {proc.info['status']}")

def buscar_proceso_por_nombre(nombre):
    print(f"\nBuscando procesos con nombre '{nombre}':")
    encontrados = [
        proc.info for proc in psutil.process_iter(['pid', 'name'])
        if nombre.lower() in proc.info['name'].lower()
    ]
    if encontrados:
        for proc in encontrados:
            print(f"PID: {proc['pid']}, Nombre: {proc['name']}")
    else:
        print("No se encontraron procesos.")

def detalles_proceso(pid):
    try:
        process = psutil.Process(pid)
        print(f"\nDetalles del proceso PID {pid}:")
        print(f"Nombre: {process.name()}")
        print(f"Estado: {process.status()}")
        print(f"Uso de CPU: {process.cpu_percent(interval=1)}%")
        print(f"Uso de memoria: {process.memory_info().rss / 1024 ** 2:.2f} MB")
    except psutil.NoSuchProcess:
        print(f"No se encontró ningún proceso con PID {pid}")

def detener_proceso(pid):
    try:
        process = psutil.Process(pid)
        process.terminate()
        print(f"\nProceso con PID {pid} detenido correctamente.")
    except psutil.NoSuchProcess:
        print(f"No se encontró ningún proceso con PID {pid}")
    except Exception as e:
        print(f"Error al detener el proceso: {e}")

# Menú interactivo
def menu():
    while True:
        print("\n--- Menú de Gestión de Procesos ---")
        print("1. Listar procesos de Python")
        print("2. Buscar proceso por nombre")
        print("3. Ver detalles de un proceso por PID")
        print("4. Detener un proceso por PID")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_procesos()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del proceso: ")
            buscar_proceso_por_nombre(nombre)
        elif opcion == "3":
            pid = int(input("Ingrese el PID: "))
            detalles_proceso(pid)
        elif opcion == "4":
            pid = int(input("Ingrese el PID a detener: "))
            detener_proceso(pid)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
