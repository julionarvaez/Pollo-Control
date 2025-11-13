#!/bin/bash

# Colores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

clear

echo -e "${BLUE}"
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║     🐔  INSTALADOR - CONTROL DE POLLOS DE ENGORDE 🐔     ║"
echo "║                                                          ║"
echo "║                  Versión 1.0 - 2025                      ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo

sleep 1

echo -e "${BLUE}[1/6]${NC} Verificando Python..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python3 no está instalado${NC}"
    echo
    echo "Por favor instalar Python 3.8 o superior:"
    echo "  • Ubuntu/Debian: sudo apt install python3 python3-venv python3-pip"
    echo "  • macOS: brew install python3"
    echo "  • Fedora: sudo dnf install python3"
    exit 1
else
    python3 --version
    echo -e "${GREEN}✅ Python detectado${NC}"
fi

echo
echo -e "${BLUE}[2/6]${NC} Creando entorno virtual..."
if [ -d "venv" ]; then
    echo -e "${YELLOW}⚠️  El entorno virtual ya existe, omitiendo...${NC}"
else
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo -e "${RED}❌ Error al crear entorno virtual${NC}"
        exit 1
    fi
    echo -e "${GREEN}✅ Entorno virtual creado${NC}"
fi

echo
echo -e "${BLUE}[3/6]${NC} Activando entorno virtual..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error al activar entorno virtual${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Entorno virtual activado${NC}"

echo
echo -e "${BLUE}[4/6]${NC} Actualizando pip..."
pip install --upgrade pip --quiet
echo -e "${GREEN}✅ pip actualizado${NC}"

echo
echo -e "${BLUE}[5/6]${NC} Instalando dependencias..."
echo "   Esto puede tomar algunos minutos..."
echo
pip install -r requirements.txt --quiet
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error al instalar dependencias${NC}"
    echo
    echo "Intentando instalar manualmente..."
    pip install Flask Flask-CORS Flask-SQLAlchemy PyJWT Werkzeug python-dotenv
fi
echo -e "${GREEN}✅ Dependencias instaladas${NC}"

echo
echo -e "${BLUE}[6/6]${NC} Creando carpetas necesarias..."
mkdir -p database exports backups uploads
echo -e "${GREEN}✅ Carpetas creadas${NC}"

echo
echo "═══════════════════════════════════════════════════════════"
echo
echo -e "${GREEN}✅ ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!${NC}"
echo
echo "═══════════════════════════════════════════════════════════"
echo
echo "📝 PRÓXIMOS PASOS:"
echo
echo "   1. Ejecutar: ./start.sh"
echo "   2. Abrir navegador en: http://localhost:8000"
echo "   3. Iniciar sesión:"
echo "      • Usuario: admin"
echo "      • Contraseña: admin123"
echo
echo "═══════════════════════════════════════════════════════════"
echo

# Hacer ejecutables los scripts
chmod +x start.sh
chmod +x stop.sh

read -p "Presiona ENTER para continuar..."