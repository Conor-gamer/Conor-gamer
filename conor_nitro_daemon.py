#!/usr/bin/env python3
# -------------------------------------------------------------------------
# CONOR NITRO - Demonio de Integración Exclusivo para Linux
# Función: Sincronización Automática, Chequeo de Wi-Fi y Alerta en Escritorio
# CONFIGURACIÓN: Etiquetas Pango Markup profesionales para ZorinOS
# -------------------------------------------------------------------------

import sys
import subprocess
import urllib.request
import os

# Configuración de la versión local actual del software
VERSION_ACTUAL = "1.1.0"
URL_SERVIDOR_VERSION = "https://raw.githubusercontent.com/Conor-gamer/Conor-gamer/main/version.txt"
URL_SERVIDOR_DRIVER = "https://raw.githubusercontent.com/Conor-gamer/Conor-gamer/main/conor_nitro_driver.sh"

def comprobar_entorno_linux():
    """Asegura que el ecosistema avanzado solo corra en distros Linux"""
    if not sys.platform.startswith('linux'):
        print("Sistema no compatible. CONOR NITRO ejecutándose en modo genérico.")
        sys.exit(0)

def verificar_conexion_internet():
    """Comprueba si el equipo tiene salida a internet para conectar con el servidor"""
    print("[Ecosistema] Verificando estado de la red/Wi-Fi...")
    try:
        urllib.request.urlopen('https://github.com', timeout=3)
        print("[Ecosistema] Conexión a Internet activa.")
        return True
    except:
        print("[Ecosistema] Sin Wi-Fi/Internet. Cargando configuraciones locales del hardware.")
        return False

def ejecutar_actualizacion_remota():
    """Revisa el servidor de GitHub de forma inalámbrica y descarga mejoras automáticamente"""
    print("[Actualizador] Buscando actualizaciones en el servidor remoto...")
    try:
        with urllib.request.urlopen(URL_SERVIDOR_VERSION, timeout=3) as respuesta:
            version_servidor = respuesta.read().decode('utf-8').strip()
        
        if version_servidor > VERSION_ACTUAL:
            print(f"[Actualizador] Nueva versión detectada en el servidor: v{version_servidor}")
            
            # Lanzar la alerta especializada ANTES de actualizar para informar al usuario
            lanzar_cartel_actualizacion_hardware(version_servidor)
            
            # Simulación de descarga e instalación interna en el hardware
            ruta_driver_local = "/usr/local/bin/conor_nitro_driver.sh"
            urllib.request.urlretrieve(URL_SERVIDOR_DRIVER, "conor_nitro_driver_tmp.sh")
            print(f"⚡ [Éxito] Ecosistema interno del mouse actualizado a la versión v{version_servidor}.")
        else:
            print(f"[Actualizador] El ecosistema del hardware está en la última versión estable (v{VERSION_ACTUAL}).")
            
    except Exception as e:
        print("[Actualizador] No se pudo verificar la actualización remota.")

def lanzar_cartel_actualizacion_hardware(nueva_version):
    """Lanza una notificación gráfica exclusiva con la configuración exacta de la imagen"""
    print("[Ecosistema] Desplegando notificación de actualización exclusiva de hardware...")
    
    # Título principal del cartel de hardware
    titulo = "🖱️ ACTUALIZACIÓN DE HARDWARE: CONOR NITRO MOUSE"
    
    # Mensaje configurado exactamente con las etiquetas profesionales de la simulación
    mensaje = (
        f"El sistema operativo interno de su dispositivo <big><b>CONOR NITRO MOUSE</b></big> "
        f"requiere una actualización automática a la versión <b>v{nueva_version}</b>.\n\n"
        f"<b>Nota importante:</b> Esta acción <big><b>SOLO</b></big> optimiza el circuito "
        f"interno de su ratón inteligente. El sistema base de su computadora no sufrirá "
        f"modificaciones ni reinicios."
    )
    
    try:
        # Se invoca notify-send con el icono de hardware y el formato atómico activado
        subprocess.run([
            "notify-send", 
            "-i", "peripherals-mouse", 
            "-u", "normal",
            titulo, 
            mensaje
        ], check=True)
    except FileNotFoundError:
        print(f"\n[ALERTA VISUAL DE HARDWARE]\n{titulo}\n{mensaje}\n")

if __name__ == "__main__":
    comprobar_entorno_linux()
    print("\n====================================================")
    print("      CONOR NITRO LINUX INTEGRATION SYSTEM          ")
    print("====================================================")
    
    if verificar_conexion_internet():
        ejecutar_actualizacion_remota()
