'''
Un cine cobra $80 por boleto. Los niños de hasta 12 años y los adultos de 60 años
o más pagan la mitad. Se necesita mostrar el precio del boleto según la edad.
'''
# PROBLEMA
# Calcular el precio en pesos del boleto de cine de una persona a partir de su
# edad.

# ENTRADAS
# edad : int, años, entero mayor o igual a 0 (se captura por teclado).

# SALIDAS
# edad   : int, años, se muestra tal como se capturó, junto con el precio.
# precio : float, pesos (MXN), se muestra con signo $, separador de miles y dos
#          decimales (por ejemplo $40.00).

# REGLAS Y SUPUESTOS
# - El boleto cuesta $80 y paga la mitad ($40) quien tiene 12 años o menos, o 60
#   años o más.
# - Límites exactos: 12 años ya paga la mitad (se usa <=); 13 años paga completo.
#   60 años ya paga la mitad (se usa >=); 59 años paga completo.
# - Las dos condiciones no se acumulan: nadie puede cumplir ambas a la vez, y el
#   descuento nunca es mayor a la mitad.
# - La edad se toma en años cumplidos, siempre como entero.
# - Todos los importes son 80 o 40 pesos; no hay redondeo de dinero.
# - La edad capturada es siempre un entero mayor o igual a 0; el programa no
#   valida la captura.

# ALGORITMO
# 1. Leer la edad con leerEdad.
# 2. Si edad <= 12 o edad >= 60:
#        precio = 80 * 0.5
# 3. En caso contrario:
#        precio = 80.0
# 4. Mostrar con mostrarPrecio la edad y el precio.

# CASOS DE PRUEBA
# edad -> precio esperado
# 8  -> $40.00  (niño, caso normal: 80 * 0.5)
# 12 -> $40.00  (límite superior de niño: paga la mitad)
# 13 -> $80.00  (apenas arriba del límite de niño: paga completo)
# 59 -> $80.00  (apenas bajo el límite de adulto mayor: paga completo)
# 60 -> $40.00  (límite de adulto mayor: paga la mitad)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No uses try/except, round ni constantes fuera de las funciones.
# - leerEdad usa input con el texto "Edad (años): " y convierte con int.
# - mostrarPrecio imprime exactamente dos líneas, en este orden:
#       Edad: {edad} años
#       Precio del boleto: ${precio:,.2f}
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerEdad() -> int : pide la edad en años por teclado y la devuelve como entero.
# calcularPrecio(edad) -> float : recibe la edad (int) y devuelve el precio del
#     boleto en pesos aplicando los pasos 2 y 3 del algoritmo.
# mostrarPrecio(edad, precio) -> None : recibe la edad (int) y el precio (float)
#     e imprime las dos líneas indicadas en las restricciones.
# Implementa el algoritmo anterior utilizando las funciones del contrato.


def leerEdad():
    edad = int(input("Edad (años): "))
    return edad


def calcularPrecio(edad):
    if edad <= 12 or edad >= 60:
        precio = 80 * 0.5
    else:
        precio = 80.0
    return precio


def mostrarPrecio(edad, precio):
    print(f"Edad: {edad} años")
    print(f"Precio del boleto: ${precio:,.2f}")
