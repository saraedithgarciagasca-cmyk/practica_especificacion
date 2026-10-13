'''
Un parque renta bicicletas a $30 por hora. Si se rentan 3 horas o más, se aplica
un 15% de descuento. Se necesita mostrar el importe a pagar según las horas de
renta.
'''
# PROBLEMA
# Calcular el importe en pesos que paga un cliente por la renta de una bicicleta
# a partir de las horas que la rentó.

# ENTRADAS
# horas : int, horas, entero mayor o igual a 1 (se captura por teclado).

# SALIDAS
# horas   : int, horas, se muestra tal como se capturó, junto con el importe.
# importe : float, pesos (MXN), se muestra con signo $, separador de miles y dos
#           decimales (por ejemplo $76.50).

# REGLAS Y SUPUESTOS
# - La tarifa es de $30 por cada hora rentada.
# - Las horas son siempre enteras; no se cobran fracciones de hora.
# - Si horas >= 3, se aplica 15% de descuento sobre el total de la renta, es
#   decir sobre todas las horas y no solo sobre las que pasan de la tercera.
# - Límite exacto: 3 horas ya recibe el descuento (se usa >=); 2 horas no.
# - Si horas < 3, no hay descuento.
# - Redondeo: ningún cálculo se redondea. El redondeo a dos decimales ocurre solo
#   al mostrar el importe.
# - Las horas capturadas son siempre un entero mayor o igual a 1; el programa no
#   valida la captura.

# ALGORITMO
# 1. Leer las horas con leerHoras.
# 2. Calcular el importe base:
#        importe = horas * 30
# 3. Si horas >= 3:
#        importe = importe * 0.85
# 4. Mostrar con mostrarRenta las horas y el importe.

# CASOS DE PRUEBA
# horas -> importe esperado
# 1 -> $30.00   (caso mínimo, sin descuento: 1 * 30)
# 2 -> $60.00   (apenas bajo el límite, sin descuento: 2 * 30)
# 3 -> $76.50   (límite del descuento: 3 * 30 = 90; 90 * 0.85 = 76.50)
# 4 -> $102.00  (con descuento: 4 * 30 = 120; 120 * 0.85 = 102.00)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No uses try/except, round ni constantes fuera de las funciones.
# - leerHoras usa input con el texto "Horas de renta: " y convierte con int.
# - mostrarRenta imprime exactamente dos líneas, en este orden:
#       Horas de renta: {horas}
#       Importe a pagar: ${importe:,.2f}
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerHoras() -> int : pide las horas de renta por teclado y las devuelve como
#     entero.
# calcularRenta(horas) -> float : recibe las horas (int) y devuelve el importe en
#     pesos aplicando los pasos 2 y 3 del algoritmo.
# mostrarRenta(horas, importe) -> None : recibe las horas (int) y el importe
#     (float) e imprime las dos líneas indicadas en las restricciones.
# Implementa el algoritmo anterior utilizando las funciones del contrato.


def leerHoras():
    horas = int(input("Horas de renta: "))
    return horas


def calcularRenta(horas):
    importe = horas * 30
    if horas >= 3:
        importe = importe * 0.85
    return importe


def mostrarRenta(horas, importe):
    print(f"Horas de renta: {horas}")
    print(f"Importe a pagar: ${importe:,.2f}")
