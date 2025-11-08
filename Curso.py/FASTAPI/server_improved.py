import socket
import threading
import sys

HOST = '0.0.0.0'  # Escuchar en todas las interfaces
PORT = 36669

# Maneja cada conexión en un hilo separado

def handle_client(conn, addr):
    print(f"Conexión desde {addr}")
    with conn:
        try:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                text = data.decode(errors='replace')
                print(f"Recibido de {addr}: {text}")
                # echo
                conn.sendall(data)
        except ConnectionResetError:
            print(f"Conexión reiniciada por {addr}")
        except Exception as e:
            print(f"Error en conexión {addr}: {e}")
    print(f"Conexión cerrada {addr}")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"Servidor escuchando en {HOST}:{PORT}")
        try:
            while True:
                conn, addr = s.accept()
                th = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
                th.start()
        except KeyboardInterrupt:
            print("Servidor detenido por usuario")
        except Exception as e:
            print(f"Error del servidor: {e}")


if __name__ == '__main__':
    main()
