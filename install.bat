@echo off
chcp 65001 > nul
color 0A
cls

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║                                                          ║
echo ║     🐔  INSTALADOR - CONTROL DE POLLOS DE ENGORDE 🐔     ║
echo ║                                                          ║
echo ║                  Versión 1.0 - 2025                      ║
echo ║                                                          ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

timeout /t 2 >nul

echo [1/6] Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python no está instalado
    echo.
    echo Por favor instalar Python 3.8 o superior desde:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
) else (
    python --version
    echo ✅ Python detectado
)

echo.
echo [2/6] Creando entorno virtual...
if exist venv (
    echo ⚠️  El entorno virtual ya existe, omitiendo...
) else (
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Error al crear entorno virtual
        pause
        exit /b 1
    )
    echo ✅ Entorno virtual creado
)

echo.
echo [3/6] Activando entorno virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Error al activar entorno virtual
    pause
    exit /b 1
)
echo ✅ Entorno virtual activado

echo.
echo [4/6] Actualizando pip...
python -m pip install --upgrade pip --quiet
echo ✅ pip actualizado

echo.
echo [5/6] Instalando dependencias...
echo    Esto puede tomar algunos minutos...
echo.
pip install -r backend\requirements.txt --quiet
if errorlevel 1 (
    echo ❌ Error al instalar dependencias
    echo.
    echo Intentando instalar manualmente...
    pip install Flask Flask-CORS Flask-SQLAlchemy PyJWT Werkzeug python-dotenv reportlab openpyxl pandas SQLAlchemy qrcode Pillow gunicorn psycopg2-binary
)
echo ✅ Dependencias instaladas

echo.
echo [6/6] Creando carpetas necesarias...
if not exist "database" mkdir database
if not exist "exports" mkdir exports
if not exist "backups" mkdir backups
if not exist "uploads" mkdir uploads
echo ✅ Carpetas creadas

echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo ✅ ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!
echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo 📝 PRÓXIMOS PASOS:
echo.
echo    1. Ejecutar: start.bat
echo    2. Abrir navegador en: http://localhost:8000
echo    3. Iniciar sesión:
echo       • Usuario: admin
echo       • Contraseña: admin123
echo.
echo ═══════════════════════════════════════════════════════════
echo.
pause