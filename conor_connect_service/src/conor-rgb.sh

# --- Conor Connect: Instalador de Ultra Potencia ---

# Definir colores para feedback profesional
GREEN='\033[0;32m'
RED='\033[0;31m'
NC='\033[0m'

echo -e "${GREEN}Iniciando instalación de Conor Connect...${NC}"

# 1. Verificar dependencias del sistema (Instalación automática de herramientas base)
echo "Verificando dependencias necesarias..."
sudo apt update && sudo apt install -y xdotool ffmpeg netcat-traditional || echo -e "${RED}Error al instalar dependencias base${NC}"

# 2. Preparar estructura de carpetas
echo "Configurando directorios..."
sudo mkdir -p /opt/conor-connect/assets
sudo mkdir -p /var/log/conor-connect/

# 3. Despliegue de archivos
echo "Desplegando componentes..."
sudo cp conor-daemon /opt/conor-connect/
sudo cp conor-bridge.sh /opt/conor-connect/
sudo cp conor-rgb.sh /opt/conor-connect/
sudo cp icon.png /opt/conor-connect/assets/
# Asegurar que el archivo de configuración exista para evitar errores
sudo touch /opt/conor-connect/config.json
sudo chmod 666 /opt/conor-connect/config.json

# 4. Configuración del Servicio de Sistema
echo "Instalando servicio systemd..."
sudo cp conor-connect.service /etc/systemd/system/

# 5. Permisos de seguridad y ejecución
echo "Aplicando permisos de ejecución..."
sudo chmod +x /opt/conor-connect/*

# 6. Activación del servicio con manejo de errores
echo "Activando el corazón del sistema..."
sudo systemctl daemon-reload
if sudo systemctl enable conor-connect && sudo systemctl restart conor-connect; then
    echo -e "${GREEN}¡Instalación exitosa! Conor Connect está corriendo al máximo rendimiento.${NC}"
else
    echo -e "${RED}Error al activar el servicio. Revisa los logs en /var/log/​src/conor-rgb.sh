#!/bin/bash

# --- Conor Connect: Instalador de Ultra Potencia ---

# Definir colores para feedback profesional
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}Iniciando instalación de Conor Connect...${NC}"

# 1. Verificar dependencias del sistema (Instalación automática de herramientas base)
echo "Verificando dependencias necesarias..."
sudo apt update && sudo apt install -y xdotool ffmpeg netcat-traditional || echo -e "${RED}Error al instalar dependencias base${NC}"

# 2. Preparar estructura de carpetas
echo "Configurando directorios..."
sudo mkdir -p /opt/conor-connect/assets
sudo mkdir -p /var/log/conor-connect/

# 3. Despliegue de archivos
echo "Desplegando componentes..."
sudo cp conor-daemon /opt/conor-connect/
sudo cp conor-bridge.sh /opt/conor-connect/
sudo cp conor-rgb.sh /opt/conor-connect/
sudo cp icon.png /opt/conor-connect/assets/
# Asegurar que el archivo de configuración exista para evitar errores
sudo touch /opt/conor-connect/config.json
sudo chmod 666 /opt/conor-connect/config.json

# 4. Configuración del Servicio de Sistema
echo "Instalando servicio systemd..."
sudo cp conor-connect.service /etc/systemd/system/

# 5. Permisos de seguridad y ejecución
echo "Aplicando permisos de ejecución..."
sudo chmod +x /opt/conor-connect/*

# 6. Activación del servicio con manejo de errores
echo "Activando el corazón del sistema..."
sudo systemctl daemon-reload
if sudo systemctl enable conor-connect && sudo systemctl restart conor-connect; then
    echo -e "${GREEN}¡Instalación exitosa! Conor Connect está corriendo al máximo rendimiento.${NC}"
else
    echo -e "${RED}Error al activar el servicio. Revisa los logs en /var/log/syslog${NC}"
fi
