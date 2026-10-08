'''
Una compañía eléctrica cobra el consumo mensual con tres tarifas: $1.00 por kWh
hasta 150 kWh, $1.50 por kWh de 151 a 280 kWh y $3.00 por kWh arriba de 280 kWh.
Se necesita calcular el importe del recibo a partir del consumo del mes.
'''
# PROBLEMA
# Calcular el importe en pesos del recibo de luz de un usuario a partir de su
# consumo mensual en kWh.

# ENTRADAS
# consumo : int, kWh, entero mayor o igual a 0 (se captura por teclado).

# SALIDAS
# pago : float, pesos (MXN), se muestra con signo $, separador de miles y
#        dos decimales (por ejemplo $1,234.50).
# consumo : int, kWh, se muestra tal como se capturó, junto con el pago.

# REGLAS Y SUPUESTOS
# - Las tarifas se aplican por bloques (tarifa progresiva): cada kWh se cobra
#   a la tarifa del bloque en el que cae, no todo el consumo a la tarifa más alta.
# - Bloque 1: kWh 1 a 150, a $1.00 por kWh.
# - Bloque 2: kWh 151 a 280, a $1.50 por kWh.
# - Bloque 3: kWh 281 en adelante, a $3.00 por kWh.
# - Límites exactos: un consumo de 150 kWh pertenece por completo al bloque 1
#   (se usa <=); un consumo de 280 kWh llega completo hasta el bloque 2 (se usa <=).
# - El consumo capturado es siempre un entero mayor o igual a 0; el programa no
#   valida la captura.
# - No hay cargos adicionales (sin IVA, sin cargo fijo, sin impuestos).
# - Redondeo: calcularPago no redondea; con consumo entero el importe siempre
#   es múltiplo de $0.50. El redondeo a dos decimales ocurre solo al mostrar.

# ALGORITMO
# 1. Leer el consumo con leerConsumo.
# 2. Si consumo <= 150:
#        pago = consumo * 1.00
# 3. En caso contrario, si consumo <= 280:
#        pago = 150 * 1.00 + (consumo - 150) * 1.50
# 4. En caso contrario:
#        pago = 150 * 1.00 + 130 * 1.50 + (consumo - 280) * 3.00
# 5. Mostrar con mostrarRecibo el consumo y el pago.

# CASOS DE PRUEBA
# consumo (kWh) -> pago esperado
# 0   -> $0.00      (mínimo posible)
# 100 -> $100.00    (caso normal, bloque 1: 100 * 1.00)
# 150 -> $150.00    (límite del bloque 1: 150 * 1.00)
# 151 -> $151.50    (apenas arriba del límite: 150 + 1 * 1.50)
# 200 -> $225.00    (bloque 2: 150 + 50 * 1.50; con tarifa única daría $300.00)
# 280 -> $345.00    (límite del bloque 2: 150 + 130 * 1.50)
# 281 -> $348.00    (apenas arriba del límite: 345 + 1 * 3.00)
# 300 -> $405.00    (bloque 3: 345 + 20 * 3.00)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No uses try/except ni constantes fuera de las funciones.
# - leerConsumo usa input con el texto "Consumo del mes (kWh): " y convierte con int.
# - mostrarRecibo imprime exactamente dos líneas:
#       Consumo: {consumo} kWh
#       Importe a pagar: ${pago:,.2f}
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerConsumo() -> int : pide el consumo en kWh por teclado y lo devuelve como entero.
# calcularPago(consumo) -> float : recibe el consumo en kWh (int) y devuelve el
#     importe en pesos aplicando los pasos 2 a 4 del algoritmo.
# mostrarRecibo(consumo, pago) -> None : recibe el consumo (int) y el pago (float)
#     e imprime las dos líneas indicadas en las restricciones.
# Implementa el algoritmo anterior utilizando las funciones del contrato.
