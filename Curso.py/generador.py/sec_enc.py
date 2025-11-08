# Ejemplo de cómo encriptar una contraseña
import os
from hashlib import scrypt

contraseña = "mi_contraseña_secreta".encode('utf-8')
salt = os.urandom(4)  # Genera un salt aleatorio de 4 bytes
# Utiliza scrypt para generar el hash de la contraseña
hashed = scrypt(
    password=contraseña,
    salt=salt,
    n=16384,
    r=8,
    p=1,
    dklen=64
)

print("Salt:", salt.hex())
print("Hash:", hashed.hex())