from ejercicios import ejercicio1_luz as ej1
from ejercicios import ejercicio2_calificacion as ej2
from ejercicios import ejercicio3_compra as ej3
from ejercicios import ejercicio4_estacionamiento as ej4


def ejecutarEjercicio1():
    consumo = ej1.leerConsumo()
    pago = ej1.calcularPago(consumo)
    ej1.mostrarRecibo(consumo, pago)


def ejecutarEjercicio2():
    p1, p2, p3 = ej2.leerParciales()
    final = ej2.calcularFinal(p1, p2, p3)
    estado = ej2.determinarEstado(p1, p2, p3, final)
    ej2.mostrarResultado(final, estado)


def ejecutarEjercicio3():
    subtotal = ej3.leerSubtotal()
    descuento = ej3.calcularDescuento(subtotal)
    iva = ej3.calcularIVA(subtotal, descuento)
    total = ej3.calcularTotal(subtotal, descuento, iva)
    ej3.mostrarTicket(subtotal, descuento, iva, total)


def ejecutarEjercicio4():
    minutos = ej4.leerMinutos()
    cobro = ej4.calcularCobro(minutos)
    ej4.mostrarCobro(minutos, cobro)


def mostrarMenu():
    print()
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN")
    print("1. Recibo de luz")
    print("2. Calificación final")
    print("3. Total de compra")
    print("4. Estacionamiento")
    print("0. Salir")


def menus():
    opcion = ""
    while opcion != "0":
        mostrarMenu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ejecutarEjercicio1()
        elif opcion == "2":
            ejecutarEjercicio2()
        elif opcion == "3":
            ejecutarEjercicio3()
        elif opcion == "4":
            ejecutarEjercicio4()
        elif opcion != "0":
            print("Opción no válida.")
