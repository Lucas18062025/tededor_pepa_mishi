import random

minimo = 1
maximo = 10

numero_azar = random.randint(minimo, maximo)
print(numero_azar)

while True:
    Intento_usuario = int(input("Introduce un número"))
    if Intento_usuario > numero_azar:
        print("Te has pasado perra! El número es menor que " + str(Intento_usuario))
    elif Intento_usuario < numero_azar:
        print("Te has quedado corto perra! El número es mayor que " + str(Intento_usuario))
    else:
        print("Enhorabuena beibe! Has acertado el número es " + str(numero_azar))
        print("Quieres jugar otra vez?")
        break  