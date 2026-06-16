#!/bin/bash

# --- Conor Bridge: Puente de alta velocidad ---
# Transmite comandos del teléfono al Daemon con latencia casi cero

PORT=8080
DAEMON_IP="127.0.0.1"
LOG_FILE="/var/log/conor-connect/conor.log"

# --- Función de Log profesional ---
log_evento() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Función para enviar comandos al Daemon de forma instantánea
enviar_al_daemon() {
    local comando=$1
    
    # Registramos el intento en el log
    log_evento "Intentando enviar comando: $comando"
    
    # Usamos netcat para inyectar el comando al daemon y cerrar la conexión al instante
    if echo "$comando" | nc -w 1 $DAEMON_IP $PORT > /dev/null 2>&1; then
        log_evento "ÉXITO: Comando ejecutado: $comando"
    else
        log_evento "ERROR: Fallo al enviar el comando: $comando"
    fi
}

# Comprobación rápida de parámetros
if [ -z "$1" ]; then
    echo "Uso: ./conor-bridge.sh [comando]"
    log_evento "ADVERTENCIA: Intento de ejecución sin parámetros."
    exit 1
fi

# Ejecución rápida
enviar_al_daemon "$1"
