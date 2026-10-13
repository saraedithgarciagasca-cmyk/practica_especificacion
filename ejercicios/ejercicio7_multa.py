'''
En una avenida el límite es de 60 km/h. Si se excede hasta por 20 km/h, la multa
es de $500. Si se excede por más de 20 km/h, la multa es de $1,000. Se necesita
mostrar la multa a partir de la velocidad del vehículo.
'''
# PROBLEMA
# Calcular la multa en pesos que recibe un vehículo a partir de su velocidad en
# una avenida con límite de 60 km/h.

# ENTRADAS
# velocidad : int, km/h, entero mayor o igual a 0 (se captura por teclado).

# SALIDAS
# velocidad : int, km/h, se muestra tal como se capturó, junto con la multa.
# multa     : int, pesos (MXN), se muestra con signo $, separador de miles y dos
#             decimales (por ejemplo $1,000.00).

# REGLAS Y SUPUESTOS
# - El límite de velocidad es 60 km/h. Circular a 60 km/h o menos no genera multa
#   (límite exacto: 60 km/h no se multa, se usa <=).
# - El exceso es velocidad - 60.
# - Si el exceso es de 1 a 20 km/h (velocidad de 61 a 80), la multa es $500
#   (límite exacto: un exceso de 20 km/h, es decir 80 km/h, paga $500, se usa <=).
# - Si el exceso es mayor a 20 km/h (velocidad de 81 o más), la multa es $1,000.
# - Las multas no se acumulan: solo se aplica la del tramo que corresponde.
# - Todos los importes son pesos enteros; no hay redondeo de dinero.
# - La velocidad capturada es siempre un entero mayor o igual a 0; el programa no
#   valida la captura.

# ALGORITMO
# 1. Leer la velocidad con leerVelocidad.
# 2. Si velocidad <= 60:
#        multa = 0
# 3. En caso contrario, si velocidad <= 80:
#        multa = 500
# 4. En caso contrario:
#        multa = 1000
# 5. Mostrar con mostrarMulta la velocidad y la multa.

# CASOS DE PRUEBA
# velocidad -> multa esperada
# 50 -> $0.00      (caso normal, bajo el límite)
# 60 -> $0.00      (límite exacto: sin multa)
# 61 -> $500.00    (apenas arriba del límite: exceso de 1 km/h)
# 80 -> $500.00    (límite del primer tramo: exceso de 20 km/h)
# 81 -> $1,000.00  (apenas arriba del primer tramo: exceso de 21 km/h)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No uses try/except, round ni constantes fuera de las funciones.
# - leerVelocidad usa input con el texto "Velocidad (km/h): " y convierte con int.
# - mostrarMulta imprime exactamente dos líneas, en este orden:
#       Velocidad: {velocidad} km/h
#       Multa: ${multa:,.2f}
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerVelocidad() -> int : pide la velocidad en km/h por teclado y la devuelve
#     como entero.
# calcularMulta(velocidad) -> int : recibe la velocidad (int) y devuelve la multa
#     en pesos aplicando los pasos 2 a 4 del algoritmo.
# mostrarMulta(velocidad, multa) -> None : recibe la velocidad (int) y la multa
#     (int) e imprime las dos líneas indicadas en las restricciones.
# Implementa el algoritmo anterior utilizando las funciones del contrato.


def leerVelocidad():
    velocidad = int(input("Velocidad (km/h): "))
    return velocidad


def calcularMulta(velocidad):
    if velocidad <= 60:
        multa = 0
    elif velocidad <= 80:
        multa = 500
    else:
        multa = 1000
    return multa


def mostrarMulta(velocidad, multa):
    print(f"Velocidad: {velocidad} km/h")
    print(f"Multa: ${multa:,.2f}")
