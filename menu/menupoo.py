from clases.ejemplo.calculadora import Calculadora
from ejercicios.ejercicio1_luzpoo import Ejercicio1Luz
from ejercicios.ejercicio2_calificacionpoo import Ejercicio2Calificacion


class Menu(object):
    def __init__(self):
        self.opcion = 0

    def mostrar_menu(self):
        print()
        print("Ejemplo programación orientada a objetos")
        print("1. Calculadora")
        print("2. Recibo de luz")
        print("3. Calificación final")
        print("0. Salir")

    def menu(self):
        self.opcion = ""
        while self.opcion != "0":
            self.mostrar_menu()
            self.opcion = input("Seleccione una opción: ")
            if self.opcion == "1":
                casio = Calculadora()
                casio.LeerNumeros()
                casio.calcularSuma()
                casio.mostrarSuma()
            elif self.opcion == "2":
                luz = Ejercicio1Luz()
                luz.leerConsumo()
                luz.calcularPago()
                luz.mostrarRecibo()
            elif self.opcion == "3":
                calif = Ejercicio2Calificacion()
                calif.leerParciales()
                calif.calcularFinal()
                calif.determinarEstado()
                calif.mostrarResultado()
            elif self.opcion == "0":
                print("Fin del programa.")
            else:
                print("Opción inválida. Intente nuevamente.") 