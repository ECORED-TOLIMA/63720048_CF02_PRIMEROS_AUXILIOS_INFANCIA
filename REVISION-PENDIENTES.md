# Revisión y pendientes — CF2_63720048

Lo que **no se puede resolver desde las fuentes** (`.xd`, `.pdf`, `_DI.docx`, `_AD.docx`) y las
decisiones que tomé para no parar. Todo lo demás sale de las fuentes.

## Bloqueado: hace falta material que no está en las fuentes

1. **Las 5 imágenes de la actividad son de otro curso.** `src/assets/actividad/imagen1..5.png` son
   los marcadores del scaffold BASE: ilustraciones de negocios (monedas, flechas, gente de
   oficina). No están en el XD ni en el PDF de este componente — **las aporta el diseñador**. Se ve
   a simple vista al abrir `#/actividad`: la primera pregunta, sobre comunicación en emergencias,
   sale ilustrada con un gráfico financiero.

   El scaffold traía 10 archivos que eran 5 imágenes duplicadas (`imagen1=imagen7`,
   `imagen2=imagen8`, `imagen3=imagen9`, `imagen4=imagen10`, `imagen5=imagen6`). Borré los 5
   duplicados sin usar; siguen en el historial de git. `gen_actividad.py` reparte una imagen por
   cada 4 preguntas (`imagen1..5`), como en CF1.

   El check `1g` de `verificar_maqueta.py` ya pasa, pero **sólo sabe detectar duplicados**: no
   puede saber que una foto es de otro curso. Que pase no significa que estén bien.

2. **Temas 3 a 6 sin maquetar.** `src/views/Tema3..6.vue` siguen en el scaffold (17 líneas). Por eso
   el check `4b` marca DESCUADRE en los cuatro: el XD dibuja 4+1+1+1 pestañas de `.cajon` y hay 0
   maquetadas. No es un fallo de maquetación, es trabajo que falta. El Tema 2 ya está y da
   `XD=4 maquetados=4 OK`.

3. **El DI trae un bloque de apertura del Tema 2 que el diseño NO dibuja.** Son las líneas 140-155
   del volcado del `_DI.docx`: la introducción del tema, los «cuatro aspectos fundamentales»
   (nivel de conciencia, respiración, pulso, signos de alarma) y los **siete pasos** para hacer la
   evaluación inicial de forma segura y ordenada.

   No es que no lo encontrara: busqué las frases en el `graphicContent.agc` del artboard `Tema-2`,
   en **todo** el `.xd` (incluido el pasteboard, por la regla `texto-dado-por-inexistente`) y en el
   PDF del diseño. Cero coincidencias en los tres. El artboard arranca directamente con el
   contenido del 2.1, y tampoco dibuja el subtítulo «2.1 Nivel de conciencia».

   Lo maqueté como está en el diseño y **dejé fuera esas 15 líneas del DI**. Hay que decidirlo con
   diseño instruccional: o el DI las quita, o el diseño las dibuja. Siguiendo el precedente de CF1
   (su nota 3), el anclaje `t_2_1` del menú apunta al primer bloque del tema, que es justamente el
   que habla del nivel de conciencia.

4. **Las diapositivas 2 y 3 del slider de 2.4 se quedan sin foto.** En toda la región del slider el
   artboard tiene **una sola imagen** (`Imagen 118`, 564x376): el diseño dibuja únicamente la
   primera diapositiva. Repetir esa foto en las otras dos era inventarme material, y el check `1b`
   lo caza como icono repetido. Si el diseñador aporta dos fotos más, se añaden a las
   diapositivas 2 y 3 con la misma estructura de columnas que la primera.

5. **La banda decorativa a sangre detrás del slider de 2.4 no está puesta.** En el XD el bloque va
   sobre una banda de 1600x936 que sale del ancho de la tarjeta (el patrón `.bg-fondo-N` de
   `_custom.sass`). Exportarla por `--rect` arrastra también el contenido de encima (la tarjeta
   blanca, el texto y la foto), así que haría falta exportar sólo el grupo del fondo. El bloque
   queda funcional y con el contenido correcto, pero sin la banda.

## Decisiones que tomé (por si hay que revertirlas)

1. **El mapa de la Síntesis se exportó del XD, no se reusó el del scaffold.** `sintesis.svg` venía
   con el mapa de otro curso más (análisis de requisitos de software: UML, casos de uso, historias
   de usuario). El de este componente está en el artboard `Sintesis – PDF` (`39c2a691`) y mide
   **1228×727 px**, justo el ancho útil de la tarjeta:

   ```
   XD_DX=14044 XD_DY=8854 python3 scripts/gen_asset.py 39c2a691 \
     --rect 186 524 1228 727 src/assets/curso/sintesis.svg
   ```

   En **SVG**, no PNG, por la regla `raster-en-vez-de-svg`: el mapa es vectorial y lleva la
   tipografía incrustada.

2. **El `alt` del mapa son dos frases y 71 palabras**, la misma forma y longitud que el de CF1
   (67 palabras), que es el que pasó la revisión: qué organiza el mapa (los seis ejes) y qué
   permite concluir. La regla `alt-inventariado` avisa a partir de ~45 palabras, pero enumerar los
   seis ejes es el contenido de la figura.

3. **En el Tema 1 los tres paneles del 1.2 quedan en 314 px de alto y el XD los dibuja 405×461.**
   La altura la manda el contenido, igual que en CF1. Antes medían 389 px —más cerca del XD— pero
   sólo por accidente: eran los 75 px del bug de `.h-100` sobre `.tarjeta--icono-arriba`
   (ver la entrada `utilidad-bootstrap-pisa-la-clase-custom` del diccionario). Si hay que clavar
   los 461 del XD, va con un `min-height` explícito, nunca con `.h-100`.

4. **Las fotos del Tema 2 van con las esquinas rectas.** El inventario del artboard trae 131
   máscaras CUADRADAS y sólo 4 con radio (292x290 y 294x332 con r=10, 1228x474 con r=20, 560x309
   con r=10), y no conseguí emparejar esas cuatro con ninguna de las cinco fotos del tema. Me
   quedé con lo que se ve en el render del artboard, que es esquina recta. Vale la pena
   comprobarlo a ojo contra el XD: si alguna lleva radio, va con `.r-10` o `.r-20`.

5. **El texto del Tema 2 se compuso por número de línea del `_DI.docx`, no transcribiéndolo.** Los
   párrafos, las dos tablas, los cinco ítems del acordeón, los cinco pasos del pulso y los tres
   niveles del slider salen del volcado de `docx_text.py`, así que son literales y no hay erratas
   de copia.

6. **La retroalimentación de la actividad va SIN el «¡Correcto!» del docx.** Lo pinta ya
   `ActividadPregunta.vue` del kit (1.0.9), y dejarlo daba «¡Correcto! ¡Correcto! …». Es la única
   licencia sobre el texto del docx. Ojo: **CF1 sí lo dejó** y por eso arrastra esa duplicación.

## Avisos del verificador que no son fallos

- `1h` marca `$color-sistema-b` y `$color-acento-botones` en la frontera de `textColor()`, pero
  **ninguna de las dos se usa en las vistas** (0 usos), así que no hay nada que comprobar a ojo.
- `4c` (altos contra el XD) sigue sin implementar en el verificador; el alto se mide a mano.
