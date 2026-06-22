#!/bin/bash

# Conor-rgb.sh - Script de control para Conor Connect
# Actualizado: 2026-06-21

echo "Iniciando control de iluminación RGB para Conor Connect..."

# Función para enviar comando al controlador
set_color() {
    local color=$1
    echo "Enviando comando de color: $color"
    # Aquí iría la lógica de comunicación con el dispositivo Steren/Smart Life
    # Ejemplo placeholder para la integración:
    curl -s -X POST http://192.168.1.50/api/set_color -d "color=$color"
}

# Lógica principal de ejecución
if [ -z "$1" ]; then
    echo "Uso: ./Conor-rgb.sh [color]"
    exit 1
else
    set_color "$1"
    echo "Color aplicado exitosamente."
fi

exit 0
