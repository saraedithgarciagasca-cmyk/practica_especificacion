'''
La calificación final de una materia se obtiene de tres parciales que valen 30%,
30% y 40%. La materia se aprueba con 70. Un parcial menor a 50 reprueba la
materia. Se necesita mostrar la calificación final y si el alumno aprobó.
'''
# PROBLEMA
# Calcular la calificación final ponderada de un alumno a partir de sus tres
# parciales y determinar si aprobó la materia.

# ENTRADAS
# p1 : float, puntos, entre 0 y 100 (primer parcial, vale 30%).
# p2 : float, puntos, entre 0 y 100 (segundo parcial, vale 30%).
# p3 : float, puntos, entre 0 y 100 (tercer parcial, vale 40%).

# SALIDAS
# final : float, puntos, se muestra con dos decimales (por ejemplo 81.00).
# estado : str, exactamente "Aprobado" o "Reprobado".

# REGLAS Y SUPUESTOS
# - Ponderación: p1 vale 30%, p2 vale 30% y p3 vale 40% (suman 100%).
# - La calificación final es la suma ponderada y se calcula como
#   (p1 * 30 + p2 * 30 + p3 * 40) / 100.
# - La materia se aprueba con final >= 70 (70 exacto aprueba).
# - Un parcial reprueba la materia solo si es menor a 50 (< 50); un parcial de
#   exactamente 50 no reprueba por sí solo.
# - Si algún parcial es menor a 50 el estado es "Reprobado" aunque la
#   calificación final sea 70 o más.
# - Si algún parcial es menor a 50, la calificación final se muestra igual,
#   calculada con la misma fórmula, sin modificarla.
# - Las tres calificaciones capturadas están siempre entre 0 y 100; el programa
#   no valida la captura.
# - Redondeo: calcularFinal no redondea y la decisión de aprobar usa el valor
#   sin redondear. El redondeo a dos decimales ocurre solo al mostrar.

# ALGORITMO
# 1. Leer los tres parciales con leerParciales.
# 2. Calcular la calificación final:
#        final = (p1 * 30 + p2 * 30 + p3 * 40) / 100
# 3. Determinar el estado:
#    3.1. Si p1 < 50 o p2 < 50 o p3 < 50:
#             estado = "Reprobado"
#    3.2. En caso contrario, si final >= 70:
#             estado = "Aprobado"
#    3.3. En caso contrario:
#             estado = "Reprobado"
# 4. Mostrar con mostrarResultado la calificación final y el estado.

# CASOS DE PRUEBA
# (p1, p2, p3) -> final esperada, estado esperado
# (80, 70, 90)    -> 81.00,  Aprobado   (caso normal: 24 + 21 + 36 = 81)
# (70, 70, 70)    -> 70.00,  Aprobado   (límite de aprobación: 21 + 21 + 28 = 70)
# (69, 70, 70)    -> 69.70,  Reprobado  (apenas bajo el límite: 20.7 + 21 + 28 = 69.7)
# (100, 100, 40)  -> 76.00,  Reprobado  (30 + 30 + 16 = 76, pero p3 < 50; con solo
#                                        el promedio daría "Aprobado")
# (50, 100, 100)  -> 85.00,  Aprobado   (límite del parcial: 50 no es menor a 50;
#                                        15 + 30 + 40 = 85)
# (49, 100, 100)  -> 84.70,  Reprobado  (apenas bajo el límite del parcial:
#                                        14.7 + 30 + 40 = 84.7)
# (100, 100, 100) -> 100.00, Aprobado   (máximo posible)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No uses try/except, min, max, round ni constantes fuera de las funciones.
# - leerParciales usa input con los textos "Parcial 1: ", "Parcial 2: " y
#   "Parcial 3: ", en ese orden, y convierte cada valor con float.
# - mostrarResultado imprime exactamente dos líneas:
#       Calificación final: {final:.2f}
#       Estado: {estado}
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerParciales() -> tuple[float, float, float] : pide por teclado los tres
#     parciales y los devuelve en una tupla (p1, p2, p3).
# calcularFinal(p1, p2, p3) -> float : recibe los tres parciales (float) y
#     devuelve la calificación final aplicando el paso 2 del algoritmo.
# determinarEstado(p1, p2, p3, final) -> str : recibe los tres parciales y la
#     calificación final (float) y devuelve "Aprobado" o "Reprobado" aplicando
#     el paso 3 del algoritmo.
# mostrarResultado(final, estado) -> None : recibe la calificación final (float)
#     y el estado (str) e imprime las dos líneas indicadas en las restricciones.
# Implementa el algoritmo anterior utilizando las funciones del contrato.


def leerParciales():
    p1 = float(input("Parcial 1: "))
    p2 = float(input("Parcial 2: "))
    p3 = float(input("Parcial 3: "))
    return p1, p2, p3


def calcularFinal(p1, p2, p3):
    final = (p1 * 30 + p2 * 30 + p3 * 40) / 100
    return final


def determinarEstado(p1, p2, p3, final):
    if p1 < 50 or p2 < 50 or p3 < 50:
        estado = "Reprobado"
    elif final >= 70:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    return estado


def mostrarResultado(final, estado):
    print(f"Calificación final: {final:.2f}")
    print(f"Estado: {estado}")
