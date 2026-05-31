#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GLib
import os

class ConorConnectGUI:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new("ConorConnect", "system-run", AppIndicator3.IndicatorCategory.APPLICATION_STATUS)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())

    def build_menu(self):
        menu = Gtk.Menu()
        
        # Opciones del menú
        item_status = Gtk.MenuItem(label="Estado: Ejecutando")
        item_status.set_sensitive(False)
        menu.append(item_status)
        
        item_sep = Gtk.SeparatorMenuItem()
        menu.append(item_sep)
        
        item_quit = Gtk.MenuItem(label="Salir")
        item_quit.connect("activate", Gtk.main_quit)
        menu.append(item_quit)
        
        menu.show_all()
        return menu

if __name__ == "__main__":
    indicator = ConorConnectGUI()
    Gtk.main()
