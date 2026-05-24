#!/usr/bin/env python3
import sys
import subprocess
import urllib.request
import time
import os

# --- CONFIGURACIÓN ---
VERSION_ACTUAL = "1.1.0"
MOUSE_ID = "1234:5678"  # Cambiá esto por el ID real de tu mouse
URL_SERVIDOR_VERSION = "https://raw.githubusercontent.com/Conor-gamer/Conor-gamer/main/version.txt"
URL_SERVIDOR_DRIVER = "https://raw.githubusercontent.com/Conor-gamer/Conor-gamer/main/conor_nitro_driver.sh"

def check_hardware():
    """Detecta si el mouse CONOR NITRO está conectado."""
    try:
        lsusb_output = subprocess.check_output("lsusb").decode()
        return MOUSE_ID in lsusb_output
    except:
        return False

def ejecutar_actualizacion_remota():
    """Revisa si hay mejoras en GitHub de forma silenciosa."""
    try:
        with urllib.request.urlopen(URL_SERVIDOR_VERSION, timeout=3) as respuesta:
            version_servidor = respuesta.read().decode('utf-8').strip()
        
        if version_servidor > VERSION_ACTUAL:
            urllib.request.urlretrieve(URL_SERVIDOR_DRIVER, "/usr/local/bin/conor_nitro_driver.sh")
            subprocess.run(["notify-send", "-i", "peripherals-mouse", "CONOR NITRO", "Sistema de hardware actualizado."])
    except:
        pass

def modo_mouse():
    """Lógica específica para el hardware del mouse."""
    print("[MODO MOUSE] Optimización de periférico activa.")

def modo_gaming():
    """Lógica específica para PC Gaming/Tostadora."""
    print("[MODO GAMING] Optimizando recursos de sistema.")

def main():
    print("Iniciando CONOR NITRO CORE...")
    while True:
        # 1. Actualización inteligente (solo si hay internet)
        try:
            if urllib.request.urlopen('https://github.com', timeout=2):
                ejecutar_actualizacion_remota()
        except:
            pass
        
        # 2. Selección de modo según el hardware
        if check_hardware():
            modo_mouse()
        else:
            modo_gaming()
            
        time.sleep(10) # Ciclo de verificación cada 10 segundos

if __name__ == "__main__":
    main()
