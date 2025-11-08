import os
import shutil
import tempfile

def limpiar_temp():
    carpetas = [
        tempfile.gettempdir(),
        os.environ.get("TEMP"),
        os.environ.get("TMP"),
        os.path.join(os.environ["SystemRoot"], "Temp")
    ]

    for carpeta in carpetas:
        if carpeta and os.path.exists(carpeta):
            print(f"🧹 Limpiando: {carpeta}")
            for elemento in os.listdir(carpeta):
                ruta = os.path.join(carpeta, elemento)
                try:
                    if os.path.isfile(ruta) or os.path.islink(ruta):
                        os.unlink(ruta)
                    elif os.path.isdir(ruta):
                        shutil.rmtree(ruta)
                except Exception as e:
                    print(f"⚠️ No se pudo borrar: {ruta} - {e}")

limpiar_temp()
print("✅ Limpieza terminada.")