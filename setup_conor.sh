#!/bin/bash
# Configuración inicial del Ecosistema CONOR NITRO
# Estableciendo el modo oscuro y activando los servicios

# 1. Configurar el tema oscuro por defecto en XFCE
xfconf-query -c xfwm4 -p /general/theme -s "Arc-Dark"
xfconf-query -c xsettings -p /Net/ThemeName -s "Arc-Dark"
xfconf-query -c xsettings -p /Net/IconThemeName -s "Papirus-Dark"

# 2. Habilitar y arrancar el Daemon de Conor Nitro
# Asumiendo que el daemon estará en /usr/local/bin/
chmod +x /usr/local/bin/conor_nitro_daemon.py
systemctl enable conor_nitro.service
systemctl start conor_nitro.service

# 3. Optimización ligera de rendimiento para hardware modesto
# Desactivamos compositor si queremos máxima velocidad (opcional)
xfconf-query -c xfwm4 -p /general/use_compositing -s false

echo "Ecosistema CONOR NITRO configurado correctamente."

