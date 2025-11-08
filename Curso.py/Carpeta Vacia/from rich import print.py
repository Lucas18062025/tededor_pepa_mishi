# ...importar code...
from rich import print
from rich.panel import Panel
from rich.console import Console

console = Console()

print("[bold magenta]¡Bienvenido a Rich![/bold magenta]")

console.print(Panel("Este es un panel con borde y color verde", title="Panel de prueba", subtitle="Rich Rocks!", style="green"))
console.print(Panel("Este es un panel con borde y color amarillo", title="Panel de prueba", subtitle="Rich Rocks!", style="yellow"))
console.print(Panel("Este es un panel con borde y color azul", title="Panel de prueba", subtitle="Rich Rocks!", style="blue"))
console.print(Panel("Este es un panel con borde y color verde", title="Panel de prueba", subtitle="Rich Rocks!", style="green"))

# Añadir esto para que la ventana espere antes de cerrarse
input("Presiona Enter para cerrar...")
# ...existing code...