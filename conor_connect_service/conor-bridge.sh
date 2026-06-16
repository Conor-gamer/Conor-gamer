#!/bin/bash

# --- Conor Bridge: Puente de alta velocidad ---
# Este script comunica el teléfono con el Daemon principal.
# Es la vía rápida para enviar comandos de teclado, mouse o control.

# Dirección y puerto de comunicación
PORT=8080
DAEMON_IP="127.0.0.1"

# Función de envío ultra rápido
# -w 1: Fuerza a netcat a cerrar la conexión en 1 segundo si no recibe respuesta
# > /dev/null 2>&1: Mantiene el script silencioso para no cargar el procesador
enviar_al_daemon() {
    local comando=$1
    if [ -n "$comando" ]; then
        echo "$comando" | nc -w 1 $DAEMON_IP $PORT > /dev/null 2>&1
    fi
}

# Validación para asegurar que no se ejecute vacío
if [ -z "$1" ]; then
    echo "Uso: ./conor-bridge.sh [comando_accion]"
    exit 1
fi

# Ejecutar el comando recibido
enviar_al_daemon "$1"
