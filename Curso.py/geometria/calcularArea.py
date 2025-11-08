PI = 3.14159

def calcular_area_circulo(radio):
    """Calcula el área de un círculo dado su radio."""
    return PI * (radio ** 2)
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura
def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    return (base * altura) / 2
def calcular_area_cuadrado(lado):
    """Calcula el área de un cuadrado dado su lado."""
    return lado ** 2
def calcular_area_trapecio(base_mayor, base_menor, altura):
    """Calcula el área de un trapecio dado sus bases y altura."""
    return ((base_mayor + base_menor) * altura) / 2
def calcular_area_elipse(a, b):
    """Calcula el área de una elipse dado sus semiejes a y b."""
    return PI * a * b
def calcular_area_sector_circular(radio, angulo):
    """Calcula el área de un sector circular dado su radio y ángulo en radianes."""
    return (angulo / (2 * PI)) * calcular_area_circulo(radio)
def calcular_area_paralelogramo(base, altura):
    """Calcula el área de un paralelogramo dado su base y altura."""
    return base * altura
def calcular_area_rombo(base_mayor, base_menor):
    """Calcula el área de un rombo dado sus diagonales."""
    return (base_mayor * base_menor) / 2
def error(e,q=1):
    input(e)
    if q:
        exit(10)