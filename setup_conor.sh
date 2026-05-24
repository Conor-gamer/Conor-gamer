#!/bin/bash
# Configuración definitiva del Ecosistema CONOR NITRO

# 1. Organizar herramientas y daemon en el sistema
mv /conor_nitro_daemon.py /usr/local/bin/
mv /conor_nitro_tools.py /usr/local/bin/
mv /mouse_firmware.py /usr/local/bin/
chmod +x /usr/local/bin/conor_nitro_daemon.py

# 2. Configurar Fondo de Pantalla Oficial
mkdir -p /usr/share/wallpapers/
mv /conor_wallpaper.png /usr/share/wallpapers/conor_wallpaper.png
xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/workspace0/last-image -n -t string -s "/usr/share/wallpapers/conor_wallpaper.png"
xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -n -t string -s "/usr/share/wallpapers/conor_wallpaper.png"

# 3. Configurar Estética Gamer (Modo Oscuro)
xfconf-query -c xfwm4 -p /general/theme -s "Arc-Dark"
xfconf-query -c xsettings -p /Net/ThemeName -s "Arc-Dark"
xfconf-query -c xsettings -p /Net/IconThemeName -s "Papirus-Dark"
xfconf-query -c xfwm4 -p /general/use_compositing -s false

# 4. Activar el cerebro del sistema (Daemon)
systemctl enable conor_nitro.service
systemctl start conor_nitro.service

echo "Ecosistema CONOR NITRO instalado y optimizado al 100%."
