# 🐔 Sistema de Control de Pollos de Engorde

Sistema completo, moderno y profesional para gestionar lotes de pollos de engorde, con control de alimentación, peso, mortalidad, sanidad, costos y rentabilidad.

![Version](https://img.shields.io/badge/version-1.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)
![Flask](https://img.shields.io/badge/flask-3.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)

---

## 📋 Características Principales

### ✅ Gestión de Lotes
- Crear, editar y cerrar lotes
- Información completa: genética, proveedor, galpón
- Estados: activo/finalizado
- Historial completo de actividades

### 📊 Registros Diarios
- Alimento y agua consumida
- Mortalidad con causas
- Peso promedio semanal
- Temperatura ambiente
- Observaciones diarias

### 💰 Control Económico
- Costos por categorías (pollitos, alimento, medicamentos, energía, etc.)
- Registro de ingresos por ventas
- Cálculo automático de rentabilidad
- Análisis de costo por kg y por pollo

### 💊 Sanidad
- Calendario de vacunación
- Registro de medicamentos y tratamientos
- Historial sanitario completo

### 📈 Análisis y Estadísticas
- **FCR** (Feed Conversion Ratio)
- **ADG** (Average Daily Gain)
- Mortalidad acumulada
- Curvas de crecimiento
- Dashboard con KPIs
- Sistema de alertas automáticas

### 🎨 Interfaz Moderna
- Diseño responsive (móvil y PC)
- Gráficos interactivos
- Sistema de pestañas intuitivo
- Modales para edición rápida

---

## 🚀 Instalación Rápida (5 minutos)

### Requisitos Previos

- **Python 3.8 o superior** → [Descargar Python](https://www.python.org/downloads/)
- **pip** (viene incluido con Python)
- **Navegador web** (Chrome, Firefox, Edge, Safari)

### Paso 1: Descargar el Proyecto

```bash
# Opción 1: Clonar desde Git
git clone https://github.com/usuario/pollo-control.git
cd pollo-control

# Opción 2: Descargar ZIP y extraer
# Luego abrir terminal en la carpeta extraída
```

### Paso 2: Crear Entorno Virtual (Recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Si hay errores, instalar manualmente:**
```bash
pip install Flask Flask-CORS Flask-SQLAlchemy PyJWT Werkzeug python-dotenv
```

**Dependencias opcionales (para exportar):**
```bash
pip install reportlab openpyxl pandas
```

### Paso 4: Iniciar el Sistema

**Opción A - Script automático (recomendado):**
```bash
python run.py
```

**Opción B - Inicio manual:**
```bash
# Iniciar backend
python app.py

# En otra terminal, iniciar frontend
cd frontend
python -m http.server 8000
```

### Paso 5: Acceder al Sistema

1. **Abrir navegador:** http://localhost:8000
2. **Iniciar sesión:**
   - Usuario: `admin`
   - Contraseña: `admin123`

---

## 📁 Estructura del Proyecto

```
pollo-control/
│
├── backend/
│   ├── app.py                    # ⭐ Aplicación principal Flask
│   ├── config.py                 # Configuración
│   ├── run.py                    # Script de inicio
│   ├── requirements.txt          # Dependencias
│   │
│   ├── services/
│   │   ├── calculos.py          # Cálculos FCR, ADG, etc.
│   │   └── exportar.py          # Exportación PDF/Excel
│   │
│   └── pollo_control.db         # Base de datos SQLite (auto-generada)
│
├── frontend/
│   └── index.html               # ⭐ Aplicación web completa
│
├── database/
│   └── init.sql                 # Script SQL de inicialización
│
├── exports/                     # Archivos exportados (auto-creada)
├── backups/                     # Copias de seguridad (auto-creada)
├── uploads/                     # Archivos subidos (auto-creada)
│
├── .env.example                 # Ejemplo de variables de entorno
├── .gitignore
└── README.md                    # Este archivo
```

---

## 🎯 Uso del Sistema

### 1. Dashboard Principal

Al iniciar sesión verás:
- **Tarjetas de estadísticas**: Lotes activos, total de aves, ganancia, FCR promedio
- **Tabla de lotes activos**: Con información resumida de cada lote
- **Botón "Nuevo Lote"**: Para crear un lote nuevo

### 2. Crear un Nuevo Lote

1. Click en **"Nuevo Lote"**
2. Completar datos:
   - **Nombre del lote** (ej: "Lote Enero 2025")
   - **Fecha de inicio**
   - **Cantidad de pollitos** (ej: 3000)
   - **Peso inicial** (gramos, típicamente 40g)
   - **Genética** (Cobb 500, Ross 308, Hubbard)
   - **Proveedor** (opcional)
   - **Galpón** (opcional)
3. Click en **"Crear Lote"**

### 3. Gestionar un Lote

Click en **"Ver"** en cualquier lote para acceder a:

#### 📊 Pestaña RESUMEN
- Tarjetas con estadísticas principales
- Gráfico de curva de crecimiento
- Indicadores clave de rendimiento

#### 📝 Pestaña REGISTROS DIARIOS
1. Click en **"Nuevo Registro"**
2. Ingresar datos del día:
   - Alimento consumido (kg)
   - Agua consumida (litros)
   - Mortalidad (número de aves)
   - Peso promedio (si corresponde pesaje)
   - Temperatura
   - Observaciones
3. Click en **"Guardar"**

**Tip:** Registrar diariamente para mantener estadísticas precisas.

#### 💰 Pestaña ECONOMÍA
1. Click en **"Nuevo Costo"**
2. Seleccionar categoría:
   - Pollitos
   - Alimento
   - Medicamentos
   - Energía
   - Transporte
   - Mano de Obra
   - Otro
3. Ingresar concepto, monto y fecha
4. Click en **"Guardar"**

El sistema calcula automáticamente:
- Total de costos
- Ganancia
- Rentabilidad %
- Costo por kg y por pollo

#### 💊 Pestaña SANIDAD
1. Click en **"Nuevo Registro Sanitario"**
2. Seleccionar tipo:
   - Vacuna
   - Antibiótico
   - Vitaminas
   - Desparasitante
   - Otro
3. Ingresar producto, dosis, fecha
4. Click en **"Guardar"**

### 4. Cerrar un Lote

Cuando se vende el lote:
1. Ir a la pestaña **Economía**
2. Registrar la venta en **"Ingresos"**
3. En el dashboard principal, cerrar el lote

---

## 📊 Indicadores y Fórmulas

### FCR (Feed Conversion Ratio)
```
FCR = Alimento total consumido (kg) / Ganancia de peso total (kg)
```
**Valores de referencia:**
- Excelente: < 1.7
- Muy bueno: 1.7 - 1.8
- Bueno: 1.8 - 2.0
- Regular: 2.0 - 2.3
- Malo: > 2.3

### ADG (Average Daily Gain)
```
ADG = (Peso final - Peso inicial) / Días del ciclo
```
**Valores de referencia (g/día):**
- Excelente: > 60
- Muy bueno: 55 - 60
- Bueno: 50 - 55
- Regular: 45 - 50
- Malo: < 45

### Mortalidad
```
Mortalidad % = (Aves muertas / Aves iniciales) × 100
```
**Valores de referencia:**
- Excelente: < 3%
- Muy bueno: 3% - 5%
- Aceptable: 5% - 8%
- Alto: > 8%

### Rentabilidad
```
Rentabilidad % = ((Ingresos - Costos) / Costos) × 100
```
**Valores de referencia:**
- Excelente: > 30%
- Muy bueno: 25% - 30%
- Bueno: 20% - 25%
- Regular: 15% - 20%
- Bajo: < 15%

---

## 📱 Acceso desde Móvil

### Mismo WiFi (Red Local)

1. **Obtener IP del computador:**
   ```bash
   # Windows
   ipconfig
   
   # Linux/Mac
   ifconfig
   # o
   ip addr
   ```
   
2. **Buscar dirección IPv4** (ej: 192.168.1.10)

3. **En el móvil abrir:**
   - Frontend: `http://192.168.1.10:8000`
   
4. **Actualizar API_URL en el frontend:**
   - Abrir `frontend/index.html`
   - Buscar: `const API_URL = 'http://localhost:5000/api';`
   - Cambiar por: `const API_URL = 'http://192.168.1.10:5000/api';`

### Internet (Avanzado)

Para acceder desde cualquier lugar, considerar:
- Usar servicios como **ngrok** para túnel seguro
- Desplegar en servidor en la nube (AWS, DigitalOcean, etc.)
- Usar **Heroku** para deployment gratuito

---

## 🔒 Seguridad

### Cambiar Contraseña del Admin

**Método 1 - Desde la aplicación:**
1. Crear nuevo usuario con `POST /api/auth/register`
2. Asignar rol admin en la base de datos
3. Eliminar usuario admin original

**Método 2 - Directamente en base de datos:**
```python
from werkzeug.security import generate_password_hash
# Generar hash de nueva contraseña
new_hash = generate_password_hash('nueva_contraseña_segura')
# Actualizar en la base de datos
```

### Recomendaciones de Seguridad

✅ **En Desarrollo:**
- Usuario admin / admin123 (por defecto)
- Base de datos local SQLite

❌ **En Producción:**
- ⚠️ CAMBIAR contraseña admin inmediatamente
- Usar variables de entorno para SECRET_KEY
- Considerar PostgreSQL en lugar de SQLite
- Implementar HTTPS
- Hacer backups regulares

### Variables de Entorno

Crear archivo `.env`:
```bash
SECRET_KEY=tu-clave-secreta-muy-larga-y-segura
DATABASE_URL=sqlite:///pollo_control.db
FLASK_ENV=production
DEBUG=False
```

---

## 💾 Backup y Restauración

### Backup Manual

La base de datos está en:
```
backend/pollo_control.db
```

**Para hacer backup:**
```bash
# Windows
copy pollo_control.db backups\backup_%date%.db

# Linux/Mac
cp pollo_control.db backups/backup_$(date +%Y%m%d).db
```

### Restaurar Backup

```bash
# Detener el servidor
# Reemplazar archivo
copy backups\backup_20250130.db pollo_control.db
# Reiniciar servidor
```

### Backup Automático (Próximamente)

El sistema incluirá:
- Backup automático semanal
- Sincronización con Google Drive/Dropbox
- Notificaciones de backup completado

---

## 📤 Exportación de Datos

### Exportar a CSV

```bash
GET /api/lotes/{id}/exportar-csv
```

Descarga archivo CSV con todos los registros diarios del lote.

### Exportar a Excel (Requiere openpyxl)

```bash
pip install openpyxl
```

Funcionalidad disponible en próxima actualización.

### Exportar a PDF (Requiere reportlab)

```bash
pip install reportlab
```

Funcionalidad disponible en próxima actualización.

---

## 🛠️ Solución de Problemas

### Error: "Token inválido"

**Solución:**
1. Cerrar sesión
2. Volver a iniciar sesión
3. Limpiar caché del navegador (Ctrl+Shift+Delete)

### Error: "No se puede conectar al servidor"

**Verificar:**
1. El servidor backend está corriendo: `python app.py`
2. El puerto 5000 está libre
3. La URL del API es correcta en el frontend

**Cambiar puerto si está ocupado:**
```bash
# En app.py cambiar:
app.run(host='0.0.0.0', port=5001)  # Usar puerto 5001

# En frontend/index.html cambiar:
const API_URL = 'http://localhost:5001/api';
```

### Error: "Base de datos bloqueada"

**Solución:**
1. Cerrar todas las conexiones
2. Detener el servidor
3. Verificar que no hay otro proceso usando la DB
4. Reiniciar el servidor

### Error al instalar dependencias

**Si falla `pip install`:**
```bash
# Actualizar pip
python -m pip install --upgrade pip

# Instalar una por una
pip install Flask
pip install Flask-CORS
pip install Flask-SQLAlchemy
pip install PyJWT
pip install Werkzeug
```

### Problemas con el navegador

**Solución:**
1. Probar en modo incógnito
2. Limpiar caché y cookies
3. Probar otro navegador
4. Verificar que JavaScript está habilitado

---

## 🚀 Mejoras Futuras

### Fase 1 (1-2 meses)
- [ ] Sistema de alertas por email/SMS
- [ ] Exportación completa PDF/Excel
- [ ] Backup automático programado
- [ ] Comparación entre lotes
- [ ] Reportes avanzados

### Fase 2 (3-6 meses)
- [ ] Predicción de peso con IA
- [ ] Optimización de alimentación
- [ ] Análisis predictivo de mortalidad
- [ ] Integración con WhatsApp

### Fase 3 (6-12 meses)
- [ ] Integración IoT (sensores, básculas)
- [ ] Cámaras con visión artificial
- [ ] Control automático de ambiente
- [ ] App móvil nativa (Android/iOS)

### Fase 4 (12+ meses)
- [ ] Gestión multi-granja
- [ ] Sistema multi-usuario con roles
- [ ] Marketplace de insumos
- [ ] Integración con contabilidad

---

## 📚 API Documentation

### Autenticación

```bash
POST /api/auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "admin123"
}

Response:
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "usuario": {...}
}
```

### Lotes

```bash
# Listar lotes
GET /api/lotes
Authorization: Bearer {token}

# Crear lote
POST /api/lotes
Authorization: Bearer {token}
Content-Type: application/json

{
  "nombre": "Lote Enero 2025",
  "fecha_inicio": "2025-01-01",
  "cantidad_inicial": 3000,
  "peso_inicial": 40,
  "genetica": "Cobb 500",
  "galpon": "Galpón 1"
}
```

**Ver documentación completa en:** `/docs/API.md` (próximamente)

---

## 🤝 Contribuir

¿Quieres mejorar el sistema? ¡Genial!

1. Fork el proyecto
2. Crear rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit cambios: `git commit -m 'Agregar nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abrir Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

---

## 👨‍💻 Autor

Desarrollado con ❤️ para la industria avícola

**Contacto:**
- Email: soporte@ejemplo.com
- GitHub: [@usuario](https://github.com/usuario)

---

## ⭐ Agradecimientos

Gracias por usar el Sistema de Control de Pollos de Engorde.

Si te ha sido útil, considera:
- ⭐ Dar una estrella al proyecto
- 🐛 Reportar bugs
- 💡 Sugerir mejoras
- 📢 Compartir con otros avicultores

---

## 📞 Soporte

¿Necesitas ayuda?

- 📧 Email: soporte@ejemplo.com
- 💬 Issues: [GitHub Issues](https://github.com/usuario/pollo-control/issues)
- 📖 Wiki: [Documentación completa](https://github.com/usuario/pollo-control/wiki)

---

**¡Éxito en tu producción avícola!** 🐔🎉#   P o l l o - C o n t r o l - E n g o r d e  
 