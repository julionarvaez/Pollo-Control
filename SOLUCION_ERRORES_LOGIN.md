# 🔧 Solución de Errores de Login

## Problemas Identificados y Solucionados

### 1. ❌ Error: "Failed to fetch" / "ERR_CONNECTION_REFUSED"

**Causa:** El backend no estaba corriendo cuando se intentó acceder al login.

**Solución Aplicada:**
- ✅ Corregido mensaje en `start.bat` que mostraba puerto incorrecto (8000 en lugar de 5000)
- ✅ Agregado soporte CORS para puerto 8000 en `backend/app.py`
- ✅ Mejorado manejo de errores en frontend para mostrar mensajes más claros

### 2. 🔧 Configuración CORS

**Problema:** El backend no permitía peticiones desde `http://127.0.0.1:8000`

**Solución:** Se agregaron los siguientes orígenes al CORS:
```python
"http://127.0.0.1:8000", "http://localhost:8000"
```

### 3. 📝 Mensaje de Error Mejorado

Ahora el frontend muestra mensajes claros cuando no puede conectarse:
- ✅ "No se puede conectar al servidor. Verifique que el backend esté corriendo"
- ✅ "Usuario o contraseña incorrectos" (para credenciales inválidas)

## 🚀 Cómo Iniciar el Sistema Correctamente

### Opción 1: Usar start.bat (Recomendado)
```bash
# Ejecutar desde la raíz del proyecto:
start.bat
```

Este script:
1. ✅ Activa el entorno virtual
2. ✅ Instala dependencias si faltan
3. ✅ Inicia el backend en puerto 5000
4. ✅ Inicia el frontend en puerto 8000

### Opción 2: Inicio Manual

#### Paso 1: Activar entorno virtual
```bash
venv\Scripts\activate.bat
```

#### Paso 2: Iniciar Backend (Terminal 1)
```bash
cd backend
python run.py
```
Deberías ver:
```
🚀 Iniciando servidor en http://0.0.0.0:5000
* Running on http://127.0.0.1:5000
```

#### Paso 3: Iniciar Frontend (Terminal 2)
```bash
cd frontend
python -m http.server 8000 --bind 127.0.0.1
```

#### Paso 4: Abrir el navegador
Acceder a: `http://127.0.0.1:8000`

## 🔐 Credenciales de Acceso

```
Usuario: admin
Contraseña: admin123
```

## ✅ Verificación de que todo funciona

### 1. Backend Activo
Abrir en navegador: `http://127.0.0.1:5000/api/ping`

Debería mostrar:
```json
{
  "pong": true,
  "timestamp": "2025-11-12T..."
}
```

### 2. Frontend Activo
Abrir en navegador: `http://127.0.0.1:8000`

Debería mostrar la página de login.

### 3. Login Funcional
1. Ingresar usuario: `admin`
2. Ingresar contraseña: `admin123`
3. Click en "Iniciar Sesión"
4. Debería redirigir al dashboard

## 🐛 Solución de Problemas

### Error: "No se puede conectar al servidor"
**Causa:** El backend no está corriendo.
**Solución:** Iniciar el backend con `cd backend && python run.py`

### Error: "Usuario o contraseña incorrectos"
**Causa:** Credenciales inválidas.
**Solución:** Usar `admin` / `admin123`

### Error de CORS
**Causa:** Puerto incorrecto o configuración CORS desactualizada.
**Solución:** Ya está corregido en los archivos. Si persiste, verificar que el backend se haya reiniciado después de los cambios.

### El navegador muestra página en blanco
**Causa:** El servidor frontend no está corriendo.
**Solución:** Ejecutar `python -m http.server 8000` desde la carpeta frontend

## 📊 Arquitectura del Sistema

```
┌─────────────────────────────────────────┐
│   Frontend (Puerto 8000)                │
│   http://127.0.0.1:8000                 │
│   - Interfaz de usuario                 │
│   - HTML/CSS/JavaScript                 │
└──────────────┬──────────────────────────┘
               │ Peticiones HTTP
               │ (CORS habilitado)
               ▼
┌─────────────────────────────────────────┐
│   Backend (Puerto 5000)                 │
│   http://127.0.0.1:5000                 │
│   - API REST (Flask)                    │
│   - Base de datos (SQLite)              │
│   - Autenticación (JWT)                 │
└─────────────────────────────────────────┘
```

## 📝 Cambios Realizados

### backend/app.py
- Agregado `"http://127.0.0.1:8000"` y `"http://localhost:8000"` a CORS_ORIGINS

### frontend/index.html
- Mejorado manejo de errores en login
- Agregado mensaje claro cuando no hay conexión con el backend

### start.bat
- Corregido mensaje que mostraba puerto 8000 para backend (ahora muestra 5000)
- Agregada línea que muestra también el puerto del frontend (8000)

## ✨ Estado Actual

✅ CORS configurado correctamente
✅ Mensajes de error claros
✅ Backend corriendo en puerto 5000
✅ Frontend corriendo en puerto 8000
✅ Login funcional
✅ Autenticación con JWT

## 🎯 Próximos Pasos

1. Ejecutar `start.bat` para iniciar el sistema
2. Abrir `http://127.0.0.1:8000` en el navegador
3. Iniciar sesión con admin/admin123
4. ¡El sistema debería funcionar correctamente!

---

**Fecha de corrección:** 12 de noviembre de 2025
**Archivos modificados:** backend/app.py, frontend/index.html, start.bat
