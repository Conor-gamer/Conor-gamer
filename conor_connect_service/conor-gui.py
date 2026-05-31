import gi
import subprocess
import os
import sys
import socket
import webbrowser
gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk, AppIndicator3

class ConorApp:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new("conor-connect", "icon", AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_icon_full("/opt/conor-connect/icon.png", "Conor")
        self.menu = Gtk.Menu()
        item_abrir = Gtk.MenuItem(label="Abrir Conor Connect")
        item_abrir.connect("activate", self.abrir_ventana)
        self.menu.append(item_abrir)
        item_salir = Gtk.MenuItem(label="Salir")
        item_salir.connect("activate", Gtk.main_quit)
        self.menu.append(item_salir)
        self.menu.show_all()
        self.indicator.set_menu(self.menu)

    def descargar_apk(self, widget):
        # AQUÍ PONÉS EL LINK DE TU APK DE GITHUB
        url = "https://github.com/Conor-gamer/Conor-gamer/releases/latest"
        webbrowser.open(url)

    def abrir_ventana(self, widget):
        nombre_pc = socket.gethostname()
        ventana = Gtk.Window(title="Conor Connect")
        ventana.set_default_size(450, 450)
        
        # Header con el nombre de tu compu
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Conor Connect"
        header.props.subtitle = nombre_pc
        ventana.set_titlebar(header)
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        main_box.set_border_width(20)
        ventana.add(main_box)

        # Dispositivos
        main_box.pack_start(Gtk.Label(label="<b>Dispositivos</b>", use_markup=True, xalign=0), False, False, 0)
        frame = Gtk.Frame()
        box_disp = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box_disp.set_border_width(15)
        box_disp.pack_start(Gtk.Label(label="Buscando dispositivos..."), True, True, 0)
        frame.add(box_disp)
        main_box.pack_start(frame, False, False, 0)

        # Configuración
        main_box.pack_start(Gtk.Label(label="<b>Configuración de la extensión</b>", use_markup=True, xalign=0), False, False, 0)
        switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        switch_box.pack_start(Gtk.Label(label="Conor Connect activo mientras bloqueado"), True, True, 0)
        switch_box.pack_start(Gtk.Switch(), False, False, 0)
        main_box.pack_start(switch_box, False, False, 0)

        # Botón APK (Acción agregada)
        main_box.pack_start(Gtk.Label(label="<b>Aplicación móvil</b>", use_markup=True, xalign=0), False, False, 0)
        btn_apk = Gtk.Button(label="   APK  Descargar APK para Android")
        btn_apk.connect("clicked", self.descargar_apk)
        btn_apk.set_size_request(200, 60)
        main_box.pack_start(btn_apk, False, False, 0)

        ventana.show_all()
        ventana.present()

if __name__ == "__main__":
    app = ConorApp()
    Gtk.main()
