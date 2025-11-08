# Primer Proyecto con Glances
# Glances es una herramienta de monitoreo de sistema en tiempo real escrita en Python.
# Uso Básico:
# Para iniciar Glances en modo estándar:
#   glances
# Características Principales:
# - Monitoreo de CPU, memoria, disco y red.
# - Interfaz web disponible con glances -w.
# - Exportación de datos a diferentes formatos.
# Recursos:
# - Documentación oficial: https://nicolargo.github.io/glances/
# - Repositorio en GitHub: https://github.com/nicolargo/glances
#Comprobar si hay un Glances ya en ejecución y el log:
# Inicia Glances en modo web (usa la ruta exacta de tu python)
# "C:\Users\NETBOOK\AppData\Local\Programs\Python\Python310\python.exe" -m glances -w
# Ver el log rápido
# Get-Content "C:\Users\NETBOOK\AppData\Local\Temp\glances-NETBOOK.log" -Tail 50
# Comprobar si hay proceso Python corriendo (posible Glances)
# Get-Process python -ErrorAction SilentlyContinue
# Buscar proceso y detenerlo (ejemplo)
# Get-Process python | Where-Object { $_.Path -like "*Python310*" }
# luego Stop-Process -Id <PID>
# Comprobar instalación de Glances
# donde está instalado Glances
# where.exe glances