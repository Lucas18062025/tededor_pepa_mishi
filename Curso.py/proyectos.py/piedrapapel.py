import random
from time import sleep

# Juego de Piedra, Papel o Tijera
op = ["piedra", "papel", "tijera"]

while True:
    user = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
    sleep(0.5)
    if user == "salir":
        print("Juego terminado.")
        break
    if user not in op:
        print("Opción no válida. Inténtalo de nuevo.")
        continue
    computer = random.choice(op)
    sleep(0.5)

    print(f"La computadora eligió: {computer}")

    if user == computer:
        print("¡Es un empate!")
    elif (user == "piedra" and computer == "tijera") or \
         (user == "papel" and computer == "piedra") or \
         (user == "tijera" and computer == "papel"):
        print("\n¡Ganaste!")
    else:
        print("\n¡Perdiste!")