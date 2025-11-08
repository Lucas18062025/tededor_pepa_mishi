import socket
import ssl
import threading
import sys

HOST = '127.0.0.1'
PORT = 36670
CERTFILE = 'cert.pem'
KEYFILE = 'key.pem'


def handle_client(conn, addr):
    print(f"TLS conexión desde {addr}")
    try:
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Recibido (TLS) de {addr}: {data.decode(errors='replace')}")
                conn.sendall(data)
    except Exception as e:
        print(f"Error en conexión TLS {addr}: {e}")
    print(f"Conexión TLS cerrada {addr}")


def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERTFILE, keyfile=KEYFILE)

    bindsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bindsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    bindsock.bind((HOST, PORT))
    bindsock.listen(5)
    print(f"Servidor TLS escuchando en {HOST}:{PORT}")

    try:
        while True:
            newsock, addr = bindsock.accept()
            try:
                ssock = context.wrap_socket(newsock, server_side=True)
            except Exception as e:
                print(f"Falló TLS handshake con {addr}: {e}")
                newsock.close()
                continue
            th = threading.Thread(target=handle_client, args=(ssock, addr), daemon=True)
            th.start()
    except KeyboardInterrupt:
        print('Servidor TLS detenido por usuario')
    finally:
        bindsock.close()


if __name__ == '__main__':
    main()
