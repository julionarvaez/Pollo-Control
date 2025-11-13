# 📚 Documentación API - Sistema de Control de Pollos

**Base URL:** `http://localhost:5000/api`

**Autenticación:** JWT Bearer Token

---

## 🔐 Autenticación

### Login

**POST** `/auth/login`

Autentica un usuario y retorna un token JWT.

**Request:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response (200):**
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "usuario": {
    "id": 1,
    "username": "admin",
    "nombre_completo": "Administrador",
    "email": "admin@granja.com",
    "rol": "admin"
  }
}
```

**Errores:**
- `400` - Faltan credenciales
- `401` - Credenciales inválidas

---

### Registrar Usuario

**POST** `/auth/register`

Crea un nuevo usuario.

**Request:**
```json
{
  "username": "usuario1",
  "password": "password123",
  "nombre_completo": "Juan Pérez",
  "email": "juan@email.com"
}
```

**Response (201):**
```json
{
  "mensaje": "Usuario creado exitosamente"
}
```

**Errores:**
- `400` - Faltan datos o usuario ya existe

---

## 🐔 Gestión de Lotes

### Listar Lotes

**GET** `/lotes`

Retorna todos los lotes.

**Headers:**
```
Authorization: Bearer {token}
```

**Response (200):**
```json
[
  {
    "id": 1,
    "nombre": "Lote Enero 2025",
    "fecha_inicio": "2025-01-01",
    "fecha_fin": null,
    "cantidad_inicial": 3000,
    "cantidad_actual": 2920,
    "estado": "activo",
    "genetica": "Cobb 500",
    "proveedor": "Incubadora Regional",
    "galpon": "Galpón 1",
    "dias_transcurridos": 28
  }
]
```

---

### Obtener Lote

**GET** `/lotes/:id`

Retorna un lote específico.

**Response (200):**
```json
{
  "id": 1,
  "nombre": "Lote Enero 2025",
  "fecha_inicio": "2025-01-01",
  "fecha_fin": null,
  "cantidad_inicial": 3000,
  "cantidad_actual": 2920,
  "genetica": "Cobb 500",
  "proveedor": "Incubadora Regional",
  "peso_inicial": 40.0,
  "galpon": "Galpón 1",
  "estado": "activo"
}
```

**Errores:**
- `404` - Lote no encontrado

---

### Crear Lote

**POST** `/lotes`

Crea un nuevo lote.

**Request:**
```json
{
  "nombre": "Lote Enero 2025",
  "fecha_inicio": "2025-01-01",
  "cantidad_inicial": 3000,
  "peso_inicial": 40.0,
  "genetica": "Cobb 500",
  "proveedor": "Incubadora Regional",
  "galpon": "Galpón 1"
}
```

**Response (201):**
```json
{
  "mensaje": "Lote creado exitosamente",
  "id": 1
}
```

**Errores:**
- `400` - Faltan datos requeridos

---

### Actualizar Lote

**PUT** `/lotes/:id`

Actualiza un lote existente.

**Request:**
```json
{
  "nombre": "Lote Enero 2025 - Actualizado",
  "genetica": "Ross 308",
  "galpon": "Galpón 2"
}
```

**Response (200):**
```json
{
  "mensaje": "Lote actualizado exitosamente"
}
```

---

### Cerrar Lote

**POST** `/lotes/:id/cerrar`

Marca un lote como finalizado.

**Response (200):**
```json
{
  "mensaje": "Lote cerrado exitosamente"
}
```

---

### Eliminar Lote

**DELETE** `/lotes/:id`

Elimina un lote y todos sus registros asociados.

**Response (200):**
```json
{
  "mensaje": "Lote eliminado exitosamente"
}
```

---

## 📝 Registros Diarios

### Listar Registros

**GET** `/lotes/:id/registros`

Retorna todos los registros diarios de un lote.

**Response (200):**
```json
[
  {
    "id": 1,
    "fecha": "2025-01-01",
    "alimento_kg": 15.5,
    "agua_litros": 45.0,
    "mortalidad": 5,
    "peso_promedio": 40.0,
    "temperatura_promedio": 32.5,
    "observaciones": "Inicio del lote"
  }
]
```

---

### Crear Registro

**POST** `/lotes/:id/registros`

Crea un nuevo registro diario.

**Request:**
```json
{
  "fecha": "2025-01-02",
  "alimento_kg": 18.2,
  "agua_litros": 52.0,
  "mortalidad": 3,
  "peso_promedio": 55.0,
  "temperatura_promedio": 32.0,
  "observaciones": "Todo normal"
}
```

**Response (201):**
```json
{
  "mensaje": "Registro creado exitosamente",
  "id": 2
}
```

**Errores:**
- `400` - Ya existe registro para esa fecha

---

### Actualizar Registro

**PUT** `/registros/:id`

Actualiza un registro existente.

**Request:**
```json
{
  "alimento_kg": 19.0,
  "observaciones": "Consumo ajustado"
}
```

**Response (200):**
```json
{
  "mensaje": "Registro actualizado exitosamente"
}
```

---

### Eliminar Registro

**DELETE** `/registros/:id`

Elimina un registro.

**Response (200):**
```json
{
  "mensaje": "Registro eliminado exitosamente"
}
```

---

## 💰 Gestión Económica

### Listar Costos

**GET** `/lotes/:id/costos`

Retorna todos los costos de un lote.

**Response (200):**
```json
[
  {
    "id": 1,
    "categoria": "Pollitos",
    "concepto": "Compra de 3000 pollitos BB",
    "monto": 4500000.00,
    "fecha": "2025-01-01",
    "observaciones": "Proveedor: Incubadora Regional"
  }
]
```

---

### Crear Costo

**POST** `/lotes/:id/costos`

Registra un nuevo costo.

**Request:**
```json
{
  "categoria": "Alimento",
  "concepto": "Alimento iniciación 500kg",
  "monto": 850000.00,
  "fecha": "2025-01-01",
  "observaciones": "Primera compra"
}
```

**Categorías válidas:**
- `Pollitos`
- `Alimento`
- `Medicamentos`
- `Energía`
- `Transporte`
- `Mano de Obra`
- `Otro`

**Response (201):**
```json
{
  "mensaje": "Costo registrado exitosamente",
  "id": 1
}
```

---

### Eliminar Costo

**DELETE** `/costos/:id`

Elimina un costo.

---

### Listar Ingresos

**GET** `/lotes/:id/ingresos`

Retorna todos los ingresos de un lote.

---

### Crear Ingreso

**POST** `/lotes/:id/ingresos`

Registra una venta.

**Request:**
```json
{
  "cantidad_vendida": 2900,
  "peso_promedio": 2500,
  "precio_por_kg": 8500,
  "fecha": "2025-02-12",
  "cliente": "Distribuidora XYZ",
  "observaciones": "Venta completa del lote"
}
```

**Response (201):**
```json
{
  "mensaje": "Ingreso registrado exitosamente",
  "id": 1,
  "total": 61625000.00
}
```

---

### Resumen Económico

**GET** `/lotes/:id/resumen-economico`

Retorna un resumen económico del lote.

**Response (200):**
```json
{
  "total_costos": 15650000.00,
  "total_ingresos": 61625000.00,
  "ganancia": 45975000.00,
  "costos_por_categoria": {
    "Pollitos": 4500000.00,
    "Alimento": 8150000.00,
    "Medicamentos": 495000.00,
    "Energía": 450000.00,
    "Mano de Obra": 1200000.00,
    "Transporte": 180000.00,
    "Otro": 250000.00
  },
  "cantidad_ventas": 1
}
```

---

## 💊 Gestión Sanitaria

### Listar Registros Sanitarios

**GET** `/lotes/:id/sanidad`

---

### Crear Registro Sanitario

**POST** `/lotes/:id/sanidad`

**Request:**
```json
{
  "tipo": "Vacuna",
  "producto": "Newcastle + Bronquitis IB",
  "dosis": "Ocular/Nasal",
  "fecha": "2025-01-05",
  "edad_dias": 5,
  "observaciones": "Primera vacunación"
}
```

**Tipos válidos:**
- `Vacuna`
- `Antibiótico`
- `Vitaminas`
- `Desparasitante`
- `Otro`

---

### Eliminar Registro Sanitario

**DELETE** `/sanidad/:id`

---

## 📊 Estadísticas y Análisis

### Obtener Estadísticas del Lote

**GET** `/lotes/:id/estadisticas`

Retorna todas las estadísticas calculadas del lote.

**Response (200):**
```json
{
  "dias_transcurridos": 28,
  "cantidad_actual": 2920,
  "peso_actual": 1527.0,
  "total_alimento": 3780.5,
  "total_agua": 4512.0,
  "total_mortalidad": 80,
  "mortalidad_porcentaje": 2.67,
  "fcr": 1.85,
  "adg": 53.11,
  "kg_producidos": 4338.74,
  "total_costos": 15650000.00,
  "total_ingresos": 0.00,
  "ganancia": -15650000.00,
  "costo_por_kg": 3607.45,
  "costo_por_pollo": 5216.67,
  "rentabilidad": -100.00,
  "consumo_promedio_diario": 135.02,
  "consumo_por_ave": 1295.04,
  "agua_alimento": 1.19
}
```

---

### Curva de Peso

**GET** `/lotes/:id/curva-peso`

Retorna datos para graficar la curva de crecimiento.

**Response (200):**
```json
[
  {
    "fecha": "2025-01-01",
    "peso": 40.0,
    "dias": 0
  },
  {
    "fecha": "2025-01-07",
    "peso": 175.0,
    "dias": 7
  },
  {
    "fecha": "2025-01-14",
    "peso": 478.0,
    "dias": 14
  }
]
```

---

### Curva de Mortalidad

**GET** `/lotes/:id/curva-mortalidad`

Retorna datos de mortalidad acumulada.

**Response (200):**
```json
[
  {
    "fecha": "2025-01-01",
    "mortalidad_diaria": 5,
    "mortalidad_acumulada": 5,
    "porcentaje": 0.17,
    "dias": 0
  }
]
```

---

### Dashboard Principal

**GET** `/dashboard`

Retorna datos del dashboard con todos los lotes activos.

**Response (200):**
```json
{
  "total_lotes_activos": 3,
  "total_aves": 8620,
  "lotes": [
    {
      "id": 1,
      "nombre": "Lote Enero 2025",
      "galpon": "Galpón 1",
      "dias": 28,
      "cantidad": 2920,
      "peso_actual": 1527.0,
      "mortalidad_porcentaje": 2.67,
      "fcr": 1.85,
      "adg": 53.11,
      "ganancia": -15650000.00,
      "rentabilidad": -100.00
    }
  ]
}
```

---

### Alertas del Lote

**GET** `/lotes/:id/alertas`

Retorna alertas basadas en los indicadores del lote.

**Response (200):**
```json
[
  {
    "tipo": "ADVERTENCIA",
    "categoria": "MORTALIDAD",
    "mensaje": "Mortalidad elevada: 5.8%. Monitorear condiciones.",
    "valor": 5.8,
    "prioridad": "media"
  }
]
```

---

### Comparar Lotes

**POST** `/comparar-lotes`

Compara indicadores de múltiples lotes.

**Request:**
```json
{
  "lotes": [1, 2, 3]
}
```

**Response (200):**
```json
[
  {
    "id": 1,
    "nombre": "Lote Enero 2025",
    "fcr": 1.85,
    "adg": 53.11,
    "mortalidad_porcentaje": 2.67,
    "rentabilidad": 293.69,
    "costo_por_kg": 3607.45,
    "dias_transcurridos": 28
  }
]
```

---

### Estadísticas Generales

**GET** `/estadisticas-generales`

Retorna estadísticas generales de todos los lotes.

**Response (200):**
```json
{
  "total_lotes": 10,
  "lotes_activos": 3,
  "lotes_finalizados": 7,
  "total_aves_procesadas": 28500,
  "fcr_promedio": 1.92,
  "mortalidad_promedio": 4.12,
  "rentabilidad_promedio": 24.35
}
```

---

## 📤 Exportación

### Exportar a CSV

**GET** `/lotes/:id/exportar-csv`

Descarga los registros diarios en formato CSV.

**Response (200):**
```
Content-Type: text/csv
Content-Disposition: attachment; filename=lote_Enero_2025_registros.csv

Fecha,Alimento (kg),Agua (L),Mortalidad,Peso (g),Temperatura (°C),Observaciones
2025-01-01,15.5,45.0,5,40.0,32.5,Inicio del lote
2025-01-02,18.2,52.0,3,55.0,32.0,Adaptación normal
...
```

---

## 🔧 Utilidades

### Health Check

**GET** `/health`

Verifica el estado del servidor y la base de datos.

**Response (200):**
```json
{
  "status": "healthy",
  "database": "connected",
  "timestamp": "2025-01-30T15:30:00.000Z"
}
```

---

### Información de la API

**GET** `/`

Retorna información general de la API.

**Response (200):**
```json
{
  "mensaje": "API Sistema Control de Pollos de Engorde",
  "version": "1.0",
  "estado": "activo",
  "endpoints": {
    "auth": "/api/auth/login, /api/auth/register",
    "lotes": "/api/lotes",
    "registros": "/api/lotes/:id/registros",
    "costos": "/api/lotes/:id/costos",
    "sanidad": "/api/lotes/:id/sanidad",
    "estadisticas": "/api/lotes/:id/estadisticas",
    "dashboard": "/api/dashboard"
  }
}
```

---

### Inicializar Base de Datos

**POST** `/init`

Inicializa la base de datos y crea el usuario admin.

**Response (201):**
```json
{
  "mensaje": "Base de datos inicializada exitosamente",
  "usuario": "admin",
  "password": "admin123",
  "advertencia": "Cambiar contraseña en producción"
}
```

**Errores:**
- `400` - Base de datos ya inicializada

---

## 🚨 Códigos de Error

| Código | Significado |
|--------|-------------|
| `200` | OK - Solicitud exitosa |
| `201` | Created - Recurso creado exitosamente |
| `400` | Bad Request - Datos inválidos o faltantes |
| `401` | Unauthorized - Token inválido o expirado |
| `404` | Not Found - Recurso no encontrado |
| `500` | Internal Server Error - Error del servidor |

---

## 📝 Notas

- Todos los endpoints (excepto `/auth/*` y `/init`) requieren autenticación con token JWT
- El token debe enviarse en el header: `Authorization: Bearer {token}`
- Los tokens expiran después de 30 días
- Las fechas deben estar en formato ISO: `YYYY-MM-DD`
- Los montos son números decimales
- La mortalidad se registra en cantidad de aves (número entero)

---

## 🔗 Ejemplos con cURL

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

### Listar Lotes
```bash
curl -X GET http://localhost:5000/api/lotes \
  -H "Authorization: Bearer eyJ0eXAi..."
```

### Crear Lote
```bash
curl -X POST http://localhost:5000/api/lotes \
  -H "Authorization: Bearer eyJ0eXAi..." \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Lote Febrero 2025",
    "fecha_inicio": "2025-02-01",
    "cantidad_inicial": 3500,
    "peso_inicial": 40,
    "genetica": "Cobb 500",
    "galpon": "Galpón 2"
  }'
```

---

**Última actualización:** Enero 2025  
**Versión de la API:** 1.0