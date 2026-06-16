#!/bin/bash

# --- Conor Bridge: Puente de alta velocidad ---
# Transmite comandos del teléfono al Daemon con latencia casi cero

PORT=8080
DAEMON_IP="127.0.0.1"

# Función para enviar comandos al Daemon de forma instantánea
enviar_al_daemon() {
    local comando=$1
    # Usamos netcat para inyectar el comando al daemon y cerrar la conexión al instante
    echo "$comando" | nc -w 1 $DAEMON_IP $PORT > /dev/null 2>&1
}

# Comprobación rápida de parámetros
if [ -z "$1" ]; then
    echo "Uso: ./conor-bridge.sh [comando]"
    exit 1
fi

# Ejecución rápida
enviar_al_daemon "$1"
