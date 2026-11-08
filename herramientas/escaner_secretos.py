#!/usr/bin/env python3
"""Escaner de secretos. Sin argumentos: revisa lo preparado en git (pre-commit). Con --todo: revisa lo que git incluiria.
Bloquea: .env, ficheros > 20 MB, patrones de claves/tokens y cualquier valor presente en .env. Nunca imprime valores."""
import os, re, subprocess, sys

RAIZ = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
LIM = 20 * 1024 * 1024
PERMITIDOS = ()
PAT = [('token de Telegram', r'\b\d{8,10}:[A-Za-z0-9_-]{30,}'), ('clave sk-', r'\bsk-[A-Za-z0-9_-]{20,}'),
       ('clave Google', r'\bAIza[A-Za-z0-9_-]{30,}'), ('token GitHub/Slack', r'\b(ghp|gho|ghs|xox[bpa])[-_][A-Za-z0-9_-]{20,}'),
       ('AWS', r'\bAKIA[0-9A-Z]{16}\b'), ('clave privada', r'-----BEGIN [A-Z ]*PRIVATE KEY-----'),
       ('asignacion de clave', r'''(?i)\b(api[_-]?key|secret|passwd|password|token)\b\s*[=:]\s*["'][A-Za-z0-9_\-\.]{24,}["']''')]

def valores_env():
    v = set()
    try:
        for l in open(os.path.join(RAIZ, '.env')):
            if '=' in l and not l.lstrip().startswith('#'):
                x = l.split('=', 1)[1].strip().strip('"\'')
                if len(x) >= 8: v.add(x.encode())
    except OSError:
        pass
    return v

def main():
    if '--todo' in sys.argv:
        out = subprocess.check_output(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=RAIZ).decode().split('\0')
    else:
        out = subprocess.check_output(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR', '-z'], cwd=RAIZ).decode().split('\0')
    envv = valores_env(); bad = []; n = 0
    pats = [(k, re.compile(p)) for k, p in PAT]
    for rel in filter(None, out):
        p = os.path.join(RAIZ, rel)
        if not os.path.isfile(p) or os.path.islink(p): continue
        n += 1
        b = os.path.basename(rel)
        if b == '.env' or (b.startswith('.env.') and b != '.env.example'): bad.append((rel, 0, 'archivo .env')); continue
        sz = os.path.getsize(p)
        if PERMITIDOS and rel.startswith(PERMITIDOS): continue
        if sz > LIM: bad.append((rel, 0, 'fichero > 20 MB')); continue
        if sz > 5_000_000: continue
        try: data = open(p, 'rb').read()
        except OSError: continue
        if b'\0' in data[:2048]: continue
        for v in envv:
            if v in data: bad.append((rel, 0, 'contiene un valor del .env'))
        txt = data.decode('utf-8', 'ignore')
        for i, line in enumerate(txt.splitlines(), 1):
            if len(line) > 2000: continue
            for k, rx in pats:
                if rx.search(line): bad.append((rel, i, k)); break
    for rel, i, k in bad: print(f'BLOQUEADO {rel}:{i}: {k}', file=sys.stderr)
    print(f'escaner de secretos: {n} archivos revisados, {len(bad)} hallazgos', file=sys.stderr)
    sys.exit(1 if bad else 0)

main()
