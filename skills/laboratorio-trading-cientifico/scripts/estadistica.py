"""Utilidades estadísticas del laboratorio (sin dependencias salvo numpy).

Uso típico:
    from estadistica import ic_bootstrap_bloques, p_placebo, benjamini_hochberg, efecto_minimo_detectable
"""
import numpy as np


def ic_bootstrap_bloques(r, bloques, n=10000, alfa=0.05, semilla=0):
    """IC de la media de r remuestreando bloques enteros (p. ej. semanas).

    r: array de R por operación; bloques: etiqueta de bloque por operación.
    """
    r = np.asarray(r, float)
    bloques = np.asarray(bloques)
    unicos = np.unique(bloques)
    grupos = [r[bloques == b] for b in unicos]
    sumas = np.array([g.sum() for g in grupos])
    cuentas = np.array([len(g) for g in grupos])
    rng = np.random.default_rng(semilla)
    idx = rng.integers(0, len(grupos), size=(n, len(grupos)))
    medias = sumas[idx].sum(1) / cuentas[idx].sum(1)
    return float(r.mean()), float(np.quantile(medias, alfa / 2)), float(np.quantile(medias, 1 - alfa / 2))


def p_placebo(real, placebos):
    """p unilateral = (k+1)/(M+1), k = placebos >= real."""
    placebos = np.asarray(placebos, float)
    k = int((placebos >= real).sum())
    return (k + 1) / (len(placebos) + 1)


def benjamini_hochberg(pvals, q=0.10):
    """Devuelve (rechazos booleanos, q-valores ajustados)."""
    p = np.asarray(pvals, float)
    m = len(p)
    orden = np.argsort(p)
    ajust = np.empty(m)
    acumulado = 1.0
    for rango, i in enumerate(orden[::-1]):
        k = m - rango
        acumulado = min(acumulado, p[i] * m / k)
        ajust[i] = acumulado
    return ajust <= q, ajust


def efecto_minimo_detectable(n, sd_r=1.2, alfa=0.05, potencia=0.80, efecto_diseno=1.0):
    """EMD aproximado (en R) para una media con n operaciones, prueba unilateral.

    efecto_diseno > 1 si las operaciones están agrupadas (bloques correlacionados).
    """
    from statistics import NormalDist
    z = NormalDist().inv_cdf(1 - alfa) + NormalDist().inv_cdf(potencia)
    return z * sd_r * np.sqrt(efecto_diseno / max(n, 1))


if __name__ == "__main__":
    rng = np.random.default_rng(1)
    r = rng.normal(0.05, 1.2, 600)
    semanas = np.repeat(np.arange(200), 3)
    print("media e IC:", ic_bootstrap_bloques(r, semanas, n=2000))
    print("p placebo:", p_placebo(0.05, rng.normal(0, 0.05, 2000)))
    print("BH:", benjamini_hochberg([0.001, 0.02, 0.04, 0.3], q=0.10))
    print("EMD con 200 op.:", round(efecto_minimo_detectable(200), 3))
