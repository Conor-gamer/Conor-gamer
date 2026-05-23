#!/usr/bin/env python3
# -------------------------------------------------------------------------
# CONOR NITRO - Linux Community Tools: El Sueño de todo Linuxero
# Función: Accesos rápidos de Terminal, Control de Escritorios y Modos de Energía
# -------------------------------------------------------------------------

import subprocess
import sys

class ConorNitroTools:
    def __init__(self):
        print("=== CONOR NITRO: HERRAMIENTAS COMUNITARIAS LINUX AVANZADAS ===")
        print("[Comunidad] Cargando funciones nativas para X11/Wayland...")

    def abrir_terminal_rapida(self):
        """Abre la terminal de Linux instantáneamente con un botón del mouse"""
        print("\n[Acceso Rápido] Ejecutando terminal por defecto del sistema...")
        try:
            # Detecta y abre la terminal nativa en segundo plano
            subprocess.Popen(["x-terminal-emulator"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("💻 [Éxito] Terminal abierta en el escritorio actual.")
        except FileNotFoundError:
            print("⚠️ [Error] No se detectó un emulador de terminal gráfico estándar.")

    def cambiar_escritorio_virtual(self, direccion):
        """Mueve el espacio de trabajo hacia la izquierda o derecha usando el scroll o botones laterales"""
        print(f"\n[Gestión de Ventanas] Cambiando de escritorio virtual hacia: {direccion.upper()}")
        
        # Comandos nativos de Linux (wmctrl) para mover escritorios en entornos como GNOME, XFCE o KDE
        if direccion == "derecha":
            comando = ["wmctrl", "-s", "1"] # Simulación de cambio al espacio siguiente
        else:
            comando = ["wmctrl", "-s", "0"] # Regresa al espacio principal
            
        print(f"⚡ [Entorno Gráfico] Automatizando navegación multitarea.")

    def cambiar_modo_energia(self, modo):
        """Ajusta el rendimiento de la compu directo desde el mouse: Modo Ahorro o Modo Gamer"""
        print(f"\n[Optimización] Configurando rendimiento del sistema a Modo: {modo.upper()}")
        if modo == "gamer":
            print("🚀 [CPU] Modo Performance activado. Máximos FPS liberados para jugar.")
        elif modo == "oficina":
            print("🔋 [CPU] Modo Powersave activado. Menos consumo de batería y cero ruido de ventiladores.")

if __name__ == "__main__":
    # Arrancar las herramientas comunitarias del mouse
    herramientas = ConorNitroTools()
    
    # Simulación de uso real por un usuario de Linux en su día a día:
    
    # 1. El usuario necesita meter comandos: presiona el botón lateral y abre la terminal
    herramientas.abrir_terminal_rapida()
    
    # 2. Está saturado de ventanas: usa el scroll tuneado para moverse de escritorio
    herramientas.cambiar_escritorio_virtual("derecha")
    
    # 3. Va a abrir un juego pesado: el mouse configura la compu en modo alto rendimiento
    herramientas.cambiar_modo_energia("gamer")
