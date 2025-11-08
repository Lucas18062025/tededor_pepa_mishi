from gtts import gTTS
import os
# proyectos.py/texto_a_voz.py
# Este script convierte un texto a voz y lo guarda como un archivo MP3.
# Asegúrate de tener instalada la biblioteca gTTS:

texto = "Marcela Marcela la chachi quiere hacer fideos."*3
idioma = "es"

tts = gTTS(text=texto, lang=idioma, slow=False)
nombre_archivo = "texto_a_voz.mp3"
tts.save(nombre_archivo)

os.system(f"start {nombre_archivo}")
# El archivo de audio se guardará en el directorio actual
# y se reproducirá automáticamente si el sistema lo permite.