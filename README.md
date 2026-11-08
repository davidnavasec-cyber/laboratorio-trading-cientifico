# Laboratorio de trading científico · Scientific Trading Lab

**ES** · [English below](#english)

> ⚠️ **Material educativo. No es asesoramiento financiero** ni promete rentabilidad. Operar con apalancamiento puede hacerte perder todo el capital. Lee el [aviso legal](AVISO_LEGAL.md).

## Qué es
Un laboratorio personal de investigación de trading algorítmico cuyo objetivo es **no engañarse**: casi todo lo que parece ventaja (un buen mes en el probador, la mejor de mil configuraciones, un ejemplo elegido a ojo) resulta ser ruido, coste o selección. Este repositorio publica el **método** y la **skill** para Claude que lo aplica.

## Qué demuestra
- Pre-registro sellado (sha256) antes de calcular resultados, y libro de intentos para corregir por pruebas múltiples.
- Controles placebo (dirección pareada y entrada al azar), juicio único fuera de muestra, costes reales (spread, comisión, swap).
- Economía del fondeo (prop firms) modelada con Monte Carlo con las reglas reales.
- Cómo llevar lo que sobrevive a un EA de MetaTrader con módulo de riesgo, modo sombra, validador independiente y automatización.
- ≈ 964 000 configuraciones contadas en 123 misiones: casi todo falló, y eso está documentado ([resumen](RESULTADOS_RESUMEN.md)).

## Qué hay aquí
| Archivo | Contenido |
|---|---|
| [`skills/laboratorio-trading-cientifico/`](skills/laboratorio-trading-cientifico/) | Skill para Claude (Claude Code, Claude.ai o API): método, referencias, plantillas y `estadistica.py` (bootstrap por bloques, p de placebo, Benjamini-Hochberg, efecto mínimo detectable; solo numpy). |
| [`ARQUITECTURA.md`](ARQUITECTURA.md) | Cómo está montado el laboratorio (datos, réplicas, motor de fondeo, validadores, automatización), sin código privado. |
| [`RESULTADOS_RESUMEN.md`](RESULTADOS_RESUMEN.md) | Hallazgos principales en una página. |
| [`herramientas/escaner_secretos.py`](herramientas/escaner_secretos.py) | Escáner de secretos usado antes de cada commit. |

## Cómo usar la skill
- **Claude Code:** copia `skills/laboratorio-trading-cientifico/` en `~/.claude/skills/` (o en `.claude/skills/` de tu proyecto).
- **Claude.ai:** empaqueta la carpeta como `.skill` y súbela en la configuración de skills (si tu plan lo permite).
- Pide, por ejemplo: «Valida esta idea de trading con el método del laboratorio» y la skill propondrá ficha, pre-registro, controles y potencia.

## Productos de pago (opcionales)
Este repositorio es gratuito y completo en sí mismo. Además, hay tres productos con licencia personal (sin redistribución) y sin datos de mercado:
- 📘 **Manual de resultados** — método, familias probadas con cifras trazables, economía y comparación de productos de fondeo: [ENLACE_TIENDA_MANUAL]
- 🛠 **Herramienta de datos** — cargador/descargador portable con manifiesto y guía de problemas conocidos: [ENLACE_TIENDA_HERRAMIENTA_DATOS]
- 🧩 **Plantillas educativas de EAs** — módulo de riesgo de fondeo, modo sombra, validador, exportador, informes y un EA de ejemplo **sin ventaja**: [ENLACE_TIENDA_PLANTILLAS]
- 🎁 **Paquete de los tres:** [ENLACE_TIENDA_PAQUETE]

Ninguno incluye estrategias rentables, señales ni datos de terceros.

## Licencias
- Código: **MIT** ([`LICENSE`](LICENSE)).
- Textos: **CC BY-NC 4.0** ([`LICENSE-TEXTOS.md`](LICENSE-TEXTOS.md)).
- Los productos de pago llevan su propia licencia personal.

## Aviso
Este repositorio es material educativo y técnico, **no asesoramiento financiero, de inversión ni de trading**. Sin garantía de ningún tipo. No hay relación con ninguna firma de fondeo, bróker o proveedor de datos. Más en [`AVISO_LEGAL.md`](AVISO_LEGAL.md).

---

<a id="english"></a>
# Scientific Trading Lab

> ⚠️ **Educational material. Not financial advice** and no promise of profitability. Leveraged trading can lose you all your capital. See the [legal notice](AVISO_LEGAL.md).

## What it is
A personal research lab for algorithmic trading built around one aim: **not fooling yourself**. Nearly everything that looks like an edge (a good month in the strategy tester, the best of a thousand configurations, an eyeballed example) turns out to be noise, cost or selection. This repository publishes the **method** and the **Claude skill** that applies it. (Documents are in Spanish; this section summarises them.)

## What it demonstrates
- Sealed pre-registration (sha256) before computing results, and an attempts ledger to correct for multiple testing.
- Placebo controls (paired direction and random entry), a single out-of-sample trial, real costs (spread, commission, swap).
- Prop-firm economics modelled with Monte Carlo using the real rules.
- How to take what survives to a MetaTrader EA with a risk module, shadow mode, an independent validator and automation.
- ≈ 964,000 configurations counted across 123 missions: nearly all failed, and that is documented ([summary](RESULTADOS_RESUMEN.md), Spanish).

## What is here
| File | Contents |
|---|---|
| [`skills/laboratorio-trading-cientifico/`](skills/laboratorio-trading-cientifico/) | Claude skill (Claude Code, Claude.ai or API): method, references, templates and `estadistica.py` (block bootstrap, placebo p-value, Benjamini-Hochberg, minimum detectable effect; numpy only). |
| [`ARQUITECTURA.md`](ARQUITECTURA.md) | How the lab is built (data, replicas, prop-firm engine, validators, automation), no private code. |
| [`RESULTADOS_RESUMEN.md`](RESULTADOS_RESUMEN.md) | Main findings on one page. |
| [`herramientas/escaner_secretos.py`](herramientas/escaner_secretos.py) | Secret scanner run before every commit. |

## Using the skill
- **Claude Code:** copy `skills/laboratorio-trading-cientifico/` into `~/.claude/skills/` (or your project's `.claude/skills/`).
- **Claude.ai:** package the folder as a `.skill` and upload it in skill settings (if your plan allows).
- Ask, e.g., "Validate this trading idea with the lab method" and the skill will propose an idea sheet, pre-registration, controls and power.

## Paid products (optional)
This repository is free and complete on its own. There are also three products under a personal licence (no redistribution) with no market data:
- 📘 **Results manual** — method, tested families with traceable figures, prop-firm economics and product comparison (Spanish): [STORE_LINK_MANUAL]
- 🛠 **Data tool** — portable loader/downloader with manifest and known-issues guide: [STORE_LINK_DATA_TOOL]
- 🧩 **Educational EA templates** — prop-firm risk module, shadow mode, validator, exporter, reports and an example EA **with no edge**: [STORE_LINK_TEMPLATES]
- 🎁 **Bundle of all three:** [STORE_LINK_BUNDLE]

None includes profitable strategies, signals or third-party data.

## Licences
- Code: **MIT** ([`LICENSE`](LICENSE)). Texts: **CC BY-NC 4.0** ([`LICENSE-TEXTOS.md`](LICENSE-TEXTOS.md)). Paid products carry their own personal licence.

## Notice
Educational and technical material, **not financial, investment or trading advice**. No warranty of any kind. No affiliation with any prop firm, broker or data vendor. See [`AVISO_LEGAL.md`](AVISO_LEGAL.md).
