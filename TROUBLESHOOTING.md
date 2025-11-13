# 🔧 Guía de Solución de Problemas - Sistema de Control de Pollos

## 🚨 Problemas Comunes y Soluciones

### 1. Error: "ERR_CONNECTION_REFUSED" (Puerto 5000)

**Síntomas:**
- El navegador muestra "ERR_CONNECTION_REFUSED"
- Error al conectar con `:5000/api/auth/login`

**Soluciones:**

#### Opción A: Reparación Automática
```bat
# Ejecutar el reparador automático
fix-dependencies.bat
```

#### Opción B: Reparación Manual
1. **Verificar entorno virtual:**
   ```bat
   # Si no existe venv, ejecutar:
   install.bat
   ```

2. **Activar entorno e instalar dependencias:**
   ```bat
   venv\Scripts\activate
   pip install Flask==3.0.0 Flask-CORS==4.0.0 Flask-SQLAlchemy==3.1.1
   pip install PyJWT==2.8.0 Werkzeug==3.0.1 python-dotenv==1.0.0
   pip install reportlab==4.0.7 openpyxl==3.1.2
   ```

3. **Ejecutar manualmente:**
   ```bat
   cd backend
   ..\venv\Scripts\python run.py
   ```

### 2. Error: "Pandas installation failed"

**Síntomas:**
- Error durante `pip install pandas`
- Mensaje sobre compilador C faltante

**Solución:**
```bat
# Pandas es OPCIONAL - el sistema funciona sin él
# Para instalarlo en Windows necesitas:
# 1. Visual Studio Build Tools 2019+
# 2. O usar una versión precompilada:
pip install pandas --only-binary=all
```

### 3. Error: "Puerto 5000 en uso"

**Síntomas:**
- "Address already in use"
- "Port 5000 is already in use"

**Soluciones:**
```bat
# Encontrar proceso usando puerto 5000:
netstat -ano | findstr :5000

# Terminar proceso (reemplazar PID):
taskkill /PID <numero_pid> /F

# O cambiar puerto en config.py:
# PORT = 5001
```

### 4. Error: "Frontend no carga"

**Síntomas:**
- Página en blanco en localhost:8000
- Error 404 o similar

**Soluciones:**
```bat
# Iniciar frontend manualmente:
cd frontend
python -m http.server 8000

# O usar otro puerto:
python -m http.server 8080
```

### 5. Error: "Base de datos no encontrada"

**Síntomas:**
- Error SQLite
- No se pueden guardar datos

**Solución:**
```bat
# El sistema auto-crea la BD, pero si falla:
cd backend
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

## 🛠️ Comandos de Diagnóstico

### Verificar instalación completa:
```bat
# Verificar Python
python --version

# Verificar dependencias
cd backend
python -c "import flask, flask_cors, flask_sqlalchemy; print('OK')"

# Verificar puertos
netstat -ano | findstr ":5000\|:8000"
```

### Reinstalación completa:
```bat
# 1. Borrar entorno actual
rmdir /s /q venv

# 2. Reinstalar todo
install.bat

# 3. Iniciar sistema
start.bat
```

## 📱 Acceso desde Móvil

1. **Obtener IP del PC:**
   ```bat
   ipconfig
   # Buscar "Dirección IPv4" (ej: 192.168.1.100)
   ```

2. **En el móvil:**
   - Abrir: `http://TU_IP:8000`
   - Ejemplo: `http://192.168.1.100:8000`

3. **Si no funciona, editar frontend/js/config.js:**
   ```javascript
   // Cambiar de:
   const API_URL = 'http://localhost:5000/api';
   
   // A:
   const API_URL = 'http://192.168.1.100:5000/api';
   ```

## 🔐 Credenciales por Defecto

- **Usuario:** admin
- **Contraseña:** admin123

## 📞 Soporte Adicional

Si los problemas persisten:

1. **Verificar requisitos del sistema:**
   - Windows 10/11
   - Python 3.8 o superior
   - 4GB RAM disponible
   - Conexión a internet (para instalar dependencias)

2. **Ejecutar como Administrador:**
   - Click derecho en `install.bat` → "Ejecutar como administrador"

3. **Firewall/Antivirus:**
   - Permitir puertos 5000 y 8000
   - Agregar excepción para Python.exe

4. **Logs detallados:**
   ```bat
   cd backend
   python run.py > debug.log 2>&1
   # Revisar debug.log para errores específicos
   ```