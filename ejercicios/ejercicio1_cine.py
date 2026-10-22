"""
Un cine necesita desarrollar un programa que permita determinar el importe de una compra de boletos. 
Cada boleto cuesta $75.00. El usuario deberá indicar cuántos boletos desea comprar. Cuando se adquieran 4 
boletos o más, se aplicará un descuento del 10% sobre el subtotal. Para compras menores a 4 boletos, no se 
aplicará descuento. 
"""


# PROBLEMA: qué se necesita resolver, en una oración. 
# Determinar el importe total de la compra de boletos en un cine, considerando descuentos por cantidad.

# ENTRADAS: cada dato con tipo, unidad y rango válido. 
#costo_boleto = $75.00
#descuento = 10% (aplicable solo si se compran 4 boletos o más)

# SALIDAS: información que se presenta, con tipo y formato. 
#importe_total = $ (valor calculado)

# REGLAS Y SUPUESTOS: valores fijos, condiciones, límites exactos y criterios de redondeo.
# - El costo del boleto es fijo en $75.00.
# - El descuento del 10% se aplica solo si se compran 4 boletos o más.
# - Los cálculos se realizarán con dos decimales.

# ALGORITMO: pasos numerados y operaciones necesarias. 
# leer costo_boleto
# leer cantidad_boletos 
# calcular subtotal = costo_boleto * cantidad_boletos
# si cantidad_boletos >= 4, aplicar descuento
# calcular importe_total = subtotal - descuento
# mostrar importe_total con dos decimales

# CASOS DE PRUEBA: entradas y resultados esperados calculados manualmente. 
# caso 1: cantidad_boletos = 1 , importe_total = 75.00
# caso 2: cantidad_boletos = 3 , importe_total = 225.00
# caso 3: cantidad_boletos = 4 , importe_total = 270.00
# caso 4: cantidad_boletos = 6 , importe_total = 405.00

# RESTRICCIONES PARA EL AGENTE: condiciones que debe respetar Copilot; la única biblioteca externa permitida es tabulate. 
# - Implementa exactamente este algoritmo, en el mismo orden. 
# - Usa únicamente las funciones del contrato, con esas firmas. 
# - No agregues clases, funciones auxiliares ni bibliotecas. 
# - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES: nombre, parámetros y valor de retorno de cada función. 
# leer_costo_boleto() -> float
# leer_cantidad_boletos() -> int
# calcular_subtotal(costo_boleto: float, cantidad_boletos: int) -> float
# aplicar_descuento(subtotal: float, cantidad_boletos: int) -> float
# calcular_importe_total(subtotal: float, descuento: float) -> float
# mostrar_importe_total(importe_total: float) -> None


def leer_costo_boleto() -> float:
    return 75.00

def leer_cantidad_boletos() -> int:
    return int(input("Ingrese la cantidad de boletos: "))

def calcular_subtotal(costo_boleto: float, cantidad_boletos: int) -> float:
    return costo_boleto * cantidad_boletos

def aplicar_descuento(subtotal: float, cantidad_boletos: int) -> float:
    if cantidad_boletos >= 4:
        return subtotal * 0.10
    return 0

def calcular_importe_total(subtotal: float, descuento: float) -> float:
    return subtotal - descuento

def mostrar_importe_total(importe_total: float) -> None:
    print(f"Importe total: ${importe_total:.2f}")