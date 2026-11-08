# Resultados en una página

Resumen de los hallazgos principales de un laboratorio real de trading algorítmico. El detalle (familias probadas una a una, tablas, cifras, motivos, economía del fondeo y comparación de productos) está en el **Manual de resultados** (ver [README](README.md)).

> Material educativo. No es asesoramiento financiero ni promete rentabilidad. Resultados pasados, entre ellos los negativos, no predicen resultados futuros. Ver [AVISO_LEGAL.md](AVISO_LEGAL.md). Textos bajo CC BY-NC 4.0.

## Alcance (cifras del libro de intentos del laboratorio, 2026-10-04 a 2026-11-07)
- **198 registros** en **123 misiones** distintas.
- **≈ 964 000 configuraciones evaluadas** (suma de los registros con cifra numérica; 38 registros no tienen una cifra de intentos). Más del 98 % proviene de una única búsqueda exhaustiva de reglas (948 880), por lo que el número de *ideas distintas* es mucho menor: lo que importa no es la cantidad, sino que **cada intento está contado** para corregir por pruebas múltiples.

## Hallazgos
1. **La mayoría de las ideas no sobrevive.** Barridas de liquidez, gatillos estructurales de temporalidad baja, rupturas de rango, reversión a la media, tendencia, efectos de calendario y gestión de la operación no superaron a los controles (placebo de dirección y entrada al azar) una vez descontados los costes reales.
2. **La volatilidad es predecible; la dirección, casi nunca.** Los gatillos añadían costes sin información direccional propia: la poca información estaba en el lado de la temporalidad alta.
3. **Una mejora de desarrollo se encoge en el juicio.** En el caso estudiado, +0,10 R en desarrollo se redujo a +0,03 R fuera de muestra. Quien planifica con la cifra de desarrollo se engaña.
4. **La única señal con confirmación** fue una asimetría de impacto medida con el lado agresor real de datos de **futuros**; no se traslada a CFD, cuyo volumen no equivale al de los futuros.
5. **La gestión de la operación (parciales, trailing, time-stop) no crea ventaja:** variación ≈ 0 frente a la entrada y salida base.
6. **Los costes mandan.** Spread, comisión y swap reales pueden ser una fracción grande de R; con objetivos pequeños, el bruto no alcanza.
7. **Lo que el ojo ve no se convierte en regla.** Los ejemplos elegidos a mano dieron resultados negativos en desarrollo al formalizarlos; un momento puede ser «especial» (más volatilidad) sin dirección.
8. **El contrato de fondeo puede tener valor esperado positivo sin ventaja de la estrategia** (pérdida acotada a la cuota, ganancia proporcional). Es valor del *contrato*, no del método. Con presupuesto pequeño, varios intentos baratos pueden superar a un producto «ilimitado» más caro; la inactividad, más que la pérdida, mata los intentos.
9. **Muchos «no» son «no concluyente».** Con pocas operaciones no hay potencia: el laboratorio lo declara en lugar de convertirlo en un sí o un no.

## Qué demuestra esto (y qué no)
- Demuestra un **método** que detecta pronto y barato lo que no funciona, y que registra los negativos.
- **No** demuestra una estrategia rentable ni ofrece señales. No hay promesa de ingresos.

## Para ir más lejos
- Método reproducible: carpeta [`skills/laboratorio-trading-cientifico/`](skills/laboratorio-trading-cientifico/).
- Próximamente: un *Manual de resultados* con la tabla completa y las cifras trazables.
