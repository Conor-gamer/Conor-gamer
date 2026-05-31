import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3

class ConorApp:
    def __init__(self):
        # Configuración del indicador en la barra
        self.indicator = AppIndicator3.Indicator.new(
            "conor-connect", "icon", AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_icon_full("/opt/conor-connect/icon.png", "Icono")
        
        # Crear el menú del indicador
        self.menu = Gtk.Menu()
        item_abrir = Gtk.MenuItem(label="Abrir Conor Connect")
        item_abrir.connect("activate", self.abrir_ventana)
        self.menu.append(item_abrir)
        
        item_salir = Gtk.MenuItem(label="Salir")
        item_salir.connect("activate", Gtk.main_quit)
        self.menu.append(item_salir)
        
        self.menu.show_all()
        self.indicator.set_menu(self.menu)

    def abrir_ventana(self, widget):
        # Crear la ventana principal estilo Zorin
        ventana = Gtk.Window(title="Conor Connect - Configuración")
        ventana.set_default_size(500, 400)
        ventana.set_position(Gtk.WindowPosition.CENTER)
        ventana.set_border_width(20)
        
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        ventana.add(main_box)
        
        # Sección de dispositivos
        label_disp = Gtk.Label(label="Dispositivos", xalign=0)
        main_box.pack_start(label_disp, False, False, 0)
        
        listbox = Gtk.ListBox()
        main_box.pack_start(listbox, True, True, 0)
        
        # Fila de ejemplo (Dispositivo)
        row = Gtk.ListBoxRow()
        box_row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.add(box_row)
        box_row.pack_start(Gtk.Label(label="Galaxy A04e"), True, True, 0)
        box_row.pack_start(Gtk.Label(label="Conectado"), False, False, 0)
        listbox.add(row)
        
        # Botón de descarga APK
        btn_download = Gtk.Button(label="Descargar APK para Android")
        btn_download.connect("clicked", self.on_download_clicked)
        main_box.pack_end(btn_download, False, False, 0)
        
        ventana.show_all()
        ventana.present()

    def on_download_clicked(self, widget):
        print("Acceso directo a la descarga de la APK activado, maje.")

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = ConorApp()
    app.run()
