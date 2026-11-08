---
name: laboratorio-trading-cientifico
description: Método científico para investigar estrategias de trading algorítmico sin engañarse - pre-registro, controles placebo, juicio único fuera de muestra, costes reales - y para convertirlas en EAs de MetaTrader y evaluar retos de fondeo (prop firms). Úsala siempre que la tarea toque estrategias de trading, backtests, réplicas en Python, EAs MQL4/MQL5, datos de Dukascopy, retos de fondeo, misiones para Claude Code o la idea de un trader que haya que validar, aunque el usuario no pida "rigor" explícitamente.
---

# Laboratorio de trading científico

El objetivo de este laboratorio es **no engañarse**. Casi todo lo que llega con aspecto de ventaja (vídeos, PDFs de traders, un buen mes en el probador, la mejor de mil configuraciones) resulta ser ruido, coste o selección. El método de abajo existe para distinguirlo. Síguelo aunque la idea parezca obviamente buena: suelen ser las que más fallan.

## Antes de empezar

1. **Lee el estado del laboratorio** si existe: un mapa de ruta, un registro de decisiones y un libro de intentos (`LIBRO_INTENTOS.csv`). Si no existen, propón crearlos con las plantillas de `assets/`.
2. **¿Ya se probó?** Busca la idea en el libro de intentos. Si ya se probó algo igual, responde con ese veredicto en lugar de repetirlo; `references/lecciones.md` recoge las lecciones generales.
3. **Datos:** antes de descargar nada, lee `references/datos.md`.
4. **MetaTrader:** si la tarea toca un terminal o una cuenta, lee primero `references/seguridad_mt5.md`.

## Reglas que no se negocian

- **Trazabilidad:** todo número de un informe sale de un script cuya salida queda guardada. Los veredictos los genera un script.
- **Pre-registro:** definiciones, parámetros, controles, criterio y potencia se fijan y se sellan (sha256) **antes** de calcular resultados. Lo que falte se declara en una adenda sellada antes de mirar.
- **Particiones:** desarrollo → (validación) → juicio. El juicio se abre **una sola vez**. Una ventana usada para decidir sobre una serie no vuelve a ser limpia para esa serie.
- **Controles:** placebo de dirección pareado y/o entrada al azar con la misma frecuencia (≥ 2,000 réplicas), p = (k+1)/(M+1), corrección por pruebas múltiples (Bonferroni o Benjamini-Hochberg). Funciones en `scripts/estadistica.py`.
- **Potencia antes de medir:** número esperado de operaciones (conteo ciego) y efecto mínimo detectable. Sin potencia, un "no" es "no concluyente".
- **Costes reales:** spread, comisión y **swap** del bróker o firma; stop duro siempre; si una vela toca stop y objetivo, cuenta como pérdida.
- **Prohibido:** ajustar mirando el juicio, añadir variantes tras ver resultados, presentar la mejor de muchas como si fuera la única, usar las estadísticas del autor de una estrategia para calibrar nada.

Detalle estadístico y trampas frecuentes: `references/metodologia.md`.

## Flujo para una idea nueva

1. **Ficha** (`assets/plantilla_ficha_idea.md`): hipótesis en una frase, mecanismo económico, datos necesarios, antecedentes.
2. **Clasificación:** (a) ya probada → veredicto existente; (b) variante menor de algo cerrado → prueba corta con puerta en desarrollo; (c) idea nueva con fundamento → cuenta contra un presupuesto de hipótesis fijado de antemano.
3. **Señalar ambigüedades** de la especificación (stops por cierre de vela, promediar a la contra, unidades en pips fijos, estados sin caducidad, filtros sin datos históricos) y proponer cómo fijarlas.
4. **Misión** con `assets/plantilla_mision.md`.
5. **Si pasa:** EA con stop duro, autoprueba, paridad con la réplica y registro adelantado (`assets/plantilla_registro.md`) antes de operar.

## Fondeo: la vara correcta

Un reto de fondeo se parece a una **opción**: la pérdida está acotada a la cuota y la ganancia no. Por eso una estrategia sin ventaja propia, pero que no pierda mucho por operación, puede tener valor esperado positivo **por el contrato**, no por la estrategia. Mídelo con simulación de Monte Carlo usando las reglas reales de la firma, y decide por **beneficio esperado a 12 y 24 meses**, no por el profit factor. Detalle y reglas típicas en `references/fondeo.md`.

## Formato de entrega

- Veredicto corto primero; luego tabla, controles, potencia, límites y "qué sigue".
- Declarar errores propios y decisiones tomadas sin consultar.
- Al cerrar una etapa, actualizar el registro de decisiones y el libro de intentos, y **detenerse** para que el operador decida.

## Referencias

- `references/metodologia.md` — métricas, diagnósticos, umbrales, trampas.
- `references/datos.md` — Dukascopy: descarga, verificación y problemas conocidos.
- `references/seguridad_mt5.md` — trabajar con MetaTrader sin poner en riesgo una cuenta.
- `references/fondeo.md` — economía de los retos y reglas que hay que verificar.
- `references/lecciones.md` — lecciones generales del laboratorio (la tabla detallada de familias probadas está en el Manual de resultados).
- `assets/` — plantillas de misión, ficha de idea y registro adelantado.
- `scripts/estadistica.py` — bootstrap por bloques, p de placebo, Benjamini-Hochberg, efecto mínimo detectable.
