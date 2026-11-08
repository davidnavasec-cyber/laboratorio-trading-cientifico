#!/usr/bin/env python3
"""Comprobador de privacidad del repositorio publico. Sin argumentos revisa lo preparado en git (pre-commit);
con --todo revisa todo lo que git incluiria. Bloquea nombres de material ajeno o de la cuenta, rutas personales,
direcciones de correo y numeros de cuenta. No imprime el texto encontrado, solo archivo:linea y categoria."""
import os, re, subprocess, sys

RAIZ = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
REGLAS = [
    ('material del profesor / estrategias del piloto', r'(?i)valentini|maxwell|carta\s+magna|hotmart|sofea|venom\s?17|m15\s*gap|gotobi|bernd'),
    ('firma de fondeo concreta', r'(?i)spice\s?prop|ftmo|apex\s*trader|topstep|tradeify'),
    ('numero de cuenta', r'\b80813\b'),
    ('ruta personal', r'/Users/|C:\\\\Users|davidnavas'),
    ('correo', r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'),
    ('telegram', r'(?i)telegram_(token|chat_id)\s*=|api\.telegram\.org/bot'),
    ('capturas / saldos', r'(?i)\bsaldo\s+\d|equidad\s+\d|balance\s*[:=]\s*\d'),
]
PROPIOS = ('herramientas/comprobador_privacidad.py',)  # contiene las reglas

def main():
    if '--todo' in sys.argv:
        out = subprocess.check_output(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=RAIZ).decode().split('\0')
    else:
        out = subprocess.check_output(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR', '-z'], cwd=RAIZ).decode().split('\0')
    bad = []; n = 0
    rx = [(k, re.compile(p)) for k, p in REGLAS]
    for rel in filter(None, out):
        p = os.path.join(RAIZ, rel)
        if rel in PROPIOS or not os.path.isfile(p) or os.path.islink(p): continue
        if os.path.splitext(rel)[1].lower() in ('.png', '.jpg', '.jpeg', '.gif', '.pdf', '.zip', '.ex4', '.ex5'):
            bad.append((rel, 0, 'binario: revisar a mano')); continue
        if os.path.getsize(p) > 5_000_000: bad.append((rel, 0, 'archivo grande')); continue
        n += 1
        for i, line in enumerate(open(p, errors='ignore'), 1):
            for k, r in rx:
                if r.search(line): bad.append((rel, i, k))
    for rel, i, k in bad: print(f'PRIVACIDAD {rel}:{i}: {k}', file=sys.stderr)
    print(f'comprobador de privacidad: {n} archivos revisados, {len(bad)} hallazgos', file=sys.stderr)
    sys.exit(1 if bad else 0)

main()
