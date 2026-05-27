#!/bin/bash

# --- Conor Bridge ---
# Permite la comunicación entre el dispositivo Android y Conor NitroOS

echo "Configurando puente de comunicación..."

# 1. Abrir el puerto en el firewall para el celular
sudo ufw allow 8080/tcp

# 2. Configurar permisos para que el usuario pueda controlar el mouse
# Esto es vital para que la app móvil mueva el puntero sin trabas
sudo usermod -aG input $USER

# 3. Optimizar el tráfico de red para baja latencia (prioridad a Conor Connect)
sudo tc qdisc add dev wlan0 root fq_codel 2>/dev/null

echo "Puente establecido. La PC está lista para recibir comandos."
