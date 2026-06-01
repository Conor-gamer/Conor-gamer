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

    def actualizar_estado(self, switch, gparam):
        is_active = switch.get_active()
        if is_active:
            self.label_status.set_text("Conor Connect: Activado")
            subprocess.run(["pkexec", "systemctl", "start", "conor-connect"]) 
        else:
            self.label_status.set_text("Conor Connect: Desactivado")
            subprocess.run(["pkexec", "systemctl", "stop", "conor-connect"])
        self.guardar_config()

    def abrir_ventana(self):
        nombre_pc = socket.gethostname()
        self.main_window = Gtk.Window(title="Conor Connect")
        self.main_window.maximize() 
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

        # Configuración con interruptor activo/desactivado
        main_box.pack_start(Gtk.Label(label="<b>Configuración</b>", use_markup=True, xalign=0), False, False, 0)
        switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        
        estado_inicial = "Activado" if self.config.get("activo", False) else "Desactivado"
        self.label_status = Gtk.Label(label=f"Conor Connect: {estado_inicial}")
        switch_box.pack_start(self.label_status, True, True, 0)
        
        self.switch = Gtk.Switch()
        self.switch.set_active(self.config.get("activo", False))
        self.switch.connect("notify::active", self.actualizar_estado)
        switch_box.pack_start(self.switch, False, False, 0)
        main_box.pack_start(switch_box, False, False, 0)

        # Botón APK Integrado
        main_box.pack_start(Gtk.Label(label="<b>Aplicación móvil</b>", use_markup=True, xalign=0), False, False, 0)
        btn_apk = Gtk.Button()
        btn_apk.set_size_request(-1, 100)
        box_btn = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=15)
        box_btn.set_halign(Gtk.Align.CENTER)
        
        img_path = "/opt/conor-connect/assets/boton_apk.png"
        if os.path.exists(img_path):
            imagen_boton = Gtk.Image.new_from_file(img_path)
            box_btn.pack_start(imagen_boton, False, False, 0)
            
        label_btn = Gtk.Label()
        label_btn.set_markup("<span size='large' weight='bold'>Descargar APK para Android</span>")
        box_btn.pack_start(label_btn, False, False, 0)
        
        btn_apk.add(box_btn)
        btn_apk.connect("clicked", self.descargar_apk)
        btn_apk.get_style_context().add_class("suggested-action")
        main_box.pack_start(btn_apk, False, False, 10)

        self.main_window.show_all()

if __name__ == "__main__":
    app = ConorApp()
    app.abrir_ventana()
    Gtk.main()
