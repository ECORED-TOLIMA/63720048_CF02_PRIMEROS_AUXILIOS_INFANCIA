# Plan de maquetación — Tema 4

Artboard `Tema-4` (`6f483d33`, 1600x10453, `XD_DX=1686 XD_DY=11700`), el más grande del curso.
Esto es el mapa de bloques leído del artboard y del `_DI.docx` (líneas **316-403**), para no
volver a renderizarlo. Los assets se regeneran con `python3 scripts/exportar_assets.py tema4`
(48 assets en `fuentes/tema4/`).

## Mapa de bloques

| # | bloque | DI | componente / medida del XD |
|---|---|---|---|
| | título 4 | 316 | `.titulo-principal` |
| | párrafo | 317 | |
| | ilustración + caja | 318 | `#8EC5FC r10 292x201@(185,454)` + `#FFE6DE r10 916x245@(497,410)` con icono 84x84 en (533,446) |
| | párrafos | 319, 320 | |
| | 3 paneles pegados | 321-323 | `#8EC5FC r=[20,0,0,20] 405x412`, `#DBC2FA 419x412`, `#FFE6DE r=[20,0,0,20] 405x412`; icono en círculo blanco DENTRO del panel |
| | párrafo | 324 | |
| **4.1** | Atención de lesiones | 325 | `#t_4_1` |
| | párrafos | 326, 327 | |
| | acordeón 3 ítems | 328-330 | `#F4EDFE r20 1020x190@(290,1654)` abierto + `#B8F4CE r20 1020x90` en 1859 y 1964 |
| | párrafo + caja + ilustración | 331, 332 | ilustración `#DBC2FA r10 292x227@(1121,2084)` |
| **4.2** | Lesiones osteomusculares | 333 | `#t_4_2` |
| | foto + párrafo + caja con icono | 334, 335 | `#DDEEFE r10 812x160@(601,2674)` + icono 84x84 en (631,2712) |
| | párrafo | 336 | |
| | **Tabla 3** (5 col x 5 filas) | 337-345 | filas `#F6F6F6 1019x78` alternando con `#FFFFFF`, desde y=3054 |
| | párrafos | 346, 347 | |
| | lista de 5 con viñeta | 348-352 | caja `#DDEEFE 1020x317@(290,3575)` |
| | párrafos | 353, 354 | |
| **4.3** | Manejo de traumas | 355 | `#t_4_3` |
| | foto + párrafos + caja | 356, 357 | `#FFE6DE r10 916x130@(497,4384)` |
| | icono 84x84 + párrafo | 358 | |
| | párrafo | 359 | |
| | 2 cajas con icono circular | 360, 361 | `#DDEEFE r10 812x140@(601,5426)` y su pareja lila |
| | párrafo | 362 | |
| **4.4** | Movilización y traslado | 363 | `#t_4_4` |
| | foto + caja con icono | 364 | |
| | párrafo | 365 | |
| | 2 cajas con icono circular | 366, 367 | |
| | párrafo | 368 | |
| | **el único `.cajon`** | 369 | pestaña 25x8 en (289,6080) |
| **4.5** | Principios de movilización | 370 | `#t_4_5` |
| | `.bloque-texto-g` | 371 | foto a media izquierda + caja blanca. **Es `.bloque-texto-g`** (`_texto-destacado.sass:224`), NO `.row.bg-4` + `.tarjeta--blanca`: está en el diccionario como `componente-inventado` |
| | párrafo | 372 | |
| | **SlyderA de 5** | 373-377 | tarjeta `#FFFFFF r1 1263x584@(169,6756)`, foto `#8EC5FC 584x330@(797,6892)` + `#DBC2FA 214x330` |
| | foto + párrafo + caja con icono | 378, 379 | |
| **4.6** | Tipos de movilización | 380 | `#t_4_6` |
| | párrafo + foto | 381 | |
| | caja salmón | 382 | `#FFE6DE 812x140@(185,8014)` |
| | párrafo | 383 | |
| | acordeón 3 ítems **numerados** | 384-386 | `#F4EDFE r20 1020x190@(290,8257)` + `#B8F4CE 1020x90@(290,8462)`; los títulos van «1. …», «2. …», «3. …» |
| | párrafo | 387 | |
| **4.7** | Técnicas de traslado | 388 | `#t_4_7` |
| | foto + caja con icono | 389 | `#FFE6DE r10 811x275@(601,8978)` + icono 84x84 en (637,9014) |
| | párrafo | 390 | |
| | lista **A-E** + ilustración | 391-395 | caja `#F4EDFE 1020x210@(290,9340)`, ilustración `#8EC5FC r10 222x148@(1068,9380)` |
| | párrafo | 396 | |
| | foto + **LineaTiempoD de 4** | 397-400 | barras `#B8F4CE r5 544x37` en y 9839/9899/9957 y abierto `#F4EDFE r5 544x190@(765,9629)` |
| | párrafo | 401 | |
| | `.tarjeta--badge-arriba` | 402 | caja `#DBC2FA r10 1020x140@(290,10174)` + badge `#8EC5FC r42 70x70@(765,10139)` (círculo con corazón) |
| | párrafo | 403 | |

## Assets (`fuentes/tema4/` -> `src/assets/curso/temas/t4/`)

| origen | destino | qué es |
|---|---|---|
| 2.svg | ilus1.svg | botiquín (apertura) |
| 3,4,5.svg | i1,i2,i3.svg | iconos de los 3 paneles (caída, líquido caliente, torcedura) |
| 9.svg | ilus2.svg | niños con botiquín (4.1) |
| 10.png | f2.png | foto rodilla (4.2) |
| 11.svg | ic1.svg | icono 84x84 (4.2) |
| 14.png | f3.png | foto sofá (4.3) |
| 15.svg | ic2.svg | icono 84x84 (4.3) |
| 16,17.svg | i4,i5.svg | iconos circulares de los 2 traumas |
| 18.png | f4.png | foto camilla (4.4) |
| 19.svg | ic3.svg | icono 84x84 ambulancia (4.4) |
| 21,22.svg | i6,i7.svg | iconos circulares de los 2 tipos de movilización |
| 24.png | f5.png | foto del `.bloque-texto-g` (4.5) |
| 28.png | f6.png | foto del slider (4.5) |
| 31.png | f7.png | foto médica (cierre de 4.5) |
| 32.svg | ic4.svg | icono 84x84 (cierre de 4.5) |
| 40.png | f8.png | foto niño en coche (4.6) |
| 44.png | f9.png | foto camilla (4.7) |
| 45.svg | ic5.svg | icono 84x84 (4.7) |
| 46.svg | ilus3.svg | ilustración de la lista A-E |
| 47.png | f10.png | foto médico con bebé (LineaTiempoD) |

Faltan por exportar a mano, como se hizo en el Tema 3 con `--grupo`/`--rect`:

- el **badge del corazón** del cierre: `--rect 765 10139 70 70`;
- los **círculos blancos** de los iconos de los tres paneles de apertura, si se quieren tal cual
  (los `3/4/5.svg` traen sólo la línea, sin el círculo).

## Cosas a respetar

- El `.bloque-texto-g` lleva la foto como `background-image`. **Nada de `require()`**: va con un
  `import` estático arriba del `<script>` y se enlaza con `:style` (regla `require-en-vite`).
- Sólo hay **un** `.cajon` en todo el tema (el check `4b` espera 1).
- Los términos con «:» de las listas van en **negrilla**, que es como están en el DOCX; las líneas
  A-E de 4.7 (391-395) hay que comprobarlas run a run antes de decidir.
- **La línea 402 del DI viene duplicada en el DOCX**: el párrafo «El traslado no consiste
  únicamente en cambiar de lugar…» está escrito dos veces seguidas en la misma celda. Va una sola
  vez; es una errata de la fuente y conviene avisar a diseño instruccional.
