#!/bin/bash

# --- Script de Instalación Final para Conor GamerOS ---

# 1. Mover los archivos a la carpeta del sistema
sudo mkdir -p /opt/conor-connect
sudo mkdir -p /opt/conor-connect/assets
sudo cp conor-daemon /opt/conor-connect/
sudo cp conor-bridge.sh /opt/conor-connect/
sudo cp conor-rgb.sh /opt/conor-connect/
sudo cp icon.png /opt/conor-connect/assets/

# 2. Instalar el servicio de systemd
sudo cp conor-connect.service /etc/systemd/system/

# 3. Dar permisos de ejecución
sudo chmod +x /opt/conor-connect/*

# 4. Activar el servicio
sudo systemctl daemon-reload
sudo systemctl enable conor-connect
sudo systemctl start conor-connect

echo "Conor Connect instalado y corriendo en el sistema. Icono configurado."
