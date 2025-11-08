import math

class calcularPerimetro:
 
    """
    Classe para calcular o perímetro de um quadrado.
    Parâmetros:
        lado (float): O comprimento do lado do quadrado.
    Métodos:
        calcular():
            Calcula e retorna o perímetro do quadrado.
    Exemplo de uso:
        >>> perimetro = calcularPerimetro(5)
        >>> resultado = perimetro.calcular()
        >>> print(resultado)
        20
    """
    # Classe para calcular o perímetro de um quadrado
    
    def __init__(self, lado):
        self.lado = lado

    def calcular(self):
        return 4 * self.lado
# Classe para calcular o perímetro de um retângulo
class calcularPerimetroRetangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular(self):
        return 2 * (self.base + self.altura)
# Classe para calcular o perímetro de um triângulo
class calcularPerimetroTriangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular(self):
        return self.lado1 + self.lado2 + self.lado3
# Classe para calcular o perímetro de um círculo
class calcularPerimetroCirculo:
    def __init__(self, raio):
        self.raio = raio

    def calcular(self):
        return 2 * math.pi * self.raio
# Classe para calcular o perímetro de um trapézio
class calcularPerimetroTrapezio:
    def __init__(self, base_maior, base_menor, lado1, lado2):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular(self):
        return self.base_maior + self.base_menor + self.lado1 + self.lado2
input("Módulo calcularPerimetro.py carregado com sucesso!")    