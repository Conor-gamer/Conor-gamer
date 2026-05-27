#!/bin/bash

# --- Conor Connect Installer ---
# Script para limpiar servicios previos e instalar Conor Connect

echo "Iniciando instalación de Conor Connect..."

# 1. Eliminación de servicios basura de Zorin/KDE Connect
echo "Limpiando servicios innecesarios..."
sudo systemctl stop zorin-connect
sudo systemctl disable zorin-connect
sudo apt purge -y zorin-connect kde-connect
sudo apt autoremove -y

# 2. Configuración del directorio principal
INSTALL_DIR="/opt/conor-connect"
sudo mkdir -p $INSTALL_DIR

# 3. Copia de archivos (Asumimos que el script está en la misma carpeta)
echo "Instalando archivos de Conor Connect..."
sudo cp -r ./* $INSTALL_DIR/

# 4. Crear el servicio de Systemd para ejecución en segundo plano
echo "Creando servicio de sistema..."
cat <<EOF | sudo tee /etc/systemd/system/conor-connect.service
[Unit]
Description=Conor Connect Service
After=network.target

[Service]
ExecStart=$INSTALL_DIR/bin/conor-daemon
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

# 5. Activar el servicio
sudo systemctl daemon-reload
sudo systemctl enable conor-connect
sudo systemctl start conor-connect

echo "¡Instalación completada con éxito, vos! Conor Connect ya está volando."
