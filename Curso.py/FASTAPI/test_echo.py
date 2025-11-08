import subprocess
import sys
import time
import os

PY = sys.executable
SERVER = os.path.join(os.path.dirname(__file__), 'server_improved.py')
CLIENT = os.path.join(os.path.dirname(__file__), 'client.py')

# Iniciar servidor en background
proc = subprocess.Popen([PY, SERVER], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

try:
    # Dar tiempo para que el servidor inicie
    time.sleep(1)
    # Ejecutar cliente
    client = subprocess.run([PY, CLIENT, 'mensaje-de-prueba'], capture_output=True, text=True, timeout=5)
    print('Salida cliente:')
    print(client.stdout)

    # Leer un poco de salida del servidor: terminarlo y leer su output con timeout
    time.sleep(0.2)
    out = ''
    try:
        proc.terminate()
        out, _ = proc.communicate(timeout=2)
    except Exception:
        try:
            proc.kill()
            out, _ = proc.communicate(timeout=1)
        except Exception:
            out = ''
    print('Salida servidor (parcial):')
    print(out)

    # Verificar que el cliente recibió eco
    if 'mensaje-de-prueba' in (client.stdout or ''):
        print('TEST OK: cliente recibió eco')
        sys.exit(0)
    else:
        print('TEST FAIL: cliente no recibió eco')
        sys.exit(2)
finally:
    proc.terminate()
    try:
        proc.wait(timeout=2)
    except Exception:
        proc.kill()
