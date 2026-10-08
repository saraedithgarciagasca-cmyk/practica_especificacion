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

(pendiente)

## Ejercicio 3. Total de compra

(pendiente)

## Ejercicio 4 (reto). Estacionamiento

(pendiente)
