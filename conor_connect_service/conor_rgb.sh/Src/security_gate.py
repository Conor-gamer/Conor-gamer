# security_gate.py

import socket
import threading

class SecurityGate:
    def __init__(self, host='0.0.0.0', port=9999, secret_token="CONOR_SECRET_2026"):
        self.host = host
        self.port = port
        self.secret_token = secret_token
        self.is_running = True

    def start_gate(self):
        gate_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        gate_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        gate_socket.bind((self.host, self.port))
        gate_socket.listen(5)
        
        print("Security Gate: Bóveda activada y blindada. Escuchando...")
        
        while self.is_running:
            conn, addr = gate_socket.accept()
            threading.Thread(target=self.verify_handshake, args=(conn, addr)).start()

    def verify_handshake(self, conn, addr):
        try:
            # Capa de protección extra: Validación de Token
            data = conn.recv(1024).decode('utf-8')
            if data == self.secret_token:
                print(f"Acceso autorizado para: {addr}")
                # Aquí procedería el handshake completo
            else:
                print(f"Intento de intrusión bloqueado: {addr}")
                conn.close()
        except Exception as e:
            conn.close()

if __name__ == '__main__':
    gate = SecurityGate()
    gate.start_gate()
