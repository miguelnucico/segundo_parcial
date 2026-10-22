from ejercicios.ejercicio1_cine import leer_costo_boleto, leer_cantidad_boletos, calcular_subtotal, aplicar_descuento, calcular_importe_total, mostrar_importe_total
from ejercicios.ejercicio2_combustible import leer_distancia_recorrida, leer_litros_consumidos, calcular_costo_total, mostrar_resultados


def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Calcular importe total de boletos de cine")
        print("2. Calcular costo total de combustible")
        print("3. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            costo_boleto = leer_costo_boleto()
            cantidad_boletos = leer_cantidad_boletos()
            subtotal = calcular_subtotal(costo_boleto, cantidad_boletos)
            descuento = aplicar_descuento(subtotal, cantidad_boletos)
            importe_total = calcular_importe_total(subtotal, descuento)
            mostrar_importe_total(importe_total)

        elif opcion == "2":
            distancia_recorrida = leer_distancia_recorrida()
            litros_consumidos = leer_litros_consumidos()
            costo_total = calcular_costo_total(litros_consumidos)
            mostrar_resultados(distancia_recorrida, litros_consumidos, costo_total)

        elif opcion == "3":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, intente nuevamente.")