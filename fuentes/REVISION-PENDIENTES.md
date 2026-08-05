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
   cada 4 preguntas (`imagen1..5`).

   El check `1g` de `verificar_maqueta.py` ya pasa, pero **sólo sabe detectar duplicados**: no
   puede saber que una foto es de otro curso. Que pase no significa que estén bien.

2. **Temas 5 y 6 sin maquetar.** `src/views/Tema5.vue` y `Tema6.vue` siguen en el scaffold (17
   líneas). Por eso el check `4b` marca DESCUADRE en los dos: el XD dibuja 1+1 pestañas de `.cajon`
   y hay 0 maquetadas. No es un fallo de maquetación, es trabajo que falta. Los temas 1 a 4 dan
   `maquetados = XD` en ese check.

   El Tema 4 llevaba además el párrafo de la línea **402 del DI duplicado en el propio DOCX** («El
   traslado no consiste únicamente en cambiar de lugar…» escrito dos veces seguidas en la misma
   celda). Se maquetó una sola vez; conviene avisar a diseño instruccional para que lo corrija en la
   fuente.

3. **El DI trae un bloque de apertura del Tema 2 que el diseño NO dibuja.** Son las líneas 140-155
   del volcado del `_DI.docx`: la introducción del tema, los «cuatro aspectos fundamentales»
   (nivel de conciencia, respiración, pulso, signos de alarma) y los **siete pasos** para hacer la
   evaluación inicial de forma segura y ordenada.

   No es que no lo encontrara: busqué las frases en el `graphicContent.agc` del artboard `Tema-2`,
   en **todo** el `.xd` (incluido el pasteboard, por la regla `texto-dado-por-inexistente`) y en el
   PDF del diseño. Cero coincidencias en los tres. El artboard arranca directamente con el
   contenido del 2.1, y tampoco dibuja el subtítulo «2.1 Nivel de conciencia».

   Lo maqueté como está en el diseño y **dejé fuera esas 15 líneas del DI**. Hay que decidirlo con
   diseño instruccional: o el DI las quita, o el diseño las dibuja. Mientras tanto, el anclaje
   `t_2_1` del menú apunta al primer bloque del tema, que es justamente el que habla del nivel de
   conciencia.

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

2. **El `alt` del mapa son dos frases y 71 palabras**, con la forma acordada: qué organiza el
   mapa (los seis ejes) y qué permite concluir. La regla `alt-inventariado` avisa a partir de ~45 palabras, pero enumerar los
   seis ejes es el contenido de la figura.

3. **En el Tema 1 los tres paneles del 1.2 quedan en 314 px de alto y el XD los dibuja 405×461.**
   La altura la manda el contenido. Antes medían 389 px —más cerca del XD— pero
   sólo por accidente: eran los 75 px del bug de `.h-100` sobre `.tarjeta--icono-arriba`
   (ver la entrada `utilidad-bootstrap-pisa-la-clase-custom` del diccionario). Si hay que clavar
   los 461 del XD, va con un `min-height` explícito, nunca con `.h-100`.

4. **Los tres rótulos de las tarjetas de apertura del Tema 3 los pone el XD, no el DI.** El DI
   (línea 235) deja el «:» que los introduce y no los enumera; el artboard sí los nombra:
   «Reanimación cardiopulmonar», «Manejo de la obstrucción de la vía aérea» y «Uso del
   desfibrilador externo automático». Se tomaron de ahí.

5. **Los tres subtítulos de OVACE son la `.titulo-tercero` del kit con el color del curso.** En el
   XD son pastillas #FFC0AC de 50 px con `r=25`. El icono NO es un asset: el nodo del XD se llama
   literalmente `house-medical-solid-full`, o sea el `fa-house-medical` de FontAwesome que ya trae
   el proyecto. El tema queda en `_custom.sass`, como `.cajon.color1` o `.acordion--principios`; no
   se inventó ninguna clase.

6. **El slider del DEA (3.4) tiene ocho pasos y sólo las tres primeras tarjetas llevan icono.** El
   artboard dibuja únicamente las tres tarjetas de la ventana visible del slider y sólo trae esos
   tres iconos. Mismo criterio que con las fotos del slider del Tema 2: antes que repetir un icono
   —que además el check `1b` caza— las cinco restantes van sin él.

7. **Las cinco precauciones del DEA (A-E) NO van en negrilla.** El XD las pinta en negrilla, pero en
   el `_DI.docx` esos párrafos no llevan `<w:b/>`, y manda el DOCX para el formato del texto
   (regla `estilo-de-texto-inventado`). Comprobado run a run en `word/document.xml`; los términos
   de las demás listas del Tema 2 y del Tema 3 sí van en negrilla en el DOCX, y así se maquetaron.

8. **Las fotos del Tema 2 van con las esquinas rectas.** El inventario del artboard trae 131
   máscaras CUADRADAS y sólo 4 con radio (292x290 y 294x332 con r=10, 1228x474 con r=20, 560x309
   con r=10), y no conseguí emparejar esas cuatro con ninguna de las cinco fotos del tema. Me
   quedé con lo que se ve en el render del artboard, que es esquina recta. Vale la pena
   comprobarlo a ojo contra el XD: si alguna lleva radio, va con `.r-10` o `.r-20`.

9. **Los iconos de 84x84 del Tema 4 se exportaron uno a uno.** El XD **reusa el mismo cuadrado
   salmón** en los seis (los rects `456463`, `456477` y `456483` aparecen repetidos), pero el glifo
   de dentro es distinto en cada uno. El pipeline automático los combinó mal y el check `1b` cazó un
   icono repetido; se sacaron por `--rect` en sus seis coordenadas: (533,446), (631,2712),
   (185,4544), (631,5454), (628,7563) y (637,9014).

10. **El panel de la `.bloque-texto-g` del 4.5 va `.color-primario`**, que en este curso es
   `#8EC5FC`, el fill del rect del XD. El componente no pinta fondo propio: lo toma de la clase de
   color que se le ponga, así que con `.color-acento-contenido` salía salmón.

11. ~~Los iconos de los tres paneles de apertura del Tema 4 van sin su círculo blanco.~~
   **RESUELTO**: se exportan por `--rect` sobre el círculo entero (`Grupo 1177470..72`, 150x150 en
   (315/727/1138, 855)), así que el SVG ya trae el círculo y no hace falta CSS.

12. ~~La primera diapositiva del slider del 4.5 es la única con foto.~~ **RESUELTO**: las otras
   cuatro estaban en el PASTEBOARD, en x=521 con y=−4808/−4448/−4088/−3728, con su marco de
   584x330. Se sacan con `--rect 533 <y+11> 560 309` y `XD_AB=pasteboard`.

15. **La lista A-E del 4.7 va SIN negrilla aunque el XD la dibuja en `Roboto-Bold`.** Los runs del
   `_DI.docx` no llevan `<w:b/>` en esos cinco puntos, y la regla firme es que manda el formato del
   DOCX. Si se prefiere el XD, es quitar el criterio y ponerlos en `b`.

16. **Los títulos del acordeón del 4.6 van sin los dos puntos finales** que el XD dibuja en dos de
   los tres («1. Movilización de emergencia:», «3. Movilización asistida:»). Los dos puntos son el
   separador del texto corrido del DI, no parte del término, y el tercero no los lleva.

17. **El Tema 4 no tiene ninguna «Figura N», así que no lleva variantes móviles de figura.** Las
   imágenes del tema son fotos y ilustraciones de acompañamiento, no figuras informativas.

18. **El encabezado de las tablas necesita su modificador.** `.tabla-a.color-acento-contenido` NO
   pinta el `thead`: el kit lo deja gris. La Tabla 3 lo pide con `.tabla--traslado`; **las Tablas 1
   y 2 del Tema 2 siguen con el encabezado gris** porque no llevan ningún modificador.

19. **Pendiente del Tema 2 (hallazgo 1.11), no tocado por ser tema cerrado:** el `SlyderA` del 2.4
   sigue con los botones y los bullets del kit y con foto sólo en la primera diapositiva. La clase
   `.slyder-a--curso` que se creó para el 4.5 le vale tal cual.

13. **El texto de los temas 2, 3 y 4 se compuso por número de línea del `_DI.docx`, no
   transcribiéndolo.** Los párrafos, las tres tablas, los acordeones, las listas numeradas, las de
   viñeta, los sliders y las tarjetas salen del volcado de `docx_text.py`, así que son literales y
   no hay erratas de copia.

14. **La retroalimentación de la actividad va SIN el «¡Correcto!» del docx.** Lo pinta ya
   `ActividadPregunta.vue` del kit (1.0.9), y dejarlo daba «¡Correcto! ¡Correcto! …». Es la única
   licencia sobre el texto del docx.

## Avisos del verificador que no son fallos

- `1h` marca `$color-sistema-b` y `$color-acento-botones` en la frontera de `textColor()`, pero
  **ninguna de las dos se usa en las vistas** (0 usos), así que no hay nada que comprobar a ojo.
- `4c` (altos contra el XD) sigue sin implementar en el verificador; el alto se mide a mano.

## Revisión visual — lo que está mirado y lo que no

**Mirado bloque a bloque contra el render del artboard:** el Tema 4 entero. Cierra en **10 650 px
contra 10 453 del artboard (+1,9 %)** y los bordes medidos cuadran: banda del 4.5 en 140..1459
(XD 136..1464), componente del 4.7 en 708..1307 (XD 705..1308) y los tres paneles pegados del
1.º bloque con el mismo radio por esquina que el XD.

**Sin revisar bloque a bloque:** los Temas 5 y 6 (sin maquetar) y la Actividad.

**Los Temas 1, 2 y 3 son la versión del maquetador** y no se tocan. De ahí quedan dos cosas
abiertas que **no** son mías de corregir pero conviene tener a la vista:

- el hallazgo 1.11 de su documento sigue sin aplicar en su propio `Tema2.vue`: el `SlyderA` del 2.4
  conserva los botones y los bullets grises del kit y sólo la primera diapositiva tiene foto. La
  clase `.slyder-a--curso` creada para el 4.5 le sirve tal cual, y las fotos que faltan están en el
  pasteboard;
- las Tablas 1 y 2 del Tema 2 salen con el encabezado gris: `.tabla-a.color-acento-contenido` **no
  pinta el `thead`**, hace falta un modificador como el `.tabla--traslado` de la Tabla 3;
- y en su `Tema1.vue` la primera de las tres tarjetas pegadas repite el título y el texto de la
  segunda («Pulmones» en las líneas 171 y 179); debería decir «Vías respiratorias».

**El check que falta en el verificador** es el `4c`: comparar el alto renderizado de
`.container.tarjeta--blanca` con el alto del artboard del `mapa-artboards.json`. Hoy se mide a mano.

## Tema 5 — decisiones y avisos

20. **El badge del corazón sale tres veces y el check `1b` lo marca como icono repetido.** Es un
   falso positivo: en el XD es **el mismo nodo** (`Rectángulo 456429`, en 965, 2155 y 5880), o sea
   que el diseño lo repite a propósito. Queda anotado como excepción en el diccionario.

21. **El `TabsA` del 5.1 abre la primera pestaña; el XD dibuja abierta la segunda.** El componente
   del kit siempre arranca en la primera y no expone una prop para cambiarlo. Cuál se dibuja abierta
   es una decisión de presentación del artboard, no contenido, así que se deja el comportamiento del
   kit. Los cuatro paneles y sus cuatro iconos sí están completos (tres salieron del pasteboard).

22. **El kit NO trae estilos para `.tabs-a`**: `TabsA.vue` existe como componente pero no hay ni una
   línea de CSS, y `.color-*--borde` que usa el catálogo tampoco existe en ningún sitio. Los estilos
   del 5.1 se escribieron con las medidas de la ficha (pestañas 295x50 `r=5`, #B8F4CE / #16D95E;
   panel blanco con filete #FCF9FF de 4 px, muestreado del PDF).

23. **La infografía del 5.2 es de puntos calientes, no una figura.** El rótulo
   `INFOGRAFIA PUNTOS CALIENTES` y los seis textos están en el pasteboard, en (2982,−7967). La
   imagen base se exportó sin las píldoras ni los «+», y los seis puntos van en % del contenedor:
   11,5/39 · 27/71 · 42,5/39 · 58/71 · 73,4/39 · 89/71.
