# Los modulos son una forma de organizar el código en Python.
# Estos archivos de código pueden contener funciones, clases y variables que pueden ser importadas en otros archivos.
# Este módulo contiene funciones para crear y manipular modelos geométricos.
# from calcularArea import *  ¡El from permite importar todas las funciones del módulo calcularArea!

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Asegura que el directorio actual esté en sys.path
import calcularArea  # Importa el módulo calcularArea
# Ejemplo de uso de las funciones del módulo calcularArea
print(calcularArea.calcular_area_circulo(3))  # Ejemplo de uso de la función calcular_area_circulo
print(calcularArea.calcular_area_rectangulo(4, 5))  # Ejemplo de uso de la función calcular_area_rectangulo
print(calcularArea.calcular_area_triangulo(3, 6))  # Ejemplo de uso de la función calcular_area_triangulo
print(calcularArea.calcular_area_cuadrado(4))  # Ejemplo de uso de la función calcular_area_cuadrado
print(calcularArea.calcular_area_trapecio(5, 3, 4))  # Ejemplo de uso de la función calcular_area_trapecio
print(calcularArea.calcular_area_rombo(5, 3))  # Ejemplo de uso de la función calcular_area_rombo.
input("Presiona Enter para cerrar...")