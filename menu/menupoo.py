from clases.ejemplo.calculadora import Calculadora 



class Menu(object): 
    def __init__(self):
        self.opcion = 0 

    
    def mostrar_menu(self): 
        print()
        print("Ejemplo programación orientada a objetos") 
        print("1. Calculadora")
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
            else:
                print("Opción inválida. Intente nuevamente.") 