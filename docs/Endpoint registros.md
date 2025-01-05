# Documentación de la API - Registros (Django REST Framework)

Esta es la documentación para la API RESTful desarrollada con Django REST Framework. La API permite realizar búsquedas avanzadas en las tablas `Bayunca` y `LaVilla` utilizando filtros de fechas y valores.

## 📦 Endpoints Disponibles

### Bayunca
- `GET /api/bayunca/`
- `POST /api/bayunca/`
- `GET /api/bayunca/{id}/`
- `PUT /api/bayunca/{id}/`
- `DELETE /api/bayunca/{id}/`

### LaVilla
- `GET /api/lavilla/`
- `POST /api/lavilla/`
- `GET /api/lavilla/{id}/`
- `PUT /api/lavilla/{id}/`
- `DELETE /api/lavilla/{id}/`

---

## 📊 Parámetros de Búsqueda

### 1. Búsqueda por `REG_CA`

Puedes filtrar registros utilizando el campo `REG_CA`.
```http
GET /api/bayunca/?REG_CA=101
```

### 2. Búsqueda por `direccion`

Puedes filtrar registros utilizando el campo `direccion`.
```http
GET /api/bayunca/?direccion=102
```

### 3. Búsqueda por Rango de Fechas

Puedes filtrar registros entre dos fechas usando `startDate` y `endDate`.
```http
GET /api/bayunca/?startDate=2024-12-01&endDate=2024-12-31
```

### 4. Búsqueda Combinada: `REG_CA` y `Rango de Fechas`
```http
GET /api/bayunca/?startDate=2024-12-01&endDate=2024-12-31&REG_CA=101
```

### 5. Búsqueda Combinada: `direccion` y `Rango de Fechas`
```http
GET /api/bayunca/?startDate=2024-12-01&endDate=2024-12-31&direccion=102
```

### 6. Búsqueda Completa: `REG_CA`, `direccion` y `Rango de Fechas`
```http
GET /api/bayunca/?startDate=2024-12-01&endDate=2024-12-31&REG_CA=101&direccion=102
```

---

## 📊 Ejemplos para `LaVilla`

### 1. Búsqueda por `REG_CA`
```http
GET /api/lavilla/?REG_CA=201
```

### 2. Búsqueda por `direccion`
```http
GET /api/lavilla/?direccion=203
```

### 3. Búsqueda por `Rango de Fechas`
```http
GET /api/lavilla/?startDate=2024-01-01&endDate=2024-01-31
```

---

## ✅ Respuestas Esperadas

**Ejemplo de Respuesta Exitosa (HTTP 200):**
```json
[
  {
    "id": 1,
    "REG_CA": 101,
    "value": 50.5,
    "direccion": 102,
    "metadata": {"sensor": "modbus"},
    "created_at": "2024-12-01T10:00:00Z",
    "updated_at": "2024-12-10T15:00:00Z"
  }
]
```

**Ejemplo de Error (HTTP 400):**
```json
{
  "error": "Formato de fecha inválido. Use el formato YYYY-MM-DD"
}
```

---

## 🔑 Autenticación
Actualmente, la API no requiere autenticación. Si se requiere, se puede habilitar usando `TokenAuthentication` o `JWT`.

---

## 📦 Gestión de Datos

### Crear un Nuevo Registro
```http
POST /api/bayunca/
Content-Type: application/json

{
    "REG_CA": 101,
    "value": 45.6,
    "direccion": 103,
    "metadata": {"sensor": "modbus"}
}
```

### Actualizar un Registro
```http
PUT /api/bayunca/1/
Content-Type: application/json

{
    "REG_CA": 101,
    "value": 50.0,
    "direccion": 102
}
```

### Eliminar un Registro
```http
DELETE /api/bayunca/1/
```

---

## 🛠️ Configuración Técnica

### Tecnologías Utilizadas:
- Django 4.x
- Django REST Framework
- django-filters

---

## 🚀 Notas Finales
- La API está optimizada para búsquedas avanzadas con filtros combinados.
- Es posible extender esta API con autenticación y permisos adicionales.

---

📧 **Contacto:** Para cualquier duda o sugerencia, no dudes en contactarnos.

