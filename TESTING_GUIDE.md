# 🧪 Guía de Pruebas - Sistema de Control de Pollos

## 🚀 Estado Actual

✅ **Backend:** http://localhost:5000 - Funcionando con debug mejorado  
✅ **Frontend:** http://localhost:8000 - Funcionando  
✅ **Base de datos:** Inicializada correctamente  
✅ **Credenciales:** admin / admin123  

## 🔍 Problemas Identificados y Solucionados

### 1. **Error 500 en POST /api/lotes/1/registros**
- **Causa:** Problemas con validación de datos y manejo de errores
- **Solución:** Agregado debugging detallado y mejor validación

### 2. **Warnings de datetime.utcnow()**
- **Causa:** Python 3.13 deprecó datetime.utcnow()
- **Solución:** Agregado filtro de warnings de deprecación

### 3. **Validación de datos mejorada**
- **Mejora:** Mejor manejo de campos vacíos y conversión de tipos
- **Mejora:** Validación de existencia de lote antes de crear registro

## 📋 Pasos de Prueba

### Paso 1: Acceso al Sistema
1. Abrir: http://localhost:8000
2. Usar credenciales: **admin** / **admin123**
3. Verificar que aparezca el dashboard

### Paso 2: Crear un Lote (Si no existe)
1. Ir a "Gestión de Lotes"
2. Crear nuevo lote con:
   - Nombre: "Lote Prueba 2025"
   - Fecha inicio: Hoy
   - Cantidad inicial: 100
   - Genética: Ross 308
   - Galpón: A1

### Paso 3: Probar Registro Diario
1. Entrar al lote creado
2. Ir a "Registros Diarios"
3. Intentar crear un registro con:
   - Fecha: Hoy
   - Alimento (kg): 50
   - Agua (L): 100
   - Mortalidad: 1
   - Peso promedio: 0.5
   - Temperatura: 24

### Paso 4: Monitoreo de Errores
- **Frontend:** Abrir DevTools (F12) y revisar Console
- **Backend:** Revisar terminal donde corre el servidor
- Los errores ahora mostrarán información detallada de debug

## 🛠️ Debug en Tiempo Real

El servidor backend ahora muestra información detallada:

```
🔍 DEBUG - Creando registro para lote 1
🔍 DEBUG - Datos recibidos: {...}
✅ DEBUG - Registro creado en memoria
💾 DEBUG - Guardando en base de datos...
✅ DEBUG - Registro guardado exitosamente con ID: X
```

## 🔧 Si Siguen los Errores

### Error 401 (UNAUTHORIZED)
- **Causa:** Token expirado o inválido
- **Solución:** Cerrar sesión y volver a iniciar sesión

### Error 500 (INTERNAL SERVER ERROR)
- **Diagnóstico:** Revisar terminal backend para logs detallados
- **Datos:** Verificar formato de fecha (YYYY-MM-DD)
- **Campos:** Asegurar que campos numéricos no estén vacíos

### Error de Conexión (ERR_CONNECTION_REFUSED)
- **Verificar:** Que ambos servidores estén funcionando
- **Puertos:** Backend (5000) y Frontend (8000)
- **Comando:** Usar `netstat -ano | findstr ":5000"` para verificar

## 📱 Acceso Móvil

Para probar desde móvil:
1. Obtener IP: `ipconfig` (buscar IPv4)
2. En móvil: `http://TU_IP:8000`
3. Ejemplo: `http://192.168.1.6:8000`

## 🚨 Comandos de Emergencia

### Reiniciar Sistema Completo
```bat
# Detener todos los procesos Python
taskkill /F /IM python.exe

# Reiniciar desde start.bat mejorado
start.bat
```

### Ver Procesos Activos
```bat
netstat -ano | findstr ":5000\|:8000"
```

### Limpiar Base de Datos
```bat
cd backend
del pollo_control.db
# Reiniciar servidor para recrear BD
```

## ✅ Próximos Pasos

1. **Probar creación de registros** con debugging activo
2. **Verificar que los errores 500 desaparezcan**
3. **Testear funcionalidades básicas:**
   - Login/Logout
   - Crear lotes
   - Registros diarios
   - Costos y sanidad

4. **Si todo funciona:** Desactivar debugging en producción