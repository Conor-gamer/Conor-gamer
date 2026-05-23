#!/usr/bin/env python3
# -------------------------------------------------------------------------
# CONOR NITRO - Gaming Edition: Lógica Interna (DPI, Perfiles y RGB)
# Arquitectura: 100% Linux Nativo
# -------------------------------------------------------------------------

import time

class ConorNitroMouse:
    def __init__(self):
        # Configuraciones de velocidad DPI para alta precisión en shooters
        self.modos_dpi = [400, 800, 1600, 3200]
        self.dpi_actual_index = 1  # Inicia por defecto en 800 DPI
        
        # Modos estéticos de iluminación RGB (Controlados por el botón superior)
        self.modos_rgb = ["Ola Arcoíris", "Estático Rojo", "Respiración Azul", "Apagado"]
        self.rgb_actual_index = 0  # Inicia por defecto en Ola Arcoíris
        
        print("=== FIRMWARE CONOR NITRO ACTIVO ===")
        self.mostrar_estado_actual()

    def mostrar_estado_actual(self):
        print(f"[Sistema] Sensibilidad actual: {self.modos_dpi[self.dpi_actual_index]} DPI")
        print(f"[Sistema] Modo de luces RGB: {self.modos_rgb[self.rgb_actual_index]}")

    def presionar_boton_dpi(self):
        """Cambia instantáneamente la velocidad del puntero al disparar o apuntar"""
        self.dpi_actual_index = (self.dpi_actual_index + 1) % len(self.modos_dpi)
        print(f"\n[Hardware] Botón DPI presionado -> Nueva velocidad: {self.modos_dpi[self.dpi_actual_index]} DPI")

    def presionar_boton_rgb(self):
        """Cambia el patrón de colores usando el botón dedicado detrás del scroll"""
        self.rgb_actual_index = (self.rgb_actual_index + 1) % len(self.modos_rgb)
        print(f"\n[Hardware] Botón RGB presionado -> Animación: {self.modos_rgb[self.rgb_actual_index]}")

    def presionar_botones_laterales(self, accion):
        """Maneja los clics de los dos botones de la parte izquierda"""
        if accion == "adelante":
            print("[Hardware] Botón Lateral Izquierdo: Navegación Adelante")
        elif accion == "atras":
            print("[Hardware] Botón Lateral Izquierdo: Navegación Atrás")

# --- Simulación del comportamiento del Mouse en ejecución ---
if __name__ == "__main__":
    # Arrancar el procesador del ratón gamer
    mouse = ConorNitroMouse()
    
    # Simulación de un usuario jugando:
    time.sleep(1)
    mouse.presionar_botones_laterales("atras")     # Usás el botón de atrás a la izquierda
    time.sleep(1)
    mouse.modos_rgb = ["Ola Arcoíris", "Estático Rojo", "Respiración Azul", "Apagado"] # Mantiene el registro
    mouse.presionar_boton_dpi()                    # Cambiás DPI para mayor precisión de disparo
    time.sleep(1)
    mouse.presionar_boton_rgb()                    # Cambiás el color de los LEDs desde el botón del scroll
