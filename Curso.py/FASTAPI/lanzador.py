import socket
import subprocess

def puerto_libre(puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', puerto)) != 0

# Lista de puertos que querés probar
puertos = [8600, 8700, 8800, 8900]

for p in puertos:
    if puerto_libre(p):
        print(f"✅ Puerto libre encontrado: {p}")
        # Lanzamos Uvicorn automáticamente
        subprocess.run([
            "uvicorn", "main:app",
            "--ssl-keyfile=key.pem",
            "--ssl-certfile=cert.pem",
            "--port", str(p)
        ])
        break
else:
    print("❌ No se encontró ningún puerto libre en la lista.")