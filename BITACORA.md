# Bitácora

Casos de prueba y registro de rechazos por ejercicio.

## Ejercicio 1. Recibo de luz

### Casos de prueba

| Caso | Entrada (kWh) | Esperado (a mano) | Obtenido | Coincide |
|------|---------------|-------------------|----------|----------|
| 1 | 0 | $0.00 | $0.00 | Sí |
| 2 | 100 | $100.00 | $100.00 | Sí |
| 3 | 150 | $150.00 | $150.00 | Sí |
| 4 | 151 | $151.50 | $151.50 | Sí |
| 5 | 200 | $225.00 | $225.00 | Sí |
| 6 | 280 | $345.00 | $345.00 | Sí |
| 7 | 281 | $348.00 | $348.00 | Sí |
| 8 | 300 | $405.00 | $405.00 | Sí |

### Rechazos

Sin rechazos. Nota: el código de este ejercicio no lo propuso Copilot (el entorno
donde se armó el proyecto no lo tiene); se implementó directamente desde la
especificación. Verificación contra el contrato:

- `leerConsumo()`: sin parámetros, devuelve `int`, texto de `input` igual al de las restricciones.
- `calcularPago(consumo)`: tres ramas con `<= 150` y `<= 280`, fórmulas idénticas a los pasos 2 a 4.
- `mostrarRecibo(consumo, pago)`: imprime exactamente las dos líneas indicadas, sin retorno.
- Sin clases, `import`, `try/except`, validaciones ni llamadas a funciones en el archivo.

## Ejercicio 2. Calificación final

### Casos de prueba

| Caso | Entrada (p1, p2, p3) | Esperado (a mano) | Obtenido | Coincide |
|------|----------------------|-------------------|----------|----------|
| 1 | 80, 70, 90 | 81.00, Aprobado | 81.00, Aprobado | Sí |
| 2 | 70, 70, 70 | 70.00, Aprobado | 70.00, Aprobado | Sí |
| 3 | 69, 70, 70 | 69.70, Reprobado | 69.70, Reprobado | Sí |
| 4 | 100, 100, 40 | 76.00, Reprobado | 76.00, Reprobado | Sí |
| 5 | 50, 100, 100 | 85.00, Aprobado | 85.00, Aprobado | Sí |
| 6 | 49, 100, 100 | 84.70, Reprobado | 84.70, Reprobado | Sí |
| 7 | 100, 100, 100 | 100.00, Aprobado | 100.00, Aprobado | Sí |

### Rechazos

Sin rechazos. Nota: el código de este ejercicio no lo propuso Copilot (el entorno
donde se armó el proyecto no lo tiene); se implementó directamente desde la
especificación. Verificación contra el contrato:

- `leerParciales()`: sin parámetros, textos de `input` y orden iguales a las restricciones, devuelve la tupla `(p1, p2, p3)` con `float`.
- `calcularFinal(p1, p2, p3)`: fórmula idéntica al paso 2, sin redondear.
- `determinarEstado(p1, p2, p3, final)`: condiciones `< 50` y `>= 70` en el orden de los pasos 3.1 a 3.3, sin `min`, `max` ni `round`.
- `mostrarResultado(final, estado)`: imprime exactamente las dos líneas indicadas, sin retorno.
- Sin clases, `import`, `try/except`, validaciones ni llamadas a funciones en el archivo.

## Ejercicio 3. Total de compra

(pendiente)

## Ejercicio 4 (reto). Estacionamiento

(pendiente)
