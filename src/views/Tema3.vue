<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 3
      h1 Soporte vital básico en primera infancia

    //- Ficha: foto (186,316) 396x281 · nota (602,437) 812x160 #DDEEFE r=10 con el icono
    //- (629,475) 84x84 #FFC0AC r=10
    .row.align-items-start.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t3/f1.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p(data-aos="fade-down") El soporte vital básico corresponde al conjunto de acciones inmediatas orientadas a mantener la oxigenación y la circulación en una persona que presenta una alteración grave de sus funciones vitales. Estas intervenciones buscan preservar la vida hasta la llegada de atención especializada, mediante la aplicación de técnicas estandarizadas y seguras.
        .bg-3.r-10.p-4.mt-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t3/ic1.png" alt="" style="width: 104px")
            .col
              p.mb-0 En la primera infancia, el soporte vital básico adquiere especial relevancia debido a la mayor vulnerabilidad de niñas y niños frente a eventos como la obstrucción de la vía aérea, la insuficiencia respiratoria y el paro cardiorrespiratorio. Estas situaciones pueden evolucionar rápidamente, por lo que requieren una intervención oportuna y adecuada por parte del primer respondiente.

    p.mt-4(data-aos="fade-down") La atención inicial se basa en la valoración de la niña o del niño y en la aplicación de técnicas específicas, de acuerdo con la emergencia identificada:

    //- Ficha: tres tarjetas (186/602/1018, 676) 396x150 #FFE6DE r=10 con su icono de 60x60
    .row.mt-4
      .col-lg-4.mb-4.mb-lg-0(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 150px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/t1.svg" alt="" style="width: 60px")
          p.mb-0
            b Reanimación cardiopulmonar
      .col-lg-4.mb-4.mb-lg-0(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 150px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/t2.svg" alt="" style="width: 60px")
          p.mb-0
            b Manejo de la obstrucción de la vía aérea
      .col-lg-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 150px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/t3.svg" alt="" style="width: 60px")
          p.mb-0
            b Uso del desfibrilador externo automático

    p.mt-5(data-aos="fade-down") La aplicación correcta y oportuna de estas técnicas contribuye a mantener o recuperar la respiración y la circulación, mientras llega la atención especializada. Por esta razón, deben realizarse de manera segura y de acuerdo con la edad y las condiciones de la niña o del niño.

    p(data-aos="fade-down") A continuación, se explica la reanimación cardiopulmonar y su aplicación según la edad de la niña o del niño, teniendo en cuenta sus características anatómicas y fisiológicas, así como las condiciones de seguridad necesarias durante la atención.

    Separador

    #t_3_1.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 3.1 RCP en lactantes

    //- Ficha: foto (1122,1211) 292x267 · nota (186,1358) 916x120 #DDEEFE r=10
    .row.align-items-start
      .col-lg-9
        p(data-aos="fade-down") La reanimación cardiopulmonar (RCP) en lactantes es una técnica de soporte vital básico que se aplica cuando el lactante no responde y no respira normalmente o solo jadea. Su finalidad es mantener temporalmente la circulación sanguínea y el aporte de oxígeno a los órganos vitales mientras llega la atención especializada. Durante el primer año de vida, el paro cardiorrespiratorio suele estar relacionado con alteraciones respiratorias; por ello, se requiere una actuación rápida, segura y organizada (American Heart Association, 2020).
        .bg-3.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Antes de iniciar la RCP, se debe verificar la seguridad del entorno y valorar la respuesta y la respiración del lactante. Si no responde y no respira normalmente, se debe solicitar ayuda, activar el sistema de emergencias mediante la línea 123 e iniciar las maniobras de reanimación, de acuerdo con la capacitación recibida.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t3/f2.png" alt="" style="width: 292px").m-auto

    p.mt-4(data-aos="fade-down") Para realizar el procedimiento, se deben seguir estas acciones:

    //- Ficha: banda (290,1548) 1020x629 #F4EDFE. Los términos van TODOS en negrilla: así los trae el
    //- DOCX, aunque en el arte sólo el primero aparezca resaltado.
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ol--cuadro.mb-0
            li
              span.lista-ol--cuadro__vineta 1
              |  #[b Verificar la seguridad:] comprobar que el lugar no represente peligro para el lactante ni para quien brinda la atención.
            li
              span.lista-ol--cuadro__vineta 2
              |  #[b Valorar la respuesta:] estimular suavemente al lactante y observar si responde mediante movimientos, sonidos o gestos.
            li
              span.lista-ol--cuadro__vineta 3
              |  #[b Observar la respiración:] verificar si respira normalmente o solo jadea, sin prolongar innecesariamente la valoración.
            li
              span.lista-ol--cuadro__vineta 4
              |  #[b Solicitar ayuda:] pedir apoyo a las personas cercanas y activar el sistema de emergencias mediante la línea 123.
            li
              span.lista-ol--cuadro__vineta 5
              |  #[b Ubicar al lactante:] colocarlo boca arriba sobre una superficie firme y plana para facilitar las maniobras.
            li
              span.lista-ol--cuadro__vineta 6
              |  #[b Iniciar las compresiones:] comprimir el centro del pecho, sobre el esternón, con el talón de una mano o mediante la técnica de los dos pulgares con las manos rodeando el tórax.
            li
              span.lista-ol--cuadro__vineta 7
              |  #[b Aplicar la profundidad adecuada:] comprimir aproximadamente un tercio del diámetro anteroposterior del tórax, equivalente a unos 4 cm.
            li
              span.lista-ol--cuadro__vineta 8
              |  #[b Mantener el ritmo:] realizar entre 100 y 120 compresiones por minuto, permitir la expansión completa del tórax y reducir al mínimo las interrupciones.
            li
              span.lista-ol--cuadro__vineta 9
              |  #[b Combinar compresiones y ventilaciones:] realizar ciclos de 30 compresiones y 2 ventilaciones cuando participa un solo reanimador, o de 15 compresiones y 2 ventilaciones cuando intervienen dos reanimadores capacitados.
            li.mb-0
              span.lista-ol--cuadro__vineta 10
              |  #[b Continuar las maniobras:] mantener la RCP hasta que el lactante muestre signos de respuesta, llegue el personal especializado, el entorno deje de ser seguro o quien brinda la atención no pueda continuar.

    //- Ficha: icono (186,2227) 84x84 #FFC0AC r=10
    .row.align-items-center.mt-5.mb-4
      .col-auto.mb-3.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t3/ic3.png" alt="" style="width: 104px")
      .col
        p(data-aos="fade-down") La aplicación ordenada de estas acciones contribuye a mantener la circulación y el aporte de oxígeno durante una emergencia. Las maniobras deben realizarse con precaución, sin ejercer una fuerza excesiva y conforme a los protocolos vigentes y la capacitación recibida.
        p.mb-0(data-aos="fade-down") Después de reconocer la técnica de RCP en lactantes, es necesario comprender otra situación de emergencia frecuente durante la primera infancia: la obstrucción de la vía aérea por cuerpo extraño. A diferencia del paro cardiorrespiratorio, esta condición puede presentarse mientras la niña o el niño está consciente, por lo que exige señales de identificación y maniobras diferentes. Por esta razón, a continuación se aborda la obstrucción de la vía aérea por cuerpo extraño (OVACE), sus manifestaciones y las acciones seguras para atenderla.
    Separador

    #t_3_2.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 3.2 Obstrucción de la vía aérea por cuerpo extraño (OVACE)

    //- Ficha: ilustración (186,3958) 292x166 sobre la caja (186,3986) 292x138 #F4EDFE r=[20,20,0,0]
    .row.align-items-start
      .col-lg-3.mb-4.mb-lg-0
        figure.r-tl-tr-10.p-3
          img(src="@/assets/curso/temas/t3/1.svg" alt="").w-100
      .col-lg-9
        p(data-aos="fade-down") La obstrucción de la vía aérea por cuerpo extraño (OVACE) es una emergencia que ocurre cuando un alimento u objeto bloquea de manera parcial o total el paso del aire hacia los pulmones. En lactantes, niñas y niños, esta situación puede evolucionar rápidamente; por ello, es fundamental reconocer las señales de alerta y actuar de manera oportuna y segura.
        p.mb-0(data-aos="fade-down") La obstrucción puede presentarse mientras se consumen alimentos o cuando se introducen objetos pequeños en la boca. El riesgo aumenta con alimentos duros, redondos o difíciles de masticar, así como con monedas, botones, piezas de juguetes y otros elementos que se encuentran al alcance de la población infantil.

    //- Ficha: pastilla (186,4164) 396x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Reconocimiento de la obstrucción

    p(data-aos="fade-down") Las manifestaciones dependen de si el paso del aire está bloqueado de forma parcial o total:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ul.lista-ul--compacta
            li
              i.fas.fa-heart
              span.mb-0 #[b Obstrucción parcial:] la niña o el niño puede toser con fuerza, emitir sonidos, respirar y responder. En este caso, se debe permitir que continúe tosiendo, observar su evolución y evitar maniobras innecesarias.
            li.mb-0
              i.fas.fa-heart
              span.mb-0 #[b Obstrucción total:] la niña o el niño no puede hablar, llorar, toser eficazmente ni respirar. También puede llevarse las manos al cuello, presentar coloración azulada alrededor de los labios o perder el conocimiento.

    p.mt-4(data-aos="fade-down") Reconocer el tipo de obstrucción permite seleccionar la actuación adecuada. No se deben introducir los dedos en la boca ni intentar retirar el objeto cuando no sea visible, ya que podría desplazarse hacia una zona más profunda.

    //- Ficha: pastilla (186,4579) 489x50
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Actuación ante una obstrucción en lactantes

    p(data-aos="fade-down") Si el lactante está consciente y presenta una obstrucción total, se deben aplicar las siguientes acciones:

    //- Ficha: seis tarjetas 396x220 #FFE6DE r=10 en (186/602/1018, 4698) y (186/602/1018, 4938)
    .row.mt-4
      .col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 220px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/i1.svg" alt="" style="width: 60px")
          p.mb-0 #[b Solicitar ayuda:] pedir apoyo y activar el sistema de emergencias mediante la línea 123.
      .col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 220px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/i2.svg" alt="" style="width: 60px")
          p.mb-0 #[b Ubicar al lactante:] colocarlo boca abajo sobre el antebrazo o el muslo, con la cabeza más baja que el pecho y sostenida de manera segura.
      .col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 220px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/i3.svg" alt="" style="width: 60px")
          p.mb-0 #[b Aplicar golpes en la espalda:] realizar cinco golpes firmes entre los omóplatos con el talón de la mano.
      .col-lg-4.mb-4.mb-lg-0(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 220px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/i4.svg" alt="" style="width: 60px")
          p.mb-0 #[b Girar al lactante:] colocarlo boca arriba, manteniendo la cabeza más baja que el pecho.
      .col-lg-4.mb-4.mb-lg-0(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 220px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/i5.svg" alt="" style="width: 60px")
          p.mb-0 #[b Realizar compresiones torácicas:] aplicar cinco compresiones en el centro del pecho, sobre el esternón.
      .col-lg-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100(style="min-height: 220px")
          figure.mb-3
            img(src="@/assets/curso/temas/t3/i6.svg" alt="" style="width: 60px")
          p.mb-0 #[b Repetir la secuencia:] alternar cinco golpes en la espalda y cinco compresiones torácicas hasta que el objeto sea expulsado, el lactante respire o pierda la respuesta.

    p.mt-5(data-aos="fade-down") No se deben realizar compresiones abdominales en lactantes, debido al riesgo de causar lesiones en los órganos internos.

    //- Ficha: pastilla (186,5267) 520x50
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Actuación ante una obstrucción en niñas y niños

    p(data-aos="fade-down") Si la niña o el niño está consciente y no puede respirar, hablar, llorar o toser eficazmente, se deben aplicar estas acciones:

    //- Ficha: banda (290,5374) 1020x360 #F4EDFE · foto (998,5404) 282x303
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4.p-md-5(data-aos="fade-down")
          .row.align-items-center
            .col-lg-8
              ul.lista-ul.lista-ul--compacta
                li
                  i.fas.fa-heart
                  span.mb-0 #[b Solicitar ayuda:] activar el sistema de emergencias mediante la línea 123.
                li
                  i.fas.fa-heart
                  span.mb-0 #[b Ubicarse detrás:] colocarse detrás de la niña o del niño y rodear su cintura con los brazos.
                li
                  i.fas.fa-heart
                  span.mb-0 #[b Posicionar las manos:] formar un puño y ubicarlo por encima del ombligo y por debajo del esternón; luego, sujetarlo con la otra mano.
                li
                  i.fas.fa-heart
                  span.mb-0 #[b Aplicar compresiones abdominales:] realizar impulsos rápidos hacia adentro y hacia arriba.
                li.mb-0
                  i.fas.fa-heart
                  span.mb-0 #[b Continuar la atención:] repetir las compresiones hasta que el objeto sea expulsado, la niña o el niño vuelva a respirar o pierda la respuesta.
            .col-lg-4.d-none.d-lg-block
              figure.m-0
                img(src="@/assets/curso/temas/t3/f4.png" alt="" style="width: 282px").m-auto

    p.mt-4(data-aos="fade-down") Las maniobras deben ajustarse al tamaño y a las condiciones físicas de la niña o del niño, evitando aplicar una fuerza desproporcionada.

    .row.justify-content-center.mt-4
      .col-lg-10
        .cajon.color1.p-4(data-aos="fade-down")
          p.mb-0 Después de reconocer las acciones para atender una obstrucción de la vía aérea, es importante abordar el uso del desfibrilador externo automático como apoyo durante la reanimación cardiopulmonar. En el siguiente apartado, se explica su función y las principales recomendaciones para utilizarlo de manera segura en lactantes, niñas y niños.

    Separador

    #t_3_3.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 3.3 Uso del desfibrilador externo automático (DEA)

    //- Ficha: foto (1122,6176) 292x217
    .row.align-items-start
      .col-lg-9
        p(data-aos="fade-down") El desfibrilador externo automático (DEA) es un dispositivo portátil que analiza el ritmo cardíaco y determina si es necesario aplicar una descarga eléctrica. Su uso durante un paro cardiorrespiratorio complementa la reanimación cardiopulmonar (RCP), pero no reemplaza las compresiones ni las ventilaciones.
        .cajon.color1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 En lactantes, niñas y niños, el DEA debe utilizarse tan pronto como esté disponible. Para menores de ocho años, se emplean preferiblemente parches pediátricos o un sistema reductor de energía. Si estos elementos no están disponibles, puede utilizarse un DEA con parches para personas adultas, siguiendo las instrucciones del dispositivo.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t3/f5.png" alt="" style="width: 292px").m-auto

    p.mt-4(data-aos="fade-down") Mientras una persona realiza la RCP, otra debe activar el sistema de emergencias mediante la línea 123 y buscar el DEA. Para utilizarlo de manera organizada y segura, se deben seguir estas acciones:

    //- Ficha: tarjetas del slider (290/637/983, 6492) 327x401 #8EC5FC r=20 con su icono de 128.
    //- El XD sólo dibuja los tres primeros iconos; los cinco restantes salen del pasteboard,
    //- elegidos por lo que representan (DEA, monitor, escudo, lupa y botiquín con visto).
    SlyderF.slyder--principios.mt-4(columnas="col-md-6 col-lg-4")
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 401px")
        figure
          img(src="@/assets/curso/temas/t3/d1.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Encender el DEA
        p.text-center.mb-0 Activar el dispositivo y escuchar atentamente las instrucciones visuales o de voz.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 401px")
        figure
          img(src="@/assets/curso/temas/t3/d2.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Descubrir el pecho
        p.text-center.mb-0 Retirar las prendas que impidan la colocación de los parches y secar la piel si se encuentra húmeda.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 401px")
        figure
          img(src="@/assets/curso/temas/t3/d3.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Seleccionar los parches
        p.text-center.mb-0 Utilizar parches pediátricos o un sistema reductor de energía cuando estén disponibles para lactantes y menores de ocho años.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 401px")
        figure
          img(src="@/assets/curso/temas/t3/d4.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Colocar los parches
        p.text-center.mb-0 Adherirlos sobre el pecho desnudo, de acuerdo con las imágenes indicadas en el dispositivo. Si los parches pueden tocarse entre sí, se debe colocar uno en el centro del pecho y otro en la espalda.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 401px")
        figure
          img(src="@/assets/curso/temas/t3/d5.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Permitir el análisis
        p.text-center.mb-0 Suspender momentáneamente las compresiones y verificar que ninguna persona toque al lactante, la niña o el niño mientras el DEA analiza el ritmo cardíaco.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 401px")
        figure
          img(src="@/assets/curso/temas/t3/d6.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Aplicar la descarga
        p.text-center.mb-0 Si el dispositivo la recomienda, comprobar que nadie esté en contacto con la persona y seguir la indicación para administrarla.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 401px")
        figure
          img(src="@/assets/curso/temas/t3/d7.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Reanudar la RCP
        p.text-center.mb-0 Reiniciar inmediatamente las compresiones y las ventilaciones después de la descarga o cuando el DEA indique que esta no es necesaria.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 401px")
        figure
          img(src="@/assets/curso/temas/t3/d8.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Seguir las instrucciones
        p.text-center.mb-0 Continuar la RCP y atender las indicaciones del dispositivo hasta que se evidencien signos de respuesta o llegue el personal especializado.

    p.mt-5(data-aos="fade-down") Durante el uso del DEA, se deben tener en cuenta las siguientes precauciones:

    //- Ficha: banda (290,6975) 1020x210 #F4EDFE · ilustración (1068,7021) 222x143 #8EC5FC r=10
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4.p-md-5(data-aos="fade-down")
          .row.align-items-center
            .col-lg-8
              ul.lista-ol--cuadro.mb-0
                li
                  span.lista-ol--cuadro__vineta A
                  |  No colocar los parches sobre ropa, piel mojada ni objetos metálicos.
                li
                  span.lista-ol--cuadro__vineta B
                  |  No permitir que los parches se toquen o se superpongan.
                li
                  span.lista-ol--cuadro__vineta C
                  |  No tocar al lactante, la niña o el niño durante el análisis ni al aplicar la descarga.
                li
                  span.lista-ol--cuadro__vineta D
                  |  No retirar los parches ni apagar el dispositivo mientras continúa la atención.
                li.mb-0
                  span.lista-ol--cuadro__vineta E
                  |  Reducir al mínimo las interrupciones de las compresiones torácicas.
            .col-lg-4.d-none.d-lg-block
              figure.m-0
                img(src="@/assets/curso/temas/t3/2.svg" alt="" style="width: 222px").m-auto

    //- Ficha: icono (186,7213) 84x84 #FFC0AC r=10
    .row.align-items-center.mt-5
      .col-auto.mb-3.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t3/ic2.png" alt="" style="width: 104px")
      .col
        p(data-aos="fade-down") El uso oportuno del DEA, combinado con una RCP de calidad, fortalece la respuesta ante un paro cardiorrespiratorio. Mantener la calma, seguir las instrucciones del dispositivo y continuar las maniobras contribuye a brindar una atención inicial segura mientras llega el personal especializado.
        p.mb-0(data-aos="fade-down") Después de reconocer las acciones de soporte vital básico, es necesario abordar otras situaciones que también pueden afectar la salud y la integridad de lactantes, niñas y niños. En el siguiente apartado, se presentan las medidas de atención inicial ante lesiones, traumatismos y situaciones que requieren una movilización segura.

</template>

<script>
export default {
  name: 'Tema3',
}
</script>
