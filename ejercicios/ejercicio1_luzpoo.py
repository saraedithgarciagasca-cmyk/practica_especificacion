class Ejercicio1Luz: 

    def __init__(self):
        self.consumo = 0
        self.pago = 0.0

    def leerConsumo(self):
        self.consumo = int(input("Consumo del mes (kWh): "))
        return self.consumo

    def calcularPago(self):
        if self.consumo <= 150:
            self.pago = self.consumo * 1.00
        elif self.consumo <= 280:
            self.pago = 150 * 1.00 + (self.consumo - 150) * 1.50
        else:
            self.pago = 150 * 1.00 + 130 * 1.50 + (self.consumo - 280) * 3.00
        return self.pago

    def mostrarRecibo(self):
        print(f"Consumo: {self.consumo} kWh")
        print(f"Importe a pagar: ${self.pago:,.2f}") 