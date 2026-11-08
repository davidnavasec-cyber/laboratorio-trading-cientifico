# Laboratorio de trading científico · Scientific Trading Lab

**ES** · [English below](#english)

> ⚠️ **Material educativo. No es asesoramiento financiero** ni promete rentabilidad. Operar con apalancamiento puede hacerte perder todo el capital. Lee el [aviso legal](AVISO_LEGAL.md).

## Qué es
Un laboratorio personal de investigación de trading algorítmico cuyo objetivo es **no engañarse**: casi todo lo que parece ventaja (un buen mes en el probador, la mejor de mil configuraciones, un ejemplo elegido a ojo) resulta ser ruido, coste o selección. Este repositorio publica el **método** y la **skill** para Claude que lo aplica.

### Tres hallazgos destacados
1. **El reto de fondeo se comporta como una opción.** La pérdida está acotada a la cuota y la ganancia no: en nuestras simulaciones el valor esperado por cuota seguía siendo positivo hasta una ventaja neta por operación de ≈ −0,05 R. Ese valor es **del contrato, no de la estrategia**.
2. **Los gatillos de temporalidad baja no superan a entrar al azar** con las mismas salidas, en forex, oro e índices (desarrollo, costes reales). Forex: un gatillo M15 con contexto D1+H4 dio −0,030 R neto (N 989) frente a +0,011 R de entrar al azar del lado en que coinciden D1 y H4 (p = 0,94). Oro: un gatillo H1 dio −0,017 R frente a +0,011 R del azar del mismo lado (percentil 95 del azar +0,089; placebo de dirección p = 0,33). Índices: un gatillo de inversión de FVG dio −0,185 R (N 56; placebo de dirección p = 0,51; azar en la ventana p = 0,98). La poca información está en la dirección; el gatillo solo añade costes.
3. **Los costes y el swap anulan las ventajas pequeñas.** Una estrategia de gatillo simple aplicada a una cartera multiactivo en H4 (N 7 756) tenía un bruto de +0,039 R por operación y unos costes de ≈ 0,06 R: neto −0,018 R. Del mismo modo, una tendencia diversificada con Sharpe +0,23 bruto pasó a **−0,41 neto** (la tendencia aportaba +0,91 %/año y el swap restaba −2,75 %/año). Y una mejora de +0,10 R en desarrollo se encogió a +0,03 R en el juicio.

## Qué demuestra
- Pre-registro sellado (sha256) antes de calcular resultados, y libro de intentos para corregir por pruebas múltiples.
- Controles placebo (dirección pareada y entrada al azar), juicio único fuera de muestra, costes reales (spread, comisión, swap).
- Economía del fondeo (prop firms) modelada con Monte Carlo con las reglas reales.
- Cómo llevar lo que sobrevive a un EA de MetaTrader con módulo de riesgo, modo sombra, validador independiente y automatización.
- ≈ 964 000 configuraciones en 123 misiones (la mayor parte, en una búsqueda exhaustiva de reglas): casi todo falló, y eso está documentado ([resumen](RESULTADOS_RESUMEN.md)).

## Qué hay aquí
| Archivo | Contenido |
|---|---|
| [`skills/laboratorio-trading-cientifico/`](skills/laboratorio-trading-cientifico/) | Skill para Claude (Claude Code, Claude.ai o API): método, referencias, plantillas y `estadistica.py` (bootstrap por bloques, p de placebo, Benjamini-Hochberg, efecto mínimo detectable; solo numpy). |
| [`ARQUITECTURA.md`](ARQUITECTURA.md) | Cómo está montado el laboratorio (datos, réplicas, motor de fondeo, validadores, automatización), sin código privado. |
| [`RESULTADOS_RESUMEN.md`](RESULTADOS_RESUMEN.md) | Hallazgos principales en una página. |
| [`herramientas/escaner_secretos.py`](herramientas/escaner_secretos.py) | Escáner de secretos usado antes de cada commit. |

## Cómo usar la skill
- **Descarga lista:** archivo `.skill` en la [release v1.0.1](https://github.com/davidnavasec-cyber/laboratorio-trading-cientifico/releases/tag/v1.0.1).
- **Claude Code:** copia `skills/laboratorio-trading-cientifico/` en `~/.claude/skills/` (o en `.claude/skills/` de tu proyecto).
- **Claude.ai:** sube el `.skill` de la release en la configuración de skills (si tu plan lo permite).
- Pide, por ejemplo: «Valida esta idea de trading con el método del laboratorio» y la skill propondrá ficha, pre-registro, controles y potencia.

## Próximamente
Este repositorio es gratuito y completo en sí mismo. Más adelante habrá productos opcionales con licencia personal, sin datos de mercado ni estrategias: un manual de resultados, una herramienta de datos y plantillas educativas de EAs.

## Sobre el autor
**David Antonio Navas** — estudiante de Tecnología en IA. [ENLACE_LINKEDIN]

## Licencias
- Código: **MIT** ([`LICENSE`](LICENSE)).
- Textos: **CC BY-NC 4.0** ([`LICENSE-TEXTOS.md`](LICENSE-TEXTOS.md)).
- Los futuros productos de pago llevarán su propia licencia personal.

## Aviso
Este repositorio es material educativo y técnico, **no asesoramiento financiero, de inversión ni de trading**. Sin garantía de ningún tipo. No hay relación con ninguna firma de fondeo, bróker o proveedor de datos. Más en [`AVISO_LEGAL.md`](AVISO_LEGAL.md).

---

<a id="english"></a>
# Scientific Trading Lab

> ⚠️ **Educational material. Not financial advice** and no promise of profitability. Leveraged trading can lose you all your capital. See the [legal notice](AVISO_LEGAL.md).

## What it is
A personal research lab for algorithmic trading built around one aim: **not fooling yourself**. Nearly everything that looks like an edge (a good month in the strategy tester, the best of a thousand configurations, an eyeballed example) turns out to be noise, cost or selection. This repository publishes the **method** and the **Claude skill** that applies it. (Documents are in Spanish; this section summarises them.)

### Three headline findings
1. **A prop-firm challenge behaves like an option.** Loss is capped at the fee while upside is not: in our simulations expected value per fee stayed positive down to a net edge per trade of ≈ −0.05 R. That value belongs to **the contract, not the strategy**.
2. **Low-timeframe triggers do not beat random entry** with the same exits, in forex, gold and indices (development sample, real costs). Forex: an M15 trigger with D1+H4 context returned −0.030 R net (N 989) versus +0.011 R for random entry on the side where D1 and H4 agree (p = 0.94). Gold: an H1 trigger returned −0.017 R versus +0.011 R for random same-side entry (95th percentile of random +0.089; direction-placebo p = 0.33). Indices: an inverse-FVG trigger returned −0.185 R (N 56; direction-placebo p = 0.51; random-in-window p = 0.98). The little information there is lies in direction; the trigger only adds costs.
3. **Costs and swap wipe out small edges.** A simple-trigger strategy applied to a multi-asset H4 portfolio (N 7,756) had a gross edge of +0.039 R per trade against costs of ≈ 0.06 R: net −0.018 R. Likewise a diversified trend strategy with a gross Sharpe of +0.23 turned into **−0.41 net** (trend earned +0.91%/yr while swap cost −2.75%/yr). And a +0.10 R improvement in development shrank to +0.03 R in the final trial.

## What it demonstrates
- Sealed pre-registration (sha256) before computing results, and an attempts ledger to correct for multiple testing.
- Placebo controls (paired direction and random entry), a single out-of-sample trial, real costs (spread, commission, swap).
- Prop-firm economics modelled with Monte Carlo using the real rules.
- How to take what survives to a MetaTrader EA with a risk module, shadow mode, an independent validator and automation.
- ≈ 964,000 configurations across 123 missions (most of them in one exhaustive rule search): nearly all failed, and that is documented ([summary](RESULTADOS_RESUMEN.md), Spanish).

## What is here
| File | Contents |
|---|---|
| [`skills/laboratorio-trading-cientifico/`](skills/laboratorio-trading-cientifico/) | Claude skill (Claude Code, Claude.ai or API): method, references, templates and `estadistica.py` (block bootstrap, placebo p-value, Benjamini-Hochberg, minimum detectable effect; numpy only). |
| [`ARQUITECTURA.md`](ARQUITECTURA.md) | How the lab is built (data, replicas, prop-firm engine, validators, automation), no private code. |
| [`RESULTADOS_RESUMEN.md`](RESULTADOS_RESUMEN.md) | Main findings on one page. |
| [`herramientas/escaner_secretos.py`](herramientas/escaner_secretos.py) | Secret scanner run before every commit. |

## Using the skill
- **Ready-made download:** `.skill` file in [release v1.0.1](https://github.com/davidnavasec-cyber/laboratorio-trading-cientifico/releases/tag/v1.0.1).
- **Claude Code:** copy `skills/laboratorio-trading-cientifico/` into `~/.claude/skills/` (or your project's `.claude/skills/`).
- **Claude.ai:** upload the release `.skill` in skill settings (if your plan allows).
- Ask, e.g., "Validate this trading idea with the lab method" and the skill will propose an idea sheet, pre-registration, controls and power.

## Coming soon
This repository is free and complete on its own. Optional products under a personal licence, with no market data or strategies, will follow: a results manual, a data tool and educational EA templates.

## About the author
**David Antonio Navas** — AI Technology student. [ENLACE_LINKEDIN]

## Licences
- Code: **MIT** ([`LICENSE`](LICENSE)). Texts: **CC BY-NC 4.0** ([`LICENSE-TEXTOS.md`](LICENSE-TEXTOS.md)). Future paid products will carry their own personal licence.

## Notice
Educational and technical material, **not financial, investment or trading advice**. No warranty of any kind. No affiliation with any prop firm, broker or data vendor. See [`AVISO_LEGAL.md`](AVISO_LEGAL.md).
