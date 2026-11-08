# Metodología estadística

## Unidad de medida
- Todo en **R** (múltiplos del riesgo inicial). E[R] neto = tras spread, comisión, swap y deslizamiento modelado.
- Intervalos de confianza por **bootstrap por bloques** (días o semanas), nunca remuestreando operaciones sueltas: las operaciones de un mismo día o semana no son independientes.

## Controles
| Control | Pregunta que responde |
|---|---|
| Placebo de dirección pareado (mismas distancias y costes, dirección invertida) | ¿La dirección aporta algo? |
| Entrada al azar (misma frecuencia por día, mismas salidas) | ¿El gatillo aporta frente a estar en el mercado? |
| Entrada al azar del mismo lado de la tendencia | ¿El gatillo aporta frente a la deriva del activo? |
| Filtro al azar que retiene la misma fracción | ¿Un filtro mejora más que quitar operaciones al azar? |
| Versión simple del mismo efecto | ¿La complejidad aporta sobre la versión académica? |

p = (k+1)/(M+1), con M ≥ 2,000. Bonferroni si hay pocas variantes; Benjamini-Hochberg con q fijado antes si hay una matriz grande de pruebas.

## Diagnósticos estándar
- **PF robusto:** PF sin la mejor operación. Si cae por debajo de 1, el resultado dependía de una operación.
- **Estabilidad en 10 bloques** cronológicos.
- **Autocorrelación:** P(gana | perdió la anterior) frente a P(gana). Solo descriptivo; nunca justifica subir el riesgo tras rachas.
- Distribución de R (pérdidas > 1R por huecos), peor racha, drawdown en R, duración, resultado por año.

## Potencia
Declara N esperado (conteo ciego de señales) y el efecto mínimo detectable al 80% antes de calcular R. Con ventajas pequeñas (< 0.1R) y pocas operaciones al año, lo esperable es "no concluyente".

## Trampas frecuentes
- **Un positivo pequeño en desarrollo sin significancia casi nunca sobrevive** al juicio.
- **La mejor de muchas configuraciones** (optimización, walk-forward, miles de variantes) rinde cerca de cero fuera de muestra.
- **Ajustar umbrales "hasta el máximo"**, invertir la estrategia en el régimen donde pierde, Kelly sin ventaja demostrada, subir el riesgo tras rachas de pérdidas: sobreajuste o falacia del jugador.
- **Stop "al cierre de vela" sin stop duro:** acierta más pero deja pérdidas de muchos R.
- **Breakeven o gestión intrabarra:** el resultado depende del orden de los ticks; evalúa al cierre de vela.
- **Órdenes límite:** sufren selección adversa (se llenan sobre todo cuando el precio sigue en contra).
- **El volumen de un CFD no es el volumen del mercado.**
- **La gestión no crea ventaja:** si tras la entrada el precio no tiene estructura, parciales, time-stops y trailing solo redistribuyen el mismo E[R]. Mide primero si hay estructura (p. ej. P(gana | no alcanzó +0.6R en n velas)).
- **Las ventajas brutas pequeñas desaparecen con los costes y el swap de los CFD.** Ejemplo medido: bruto +0,039 R por operación frente a costes ≈ 0,06 R (spread, comisión y swap) → neto −0,018 R con 7 756 operaciones; resta siempre los costes reales antes de celebrar un bruto positivo.
- **Métricas de resultado calculadas en la ventana de juicio** la contaminan: diagnostica solo en desarrollo.
