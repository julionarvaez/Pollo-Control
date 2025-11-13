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
echo "║        🐔  SISTEMA DE CONTROL DE POLLOS 🐔                ║"
echo "║                                                          ║"
echo "║                  Iniciando Sistema...                    ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo -e "${RED}❌ Entorno virtual no encontrado${NC}"
    echo
    echo "Por favor ejecutar primero: ./install.sh"
    echo
    exit 1
fi

# Activar entorno virtual
source venv/bin/activate

echo -e "${GREEN}✅ Entorno virtual activado${NC}"
echo
echo -e "${BLUE}🚀 Iniciando servidor backend...${NC}"
echo
echo "═══════════════════════════════════════════════════════════"
echo
echo -e "${GREEN}🌐 Acceso al sistema:${NC}"
echo "   • Frontend: http://localhost:8000"
echo "   • Backend API: http://localhost:5000"
echo
echo -e "${GREEN}🔐 Credenciales:${NC}"
echo "   • Usuario: admin"
echo "   • Contraseña: admin123"
echo
echo "═══════════════════════════════════════════════════════════"
echo
echo -e "${YELLOW}⚠️  Para detener el servidor presiona CTRL+C${NC}"
echo
echo "═══════════════════════════════════════════════════════════"
echo

# Función para manejar CTRL+C
function cleanup {
    echo
    echo
    echo -e "${YELLOW}🛑 Deteniendo servidor...${NC}"
    kill $FRONTEND_PID 2>/dev/null
    kill $BACKEND_PID 2>/dev/null
    echo -e "${GREEN}✅ Servidor detenido${NC}"
    echo
    exit 0
}

trap cleanup SIGINT SIGTERM

# Iniciar frontend en segundo plano
cd frontend
python3 -m http.server 8000 > /dev/null 2>&1 &
FRONTEND_PID=$!
cd ..

# Iniciar backend
cd backend
python3 run.py
BACKEND_PID=$!

wait $BACKEND_PID