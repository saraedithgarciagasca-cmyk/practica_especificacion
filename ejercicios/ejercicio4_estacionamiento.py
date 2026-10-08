'''
Un estacionamiento cobra $20 la primera hora y $15 por cada hora adicional o
fracción. El cobro máximo es de $150. El sistema recibe el tiempo de estancia en
minutos y muestra el importe a cobrar.
'''
# PROBLEMA
# Calcular el importe en pesos que el estacionamiento cobra a un cliente a partir
# de los minutos que estuvo su vehículo.

# ENTRADAS
# minutos : int, minutos, entero mayor o igual a 1 (se captura por teclado).

# SALIDAS
# minutos : int, minutos, se muestra tal como se capturó, junto con el cobro.
# cobro   : int, pesos (MXN), se muestra con signo $, separador de miles y dos
#           decimales (por ejemplo $35.00).

# REGLAS Y SUPUESTOS
# - La primera hora cuesta $20. Cualquier estancia de 1 a 60 minutos cuesta $20,
#   aunque no se complete la hora (límite exacto: 60 minutos cuesta $20, se usa <=).
# - Cada hora adicional, o fracción de hora adicional, cuesta $15. La primera hora
#   adicional comienza en el minuto 61.
# - Redondeo de la fracción: toda fracción de hora adicional se redondea hacia
#   arriba a una hora completa y se cobra completa. Con minutos adicionales
#   (minutos - 60), las horas adicionales son el cociente redondeado hacia arriba
#   de minutos adicionales entre 60, calculado solo con enteros como
#   (minutos - 60 + 59) // 60. No se cobra proporcional ni se descarta la fracción.
# - Ejemplo del redondeo: 61 minutos son 1 hora adicional; 120 minutos son 1 hora
#   adicional exacta; 121 minutos son 2 horas adicionales.
# - Cobro máximo: el cobro nunca excede $150. Si el cálculo da más de 150, el
#   cobro es 150 (límite exacto: un cálculo de 150 se queda en 150, se usa >).
# - Módulos de la biblioteca estándar: NO se permite usar ninguno. El archivo no
#   debe contener import (ni math, ni otro). El redondeo hacia arriba se hace
#   solo con aritmética entera, como indica la regla de redondeo.
# - Todos los importes son pesos enteros, por lo que no hay redondeo de dinero.
# - El número de minutos capturado es siempre un entero mayor o igual a 1; el
#   programa no valida la captura.

# ALGORITMO
# 1. Leer los minutos con leerMinutos.
# 2. Si minutos <= 60:
#        cobro = 20
# 3. En caso contrario:
#        horas_adicionales = (minutos - 60 + 59) // 60
#        cobro = 20 + horas_adicionales * 15
# 4. Si cobro > 150:
#        cobro = 150
# 5. Mostrar con mostrarCobro los minutos y el cobro.

# CASOS DE PRUEBA
# minutos -> cobro esperado
# 1   -> $20.00   (mínimo posible: primera hora)
# 45  -> $20.00   (caso normal, dentro de la primera hora)
# 60  -> $20.00   (límite de la primera hora)
# 61  -> $35.00   (apenas arriba del límite: 1 minuto extra cobra 1 hora adicional:
#                  20 + 1 * 15)
# 120 -> $35.00   (1 hora adicional exacta, sin fracción: 20 + 1 * 15)
# 121 -> $50.00   (1 minuto sobre la hora exacta cobra otra hora: 20 + 2 * 15)
# 150 -> $50.00   (90 minutos adicionales = 1.5 horas, se redondean a 2: 20 + 2 * 15;
#                  si la fracción se descartara daría $35.00 y si se cobrara
#                  proporcional daría $42.50)
# 540 -> $140.00  (480 minutos adicionales = 8 horas exactas: 20 + 8 * 15; justo
#                  bajo el tope)
# 541 -> $150.00  (9 horas adicionales: 20 + 9 * 15 = 155, se topa a 150)
# 600 -> $150.00  (540 minutos adicionales = 9 horas: 20 + 9 * 15 = 155, se topa a 150)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No uses import de ningún módulo (ni math ni ningún otro de la biblioteca estándar).
# - No uses min, max, round, ni división con / (solo la división entera //).
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No uses try/except ni constantes fuera de las funciones.
# - leerMinutos usa input con el texto "Tiempo de estancia (minutos): " y convierte con int.
# - mostrarCobro imprime exactamente dos líneas:
#       Tiempo de estancia: {minutos} minutos
#       Importe a cobrar: ${cobro:,.2f}
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerMinutos() -> int : pide el tiempo de estancia en minutos por teclado y lo
#     devuelve como entero.
# calcularCobro(minutos) -> int : recibe los minutos (int) y devuelve el importe
#     en pesos aplicando los pasos 2 a 4 del algoritmo.
# mostrarCobro(minutos, cobro) -> None : recibe los minutos (int) y el cobro (int)
#     e imprime las dos líneas indicadas en las restricciones.
# Implementa el algoritmo anterior utilizando las funciones del contrato.
