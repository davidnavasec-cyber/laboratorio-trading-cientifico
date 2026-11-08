# Datos (Dukascopy y otros)

## Organización recomendada
- `DATOS/crudo/` (archivos originales), `DATOS/m1/<ACTIVO>/<AÑO>.parquet` con columnas fijas, `DATOS/derivados/{H1,H4,D1}/`.
- Un **manifiesto** (ruta, activo, rango, hash) y una herramienta única de carga y descarga; una guía `LEEME_DATOS.md` que el agente lea siempre antes de buscar datos.

## Descarga desde Dukascopy
- Fuente pública: archivos `.bi5`. El servidor limita el ritmo: usar **pocas conexiones simultáneas (≈ 4)**, reintentos con espera creciente, caché atómica (`.tmp` → renombrar), reanudación y solo lo que falta. Orden de magnitud: horas por activo y década.
- Verificar al final que no quedan días con error; algunas herramientas devuelven "éxito" aunque falten días.
- No uses APIs internas no documentadas ni técnicas para saltarse límites o bloqueos: si responden 403, se respeta.
- Herramientas de terceros: pruébalas con un mes antes de confiar (algunas devuelven archivos vacíos).

## Problemas conocidos
- En índices, Dukascopy incluye **velas de relleno** (volumen 0) que algunas cachés eliminan: dos fuentes "iguales" pueden diferir por eso. Arbitra cualquier fuente contra el bi5 crudo en una muestra de días antes de usarla.
- Fuentes locales antiguas pueden tener **tramos corruptos** (meses enteros que no coinciden con el bi5): arbitra por tramos, no solo un par de días.
- El volumen del proveedor es un campo de liquidez, no un conteo de operaciones del mercado.
- Acciones: las fuentes gratuitas suelen omitir empresas deslistadas → **sesgo de supervivencia**: el resultado es solo una cota superior.
- Respeta las condiciones de uso de cada fuente (algunas prohíben la descarga automatizada sin permiso).
