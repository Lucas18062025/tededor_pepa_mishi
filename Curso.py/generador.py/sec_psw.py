import string
import random
# Genera una contraseña aleatoria de una longitud especificada
def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation # Letras mayúsculas y minúsculas, dígitos y caracteres especiales
    # Asegura que la contraseña tenga al menos un carácter de cada tipo
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña
# Ejemplo de uso
print("\n", "🔐🔑", generar_contraseña(12))  # Genera una contraseña de 12 caracteres