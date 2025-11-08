import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

#!/usr/bin/env python3
# puertos.py
# Escanea puertos TCP de una IP (por defecto: tu IP local).
# Úsalo solo en equipos/redes que poseas o tengas permiso para auditar.


def get_local_ip():
    """Obtiene la IP local usada para salir a Internet (no hace conexión real)."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Conectar a IP pública no envía datos; sirve para obtener la IP local
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

def scan_port(target, port, timeout=0.5):
    """Devuelve True si el puerto está abierto (TCP)."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            result = s.connect_ex((target, port))
            return result == 0
        except Exception:
            return False

def parse_range(rng):
    """Parsea rangos como '20-80' o lista separada por comas '22,80,443' o ambos."""
    ports = set()
    for part in rng.split(','):
        part = part.strip()
        if not part:
            continue
        if '-' in part:
            start, end = part.split('-', 1)
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))
    return sorted(p for p in ports if 1 <= p <= 65535)

def main():
    parser = argparse.ArgumentParser(description="Escanea puertos TCP de una IP (usa solo en equipos que poseas).")
    parser.add_argument("target", nargs="?", help="IP o host a escanear (por defecto: tu IP local).")
    parser.add_argument("-p", "--ports", default="1-1024",
                        help="Puertos a escanear. Ej: '22,80,443' o '1-1024'. Por defecto: 1-1024")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Timeout por intento (segundos).")
    parser.add_argument("-w", "--workers", type=int, default=100, help="Hilos concurrentes.")
    args = parser.parse_args()

    target = args.target if args.target else get_local_ip()
    try:
        target_ip = socket.gethostbyname(target)
    except Exception as e:
        print(f"Error resolviendo '{target}': {e}")
        return

    ports = parse_range(args.ports)
    open_ports = []

    print(f"Escaneando {target} ({target_ip}) puertos: {len(ports)} (timeout={args.timeout}s)")

    try:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            future_to_port = {ex.submit(scan_port, target_ip, port, args.timeout): port for port in ports}
            for fut in as_completed(future_to_port):
                port = future_to_port[fut]
                try:
                    if fut.result():
                        open_ports.append(port)
                        print(f"Puerto abierto: {port}")
                except Exception:
                    pass
    except KeyboardInterrupt:
        print("\nInterrumpido por usuario.")
        return

    if open_ports:
        open_ports.sort()
        print("\nPuertos abiertos encontrados:")
        for p in open_ports:
            print(f" - {p}")
    else:
        print("\nNo se encontraron puertos abiertos en el rango especificado.")

if __name__ == "__main__":
    main()