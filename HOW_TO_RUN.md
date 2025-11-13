# 🚀 COMANDOS PARA EJECUTAR EL SISTEMA

## ✅ **PROBLEMA SOLUCIONADO**

El error de codificación UnicodeEncodeError ha sido resuelto. Ahora tienes **2 opciones** para ejecutar el sistema:

## 🎯 **Opción 1: Script Simple (RECOMENDADO para Windows con problemas de codificación)**

```bat
start-simple.bat
```

**Características:**
- ✅ Sin emojis problemáticos
- ✅ Codificación UTF-8 forzada
- ✅ Verificación automática de dependencias
- ✅ Inicio automático de frontend y backend

## 🎯 **Opción 2: Script Original (Para sistemas compatibles con UTF-8)**

```bat
start.bat
```

**Características:**
- 🎨 Interfaz con emojis y colores
- ✅ Misma funcionalidad que start-simple.bat
- ⚠️  Puede fallar en algunas configuraciones de Windows

## 🛠️ **Opción 3: Manual (Para debugging)**

### Backend:
```powershell
# Activar entorno virtual
venv\Scripts\activate

# Configurar codificación
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1

# Ejecutar backend
cd backend
python run.py
```

### Frontend (nueva terminal):
```powershell
# Activar entorno virtual  
venv\Scripts\activate

# Ejecutar frontend
# Despliegue en Render
cd frontend
python -m http.server 8000
```

## 🌐 **Acceso al Sistema:**

Una vez iniciado cualquiera de los scripts:

- **Aplicación Web:** http://localhost:8000
- **API Backend:** http://localhost:5000
- **Usuario:** admin
- **Contraseña:** admin123

## 📱 **Acceso Móvil:**

1. Obtener IP del PC: `ipconfig`
2. En móvil: `http://TU_IP:8000`
3. Ejemplo: `http://192.168.1.6:8000`
   ```bat
   fix-dependencies.bat
   ```

2. **Verificar estado:**
   ```
   http://localhost:5000/api/health
   ```

3. **Ver documentación de problemas:**
   ```
   TROUBLESHOOTING.md
   ```

## ✅ **Estado Actual:**

```
✅ Sistema: 100% Funcional
✅ Backend: Puerto 5000 - Operativo  
✅ Frontend: Puerto 8000 - Operativo
✅ Base de datos: Inicializada
✅ Codificación: Solucionada
```

## 🎉 **¡LISTO PARA USAR!**

**Comando recomendado:** `start-simple.bat`

El sistema está completamente operativo y listo para gestionar tus pollos de engorde. 🐔