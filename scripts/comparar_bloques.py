#!/usr/bin/env python3
"""Compara MI RENDER contra el render del ARTBOARD bloque a bloque, en números.

Por qué existe: los assets se venían midiendo (`gen_asset.py --pag N` da la correlación) pero el
LAYOUT se juzgaba a ojo, y de ahí salían los cuatro errores que se repiten — color equivocado,
separación inventada, ancho de columna mal medido e imagen sin su tratamiento. Esto los convierte
en una tabla de diferencias.

Qué mide, por cada bloque de la pantalla (un bloque = una franja horizontal con contenido):
  · el HUECO con la franja anterior — no la `y` absoluta: en cuanto un bloque mide distinto, la `y`
    de todos los de abajo se desplaza y la tabla se llena de ruido. El hueco es un error local
  · ancho e izquierda del contenido de la franja
  · color de fondo dominante de la franja
  · el alto de la franja

Uso:  comparar_bloques.py <ruta> <pagina> [--desde Y] [--hasta Y] [--base URL] [--tol 8]
      p. ej.  comparar_bloques.py curso/tema2 4 --desde 5400 --hasta 6844

El origen se ancla en el borde SUPERIOR de la tarjeta blanca (`.tarjeta--blanca`) en los dos lados,
que es el único punto común: el banner del render y el del PDF no miden lo mismo.
"""
import subprocess
import sys

import numpy as np
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
PDF_DPI2 = 2                      # la caché del PDF está a 144 dpi = 2 px por punto


def arg(nombre, defecto, tipo):
    return tipo(sys.argv[sys.argv.index(nombre) + 1]) if nombre in sys.argv else defecto


def franjas(a, x0, x1, umbral=6):
    """Devuelve las franjas horizontales con contenido: [(y_ini, y_fin, izq, der, color)]."""
    zona = a[:, x0:x1]
    fondo = np.median(zona.reshape(-1, 3), axis=0)
    dif = (np.abs(zona.astype(int) - fondo.astype(int)).sum(2) > 24)
    filas = dif.sum(1) > umbral
    out, ini = [], None
    for y, hay in enumerate(filas):
        if hay and ini is None:
            ini = y
        elif not hay and ini is not None:
            if y - ini >= 6:
                out.append((ini, y))
            ini = None
    if ini is not None:
        out.append((ini, len(filas)))
    res = []
    for y0, y1 in out:
        cols = dif[y0:y1].sum(0) > 0
        if not cols.any():
            continue
        izq, der = int(np.argmax(cols)), int(len(cols) - np.argmax(cols[::-1]))
        trozo = zona[y0:y1, izq:der].reshape(-1, 3)
        vals, cuentas = np.unique(trozo, axis=0, return_counts=True)
        color = vals[cuentas.argmax()]
        res.append((y0, y1, izq + x0, der + x0, '#%02X%02X%02X' % tuple(color)))
    return res


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    ruta, pagina = sys.argv[1], int(sys.argv[2])
    desde, hasta = arg('--desde', 0, int), arg('--hasta', 10**9, int)
    base = arg('--base', 'http://localhost:5175/CF2_63720048/', str)
    tol = arg('--tol', 8, int)
    tmp = '/tmp/comparar-bloques'
    subprocess.run(['mkdir', '-p', tmp], check=True)

    # 1. mi render, a 1600 de ancho (el del artboard) y alto de sobra
    png = f'{tmp}/mio.png'
    subprocess.run(['google-chrome', '--headless=new', '--disable-gpu', '--no-sandbox',
                    '--hide-scrollbars', '--virtual-time-budget=15000',
                    '--window-size=1600,26000', f'--screenshot={png}',
                    f'{base}?noaos#/{ruta}'], capture_output=True)
    mio = np.asarray(Image.open(png).convert('RGB'))

    # 2. el artboard, de la caché del PDF a 144 dpi, reescalado a 1600 de ancho
    art = Image.open(f'/tmp/xd-pdf-144dpi/CF2_63720048/p{pagina}.png').convert('RGB')
    art = art.resize((1600, art.height // PDF_DPI2))
    arr = np.asarray(art)

    # 3. origen común: el borde superior de la tarjeta blanca. En los dos lados es la primera fila
    #    donde una franja central ancha se vuelve blanca de lado a lado.
    def borde_tarjeta(a):
        centro = a[:, 300:1300]
        blancas = (centro.min(2) > 248).mean(1) > 0.97
        for y in range(60, len(blancas)):
            if blancas[y] and blancas[y + 1] and blancas[y + 2]:
                return y
        return 0
    o_mio, o_art = borde_tarjeta(mio), borde_tarjeta(arr)
    print(f'origen (borde de la tarjeta blanca): mío y={o_mio}  artboard y={o_art}')

    fm = [(y0 - o_mio, y1 - o_mio, iz, de, c) for y0, y1, iz, de, c in franjas(mio, 150, 1450)
          if desde <= y0 - o_mio <= hasta]
    fa = [(y0 - o_art, y1 - o_art, iz, de, c) for y0, y1, iz, de, c in franjas(arr, 150, 1450)
          if desde <= y0 - o_art <= hasta]

    print(f'\nfranjas con contenido: artboard {len(fa)} · mío {len(fm)}')

    def huecos(fs):
        return [0] + [fs[i][0] - fs[i - 1][1] for i in range(1, len(fs))]
    ha, hm = huecos(fa), huecos(fm)

    print(f'\n{"artboard":>36}   {"mío":>36}   diferencias')
    print(f'{"y":>6} {"hueco":>6} {"alto":>5} {"x":>5} {"ancho":>5} {"fondo":>8}   '
          f'{"y":>6} {"hueco":>6} {"alto":>5} {"x":>5} {"ancho":>5} {"fondo":>8}')
    problemas = []
    for i in range(max(len(fa), len(fm))):
        A = fa[i] if i < len(fa) else None
        M = fm[i] if i < len(fm) else None
        if A and M:
            marcas = []
            if abs(hm[i] - ha[i]) > tol * 3:
                marcas.append(f'hueco {hm[i] - ha[i]:+d}')
            if abs((M[3] - M[2]) - (A[3] - A[2])) > tol:
                marcas.append(f'ancho {(M[3] - M[2]) - (A[3] - A[2]):+d}')
            if abs(M[2] - A[2]) > tol:
                marcas.append(f'x {M[2] - A[2]:+d}')
            if A[4] != M[4]:
                marcas.append(f'fondo {A[4]}->{M[4]}')
            if abs((M[1] - M[0]) - (A[1] - A[0])) > tol * 4:
                marcas.append(f'alto {(M[1] - M[0]) - (A[1] - A[0]):+d}')
            print(f'{A[0]:>6} {ha[i]:>6} {A[1]-A[0]:>5} {A[2]:>5} {A[3]-A[2]:>5} {A[4]:>8}   '
                  f'{M[0]:>6} {hm[i]:>6} {M[1]-M[0]:>5} {M[2]:>5} {M[3]-M[2]:>5} {M[4]:>8}   '
                  f'{" · ".join(marcas)}')
            if marcas:
                problemas.append((A[0], marcas))
        elif A:
            print(f'{A[0]:>6} {ha[i]:>6} {A[1]-A[0]:>5} {A[2]:>5} {A[3]-A[2]:>5} {A[4]:>8}   '
                  f'{"—":>36}   FALTA EN MI RENDER')
            problemas.append((A[0], ['falta el bloque']))
        else:
            print(f'{"—":>36}   {M[0]:>6} {hm[i]:>6} {M[1]-M[0]:>5} {M[2]:>5} {M[3]-M[2]:>5} '
                  f'{M[4]:>8}   SOBRA EN MI RENDER')
            problemas.append((M[0], ['bloque de más']))
    print(f'\n{len(problemas)} bloques con diferencia' if problemas else '\nsin diferencias')
    return 1 if problemas else 0


if __name__ == '__main__':
    sys.exit(main())
