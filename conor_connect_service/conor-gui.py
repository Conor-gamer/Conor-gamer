import gi
import subprocess
import os
import sys
import socket
import webbrowser
import json
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class ConorApp:
    def __init__(self):
        self.verificar_actualizaciones()
        self.config_file = "/opt/conor-connect/config.json"
        self.config = self.cargar_config()
        self.main_window = None

    def cargar_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                return json.load(f)
        return {"activo": False}

    def guardar_config(self, widget=None, state=None):
        self.config["activo"] = self.switch.get_active()
        with open(self.config_file, "w") as f:
            json.dump(self.config, f)

    def verificar_actualizaciones(self):
        try:
            subprocess.run(["git", "-C", "/opt/conor-connect", "pull", "origin", "main"], 
                           capture_output=True, text=True)
        except Exception as e:
            print(f"No se pudo actualizar: {e}")

    def descargar_apk(self, widget):
        url = "https://github.com/Conor-gamer/Conor-gamer/releases/latest"
        webbrowser.open(url)

    def abrir_ventana(self):
        nombre_pc = socket.gethostname()
        self.main_window = Gtk.Window(title="Conor Connect")
        self.main_window.fullscreen()
        self.main_window.set_keep_above(True)
        self.main_window.connect("destroy", Gtk.main_quit)
        
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Conor Connect"
        header.props.subtitle = nombre_pc
        self.main_window.set_titlebar(header)
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        main_box.set_border_width(20)
        self.main_window.add(main_box)

        # Dispositivos
        main_box.pack_start(Gtk.Label(label="<b>Dispositivos</b>", use_markup=True, xalign=0), False, False, 0)
        frame = Gtk.Frame()
        box_disp = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box_disp.set_border_width(15)
        box_disp.pack_start(Gtk.Label(label="Buscando dispositivos..."), True, True, 0)
        frame.add(box_disp)
        main_box.pack_start(frame, False, False, 0)

        # Configuración con Autoguardado
        main_box.pack_start(Gtk.Label(label="<b>Configuración</b>", use_markup=True, xalign=0), False, False, 0)
        switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        switch_box.pack_start(Gtk.Label(label="Conor Connect activo mientras bloqueado"), True, True, 0)
        
        self.switch = Gtk.Switch()
        self.switch.set_active(self.config.get("activo", False))
        self.switch.connect("notify::active", self.guardar_config)
        switch_box.pack_start(self.switch, False, False, 0)
        main_box.pack_start(switch_box, False, False, 0)

        # Botón APK
        main_box.pack_start(Gtk.Label(label="<b>Aplicación móvil</b>", use_markup=True, xalign=0), False, False, 0)
        btn_apk = Gtk.Button()
        img_path = "/opt/conor-connect/boton_apk.png"
        if os.path.exists(img_path):
            imagen_boton = Gtk.Image.new_from_file(img_path)
            btn_apk.add(imagen_boton)
        else:
            btn_apk.set_label("Descargar APK")
            
        btn_apk.connect("clicked", self.descargar_apk)
        btn_apk.set_relief(Gtk.ReliefStyle.NONE)
        main_box.pack_start(btn_apk, False, False, 0)

        self.main_window.show_all()

if __name__ == "__main__":
    app = ConorApp()
    app.abrir_ventana()
    Gtk.main()
