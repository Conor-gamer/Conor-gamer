#!/bin/bash

# --- Conor Connect: Instalador de Ultra Potencia (Final y Profesional) ---

# Definir colores para feedback profesional
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

# Asegurar que el script sepa dónde está trabajando
cd "$(dirname "$0")"

echo -e "${GREEN}Iniciando instalación total de Conor Connect...${NC}"

# 1. Actualización profunda y dependencias
echo "Actualizando sistema y verificando dependencias..."
sudo apt update && sudo apt upgrade -y && sudo apt install -y xdotool ffmpeg netcat-traditional || { echo -e "${RED}Error en la actualización o instalación de dependencias${NC}"; exit 1; }

# 2. Preparar estructura de carpetas
echo "Configurando directorios..."
sudo mkdir -p /opt/conor-connect/assets
sudo mkdir -p /var/log/conor-connect/

# --- Preparación del archivo de LOG ---
sudo touch /var/log/conor-connect/conor.log
sudo chmod 666 /var/log/conor-connect/conor.log

# 3. Despliegue de archivos
echo "Desplegando componentes..."
sudo cp src/conor-daemon /opt/conor-connect/
sudo cp src/conor-bridge.sh /opt/conor-connect/
sudo cp src/conor-rgb.sh /opt/conor-connect/
sudo cp src/conor-gui.py /opt/conor-connect/
sudo cp assets/icon.png /opt/conor-connect/assets/
sudo cp assets/boton_apk.png /opt/conor-connect/assets/

# Asegurar configuración
sudo touch /opt/conor-connect/config.json
sudo chmod 666 /opt/conor-connect/config.json

# 4. Configuración del Servicio
echo "Instalando servicio systemd..."
sudo cp systemd/conor-connect.service /etc/systemd/system/

# 5. Permisos de ejecución
echo "Aplicando permisos..."
sudo chmod +x /opt/conor-connect/*

# 6. Activación del servicio
echo "Activando el corazón del sistema..."
sudo systemctl daemon-reload
if sudo systemctl enable conor-connect && sudo systemctl restart conor-connect; then
    echo -e "${GREEN}¡Instalación exitosa! Conor Connect está corriendo al máximo rendimiento.${NC}"
else
    echo -e "${RED}Error al activar el servicio. Revisa los logs en /var/log/syslog${NC}"
fi
