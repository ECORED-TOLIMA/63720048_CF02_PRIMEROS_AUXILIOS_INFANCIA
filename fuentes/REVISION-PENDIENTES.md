# Revisión y pendientes — CF2_63720048

**Técnicas de primeros auxilios en primera infancia.** Este documento recoge lo que **no se puede
resolver desde las fuentes** (`.xd`, `.pdf`, `_DI.docx`, `_AD.docx`), las **decisiones** que tomé
para no detener el trabajo —cada una revertible— y **qué quedó verificado y cómo**.

Se lee en este orden: lo bloqueado (§2) es lo único que necesita que alguien aporte algo; lo demás es
información para revisar, no trabajo pendiente.

---

## 1. Estado del entregable

| Pantalla | Estado | Verificación |
|---|---|---|
| Portada, Introducción | del maquetador | intactas |
| Tema 1, 2 y 3 | del maquetador (`b3da27e`) | intactas; ver §3 |
| **Tema 4** · Lesiones, traumatismos y movilización | maquetado | alto 10 650 frente a 10 453 del artboard (**+1,9 %**); cajones 1/1 |
| **Tema 5** · Situaciones específicas | maquetado | 22 diferencias de bloque sobre 51 franjas; cajones 1/1 |
| **Tema 6** · Comunicación y cadena de custodia | maquetado | cajones 1/1; sin desbordes en móvil |
| **Síntesis** | maquetada | el anexo es la pág. 10 de este curso; el mapa da **0,945** al reexportarlo |
| **Actividad** | maquetada | 20 preguntas, barajado doble, contrastada contra las tablas del `_AD.docx` |

En todas: **0 vistas rotas**, **0 elementos animados que no lleguen a aparecer** y **0 desbordes
horizontales a 485 px**.

---

## 2. BLOQUEADO — hace falta material que no está en las fuentes

Esto es lo único que no puedo resolver yo.

1. **Las 5 imágenes de la actividad son de otro curso.** `src/assets/actividad/imagen1..5.png` son
   los marcadores del scaffold: ilustraciones de negocios y tecnología. **No están en el XD ni en el
   PDF de este componente — las aporta el diseñador.** Se ve a simple vista al abrir `#/actividad`:
   una pregunta sobre hemorragias ilustrada con una placa de circuitos.

   El scaffold traía 10 archivos que eran 5 imágenes duplicadas; borré los 5 duplicados sin usar. El
   check automático de imágenes repetidas pasa, pero **sólo sabe detectar duplicados**: no puede
   saber que una foto es de otro curso.

2. **El pódcast del 6.1 no tiene audio.** El DI sólo da el nombre del guion
   (`63720048_CF02_Guion_podcast`) y el XD dibuja el reproductor. Va un **MP3 mudo de 180 s** con ese
   nombre exacto para que el componente funcione y muestre la duración. Cuando llegue el audio real,
   basta con sustituir el archivo.

3. **No hay URL de vídeo en ninguna fuente** para la Introducción: sólo aparece el nombre del guion.

4. **El DI trae un bloque de apertura del Tema 2 que el diseño NO dibuja** (líneas 140-155 del
   volcado): la introducción del tema, los «cuatro aspectos fundamentales» y los siete pasos de la
   evaluación inicial. Busqué las frases en el artboard, en **todo** el `.xd` —pasteboard incluido— y
   en el PDF: cero coincidencias en los tres. **Hay que decidirlo con diseño instruccional: o el DI
   las quita, o el diseño las dibuja.**

---

## 3. Pendiente en los temas cerrados (1, 2 y 3)

Estos temas son del maquetador y **no los he tocado**: `git diff` sobre sus tres vistas y sobre sus
assets sale vacío. Lo anoto sólo para que esté a la vista.

5. **El hallazgo 1.11 de su propio documento sigue sin aplicar en su `Tema2.vue`:** el slider del 2.4
   conserva los botones y los bullets grises del kit y sólo la primera diapositiva tiene foto. La
   clase `.slyder-a--curso` que creé para el 4.5 le sirve tal cual, y **las fotos que faltan están en
   el pasteboard** del `.xd` (misma técnica con la que saqué las de los temas 4, 5 y 6).

6. **Las Tablas 1 y 2 del Tema 2 salen con el encabezado gris.** `.tabla-a.color-acento-contenido`
   **no pinta el `thead`**: el kit lo deja en su gris pase lo que pase. Hace falta un modificador,
   como el `.tabla--traslado` que escribí para la Tabla 3.

7. **En su `Tema1.vue`, la primera de las tres tarjetas pegadas repite el título y el texto de la
   segunda** («Pulmones» en las líneas 171 y 179). Debería decir «Vías respiratorias».

8. **La banda decorativa a sangre detrás del slider del 2.4 no está puesta.** Exportarla por
   rectángulo arrastra también el contenido de encima, así que haría falta exportar sólo el grupo del
   fondo.

---

## 4. Decisiones que tomé (por si hay que revertirlas)

### Fuentes y contenido

9. **El texto sale del `_DI.docx`, transcrito, no redactado.** Párrafos, tablas, acordeones, listas,
   sliders y tarjetas salen del volcado del documento, así que son literales.

10. **La lista A-E del 4.7 y las cinco precauciones del DEA (3.4) van SIN negrilla**, aunque el XD las
    dibuja en `Roboto-Bold`: los runs del DOCX no llevan negrilla y la regla firme es que manda el
    formato del documento. Si se prefiere el XD, es cambiar el criterio.

11. **Los títulos del acordeón del 4.6 van sin los dos puntos finales** que el XD dibuja en dos de los
    tres. Los dos puntos son el separador del texto corrido del DI, no parte del término.

12. **Los tres rótulos de las tarjetas de apertura del Tema 3 los pone el XD, no el DI**, que deja el
    «:» que los introduce sin enumerarlos.

13. **En la actividad, `titulo` es el TIPO y `tema` el nombre.** El encabezado del `_AD.docx` dice
    «ACTIVIDAD DIDÁCTICA **CUESTIONARIO**» y eso es lo que el kit pinta como título; «Misión: salvar
    vidas» es el nombre de la actividad y va en `tema`. Estaban al revés.

14. **La retroalimentación de la actividad va SIN el «¡Correcto!» del docx**, porque el kit ya pinta
    esa etiqueta y si no sale duplicada. Es la única licencia sobre el texto del documento.

15. **Los títulos de resultado no se escriben.** El docx no los da y el kit trae sus valores por
    defecto. Estaban puestos a mano y uno decía «VUELVA A INTENTARLO» donde el kit dice «VUELVE».

16. **El enlace del botón «Descargar» del 6.3 SÍ está en el DI** y se usó tal cual, sin inventarlo: el
    manual de cadena de custodia de la Fiscalía General de la Nación.

### Componentes y medidas

17. **El mapa de la Síntesis se exportó del XD en SVG**, no se reusó el del scaffold, que traía el
    mapa de otro curso. Mide 1228 px, el ancho útil de la tarjeta.

18. **El `TabsA` del 5.1 abre la primera pestaña; el XD dibuja abierta la segunda.** El componente del
    kit siempre arranca en la primera y no expone una prop para cambiarlo. Cuál se dibuja abierta es
    una decisión de presentación del artboard, no contenido.

19. **El kit NO trae estilos para las pestañas.** El componente `TabsA` existe pero no hay ni una
    línea de CSS, y la clase de borde que usa el catálogo tampoco existe en ningún sitio. Los estilos
    del 5.1 los escribí con las medidas de la ficha: pestañas 295×50 con radio 5, verde claro y
    `#16D95E` la abierta; panel blanco con filete `#FCF9FF` de 4 px, muestreado del PDF.

20. **La infografía del 5.2 es de puntos calientes, no una figura.** El rótulo y los seis textos están
    en el pasteboard del XD. La imagen base va sin las píldoras ni los «+», que los pinta el
    componente, y los seis puntos van en porcentaje del contenedor.

21. **El color de la tarjeta del acordeón va por la prop del componente, no por CSS.** El kit expone
    `clase-tarjeta`; forzarlo con `!important` era pelearse con el propio componente. Los temas
    cerrados siguen por la vía antigua y **renderizan idénticos** (comprobado).

22. **En el Tema 1 los tres paneles del 1.2 quedan en 314 px de alto y el XD los dibuja 405×461.** La
    altura la manda el contenido. Si hay que clavar los 461, va con un alto mínimo explícito.

23. **Las fotos del Tema 2 van con las esquinas rectas.** El inventario trae 131 máscaras cuadradas y
    sólo 4 con radio, y no conseguí emparejar esas cuatro con ninguna de las cinco fotos del tema.
    Vale la pena comprobarlo a ojo.

24. **El Tema 4 no lleva variantes móviles de figura porque no tiene ninguna «Figura N».** Comprobado
    contra el pasteboard: en todo el `.xd` existen **tres** variantes móviles —la Figura 1 del Tema 1,
    la Figura 2 del Tema 2 y la infografía del Tema 5— y las tres están puestas.

---

## 5. Erratas y rarezas de la fuente, reproducidas tal cual

25. **El DI duplica cuatro párrafos dentro de su propia celda** (los cierres del 4.7, el 5.1, el 5.3 y
    el Tema 6). Se maquetaron una sola vez; conviene corregirlo en la fuente.

26. **Los tres paneles ocultos de las pestañas del 5.1 traen un *lorem ipsum* de la plantilla del
    kit** («This is a normal paragraph (p element)…») que el diseñador no borró. No se transcribió; el
    texto bueno es el que va después y coincide con el DI.

27. **El `.xd` que llegó con la revisión es NUEVO pero no es un rediseño.** 97 entradas iguales, 0
    recursos nuevos, mismos nodos; lo único, 12 textos del pasteboard convertidos a curvas y el
    artboard del Tema 2 retocado. Como fuente es igual o algo peor que el anterior.

---

## 6. Avisos del verificador que NO son fallos

28. **«Icono repetido» en el badge del corazón del Tema 5 (×3) y en el icono de las nueve pastillas
    del Tema 6.** Son falsos positivos: en el XD es **el mismo nodo** repetido a propósito. La regla
    vale para una fila de tarjetas, no para un adorno que el diseño reutiliza.

29. **Los separadores entre subtemas no los detecta la comparación de bloques**: son una banda gris de
    7 px demasiado tenue. Están puestos.

30. **El PDF de diseño miente con el color de las bandas a sangre.** Las pinta violeta oscuro y en el
    XD son degradados claros. Pasó en el 2.4, en el 4.5 y en el 5.3. Manda el XD.

---

## 7. Qué está verificado, y cómo

Para que se sepa qué respalda cada «está bien»:

- **Assets**: cada foto se compara por correlación contra el mismo rectángulo del PDF de diseño. Las
  de los temas 4, 5 y 6 están entre **0,971 y 0,999**. Los vectores se exportan por su rectángulo,
  uno a uno, para no cruzar iconos.
- **Layout**: cada pantalla se mide bloque a bloque contra el render del artboard, emparejando por
  color y ancho.
- **Estático**: assets inexistentes, iconos repetidos, ancho de columna contra el ancho de la imagen,
  columnas vacías, placeholders del scaffold y la actividad contra las tablas del docx.
- **Navegador**: vistas rotas, elementos animados que no llegan a aparecer, desbordes a 485 px y cajas
  que se salen de su columna a 1440 px.
- **Cajones**: se cuentan las pestañas de 25×8 del XD y se comparan con los maquetados. En los temas
  4, 5 y 6 la cuenta da exacta, y en los dos últimos **fue este check el que encontró el cajón que se
  me había pasado**.

**Lo que NO está verificado:** la revisión visual pantalla por pantalla de los temas 1, 2 y 3, que son
del maquetador y no he tocado.
