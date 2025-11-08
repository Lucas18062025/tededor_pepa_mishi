# ...existing code...
import pyttsx3
import os

# Abrir el libro con encoding explícito
script_dir = os.path.dirname(os.path.abspath(__file__))
book_path = os.path.join(script_dir, "book.txt")
with open(book_path, encoding="utf-8") as book_file:
    book_text = book_file.readlines()

engine = pyttsx3.init()

# Buscar una voz en español entre las voces instaladas
voices = engine.getProperty("voices")
es_voice = None

def _langs_to_str(langs):
    try:
        parts = []
        for item in langs:
            if isinstance(item, bytes):
                parts.append(item.decode("utf-8", errors="ignore"))
            else:
                parts.append(str(item))
        return " ".join(parts).lower()
    except Exception:
        return str(langs).lower()

for v in voices:
    name = (v.name or "").lower()
    lang = _langs_to_str(getattr(v, "languages", []))
    if "spanish" in name or "español" in name or "es" in lang or "es-es" in lang or "es_" in lang:
        es_voice = v
        break

if es_voice:
    engine.setProperty("voice", es_voice.id)
else:
    print("Aviso: no se encontró voz en español. Se usará la voz por defecto.")

# Ajustes opcionales
engine.setProperty("rate", 150)  # velocidad de lectura
engine.setProperty("volume", 1.0)  # volumen 0.0 - 1.0

# Encolar todo y reproducir (más eficiente que runAndWait en cada línea)
for line in book_text:
    engine.say(line)
engine.runAndWait()
# ...existing code...