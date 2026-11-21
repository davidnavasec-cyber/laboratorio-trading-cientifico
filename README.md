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

## Comprar
Todos los productos son material educativo y técnico, con licencia personal y sin datos de mercado. **Pago en USDT o USDC, mismo precio** (otras vías en dólares por correo). Entrega por correo con el archivo adjunto.

| Producto | Qué es | Precio (USDT / USDC) |
|---|---|---:|
| 📘 **Manual de resultados** (PDF, español) | Método y economía del fondeo; cada cifra verificada | **25** |
| 🛠 **Herramienta de datos** (Python) | Cargar, verificar y convertir velas M1 → H1/H4/D1; sin datos | **39** |
| 🧩 **Plantillas educativas de EAs** (MQL5) | Módulo de riesgo de fondeo, modo sombra y autopruebas; ejemplo sin ventaja | **49** |
| 🎁 **Paquete completo** | Los tres · ahorras 28 | **85** |

**Contacto:** danc.ventas@gmail.com

### Cómo pagar
**Pago en USDT o USDC.** No se publica ninguna dirección: te la enviamos por correo en cada pedido.
1) Escribe a danc.ventas@gmail.com con el **producto** que quieres. 2) Te respondemos con el **precio**, el **token** (USDT o USDC), la **red** y la **dirección de pago** de ese pedido. 3) Pagas y nos envías el **hash** de la transacción. 4) Comprobamos que llegó el **importe completo** y te enviamos el archivo y la licencia por correo.

### Redes recomendadas
| Token | Recomendadas | También se acepta | Nunca |
|---|---|---|---|
| **USDT** | Polygon · BNB Chain (BEP-20) | Ethereum (ERC-20): el gas, más caro, lo paga el cliente | Tron (TRC-20) |
| **USDC** | Polygon · BNB Chain (BEP-20) | Ethereum (ERC-20): el gas, más caro, lo paga el cliente | Tron (TRC-20) |

Polygon y BNB Chain son baratas y rápidas. **La red exacta y la dirección se confirman siempre por correo antes de pagar.**

> **Antes de pagar**
> 1. Aceptamos **solo USDT o USDC**, en la red que te indiquemos por correo. **No envíes por Tron (TRC-20)**. Otro token u otra red puede perder los fondos de forma **irrecuperable**.
> 2. Usa **únicamente la dirección que te enviamos por correo para tu pedido**; ninguna otra página ni mensaje la publica. Compárala carácter a carácter.
> 3. Las comisiones de red (y las de tu exchange) corren por tu cuenta: debe llegar el **precio completo**.
> 4. Los pagos en blockchain son **irreversibles**.

**Otras vías, solo por correo y bajo pedido:** transferencia entre usuarios de Takenos, o ACH desde una cuenta bancaria de EE. UU. Pídelas en tu primer correo; no se aceptan Wire, SWIFT ni tarjeta.

### Condiciones comunes
- Entrega por **correo con el archivo adjunto**, normalmente en 24 horas hábiles tras comprobar que llegó el pago completo (plazo orientativo).
- **Sin reembolso una vez descargado, salvo archivo dañado o no conforme a la descripción:** lo sustituimos o devolvemos el importe (en el mismo token, menos comisiones de red).
- Las correcciones de errores de la versión 1.x son gratuitas para quien ya compró.
- Pagos incompletos, de más o por una red equivocada: te contactaremos; no se entrega hasta cubrir el importe.
- Licencia personal (una por persona; para empresas o equipos, escribe al correo). Sin redistribución.
- Material educativo y técnico; **no es asesoramiento financiero**, no promete rentabilidad y no incluye estrategias ni señales. Operar conlleva riesgo de pérdida total.

**Probado en** macOS con Python 3.9 y 3.14 (herramienta y plantillas); Linux y Windows no probados aún.

## Sobre el autor
**David Antonio Navas** — estudiante de Tecnología en IA. Contacto: danc.ventas@gmail.com

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

## Buy
All products are educational and technical material under a personal licence, with no market data. **Pay in USDT or USDC, same price** (other dollar options by email). Delivery by email with the file attached.

| Product | What it is | Price (USDT / USDC) |
|---|---|---:|
| 📘 **Results Manual** (PDF, in Spanish) | Method and prop-firm economics; every figure verified | **25** |
| 🛠 **Data Tool** (Python) | Load, verify and convert M1 candles → H1/H4/D1; no data included | **39** |
| 🧩 **Educational EA Templates** (MQL5) | Prop-firm risk module, shadow mode and self-tests; no-edge example | **49** |
| 🎁 **Complete Bundle** | All three · you save 28 | **85** |

**Contact:** danc.ventas@gmail.com

### How to pay
**Pay in USDT or USDC.** No payment address is published: we email it to you for each order.
1) Email danc.ventas@gmail.com with the **product** you want. 2) We reply with the **price**, the **token** (USDT or USDC), the **network** and the **payment address** for that order. 3) You pay and send us the transaction **hash**. 4) We check that the **full amount** arrived and email you the file and the licence.

### Recommended networks
| Token | Recommended | Also accepted | Never |
|---|---|---|---|
| **USDT** | Polygon · BNB Chain (BEP-20) | Ethereum (ERC-20): the higher gas fee is paid by the customer | Tron (TRC-20) |
| **USDC** | Polygon · BNB Chain (BEP-20) | Ethereum (ERC-20): the higher gas fee is paid by the customer | Tron (TRC-20) |

Polygon and BNB Chain are cheap and fast. **The exact network and address are always confirmed by email before you pay.**

> **Before paying**
> 1. We accept **USDT or USDC only**, on the network we tell you by email. **Do not send over Tron (TRC-20)**. Another token or network may lose the funds **irrecoverably**.
> 2. Use **only the address we email you for your order**; no other page or message publishes it. Compare it character by character.
> 3. Network fees (and your exchange's fees) are on you: the **full price** must arrive.
> 4. Blockchain payments are **irreversible**.

**Other options, by email on request only:** transfer between Takenos users, or ACH from a US bank account. Ask for them in your first email; no wires, SWIFT or cards.

### Common terms
- Delivery by **email with the file attached**, usually within 24 business hours after we confirm the full payment arrived (indicative).
- **No refunds once downloaded, unless the file is damaged or does not match the description:** we will replace it or refund you (in the same token, minus network fees).
- Bug fixes for version 1.x are free for existing buyers.
- Underpayments, overpayments or wrong-network payments: we will contact you; nothing is delivered until the amount is covered.
- Personal licence (one per person; for companies or teams, email us). No redistribution.
- Educational and technical material; **not financial advice**, no promise of profitability, no strategies or signals included. Trading carries a risk of total loss.

**Tested on** macOS with Python 3.9 and 3.14 (tool and templates); Linux and Windows not tested yet.

## About the author
**David Antonio Navas** — AI Technology student. Contact: danc.ventas@gmail.com

## Licences
- Code: **MIT** ([`LICENSE`](LICENSE)). Texts: **CC BY-NC 4.0** ([`LICENSE-TEXTOS.md`](LICENSE-TEXTOS.md)). Paid products come with their own personal licence.

## Notice
Educational and technical material, **not financial, investment or trading advice**. No warranty of any kind. No affiliation with any prop firm, broker or data vendor. See [`AVISO_LEGAL.md`](AVISO_LEGAL.md).
