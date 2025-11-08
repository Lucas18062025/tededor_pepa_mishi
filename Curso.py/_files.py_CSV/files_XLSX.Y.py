import pandas as pd

# Leer el archivo CSV y guardarlo como Excel
df = pd.read_csv('personas.csv')
df.to_excel('personas.xlsx', index=False)
print("Archivo 'personas.xlsx' creado con éxito.")