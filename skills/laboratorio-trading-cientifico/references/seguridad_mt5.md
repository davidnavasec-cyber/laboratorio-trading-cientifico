# Seguridad con MetaTrader

Una cuenta de evaluación o fondeada es dinero real. Un error de configuración cuesta un reto.

- **El agente nunca activa el trading algorítmico** ni abre, cierra o modifica posiciones. Lo hace el operador tras una validación PASS.
- **Escribir configuración solo con el terminal cerrado**; con el terminal abierto, solo lectura.
- Copia de seguridad con hashes antes de cualquier cambio; **perfiles nuevos** en lugar de editar los existentes; informe final de archivos nuevos o cambiados frente a la copia.
- **Pruebas en una instalación aislada** (sin trading en vivo): probador por línea de comandos (`terminal64.exe /config:archivo.ini` con sección `[Tester]` y `ShutdownTerminal=1`), autopruebas y scripts de lectura.
- Scripts que buscan el proceso del terminal por nombre pueden tocar el terminal equivocado si hay dos abiertos: identifica la instalación por ruta.
- **Validación independiente:** un script distinto del instalador compara perfil, gráficos, entradas campo a campo, hashes de los `.ex5` y líneas de arranque del registro con lo registrado. Cualquier diferencia es FAIL.
- **Modo sombra:** para medir un EA en vivo sin riesgo, que simule operaciones con ticks reales y no pueda enviar órdenes (guardas en el código, magic propio, autoprueba que lo verifica).
- Toda versión nueva: compilación sin errores ni advertencias, autoprueba y paridad con la versión anterior (mismas señales; listar qué cambia y por qué).
- En el cálculo de stops: lado bid/ask correcto, normalización al tamaño del tick, distancias mínimas del bróker (`STOPS_LEVEL`, `FREEZE_LEVEL`), y el lote calculado con el mismo stop que se envía. Nunca abrir con más riesgo del calculado (si el lote mínimo no cabe, rechazar y registrar).
