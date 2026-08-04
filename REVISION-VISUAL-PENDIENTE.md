# Revisión visual pendiente — lo que NO verifiqué

Corrección honesta a lo que dije en los commits de los temas 2, 3 y 4. Cuando escribí
«verificado», lo que estaba verificado era esto:

- los checks automáticos de `verificar_maqueta.py` en verde (1, 1b, 1c, 1d, 2, 3, 4, 4b, 4d);
- una o dos capturas de zonas concretas.

Eso **no es revisar la pantalla**. Los checks miden assets que faltan, vistas rotas, desborde
horizontal, cajas fuera de su columna y el recuento de `.cajon`. Ninguno de ellos ve «este bloque
se ve mal». Los temas se dieron por buenos sin mirarlos de arriba abajo.

## Confirmado roto: el bloque 2.4 del Tema 2

Mirado en `#/curso/tema2` a 1440 px:

1. **Falta la tarjeta blanca del XD** (`456178 1263x584@(170,5851)`, grupo `Grupo 1180933`). El
   contenido del slider va suelto sobre el fondo de la página.
2. **Falta la banda decorativa a sangre** y, sin ella y sin la tarjeta, los tres puntos del slider
   quedan sueltos encima del párrafo siguiente. Las flechas de anterior/siguiente no se ven.
3. **Las viñetas son `fa-circle` en salmón**: círculos gruesos donde el XD dibuja puntos pequeños.
4. **Huecos de varios cientos de píxeles** entre bloques, y la ilustración de cierre descolgada
   abajo a la derecha, lejos del texto al que acompaña.

La banda la había anotado como «pendiente» en `REVISION-PENDIENTES.md` (punto 5 de bloqueados).
Eso fue un error de criterio: sin la banda **y sin la tarjeta** el bloque no se sostiene, así que
no era un pendiente decorativo, era un bloque sin terminar. Y aun así se commiteó como maquetado.

## Lo que hay que hacer, y no está hecho

- **Repasar los cuatro temas pantalla por pantalla** contra el render del artboard, bloque por
  bloque. No por muestreo.
- Empezar por 2.4, que es el peor.
- Revisar en particular los bloques que monté sin verlos renderizados: los sliders de 2.4, 3.4 y
  4.5, la `LineaTiempoD` de 4.7 y el cierre en `.tarjeta--badge-arriba` de 4.7.
- Revisar el espaciado: los `mt-4`/`mt-5` los puse por criterio propio, no medidos contra el XD.
  Los huecos grandes del 2.4 vienen de ahí.

## Para el verificador

El check que falta es justamente el que habría cazado esto: comparar el **alto renderizado** de
`.container.tarjeta--blanca` con el alto del artboard del `mapa-artboards.json`. Está anotado como
pendiente en el propio `verificar_maqueta.py` (check `4c`). Un tema que en el XD mide 6844 px y en
la maqueta mide bastante más tiene huecos de más, y eso sí es automatizable.
