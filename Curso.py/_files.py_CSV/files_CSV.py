import csv
import pandas as pd

with open('personas.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['Nombre', 'Edad', 'Ciudad'])
    # Write data
    writer.writerow(['Juancho', 21, 'Jujuy'])
    writer.writerow(['Ana', 30, 'Buenos Aires'])
    writer.writerow(['Luis', 25, 'Cordoba'])
    writer.writerow(['Maria', 28, 'Rosario'])
    writer.writerow(['Carlos', 22, 'Mendoza'])
    writer.writerow(['Sofia', 27, 'Salta'])
    writer.writerow(['Diego', 24, 'Tucuman'])
    writer.writerow(['Lucia', 29, 'Santa Fe'])
    writer.writerow(['Pedro', 26, 'Neuquen'])
    writer.writerow(['Elena', 23, 'Chaco'])
    # Write a final empty row
    writer.writerow([])
print("Archivo 'personas.csv' creado con éxito.")
input("Presiona Enter para continuar...")
import pandas as pd