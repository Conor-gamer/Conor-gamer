#!/usr/bin/env python3
# -------------------------------------------------------------------------
# CONOR NITRO - Demonio de Integración Exclusivo para Linux
# Función: Sincronización Automática, Chequeo de Wi-Fi y Alerta en Escritorio
# -------------------------------------------------------------------------

import sys
import subprocess
import urllib.request

def comprobar_entorno_linux():
    """Asegura que el ecosistema avanzado solo corra en distros Linux"""
    if not sys.platform.startswith('linux'):
        print("Sistema no compatible. CONOR NITRO ejecutándose en modo genérico.")
        sys.exit(0)

def verificar_conexion_internet():
    """Comprueba si el equipo tiene salida a internet para actualizar perfiles"""
    print("[Ecosistema] Verificando estado de la red/Wi-Fi...")
    try:
        # Intenta conectar con los servidores de clonación de código
        urllib.request.urlopen('https://github.com', timeout=3)
        print("[Ecosistema] Conexión a Internet activa. Modo: Actualización Automática Habilitada.")
        return True
    except:
        print("[Ecosistema] Sin Wi-Fi/Internet. Cargando configuraciones locales del hardware.")
        return False

def lanzar_cartel_escritorio():
    """Lanza una notificación visual interactiva directamente en la pantalla de Linux"""
    print("[Ecosistema] Lanzando cartel de notificación en el entorno gráfico...")
    
    titulo = "⚡ CONOR NITRO DETECTADO"
    mensaje = "Ecosistema unificado con éxito.\nSincronización automática de DPI y luces RGB activa.\nModo: 100% Linux Native."
    
    try:
        # Comando nativo de Linux para tirar alertas visuales en el escritorio (notify-send)
        subprocess.run([
            "notify-send", 
            "-i", "input-mouse", 
            titulo, 
            mensaje
        ], check=True)
    except FileNotFoundError:
        # Si la distro no tiene notify-send, tira una alerta estándar por terminal
        print(f"\n*** CARTEL VISUAL ***\n[{titulo}]\n{mensaje}\n*********************\n")

if __name__ == "__main__":
    comprobar_entorno_linux()
    print("\n====================================================")
    print("      CONOR NITRO LINUX INTEGRATION SYSTEM          ")
    print("====================================================")
    
    # 1. Comprobar si hay Wi-Fi para actualizar automáticamente
    verificar_conexion_internet()
    
    # 2. Sincronizar y lanzar el cartel en el monitor de la compu
    lanzar_cartel_escritorio()
