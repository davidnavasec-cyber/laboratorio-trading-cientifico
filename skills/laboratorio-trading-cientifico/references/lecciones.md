# Lecciones generales de un laboratorio real

La tabla detallada de familias de estrategias probadas, con su resultado y su motivo, no forma parte de esta skill: está en el *Manual de resultados* (producto aparte). Aquí van solo las lecciones que se aplican a cualquier idea.

## Lecciones sobre el método
- **La volatilidad es predecible; la dirección casi nunca.** Antes de buscar un gatillo, mide cuánta información direccional hay.
- **Casi todo lo que parece ventaja es ruido, coste o selección:** un buen mes en el probador, la mejor de mil configuraciones, un ejemplo elegido a ojo. Exige el control que decide (placebo de dirección pareado y entrada al azar con las mismas salidas y la misma frecuencia).
- **Un gatillo debe superar a entrar al azar del lado de la temporalidad alta**, con las mismas salidas. Si no, la poca información está en la dirección y el gatillo solo añade costes. Ejemplo medido en forex: gatillo −0,030 R frente a +0,011 R del azar del lado en que coinciden D1 y H4 (p = 0,94, N 989).
- **Lo que el ojo ve no es una regla.** Reproduce los ejemplos elegidos a ojo con una regla evaluada dejando fuera tramos enteros antes de gastar presupuesto de búsqueda. Un momento puede ser «especial» (más volatilidad) sin tener dirección.
- **Desconfía del ganador entre varias pruebas** y de elegir, tras ver el desarrollo, el filtro o la variante que va a juicio. Compara siempre con un control del mismo tamaño y corrige por pruebas múltiples.
- **Una mejora de desarrollo suele encogerse en el juicio** (el efecto medido en la muestra de búsqueda es optimista). Planifica con la cifra encogida.
- **Sin potencia, un «no» es «no concluyente».** Calcula el número de operaciones esperado y el efecto mínimo detectable antes de medir.
- **La gestión de la operación (parciales, trailing, time-stop…) rara vez crea ventaja**: mueve la forma de la distribución, no su media. Pruébala con las mismas entradas y controles.
- **Los costes anulan las ventajas pequeñas.** Ejemplo medido: una estrategia de gatillo simple en una cartera multiactivo de H4 tuvo un bruto de +0,039 R por operación y unos costes de ≈ 0,06 R (spread, comisión y swap): neto −0,018 R con 7 756 operaciones. Con objetivos pequeños y costes altos, el bruto tiene que ser grande; antes de buscar un gatillo, resta los costes reales a la ventaja bruta posible.

## Lecciones sobre datos y costes
- Mide los **spreads, comisiones y swap reales** del bróker o la firma; en temporalidades bajas sobre índices pueden ser una fracción grande de R.
- El **volumen de un CFD no se parece al de un futuro**; no extrapoles.
- Arbitra cualquier fuente de datos contra el original en una muestra de días; los datos gratuitos pueden tener huecos, relleno o sesgo de supervivencia.

## Lecciones sobre fondeo
- El **contrato de fondeo puede tener valor esperado positivo sin ventaja de la estrategia** (pérdida acotada a la cuota, ganancia proporcional). Es valor del contrato, no de la estrategia: dilo siempre así y muestra los escenarios (ventaja medida, neta cero y ligeramente negativa).
- **Decide por simulación con las reglas reales y con la regla de inactividad delante.** Con presupuesto pequeño, varios intentos baratos pueden superar a un producto más caro; la inactividad, no la pérdida, suele matar los intentos.
- Las discrepancias entre la web y el área de cliente de la firma se anotan y se preguntan antes de operar.

## Qué hacer con una idea que falla
Registrarla (qué se probó, con qué datos, con qué resultado), cerrarla y **no reabrirla** sin una razón nueva escrita. Un laboratorio que documenta sus negativos ahorra meses.
