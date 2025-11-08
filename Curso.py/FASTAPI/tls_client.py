import socket
import ssl
import sys

HOST = '127.0.0.1'
PORT = 36670


def main(message: str):
    context = ssl.create_default_context()
    # Para pruebas con certificado autofirmado, no verificar el hostname ni la cadena
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            print(f"Conectado TLS a {HOST}:{PORT}")
            ssock.sendall(message.encode())
            data = ssock.recv(1024)
            print(f"Recibido (TLS): {data.decode()}")


if __name__ == '__main__':
    msg = ' '.join(sys.argv[1:]) or 'Hola TLS cliente'
    main(msg)
