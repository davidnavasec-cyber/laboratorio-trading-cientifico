# Fondeo (prop firms)

## La economía
- El reto se comporta como una **opción**: pérdida acotada a la cuota (a menudo reembolsable con el primer retiro), ganancia proporcional al tamaño de la cuenta.
- Consecuencia: el valor esperado por cuota puede ser positivo con una ventaja neta por operación ligeramente negativa (en nuestras simulaciones, el umbral rondaba −0.05R a −0.1R). Ese valor es del contrato; dilo siempre así.
- Con ventaja cero, la probabilidad de alcanzar el objetivo antes que el límite depende de las distancias (≈ límite / (objetivo + límite) por fase), no del riesgo por operación; el riesgo cambia sobre todo la **velocidad**.
- Decide por **beneficio esperado a 12 y 24 meses** (con recompra de retos), probabilidad de pérdida y percentiles, simulando con Monte Carlo las reglas reales.
- La **inactividad** y la frecuencia mandan: muchas cuentas se pierden por tiempo, no por pérdidas.

## Reglas que hay que verificar (cambian por firma y producto)
Objetivo por fase, pérdida diaria (base y hora de reinicio), pérdida total (estática o móvil), días mínimos y rentables, inactividad, consistencia, riesgo máximo por "idea" u operación, copia de operaciones entre cuentas, cuentas simultáneas, uso de EAs, noticias, mantener de noche y fin de semana, retiros y reembolso. Cita la fuente oficial con fecha; pregunta a soporte lo que no esté escrito.

## Prácticas que funcionaron
- Un módulo de riesgo que lea **toda la cuenta** (todos los EAs) antes de abrir: pérdida del día + riesgo abierto + nuevo ≤ una fracción del límite diario.
- Tratar activos muy correlacionados como una sola idea para los topes por idea.
- Política "riesgo normal o no operar": reducir el lote progresivamente cerca del límite puede parecer "riesgo casi nulo" a la firma.
- Escalar solo tras comprobar en la realidad lo que el modelo supone (pagos cobrados, cero infracciones, costes reales cercanos al modelo).

## Prácticas que no
- Subir el riesgo tras rachas de pérdidas, "aceleradores de varianza", Kelly sin ventaja, operaciones diminutas para cumplir días o evitar la inactividad.
