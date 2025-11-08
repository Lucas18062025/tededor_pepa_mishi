import socket
import sys

HOST = '127.0.0.1'
PORT = 36669


def main(message: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Conectado a {HOST}:{PORT}")
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Recibido del servidor: {data.decode()}")


if __name__ == '__main__':
    msg = ' '.join(sys.argv[1:]) or 'Hola desde cliente'
    main(msg)
