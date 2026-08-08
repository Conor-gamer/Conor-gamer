#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
import subprocess
os = __import__('os')

class ConorConnectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conor Connect - PC Controller")
        self.root.geometry("380x450")
        self.root.config(bg="#1e1e1e")
        self.root.resizable(False, False)

        # Título de la app
        title_label = tk.Label(root, text="CONOR CONNECT", fg="#00ffcc", bg="#1e1e1e", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=20)

        # Estado actual (Conectado / Desconectado)
        self.status_frame = tk.Frame(root, bg="#1e1e1e")
        self.status_frame.pack(pady=10)

        self.status_indicator = tk.Label(self.status_frame, text="●", fg="red", bg="#1e1e1e", font=("Helvetica", 24))
        self.status_indicator.pack(side=tk.LEFT, padx=5)

        self.status_text = tk.Label(self.status_frame, text="Desconectado", fg="white", bg="#1e1e1e", font=("Helvetica", 12))
        self.status_text.pack(side=tk.LEFT, padx=5)

        # Interruptor Principal (Switch Real)
        self.switch_var = tk.BooleanVar()
        self.switch_btn = tk.Button(
            root, 
            text="APAGADO", 
            bg="#cc3333", 
            fg="white", 
            font=("Helvetica", 12, "bold"),
            width=15,
            relief=tk.FLAT,
            command=self.toggle_service
        )
        self.switch_btn.pack(pady=30)

        # Botones de funciones reales
        btn_style = {"bg": "#333333", "fg": "white", "font": ("Helvetica", 10), "width": 25, "bd": 0, "activebackground": "#00ffcc"}

        tk.Button(root, text="Forzar Sincronización RGB", command=self.run_rgb, **btn_style).pack(pady=8)
        tk.Button(root, text="Ver Registro de Logs", command=self.ver_logs, **btn_style).pack(pady=8)

        # Comprobar estado real al iniciar
        self.actualizar_estado_real()

    def toggle_service(self):
        # Función 100% real que prende o apaga el servicio systemd de Conor Connect
        is_active = self.switch_var.get()
        
        if not is_active:
            # Intentar encender
            resultado = subprocess.run(["sudo", "systemctl", "start", "conor-connect"], capture_output=True)
            if resultado.returncode == 0:
                self.switch_var.set(True)
                self.switch_btn.config(text="ENCENDIDO", bg="#28a745")
                self.status_indicator.config(fg="#28a745")
                self.status_text.config(text="Conectado y Activo")
            else:
                messagebox.showerror("Error", "No se pudo encender el servicio. ¿Tenés permisos root?")
        else:
            # Intentar apagar
            resultado = subprocess.run(["sudo", "systemctl", "stop", "conor-connect"], capture_output=True)
            if resultado.returncode == 0:
                self.switch_var.set(False)
                self.switch_btn.config(text="APAGADO", bg="#cc3333")
                self.status_indicator.config(fg="red")
                self.status_text.config(text="Desconectado")
            else:
                messagebox.showerror("Error", "No se pudo apagar el servicio.")

    def actualizar_estado_real(self):
        # Revisa en el sistema operativo si el servicio está corriendo de verdad
        try:
            resultado = subprocess.run(["systemctl", "is-active", "--quiet", "conor-connect"])
            if resultado.returncode == 0:
                self.switch_var.set(True)
                self.switch_btn.config(text="ENCENDIDO", bg="#28a745")
                self.status_indicator.config(fg="#28a745")
                self.status_text.config(text="Conectado y Activo")
            else:
                self.switch_var.set(False)
                self.switch_btn.config(text="APAGADO", bg="#cc3333")
                self.status_indicator.config(fg="red")
                self.status_text.config(text="Desconectado")
        except Exception:
            pass

    def run_rgb(self):
        # Ejecuta el script de luces o comandos que ya tenías
        subprocess.Popen(["/opt/conor-connect/conor-rgb.sh"])
        messagebox.showinfo("Conor Connect", "Comando RGB enviado al sistema.")

    def ver_logs(self):
        # Abre o muestra el log que programamos antes
        if os.path.exists("/var/log/conor-connect/conor.log"):
            os.system("xdg-open /var/log/conor-connect/conor.log")
        else:
            messagebox.showwarning("Aviso", "El archivo de registro todavía no existe.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConorConnectApp(root)
    root.mainloop()
