Estilizar el encabezado de personas

Este directorio contiene `files_CSV.py` que crea `personas.csv` y `files_XLSX.py` que convierte ese CSV a `personas.xlsx` aplicando estilo al encabezado (negrita y fondo coloreado) usando `openpyxl`.

Instalación:

En Windows (cmd.exe):

    pip install openpyxl

Uso:

1. Genera `personas.csv` si no existe:

    python files_CSV.py

2. Convierte y estiliza a Excel:

    python files_XLSX.py

Alternativas:

- Usar `rich` para tablas coloreadas en consola.
- Generar HTML con CSS para mostrar encabezado resaltado en navegador.
