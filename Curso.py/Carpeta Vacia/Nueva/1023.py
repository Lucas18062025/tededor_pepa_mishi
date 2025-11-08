console = input("Ingresa un texto: ")
from rich import print
from rich.panel import Panel
from rich.console import Console
console = Console()
print("[bold red]                                         ¡Bienvenido a Rich!👋[/bold red]")
console.print(Panel("Este es un panel con borde y color green", title="Panel de prueba", subtitle="Hooli.py !", style="green"))
console.print(Panel("Este es un panel con borde y color yellow", title="Panel de prueba", subtitle="Holii.py !", style="yellow"))
console.print(Panel("Este es un panel con borde y color blue", title="Panel de prueba", subtitle="Holii.py !", style="blue"))
console.print(Panel("Este es un panel con borde y color red", title="Panel de prueba", subtitle="Holii.py !", style="red"))
print(f"[bold green]                                           Aquí toy yo 😋 [/bold green]")
input("Presiona Enter para cerrar...")
