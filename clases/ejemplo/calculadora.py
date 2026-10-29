class Calculadora(object):
    def __init__(self):
        self.numero1 = 0 
        self.numero2 = 0
        self.suma = 0 

    def LeerNumeros(self): 
        self.numero1 = int(input("Número 1: "))
        self.numero2 = int(input("Número 2: ")) 

    def calcularSuma(self):
        self.suma = self.numero1 + self.numero2 

    def mostrarSuma(self):
        print(f"La suma es: {self.suma}") 