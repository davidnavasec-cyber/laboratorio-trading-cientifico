# REGISTRO ADELANTADO — <nombre>_<AAAAMMDD>

**Se sella (sha256 de cada archivo + manifiesto) antes de la primera operación. Nada de esta carpeta se edita después; los cambios van en anotaciones nuevas.**

- **Qué se registra:** EA, versión y sha256 del `.ex5`; `.set` exactos con sha256; cuenta/firma/producto.
- **Hipótesis y origen:** (incluida la evidencia previa y si se eligió tras mirar resultados).
- **Inicio:** fecha y hora de servidor de la activación (en `ANOTACION_INICIO.md`). Solo cuentan operaciones posteriores.
- **Criterio de juicio:** p. ej. ≥ N operaciones nuevas, E[R] neto > 0 con IC 95% por semanas que excluya el cero.
- **Potencia:** efecto mínimo detectable y tiempo esperado hasta N.
- **Condiciones de parada:** (p. ej. infracciones, costes reales > 1.5× el modelo, avisos de la firma).
- **Cambios permitidos sin registro nuevo:** solo correcciones con impacto medido en R inferior a un umbral fijado aquí.
