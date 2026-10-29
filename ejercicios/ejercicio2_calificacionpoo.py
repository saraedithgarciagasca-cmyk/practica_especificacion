
class Ejercicio2Calificacion:

    def __init__(self):
        self.p1 = 0.0
        self.p2 = 0.0
        self.p3 = 0.0
        self.final = 0.0
        self.estado = ""

    def leerParciales(self):
        self.p1 = float(input("Parcial 1: "))
        self.p2 = float(input("Parcial 2: "))
        self.p3 = float(input("Parcial 3: "))
        return self.p1, self.p2, self.p3

    def calcularFinal(self):
        self.final = (self.p1 * 30 + self.p2 * 30 + self.p3 * 40) / 100
        return self.final

    def determinarEstado(self):
        if self.p1 < 50 or self.p2 < 50 or self.p3 < 50:
            self.estado = "Reprobado"
        elif self.final >= 70:
            self.estado = "Aprobado"
        else:
            self.estado = "Reprobado"
        return self.estado

    def mostrarResultado(self):
        print(f"Calificación final: {self.final:.2f}")
        print(f"Estado: {self.estado}") 