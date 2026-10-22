"""
Un conductor necesita conocer el rendimiento de combustible de su vehículo y el costo de un recorrido. El 
usuario deberá proporcionar la distancia recorrida en kilómetros y la cantidad de litros consumidos. El 
precio por litro será de $24.00.
"""


# PROBLEMA: qué se necesita resolver, en una oración. 
# Determinar el costo total de un recorrido en función de la distancia y el consumo de combustible.

# ENTRADAS: cada dato con tipo, unidad y rango válido. 
# distancia_recorrida = float (km), > 0
# litros_consumidos = float (L), > 0
# precio_por_litro = $24.00

# SALIDAS: información que se presenta, con tipo y formato. 
# costo_total = $ (valor calculado)

# REGLAS Y SUPUESTOS: valores fijos, condiciones, límites exactos y criterios de redondeo.
# - El costo del litro de combustible es fijo en $24.00.
# - Los cálculos se realizarán con dos decimales.

# ALGORITMO: pasos numerados y operaciones necesarias.
# leer distancia_recorrida
# leer litros_consumidos
# leer precio_por_litro = 24.00
# calcular costo_total = litros_consumidos * precio_por_litro
# calcular rendimiento por litro = distancia_recorrida / litros_consumidos
# mostrar resultados: distancia_recorrida, litros_consumidos, costo_total, rendimiento por litro

# CASOS DE PRUEBA: entradas y resultados esperados calculados manualmente. 
# caso 1: distancia_recorrida = 120, litros_consumidos = 10, costo_total = 240.00
# caso 2: distancia_recorrida = 250, litros_consumidos = 20, costo_total = 480.00
# caso 3: distancia_recorrida = 180, litros_consumidos = 15, costo_total = 360.00
# caso 4: distancia_recorrida = 300, litros_consumidos = 25, costo_total = 600.00

# RESTRICCIONES PARA EL AGENTE: condiciones que debe respetar Copilot; la única biblioteca externa permitida es tabulate. 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES: nombre, parámetros y valor de retorno de cada función. 
# leer_distancia_recorrida() -> float
# leer_litros_consumidos() -> float
# calcular_costo_total(litros_consumidos: float) -> float
# mostrar_resultados(distancia_recorrida: float, litros_consumidos: float, costo_total: float) -> None


def leer_distancia_recorrida() -> float:
    return float(input("Ingrese la distancia recorrida en kilómetros: "))

def leer_litros_consumidos() -> float:
    return float(input("Ingrese los litros consumidos: "))

def calcular_costo_total(litros_consumidos: float) -> float:
    precio_por_litro = 24.00
    return litros_consumidos * precio_por_litro

def mostrar_resultados(distancia_recorrida: float, litros_consumidos: float, costo_total: float) -> None:
    rendimiento_por_litro = distancia_recorrida / litros_consumidos
    print(f"Distancia recorrida: {distancia_recorrida} km")
    print(f"Litros consumidos: {litros_consumidos} L")
    print(f"Costo total: ${costo_total:.2f}")
    print(f"Rendimiento por litro: {rendimiento_por_litro:.2f} km/L")
