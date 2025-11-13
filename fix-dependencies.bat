@echo off
chcp 65001 > nul
color 0C
cls

echo.
echo ╔══════════════════════════════════════════════════════════╗
echo ║                                                          ║
echo ║     🔧  REPARADOR DE DEPENDENCIAS - POLLO CONTROL 🔧     ║
echo ║                                                          ║
echo ║            Solucionando problemas comunes...            ║
echo ║                                                          ║
echo ╚══════════════════════════════════════════════════════════╝
echo.

REM Verificar si existe el entorno virtual
if not exist venv (
    echo ❌ Entorno virtual no encontrado
    echo.
    echo Ejecutando instalación completa...
    echo.
    call install.bat
    if errorlevel 1 (
        echo ❌ Error en la instalación
        pause
        exit /b 1
    )
)

echo ✅ Activando entorno virtual...
call venv\Scripts\activate.bat

echo.
echo 🔍 Verificando estado de Python...
python --version
if errorlevel 1 (
    echo ❌ Python no encontrado en el entorno virtual
    echo.
    echo Reinstalando entorno virtual...
    rmdir /s /q venv
    call install.bat
    pause
    exit /b 1
)

echo.
echo 🧹 Limpiando instalaciones anteriores problemáticas...
pip uninstall -y pandas numpy scipy matplotlib

echo.
echo 📦 Instalando dependencias críticas...
pip install --upgrade pip
pip install Flask==3.0.0
pip install Flask-CORS==4.0.0  
pip install Flask-SQLAlchemy==3.1.1
pip install PyJWT==2.8.0
pip install Werkzeug==3.0.1
pip install python-dotenv==1.0.0

echo.
echo 📊 Instalando dependencias de exportación...
pip install reportlab==4.0.7
pip install openpyxl==3.1.2

echo.
echo 🏥 Verificando instalación...
python -c "
try:
    import flask
    import flask_cors
    import flask_sqlalchemy
    import jwt
    import werkzeug
    import reportlab
    import openpyxl
    print('✅ Todas las dependencias críticas instaladas correctamente')
except ImportError as e:
    print(f'❌ Error de importación: {e}')
    exit(1)
"

if errorlevel 1 (
    echo.
    echo ❌ Aún hay problemas con las dependencias
    echo 💡 Intentar:
    echo    1. Reinstalar Python desde python.org
    echo    2. Ejecutar como Administrador
    echo    3. Verificar conexión a internet
    pause
    exit /b 1
)

echo.
echo ✅ ¡Dependencias reparadas exitosamente!
echo.
echo 🚀 Puedes ahora ejecutar: start.bat
echo.
pause