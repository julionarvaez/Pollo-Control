@echo off
chcp 65001 > nul
color 0B
cls

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║                                                          ║
echo ║        🐔  SISTEMA DE CONTROL DE POLLOS 🐔                ║
echo ║                                                          ║
echo ║                  Iniciando Sistema...                    ║
echo ║                                                          ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

REM Verificar si existe el entorno virtual
if not exist venv (
    echo ❌ Entorno virtual no encontrado
    echo.
    echo Por favor ejecutar primero: install.bat
    echo.
    pause
    exit /b 1
)

REM Activar entorno virtual
call venv\Scripts\activate.bat

echo ✅ Entorno virtual activado
echo.
echo 🚀 Iniciando servidor backend...
echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo 🌐 Acceso al sistema:
echo    • Backend API: http://127.0.0.1:5000
echo    • Frontend: http://127.0.0.1:8000
echo.
echo 🔐 Credenciales:
echo    • Usuario: admin
echo    • Contraseña: admin123
echo.
echo ═══════════════════════════════════════════════════════════
echo.
echo ⚠️  Para detener el servidor presiona CTRL+C
echo.
echo ═══════════════════════════════════════════════════════════
echo.

REM Iniciar backend y frontend
echo 🔧 Verificando dependencias...
echo.

REM Verificar e instalar todas las dependencias desde requirements.txt
if exist backend\requirements.txt (
    echo 📦 Instalando dependencias desde requirements.txt...
    call venv\Scripts\pip.exe install -q -r backend\requirements.txt
    echo ✅ Dependencias instaladas
    echo.
) else (
    echo ⚠️  Archivo requirements.txt no encontrado, instalando dependencias básicas...
    call venv\Scripts\pip.exe install -q Flask==3.0.0 Flask-CORS==4.0.0 Flask-SQLAlchemy==3.1.1 PyJWT==2.8.0 Werkzeug==3.0.1 python-dotenv==1.0.0 qrcode[pil]==7.4.2
    echo ✅ Dependencias básicas instaladas
    echo.
)

echo.
echo 🚀 Iniciando servidores...

REM Asegurar variables de entorno para backend
set FLASK_ENV=development
set HOST=0.0.0.0
set PORT=5000
set RELOAD=1

REM Iniciar frontend en ventana separada
start "Servidor Frontend - Puerto 8000" cmd /k "chcp 65001 && cd /d "%~dp0frontend" && set PYTHONIOENCODING=utf-8 && "%~dp0venv\Scripts\python.exe" -m http.server 8000 --bind 127.0.0.1"

REM Esperar un momento para que el frontend inicie
timeout /t 2 >nul

REM Iniciar backend con codificación UTF-8 y autoreload
cd backend
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
"%~dp0venv\Scripts\python.exe" run.py

pause