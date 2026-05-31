#!/bin/bash

# Instalar dependencias necesarias para la interfaz y el sistema
echo "Instalando dependencias necesarias..."
sudo apt update
sudo apt install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-appindicator3-0.1

# Crear carpeta de instalación
echo "Configurando directorios..."
sudo mkdir -p /opt/conor-connect

# Copiar archivos del proyecto
echo "Copiando archivos..."
sudo cp conor-daemon /opt/conor-connect/
sudo cp conor-gui.py /opt/conor-connect/
# Aquí usamos tu archivo icon.png directamente
sudo cp icon.png /opt/conor-connect/

# Dar permisos de ejecución
sudo chmod +x /opt/conor-connect/conor-daemon
sudo chmod +x /opt/conor-connect/conor-gui.py

# Configurar el lanzador de la aplicación
echo "Creando acceso directo en el sistema..."
sudo cp conor-connect.desktop /usr/share/applications/

# Configurar y activar el servicio de fondo
echo "Activando el servicio Conor Connect..."
cat <<EOF | sudo tee /etc/systemd/system/conor-connect.service
[Unit]
Description=Conor Connect Service
After=network.target

[Service]
ExecStart=/opt/conor-connect/conor-daemon
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable conor-connect
sudo systemctl restart conor-connect

echo "¡Instalación completada con éxito, vos! Conor Connect ya está volando con su icono."
