#!/bin/bash
# -------------------------------------------------------------------------
# CONOR NITRO - Gaming Edition: Controlador Base de Hardware (Cable USB)
# Arquitectura: 100% Linux Nativo mediante ConfigFS
# -------------------------------------------------------------------------

set -e

# Directorio del Kernel para configurar el Gadget USB
GADGET_DIR="/sys/kernel/config/usb_gadget/conor_nitro"

echo "Configurando la interfaz de hardware para CONOR NITRO..."

# 1. Crear la estructura del dispositivo en el Kernel
mkdir -p "$GADGET_DIR"
cd "$GADGET_DIR"

# 2. Identificadores de Hardware Únicos (Vendor ID y Product ID)
echo "0x1d6b" > idVendor   # Linux Foundation
echo "0x0104" > idProduct  # Dispositivo compuesto avanzado (Gamer)
echo "0x0100" > bcdDevice
echo "0x0200" > bcdUSB

# 3. Cadenas de texto de identificación oficial de la marca
mkdir -p strings/0x409
echo "Conor-gaming" > strings/0x409/manufacturer
echo "CONOR NITRO Gaming Mouse" > strings/0x409/product

# 4. Configurar la función HID avanzada (Mapeo físico del mouse)
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 4 > functions/hid.usb0/report_length  # Longitud de datos para transferencias rápidas

# DESCRIPTOR HID GAMER (5 Botones + Ejes X/Y + Scroll):
echo -ne \\x05\\x01\\x09\\x02\\xa1\\x01\\x09\\x01\\xa1\\x00\\x05\\x09\\x19\\x01\\x29\\x05\\x15\\x00\\x25\\x01\\x95\\x05\\x75\\x01\\x81\\x02\\x95\\x01\\x75\\x03\\x81\\x03\\x05\\x01\\x09\\x30\\x09\\x31\\x09\\x38\\x15\\x81\\x25\\x7f\\x75\\x08\\x95\\x03\\x81\\x06\\xc0\\xc0 > functions/hid.usb0/report_desc

# 5. Enlazar los botones y el sensor a la configuración del cable USB
mkdir -p configs/c.1/strings/0x409
echo "Conor Nitro Gaming Configuration" > configs/c.1/strings/0x409/configuration
ln -sf functions/hid.usb0 configs/c.1/

# 6. Habilitar la línea de datos física (UDC)
ls /sys/class/udc/ > UDC
echo "Controlador CONOR NITRO cargado exitosamente en el bus USB."

# =========================================================================
# AUTOMATIZACIÓN E INSTALACIÓN DE RECURSOS
# =========================================================================

# A. Descompresión de recursos (Ahora el sistema los jala automáticamente)
if [ -f "/tmp/conor-recursos.zip" ]; then
    echo "Detectando paquete de recursos, instalando en /opt/..."
    mkdir -p /opt/conor-recursos
    unzip -o /tmp/conor-recursos.zip -d /opt/conor-recursos/
    chmod +x /opt/conor-recursos/*
    rm /tmp/conor-recursos.zip
fi

# B. Regla UDEV para el daemon
UDEV_RULE="/etc/udev/rules.d/99-conor-nitro.rules"
if [ ! -f "$UDEV_RULE" ]; then
    echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="1d6b", ATTR{idProduct}=="0104", ACTION=="add", RUN+="/usr/local/bin/conor_nitro_daemon.py"' | tee "$UDEV_RULE" > /dev/null
    echo "[Automatización] Regla de auto-arranque vinculada al hardware con éxito."
fi
