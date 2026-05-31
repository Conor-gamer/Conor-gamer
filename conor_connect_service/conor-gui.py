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
        
        # Opción para abrir la ventana
        item_abrir = Gtk.MenuItem(label="Abrir Conor Connect")
        item_abrir.connect("activate", self.abrir_ventana)
        self.menu.append(item_abrir)
        
        # Opción para salir
        item_salir = Gtk.MenuItem(label="Salir")
        item_salir.connect("activate", Gtk.main_quit)
        self.menu.append(item_salir)
        
        self.menu.show_all()
        self.indicator.set_menu(self.menu)

    def abrir_ventana(self, widget):
        # Crear la ventana principal
        ventana = Gtk.Window(title="Conor Connect - Configuración")
        ventana.set_default_size(400, 300)
        ventana.set_position(Gtk.WindowPosition.CENTER)
        
        # Layout de la ventana
        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        ventana.add(caja)
        
        label = Gtk.Label(label="Bienvenido a Conor Connect")
        caja.pack_start(label, True, True, 0)
        
        btn_vincular = Gtk.Button(label="Vincular nuevo dispositivo")
        caja.pack_start(btn_vincular, True, True, 0)
        
        ventana.show_all()

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = ConorApp()
    app.run()
