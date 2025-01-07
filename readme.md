# Instrucciones para correr el proyecto en Django

Para ejecutar correctamente este proyecto, se deben seguir los siguientes pasos en el orden especificado:

1. **Clonar el repositorio**
```bash
git clone <URL_DEL_REPOSITORIO>
cd <nombre_del_proyecto>
```
Clona el repositorio del proyecto y accede al directorio del proyecto.

2. **Crear y activar un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
Crea un entorno virtual aislado para la instalación de dependencias y lo activa.

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```
Instala las dependencias necesarias listadas en `requirements.txt`.

4. **Preparar la base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```
`makemigrations` genera archivos de migración, que son instrucciones para modificar la estructura de la base de datos basándose en los cambios realizados en los modelos.
`migrate` aplica esas migraciones a la base de datos, asegurando que esté sincronizada con los modelos definidos.

5. **Crear un superusuario (opcional)**
```bash
python manage.py createsuperuser
```
Crea un usuario administrador para acceder al panel de administración de Django.

6. **Cargar datos de las plantas**
```bash
python manage.py loaddata plants_seeder.json
```
Carga un conjunto de datos predefinido desde un archivo JSON en la base de datos. Este archivo contiene información sobre las plantas disponibles para ser utilizadas en la aplicación.

7. **Iniciar el servidor de desarrollo**
```bash
python manage.py runserver
```
Inicia el servidor de desarrollo de Django para probar la aplicación localmente.

El proyecto estará disponible en `http://localhost:8000`.

Para acceder a la documentación de los endpoints, visita: `http://localhost:8000/docs/`
Para acceder al administrador de Django, visita: `http://localhost:8000/admin/`

## Aplicación Plantas
La aplicación Plantas incluye los siguientes modelos:
- **Bayunca1**
- **LaVilla**
- **Oldt**
- **Solchacras**
- **Solsantonio**
- **Solhuaqui**
- **Sanpedro**
- **Gonzaenergy**
- **Produlesti**
- **General**

Estos modelos representan tablas en la base de datos donde se almacena la información de cada planta. El modelo `General` está diseñado para almacenar plantas personalizadas creadas por el usuario.

Para más detalles sobre los modelos de plantas, consultar la documentación en `http://localhost:8000/docs/#plants`.

### Campos de la tabla Plantas
- **id**: Identificador único de cada planta. Se utiliza para referenciar la planta en operaciones como consultas, actualizaciones o eliminaciones.
- **name**: Nombre de la planta fotovoltaica. Permite identificarla de manera descriptiva, se recomienda un nombre sin espacios.
- **province**: Provincia o región donde está ubicada la planta. Proporciona información geográfica detallada.
- **country**: País donde se encuentra la planta. Facilita clasificar las plantas por ubicación nacional.
- **potenciaDC**: Potencia en corriente directa (DC) de la planta en megavatios (MW). Representa la capacidad energética instalada.
- **scada**: Sistema de supervisión y adquisición de datos (SCADA) utilizado en la planta. Permite gestionar y monitorizar las operaciones.
- **protocoloComunicacion**: Protocolo de comunicación usado por la planta (ejemplo: `MODBUS` o `IEC104`). Define cómo se transmiten los datos entre dispositivos.
- **ip**: Dirección IP del sistema de control o SCADA de la planta. Es necesario para la comunicación con la planta.
- **puerto**: Puerto de comunicación asociado al protocolo usado por la planta. Define el punto de acceso para las conexiones.
- **modelo**: Modelo asociado a la planta. Permite guardar la informacion de la plantaen la tabla(modelo especificado).
- **credenciales**: Información de autenticación requerida para acceder al SCADA o API de la planta (si aplica). Generalmente contiene un objeto con claves como `username` y `password`.
- **metadata**: Información adicional o personalizada relacionada con la planta, en formato JSON. Se utiliza para almacenar detalles específicos que no están cubiertos por otras columnas. Para el caso de modbus se requiere informacion de valores tales como: `start_address`: Dirección inicial de lectura, `max_registers`: Cantidad máxima de registros a leer, `interval`: Intervalo en segundos entre lecturas, `block_registers`: bloques maximos de lectura.
Para IEC104 en el campo metadata se debe agregar los valores de `tick_rate_ms, command_timeout_ms, time_sender_sleep_ms, time_connect_ms y originator_address` en formato JSON.
- **active**: Columna de tipo boolean para identificar si la planta se encuentra activa(true) o inactiva(false), si el valor es (true) el cliente ejecutara la captura de datos.

#### **Modbus Configuración**

En el campo `metadata` se debe agregar los valores de `start_address`, `max_registers` e `interval` en formato JSON. Estos valores serán consultados por el cliente de Modbus para configuración. Si estos campos no se agregan, se tomarán por defecto los siguientes valores:

- `start_address`: 0
- `max_registers`: 10
- `interval`: 5
- `block_registers`: 125


### Descripción de los Campos:

- **`start_address`**: Dirección inicial de lectura en el dispositivo Modbus.
- **`max_registers`**: Cantidad máxima de registros a leer desde la dirección inicial.
- **`interval`**: Intervalo en segundos entre lecturas consecutivas.
- **`block_registers`**: Bloques maximos de lectura para modbus el valor maximo es 125 si el valor es mayor el programa tomara 125 por defecto.

```json
"metadata": {
    "start_address": 0,
    "max_registers": 10,
    "interval": 5,
    "block_registers": 125
}
```
---

#### **IEC 104 Configuración**

En el campo `metadata` se debe agregar los valores de `tick_rate_ms`, `command_timeout_ms`, `time_sender_sleep_ms`, `time_connect_ms` y `originator_address` en formato JSON. Estos valores serán utilizados por el cliente IEC 104 para su configuración. Si estos campos no se agregan, se tomarán por defecto los siguientes valores:

- `tick_rate_ms`: 5000
- `command_timeout_ms`: 5000
- `time_sender_sleep_ms`: 5000
- `time_connect_ms`: 1000
- `originator_address`: 123


#### Descripción de los Campos:

- **`tick_rate_ms`**: Especifica la frecuencia con la que el cliente IEC 104 procesa eventos internos, como la recepción de datos, el manejo de comandos, y las actualizaciones de puntos.
- **`command_timeout_ms`**: Tiempo máximo en milisegundos para esperar una respuesta a un comando antes de considerar un error.
- **`time_sender_sleep_ms`**: Introduce pausas explícitas en el bucle principal del programa para limitar con qué frecuencia este realiza ciertas acciones (como recorrer puntos y enviar datos). (frecuencia del bucle que procesa y envía los datos). Se recomienda que este valor sea igual a tick_rate_ms.
- **`time_connect_ms`**: Tiempo en milisegundos que el cliente espera antes de intentar reconectarse si no está conectado.
- **`originator_address`**: Identificador único del cliente dentro del sistema IEC 104.


#### Ejemplo JSON para Configuración

```json
"metadata": {
  "tick_rate_ms": 5000,
  "command_timeout_ms": 5000,
  "time_sender_sleep_ms": 5000,
  "time_connect_ms": 1000,
  "originator_address": 123
}
```
---
## **Nota importante**
- El campo `protocoloComunicacion` solo acepta los valores:
  - `MODBUS`
  - `IEC104`

### **Modelo de respuesta de la tabla Planta**
```json
  {
    "id": 1,
    "name": "OLDT",
    "province": "Tolú Viejo",
    "country": "Colombia",
    "potencia_dc": 12.94,
    "scada": "Webdom",
    "protocolo_comunicacion": "MODBUS",
    "ip": "192.0.0.1",
    "puerto": 502,
    "modelo": "Oldt",
    "credenciales": null,
    "metadata": {
      "start_address": 0,
      "max_registers": 10,
      "interval": 5,
      "block_registers": 125
    },
    "active": false,
    "created_at": "2024-01-06T00:00:00Z",
    "updated_at": "2024-01-06T00:00:00Z"
  }
```

## Aplicacion Señales
La tabla `Señales` está destinada a almacenar la información del mapa de señales de la planta para los protocolos IEC104 y Modbus. Un mapa de señales es un conjunto de registros o direcciones que permiten identificar y monitorear variables específicas de la planta, como voltajes, corrientes, potencias, entre otros.

Esta tabla tiene una relación con la tabla `plantas` y cada señal está asociada a una planta específica. 

Para más detalles sobre los endpoints relacionados con señales, consultar la documentación en `http://localhost:8000/docs/#signals`.

### Campos de la tabla Señales
- **reg_ca**: Número de registro utilizado para identificar la variable medida. En Modbus es la dirección de inicio (Start Address) y en IEC104 es la dirección común del objeto (Common Address).
- **direccion**: Dirección asociada a la medición o registro, utilizada como identificador del punto de origen de los datos. En IEC104 es el Information Object Address (IOA). Puede ser nulo.
- **meta**: Etiqueta o nombre descriptivo del estado del dispositivo o variable monitoreada. Aplicable tanto a Modbus como a IEC104.
- **description**: Descripción textual del estado o variable monitoreada. Aplicable a Modbus e IEC104.
- **object_type**: Tipo de objeto o registro utilizado. En IEC104 puede ser valores como 'M_ME_NC_1'. No aplica para Modbus.
- **data_type**: Tipo de dato registrado, como 'Single' o 'Double'. Solo aplica a Modbus.
- **scaler**: Factor de escala o conversión aplicado al valor medido. En Modbus se usa como factor de escala, mientras que en IEC104 se utiliza como factor de conversión.
- **units**: Unidades de medida del valor registrado, como Voltios o Amperios. Aplica para Modbus e IEC104.
- **inversor**: Identificación del inversor asociado al registro. Aplica para Modbus e IEC104.
- **panel**: Nombre del panel o subgrupo de equipos al que está asociado el registro. Aplica para Modbus e IEC104.
- **equip_sist**: Equipo o sistema específico relacionado con el registro de medición. Aplica para Modbus e IEC104.
- **min_value**: Valor mínimo permitido para la variable monitoreada. Aplica para Modbus e IEC104.
- **max_value**: Valor máximo permitido para la variable monitoreada. Aplica para Modbus e IEC104.
- **planta_id**: Identificación única de la planta a la que pertenece el registro. Aplica para Modbus e IEC104.
- **protocolo**: Protocolo de comunicación utilizado para la transmisión de datos. Debe ser `MODBUS` o `IEC104`.
- **metadata**: Metadatos adicionales del registro, utilizados para almacenar información extra sobre la medición. Aplica para Modbus e IEC104.

## Aplicación Registros

La aplicación `Registros` contiene las siguientes plantas:
- `Bayunca 1`
- `La Villa`
- `Oldt`
- `Solchacras`
- `Solsantonio`
- `Solhuaqui`
- `San Pedro`
- `Gonzaenergy`
- `Produlesti`

Cada planta tiene un modelo que la relaciona directamente, a diferencia del modelo `General` que no tiene una planta asignada y está diseñado para plantas personalizadas.

Las tablas almacenan los registros capturados por los clientes de IEC104 o Modbus. Los endpoints de cada planta están documentados y dependen del nombre de la planta, por ejemplo, para `Bayunca` el endpoint es `/api/bayunca/`. La documentación completa del uso de cada endpoint puede encontrarse en `http://localhost:8000/docs/`.

### Campos de la tabla Registros

- **id**: Identificador único de cada registro. Es generado automáticamente y se utiliza para referenciar registros específicos.
- **REG_CA**: Start Address para Modbus o Common Address para IEC104.
- **value**: Valor medido o registrado, como una lectura de sensor o métrica relevante para la planta.
- **direccion**: Dirección asociada a la medición o registro, como un identificador del punto de origen de los datos. Puede ser nulo. Para IEC104 es el IO Address.
- **metadata**: Información adicional en formato JSON que describe el contexto de la medición, como el tipo de sensor, la unidad de medida, etc.
- **plant_id**: Planta asociada al registro.
- **createdAt**: Fecha y hora en que se creó el registro. Útil para el seguimiento y auditoría de datos.
- **updatedAt**: Fecha y hora de la última actualización del registro. Indica cuándo fue modificado por última vez.

## Documentación de Uso de JWT para Usuarios de la API

Esta documentación explica cómo un usuario de la API puede autenticarse y acceder a los recursos protegidos utilizando JSON Web Tokens (JWT).

### Autenticación con JWT

Para acceder a los recursos protegidos de la API, primero debe obtener un token de acceso (JWT).

### Duración por defecto del Token
La duración predeterminada de los tokens JWT es la siguiente:

- **Token de acceso:** Tiene una duración de 60 minutos y se utiliza para realizar solicitudes a los endpoints protegidos.
- **Token deslizante de acceso:** Tiene una duración de 30 días y se utiliza en escenarios donde se requiere una autenticación persistente.
- **Token de refresco deslizante:** Permite renovar el token de acceso y tiene una duración de 1 día.
- **Token deslizante para usuarios tardíos:** Los tokens de acceso y de refresco para usuarios con actividad tardía tienen la misma duración, es decir, 30 días y 1 día respectivamente.

#### 1. Obtener Token de Acceso
Realice una petición POST al endpoint `/api/token/` con sus credenciales de usuario:

```bash
curl -X POST http://localhost:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{"username": "admin", "password": "password123"}'
```

**Respuesta:**
```json
{
    "access": "<ACCESS_TOKEN>",
    "refresh": "<REFRESH_TOKEN>"
}
```

El `ACCESS_TOKEN` es utilizado para acceder a los recursos protegidos, mientras que el `REFRESH_TOKEN` es usado para renovar el token de acceso.

---

#### 2. Acceder a un Recurso Protegido
Utilice el `ACCESS_TOKEN` recibido para acceder a un recurso protegido. Ejemplo con el endpoint `/api/bayunca/`:

```bash
curl -X GET http://localhost:8000/api/bayunca/ \
-H "Authorization: Bearer <ACCESS_TOKEN>"
```

**Respuesta esperada:**
```json
{
    "message": "Datos de Bayunca accesibles solo con JWT."
}
```

---

#### 3. Renovar el Token de Acceso
Cuando el `ACCESS_TOKEN` expire, podrá solicitar uno nuevo usando el `REFRESH_TOKEN`:

```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
-H "Content-Type: application/json" \
-d '{"refresh": "<REFRESH_TOKEN>"}'
```

**Respuesta:**
```json
{
    "access": "<NEW_ACCESS_TOKEN>"
}
```

---

#### Notas Importantes
- El token de acceso (`ACCESS_TOKEN`) tiene una duración limitada.
- Utilice siempre el encabezado `Authorization: Bearer <ACCESS_TOKEN>` para realizar solicitudes a endpoints protegidos.
- No comparta sus tokens con terceros para mantener la seguridad de la API.

Para más información, consulte con el administrador de la API.
