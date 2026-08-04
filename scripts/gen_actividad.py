#!/usr/bin/env python3
"""Genera `src/views/Actividad.vue` a partir del `_AD.docx` (la actividad didáctica).

Esta pantalla **no se mide contra ningún diseño**: el XD no trae artboard de Actividad
(11 artboards para 11 páginas del PDF, todas asignadas). Sale del docx montada sobre el
`ActividadController` del kit.

Lo que hay que tener en cuenta del componente (leerlo antes de tocar los datos):

- **El kit presenta sólo 10 preguntas** (`MAX_PREGUNTAS = 10` + `slice(0, 10)` en
  `actividadCuestionario/Actividad.vue`). De ahí: van TODAS las del docx (es un banco),
  **`barajarPreguntas` DEBE ir en `true`** (con `false` el `slice` daría siempre las mismas 10
  en el mismo orden) y el botón «Volver a intentarlo» sólo aparece si el banco es mayor que 10.
- **La retroalimentación se duplica** si se deja el prefijo: `ActividadPregunta.vue` ya pinta
  su propia etiqueta «¡Correcto!»/«¡Incorrecto!» antes del mensaje, y los del docx empiezan
  por ella → se le quita.
- El kit reserva la columna `col-5` de la imagen **sin `v-if`**, así que cada pregunta lleva
  imagen. Se reparte una por cada 4 preguntas (`imagen1..5`), que son los 5 marcadores del
  scaffold BASE (de otro curso; anotados en REVISION-PENDIENTES.md).
- El umbral del 70 % está **hardcodeado** en el kit y coincide con lo que pide el docx.

Uso: gen_actividad.py [--print]
"""
import math
import os
import re
import subprocess
import sys
import config as C

AD = C.uno_docx('_AD.docx')
SALIDA = f'{C.ENTREGABLE}/src/views/Actividad.vue'
SCRIPTS = os.path.dirname(os.path.abspath(__file__))


def filas():
    """Las filas de las tablas del docx, como listas de celdas."""
    txt = subprocess.run(['python3', f'{SCRIPTS}/docx_text.py', AD],
                         capture_output=True, text=True, check=True).stdout
    out = []
    for linea in txt.splitlines():
        if linea.startswith('| '):
            out.append([c.strip() for c in linea.strip('|').split('|')])
    return out


def js(s):
    """Escapa una cadena para un literal JavaScript de comilla simple."""
    return s.replace('\\', '\\\\').replace("'", "\\'")


def main():
    fs = filas()
    campos = {}
    preguntas = []
    actual = None

    for celdas in fs:
        etiqueta = celdas[0]
        valor = celdas[1] if len(celdas) > 1 else ''
        if etiqueta.startswith('Nombre de la Actividad'):
            campos['titulo'] = valor.rstrip('.')
        elif etiqueta.startswith('Objetivo de la actividad'):
            campos['objetivo'] = valor
        elif etiqueta.startswith('Instrucciones para el aprendiz'):
            # el docx separa los párrafos con ¶: se conservan como <br><br>
            campos['instrucciones'] = ' '.join(v.strip() for v in valor.split('¶'))
        elif etiqueta.startswith('Mensaje cuando supera'):
            campos['aprobado'] = valor
        elif etiqueta.startswith('Mensaje cuando el porcentaje'):
            campos['reprobado'] = valor
        elif re.match(r'^Pregunta \d+$', etiqueta):
            actual = {'id': int(etiqueta.split()[1]), 'texto': valor, 'opciones': []}
            preguntas.append(actual)
        elif etiqueta.startswith('Opción') and actual:
            marca = celdas[2].strip().upper() if len(celdas) > 2 else ''
            actual['opciones'].append({
                'id': etiqueta.replace('Opción', '').strip().strip(')'),
                'texto': valor,
                'correcta': marca == 'X',
            })
        elif etiqueta.startswith('Comentario respuesta correcta') and actual:
            # ⚠️ quitar el «¡Correcto!» del docx: el componente ya pinta su etiqueta
            actual['ok'] = re.sub(r'^¡Correcto!\s*', '', valor)
        elif etiqueta.startswith('Comentario respuesta incorrecta') and actual:
            actual['no'] = re.sub(r'^¡Incorrecto!\s*', '', valor)

    faltan = [p['id'] for p in preguntas if not any(o['correcta'] for o in p['opciones'])]
    if faltan:
        raise SystemExit(f'⚠️ sin respuesta marcada con X: preguntas {faltan}')

    bloques = []
    for p in preguntas:
        ops = ',\n'.join(
            f"            {{\n              id: '{o['id']}',\n"
            f"              texto: '{js(o['texto'])}',\n"
            f"              esCorrecta: {'true' if o['correcta'] else 'false'},\n            }}"
            for o in p['opciones'])
        bloques.append(
            f"        {{\n          id: {p['id']},\n"
            f"          texto: '{js(p['texto'])}',\n"
            f"          imagen: '@/assets/actividad/imagen{math.ceil(p['id'] / 4)}.png',\n"
            f"          barajarRespuestas: true,\n          opciones: [\n{ops},\n          ],\n"
            f"          mensaje_correcto: '{js(p.get('ok', ''))}',\n"
            f"          mensaje_incorrecto: '{js(p.get('no', ''))}',\n        }}")

    TODOS = ',\n'.join(bloques)
    vue = f'''<template lang="pug">
.curso-main-container.pb-3
  BannerInterno(icono="far fa-question-circle" titulo="Actividad didáctica")
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5
    #Actividad
    ActividadController(:cuestionario="cuestionario")

</template>

<script>
//- GENERADO por `scripts/gen_actividad.py` desde `xds/1/22810005_CF01_AD.docx`.
//- No editar a mano: volver a correr el script si cambia el docx.
import ActividadController from '@ecored-sena/boulder-kit/plugin/components/actividad/ActividadController.vue'

export default {{
  name: 'ActividadDidactica',
  components: {{
    ActividadController,
  }},
  data: () => ({{
    cuestionario: {{
      tema: 'Fundamentos de programación en Python',
      titulo: '{js(campos.get("titulo", "Cuestionario"))}',
      introduccion:
        '<b>Objetivo:</b> {js(campos.get("objetivo", ""))}<br><br>{js(campos.get("instrucciones", ""))}',
      // el kit sólo muestra 10 de las {len(preguntas)}: barajar es OBLIGATORIO
      barajarPreguntas: true,
      titulo_aprobado: '¡BUEN TRABAJO!',
      titulo_reprobado: 'VUELVA A INTENTARLO',
      mensaje_aprobado: '{js(campos.get("aprobado", ""))}',
      mensaje_reprobado: '{js(campos.get("reprobado", ""))}',
      preguntas: [
{TODOS},
      ],
    }},
  }}),
}}
</script>

<style lang="sass"></style>
'''
    if '--print' in sys.argv:
        print(vue)
    else:
        open(SALIDA, 'w').write(vue)
        print(f'{SALIDA}: {len(preguntas)} preguntas, '
              f'{sum(len(p["opciones"]) for p in preguntas)} opciones')


main()
