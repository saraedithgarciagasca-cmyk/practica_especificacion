'''
Una tienda aplica 10% de descuento en compras de $1,000 o más y 20% en compras
de $5,000 o más. A la compra se le agrega el 16% de IVA. Se necesita mostrar el
ticket con subtotal, descuento, IVA y total.
'''
# PROBLEMA
# Calcular el descuento, el IVA y el total a pagar de una compra a partir de su
# subtotal, y mostrar el ticket al cliente de la tienda.

# ENTRADAS
# subtotal : float, pesos (MXN), mayor o igual a 0, suma de los artículos antes
#            de descuento e IVA (se captura por teclado).

# SALIDAS
# subtotal  : float, pesos, se muestra con signo $, separador de miles y dos decimales.
# descuento : float, pesos, monto del descuento mostrado como cantidad positiva,
#             con signo $, separador de miles y dos decimales.
# iva       : float, pesos, con signo $, separador de miles y dos decimales.
# total     : float, pesos, con signo $, separador de miles y dos decimales.

# REGLAS Y SUPUESTOS
# - El porcentaje de descuento depende del subtotal capturado, antes de aplicar
#   el descuento.
# - Si subtotal >= 5000, el descuento es 20% del subtotal.
# - Si subtotal >= 1000 y subtotal < 5000, el descuento es 10% del subtotal.
# - Si subtotal < 1000, el descuento es 0.
# - Los descuentos no se acumulan: una compra de $5,000 o más recibe solo 20%,
#   no 20% más 10%.
# - Límites exactos: $1,000 recibe 10% (se usa >=); $5,000 recibe 20% (se usa >=).
# - El IVA es 16% y se calcula sobre el subtotal ya con el descuento aplicado
#   (subtotal - descuento), no sobre el subtotal original.
# - El total es el subtotal, menos el descuento, más el IVA.
# - El subtotal capturado es siempre un número mayor o igual a 0; el programa no
#   valida la captura.
# - Redondeo: ningún cálculo se redondea. El redondeo a dos decimales ocurre solo
#   al mostrar el ticket.

# ALGORITMO
# 1. Leer el subtotal con leerSubtotal.
# 2. Calcular el descuento:
#    2.1. Si subtotal >= 5000:
#             descuento = subtotal * 0.20
#    2.2. En caso contrario, si subtotal >= 1000:
#             descuento = subtotal * 0.10
#    2.3. En caso contrario:
#             descuento = 0.0
# 3. Calcular el IVA:
#        iva = (subtotal - descuento) * 0.16
# 4. Calcular el total:
#        total = subtotal - descuento + iva
# 5. Mostrar con mostrarTicket el subtotal, el descuento, el IVA y el total.

# CASOS DE PRUEBA
# subtotal -> descuento, IVA, total esperados
# 500    -> $0.00,     $80.00,  $580.00    (caso normal sin descuento: IVA 500 * 0.16)
# 900    -> $0.00,     $144.00, $1,044.00  (apenas bajo el límite de 1,000: IVA 900 * 0.16)
# 1000   -> $100.00,   $144.00, $1,044.00  (límite del 10%: base 900; IVA 900 * 0.16;
#                                           si el IVA se calculara sobre 1,000 daría
#                                           IVA $160.00 y total $1,060.00)
# 4999   -> $499.90,   $719.86, $5,218.96  (apenas bajo el límite de 5,000: base 4,499.10;
#                                           IVA 719.856; total 5,218.956)
# 5000   -> $1,000.00, $640.00, $4,640.00  (límite del 20%: base 4,000; IVA 4,000 * 0.16)

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No uses try/except, round ni constantes fuera de las funciones.
# - leerSubtotal usa input con el texto "Subtotal de la compra: $" y convierte con float.
# - mostrarTicket imprime exactamente cuatro líneas, en este orden:
#       Subtotal: ${subtotal:,.2f}
#       Descuento: ${descuento:,.2f}
#       IVA (16%): ${iva:,.2f}
#       Total: ${total:,.2f}
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerSubtotal() -> float : pide el subtotal en pesos por teclado y lo devuelve
#     como float.
# calcularDescuento(subtotal) -> float : recibe el subtotal (float) y devuelve el
#     monto del descuento en pesos aplicando el paso 2 del algoritmo.
# calcularIVA(subtotal, descuento) -> float : recibe el subtotal y el descuento
#     (float) y devuelve el IVA en pesos aplicando el paso 3 del algoritmo.
# calcularTotal(subtotal, descuento, iva) -> float : recibe el subtotal, el
#     descuento y el IVA (float) y devuelve el total a pagar aplicando el paso 4.
# mostrarTicket(subtotal, descuento, iva, total) -> None : recibe los cuatro
#     valores (float) e imprime las cuatro líneas indicadas en las restricciones.
# Implementa el algoritmo anterior utilizando las funciones del contrato.
