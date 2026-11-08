# Arquitectura del laboratorio

Cómo está montado un laboratorio de investigación de trading algorítmico **diseñado para no engañarse**. Describe piezas y flujos; no incluye código privado, datos, ni estrategias. Las piezas con código reutilizable llegarán como productos aparte (ver «Próximamente» en el [README](README.md)).

> Material educativo. No es asesoramiento financiero. Ver [AVISO_LEGAL.md](AVISO_LEGAL.md). Textos bajo CC BY-NC 4.0 (ver [LICENSE-TEXTOS.md](LICENSE-TEXTOS.md)).

## Vista general

```
 idea ─► ficha ─► pre-registro sellado (sha256) ─► réplica en Python ─► controles ─► veredicto
                                                          │                              │
                                       DATOS (una sola raíz)                 libro de intentos + registro de decisiones
                                                          │
                       pasa la puerta ─► EA con stop duro ─► autoprueba + paridad ─► registro adelantado ─► validador ─► operador
                                                                                                                 │
                                                                     modo sombra / informes diario y semanal ◄───┘
```

## 1. Datos
- **Una sola raíz canónica**: `crudo/` (originales), `m1/<ACTIVO>/<AÑO>.parquet` con columnas fijas y `derivados/{H1,H4,D1}/`, más un **manifiesto** (ruta, activo, rango, hash).
- **Una herramienta única** para cargar y descargar, y una guía de **problemas conocidos** (velas de relleno, tramos corruptos, sesgo de supervivencia, volumen que no es conteo de operaciones).
- Regla: antes de descargar, se consulta la guía; no se descarga lo que ya existe; los datos de terceros no se redistribuyen.

## 2. Réplicas y motor de pruebas
- Cada idea se implementa como una **réplica en Python** de la regla, con las mismas entradas/salidas que tendrá el EA.
- **Costes reales** (spread, comisión, swap), stop duro, y la regla pesimista: si una vela toca stop y objetivo, es pérdida.
- **Controles**: placebo de dirección pareado y entrada al azar con la misma frecuencia (≥ 2 000 réplicas), p = (k+1)/(M+1), corrección por pruebas múltiples, bootstrap por bloques y efecto mínimo detectable (ver `skills/.../scripts/estadistica.py`).
- **Particiones**: desarrollo → validación → juicio. El juicio se abre **una vez** y solo si se pasó la puerta de desarrollo.

## 3. Pre-registro y trazabilidad
- Definiciones, espacio de búsqueda, controles, criterio y potencia se fijan en un documento y se **sellan con sha256 antes de calcular resultados**. Lo que falta se declara en una adenda sellada antes de mirar.
- Todo número de un informe sale de un script cuya salida queda en archivo; los veredictos los genera un script.
- **Libro de intentos** (cuántas configuraciones se probaron de verdad) y **registro de decisiones**: son la defensa contra la selección del mejor resultado.

## 4. Motor de economía del fondeo
- El reto de fondeo se modela como una **opción** (pérdida acotada a la cuota, ganancia proporcional).
- Simulación de Monte Carlo con las **reglas reales** de cada producto (objetivo, pérdida diaria y total, días mínimos, inactividad, consistencia, retiros) y recompra de retos.
- Decisión por **beneficio esperado a 12 y 24 meses**, probabilidad de pérdida y percentiles, mostrando siempre los escenarios (ventaja medida, neta cero, ligeramente negativa).
- El valor esperado del contrato **no es ventaja de la estrategia**; se dice en cada tabla.

## 5. EAs, módulo de riesgo y modo sombra
- Un EA solo se escribe si la idea pasó la puerta. Debe **compilar 0 errores/0 advertencias**, tener **autoprueba** y **paridad** con la réplica (mismas señales).
- **Módulo de riesgo de fondeo**: lee toda la cuenta antes de abrir (pérdida del día + riesgo abierto + nuevo ≤ fracción del límite) y rechaza en vez de abrir con más riesgo del calculado.
- **Modo sombra**: mide una estrategia en vivo sin riesgo (simula con ticks reales; no puede enviar órdenes; guardas en el código, *magic* propio, autoprueba que lo verifica).

## 6. Validadores y seguridad con MetaTrader
- Un **instalador** y un **validador independiente** (solo lectura) comparan perfil, gráficos, entradas, hashes de los `.ex5` y líneas de arranque con el registro; cualquier diferencia es FAIL.
- Reglas operativas: el agente nunca activa el trading ni abre/cierra posiciones; escribir en el terminal solo con él cerrado; copias con hashes antes de cambiar; pruebas en una instalación aislada sin trading en vivo (ver `skills/.../references/seguridad_mt5.md`).

## 7. Automatización
- **Servicio exportador** (solo lectura) que escribe periódicamente el estado de la cuenta a archivos.
- **Informe diario y revisión semanal** programados (`launchd`/`cron`) que leen esa exportación y envían un resumen por **Telegram**; si faltan datos recientes, avisan en vez de informar con datos viejos.
- Credenciales **solo en variables de entorno o un `.env` fuera del control de versiones**, con un **escáner de secretos antes de cada commit**.

## 8. Gobierno del repositorio
- Dos repositorios: uno **privado** con el laboratorio completo, y uno **público** (este) con la metodología y la skill. Lo que sea de terceros (datos, métodos ajenos) o de la cuenta nunca sale del privado.
- Escáner de secretos y comprobador de privacidad obligatorios antes de cada subida.
