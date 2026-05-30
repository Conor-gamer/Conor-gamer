#!/bin/bash

# --- Conor Connect Installer ---
# Script para limpiar servicios previos e instalar Conor Connect

echo "Iniciando instalación de Conor Connect, maje..."

# 1. Eliminación de servicios basura
echo "Limpiando servicios innecesarios..."
sudo systemctl stop zorin-connect 2>/dev/null
sudo systemctl disable zorin-connect 2>/dev/null
sudo apt purge -y zorin-connect kde-connect
sudo apt autoremove -y

# 2. Configuración del directorio
INSTALL_DIR="/opt/conor-connect"
sudo mkdir -p $INSTALL_DIR

# 3. Copia de archivos
echo "Instalando archivos de Conor Connect..."
sudo cp conor-daemon conor-bridge.sh conor-rgb.sh $INSTALL_DIR/
sudo cp icon.png $INSTALL_DIR/

# 4. Dar permisos de ejecución
sudo chmod +x $INSTALL_DIR/conor-daemon
sudo chmod +x $INSTALL_DIR/*.sh

# 5. Crear el servicio de Systemd
echo "Creando servicio de sistema..."
cat <<EOF | sudo tee /etc/systemd/system/conor-connect.service
[Unit]
Description=Conor Connect Service
After=network.target

[Service]
ExecStart=$INSTALL_DIR/conor-daemon
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# 6. Activar el servicio
sudo systemctl daemon-reload
sudo systemctl enable conor-connect
sudo systemctl start conor-connect

echo "¡Instalación completada con éxito, vos! Conor Connect ya está volando."
