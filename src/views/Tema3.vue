<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 3
      h1 Soporte vital básico en primera infancia

    .row.align-items-center.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure.m-0
          img(src="@/assets/curso/temas/t3/f1.png" alt="").w-100
      .col-lg-8
        p.mb-0(data-aos="fade-down") El soporte vital básico corresponde al conjunto de acciones inmediatas orientadas a mantener la oxigenación y la circulación en una persona que presenta una alteración grave de sus funciones vitales. Estas intervenciones buscan preservar la vida hasta la llegada de atención especializada, mediante la aplicación de técnicas estandarizadas y seguras.

    //- La caja del XD arranca en x=602 y mide 812: va a la derecha, no a todo el ancho.
    .row.justify-content-end.mt-4
      .col-lg-8
        .bg-3.r-10.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-md-0
              figure
                img(src="@/assets/curso/temas/t3/ic3.svg" alt="" style="width: 84px")
            .col
              p.mb-0 En la primera infancia, el soporte vital básico adquiere especial relevancia debido a la mayor vulnerabilidad de niñas y niños frente a eventos como la obstrucción de la vía aérea, la insuficiencia respiratoria y el paro cardiorrespiratorio. Estas situaciones pueden evolucionar rápidamente, por lo que requieren una intervención oportuna y adecuada por parte del primer respondiente.

    p.mt-4(data-aos="fade-down") La atención inicial se basa en la valoración de la niña o del niño y en la aplicación de técnicas específicas, de acuerdo con la emergencia identificada:

    .row.mt-4
      .col-lg-4.mb-4.mb-lg-0(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i1.svg" alt="" style="width: 60px")
          p.mb-0.mt-3
            b Reanimación cardiopulmonar
      .col-lg-4.mb-4.mb-lg-0(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i2.svg" alt="" style="width: 60px")
          p.mb-0.mt-3
            b Manejo de la obstrucción de la vía aérea
      .col-lg-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i3.svg" alt="" style="width: 60px")
          p.mb-0.mt-3
            b Uso del desfibrilador externo automático

    p.mt-4(data-aos="fade-down") La aplicación correcta y oportuna de estas técnicas contribuye a mantener o recuperar la respiración y la circulación, mientras llega la atención especializada. Por esta razón, deben realizarse de manera segura y de acuerdo con la edad y las condiciones de la niña o del niño.

    p(data-aos="fade-down") A continuación, se explica la reanimación cardiopulmonar y su aplicación según la edad de la niña o del niño, teniendo en cuenta sus características anatómicas y fisiológicas, así como las condiciones de seguridad necesarias durante la atención.

    Separador

    #t_3_1.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 3.1 RCP en lactantes

    .row.align-items-start
      .col-lg-8
        p(data-aos="fade-down") La reanimación cardiopulmonar (RCP) en lactantes es una técnica de soporte vital básico que se aplica cuando el lactante no responde y no respira normalmente o solo jadea. Su finalidad es mantener temporalmente la circulación sanguínea y el aporte de oxígeno a los órganos vitales mientras llega la atención especializada. Durante el primer año de vida, el paro cardiorrespiratorio suele estar relacionado con alteraciones respiratorias; por ello, se requiere una actuación rápida, segura y organizada (American Heart Association, 2020).
        .bg-3.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Antes de iniciar la RCP, se debe verificar la seguridad del entorno y valorar la respuesta y la respiración del lactante. Si no responde y no respira normalmente, se debe solicitar ayuda, activar el sistema de emergencias mediante la línea 123 e iniciar las maniobras de reanimación, de acuerdo con la capacitación recibida.
      .col-lg-4.mt-4.mt-lg-0
        figure.m-0
          img(src="@/assets/curso/temas/t3/f2.png" alt="").w-100

    p.mt-4(data-aos="fade-down") Para realizar el procedimiento, se deben seguir estas acciones:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ol--cuadro.mb-0
            li
              .lista-ol--cuadro__vineta
                span 1
              | #[b Verificar la seguridad:] comprobar que el lugar no represente peligro para el lactante ni para quien brinda la atención.
            li
              .lista-ol--cuadro__vineta
                span 2
              | #[b Valorar la respuesta:] estimular suavemente al lactante y observar si responde mediante movimientos, sonidos o gestos.
            li
              .lista-ol--cuadro__vineta
                span 3
              | #[b Observar la respiración:] verificar si respira normalmente o solo jadea, sin prolongar innecesariamente la valoración.
            li
              .lista-ol--cuadro__vineta
                span 4
              | #[b Solicitar ayuda:] pedir apoyo a las personas cercanas y activar el sistema de emergencias mediante la línea 123.
            li
              .lista-ol--cuadro__vineta
                span 5
              | #[b Ubicar al lactante:] colocarlo boca arriba sobre una superficie firme y plana para facilitar las maniobras.
            li
              .lista-ol--cuadro__vineta
                span 6
              | #[b Iniciar las compresiones:] comprimir el centro del pecho, sobre el esternón, con el talón de una mano o mediante la técnica de los dos pulgares con las manos rodeando el tórax.
            li
              .lista-ol--cuadro__vineta
                span 7
              | #[b Aplicar la profundidad adecuada:] comprimir aproximadamente un tercio del diámetro anteroposterior del tórax, equivalente a unos 4 cm.
            li
              .lista-ol--cuadro__vineta
                span 8
              | #[b Mantener el ritmo:] realizar entre 100 y 120 compresiones por minuto, permitir la expansión completa del tórax y reducir al mínimo las interrupciones.
            li
              .lista-ol--cuadro__vineta
                span 9
              | #[b Combinar compresiones y ventilaciones:] realizar ciclos de 30 compresiones y 2 ventilaciones cuando participa un solo reanimador, o de 15 compresiones y 2 ventilaciones cuando intervienen dos reanimadores capacitados.
            li.mb-0
              .lista-ol--cuadro__vineta
                span 10
              | #[b Continuar las maniobras:] mantener la RCP hasta que el lactante muestre signos de respuesta, llegue el personal especializado, el entorno deje de ser seguro o quien brinda la atención no pueda continuar.

    .row.align-items-start.mt-4
      .col-auto.mb-3.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t3/ic1.svg" alt="" style="width: 84px")
      .col
        p(data-aos="fade-down") La aplicación ordenada de estas acciones contribuye a mantener la circulación y el aporte de oxígeno durante una emergencia. Las maniobras deben realizarse con precaución, sin ejercer una fuerza excesiva y conforme a los protocolos vigentes y la capacitación recibida.
        p.mb-0(data-aos="fade-down") Después de reconocer la técnica de RCP en lactantes, es necesario comprender cómo se adapta este procedimiento a la población infantil. En niñas y niños, la valoración, la profundidad de las compresiones y la técnica empleada deben ajustarse a su edad, tamaño y condiciones físicas, como se explica a continuación.

    Separador

    #t_3_2.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 3.2 RCP en población infantil

    .row.align-items-start
      .col-lg-3.mb-4.mb-lg-0
        figure.m-0
          img(src="@/assets/curso/temas/t3/f3.png" alt="").w-100
      .col-lg-9
        p(data-aos="fade-down") La reanimación cardiopulmonar (RCP) en la población infantil se aplica cuando la niña o el niño no responde y no respira normalmente o solo jadea. Su finalidad es mantener temporalmente la circulación sanguínea y el aporte de oxígeno a los órganos vitales mientras llega la atención especializada.
        .cajon.color1.p-4.mt-4(data-aos="fade-down")
          p Este procedimiento se realiza en niñas y niños desde un año hasta la aparición de signos de pubertad. Cuando estos signos están presentes, se aplican las técnicas de RCP correspondientes a las personas adultas.
          p.mb-0 Antes de iniciar las maniobras, se debe verificar la seguridad del entorno y valorar la respuesta y la respiración. Si la niña o el niño no responde y no respira normalmente, se debe solicitar ayuda, activar el sistema de emergencias mediante la línea 123 e iniciar la RCP, según la capacitación recibida.

    p.mt-4(data-aos="fade-down") Para realizar el procedimiento de manera organizada, se deben aplicar las siguientes acciones:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ol--cuadro.mb-0
            li
              .lista-ol--cuadro__vineta
                span 1
              | #[b Verificar la seguridad:] comprobar que el lugar no represente peligro para la niña, el niño ni para quien brinda la atención.
            li
              .lista-ol--cuadro__vineta
                span 2
              | #[b Valorar la respuesta:] estimular suavemente a la niña o al niño y observar si responde mediante movimientos, sonidos o gestos.
            li
              .lista-ol--cuadro__vineta
                span 3
              | #[b Observar la respiración:] verificar si respira normalmente o solo jadea, sin prolongar innecesariamente la valoración.
            li
              .lista-ol--cuadro__vineta
                span 4
              | #[b Solicitar ayuda:] pedir apoyo a las personas cercanas y activar el sistema de emergencias mediante la línea 123.
            li
              .lista-ol--cuadro__vineta
                span 5
              | #[b Ubicar a la niña o al niño:] colocarlo boca arriba sobre una superficie firme y plana para facilitar las maniobras.
            li
              .lista-ol--cuadro__vineta
                span 6
              | #[b Posicionar las manos:] ubicar el talón de una mano en el centro del pecho, sobre la mitad inferior del esternón. Según el tamaño de la niña o del niño, se puede utilizar una o ambas manos.
            li
              .lista-ol--cuadro__vineta
                span 7
              | #[b Aplicar las compresiones:] comprimir el tórax aproximadamente un tercio de su profundidad, equivalente a unos 5 cm.
            li
              .lista-ol--cuadro__vineta
                span 8
              | #[b Mantener el ritmo:] realizar entre 100 y 120 compresiones por minuto, permitir la expansión completa del tórax y reducir las interrupciones.
            li
              .lista-ol--cuadro__vineta
                span 9
              | #[b Combinar compresiones y ventilaciones:] realizar ciclos de 30 compresiones y 2 ventilaciones cuando participa un solo reanimador, o de 15 compresiones y 2 ventilaciones cuando intervienen dos reanimadores capacitados.
            li.mb-0
              .lista-ol--cuadro__vineta
                span 10
              | #[b Continuar las maniobras:] mantener la RCP hasta que la niña o el niño muestre signos de respuesta, llegue el personal especializado, el entorno deje de ser seguro o quien brinda la atención no pueda continuar.

    .row.justify-content-center.mt-4
      .col-lg-10
        .cajon.color1.p-4(data-aos="fade-down")
          p.mb-0 La aplicación ordenada de estas acciones contribuye a mantener la circulación sanguínea y el aporte de oxígeno durante la emergencia. Las maniobras deben adaptarse al tamaño y a las condiciones físicas de la niña o del niño, sin aplicar una fuerza excesiva y de acuerdo con la capacitación recibida.

    Separador

    #t_3_3.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 3.3 Obstrucción de la vía aérea por cuerpo extraño (OVACE)

    p(data-aos="fade-down") La obstrucción de la vía aérea por cuerpo extraño (OVACE) es una emergencia que ocurre cuando un alimento u objeto bloquea de manera parcial o total el paso del aire hacia los pulmones. En lactantes, niñas y niños, esta situación puede evolucionar rápidamente; por ello, es fundamental reconocer las señales de alerta y actuar de manera oportuna y segura.

    p(data-aos="fade-down") La obstrucción puede presentarse mientras se consumen alimentos o cuando se introducen objetos pequeños en la boca. El riesgo aumenta con alimentos duros, redondos o difíciles de masticar, así como con monedas, botones, piezas de juguetes y otros elementos que se encuentran al alcance de la población infantil.

    figure.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/temas/t3/ilus1.svg" alt="" style="width: 292px")

    h3.titulo-tercero.mt-5(data-aos="fade-down")
      i.fas.fa-house-medical
      span Reconocimiento de la obstrucción

    p(data-aos="fade-down") Las manifestaciones dependen de si el paso del aire está bloqueado de forma parcial o total:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ul--color.mb-0
            li
              i.fas.fa-heart
              span.mb-0 #[b Obstrucción parcial:] la niña o el niño puede toser con fuerza, emitir sonidos, respirar y responder. En este caso, se debe permitir que continúe tosiendo, observar su evolución y evitar maniobras innecesarias.
            li.mb-0
              i.fas.fa-heart
              span.mb-0 #[b Obstrucción total:] la niña o el niño no puede hablar, llorar, toser eficazmente ni respirar. También puede llevarse las manos al cuello, presentar coloración azulada alrededor de los labios o perder el conocimiento.

    p.mt-4(data-aos="fade-down") Reconocer el tipo de obstrucción permite seleccionar la actuación adecuada. No se deben introducir los dedos en la boca ni intentar retirar el objeto cuando no sea visible, ya que podría desplazarse hacia una zona más profunda.

    h3.titulo-tercero.mt-5(data-aos="fade-down")
      i.fas.fa-house-medical
      span Actuación ante una obstrucción en lactantes

    p(data-aos="fade-down") Si el lactante está consciente y presenta una obstrucción total, se deben aplicar las siguientes acciones:

    .row.mt-4
      .col-md-6.col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i4.svg" alt="" style="width: 60px")
          p.mb-0.mt-3 #[b Solicitar ayuda:] pedir apoyo y activar el sistema de emergencias mediante la línea 123.
      .col-md-6.col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i5.svg" alt="" style="width: 60px")
          p.mb-0.mt-3 #[b Ubicar al lactante:] colocarlo boca abajo sobre el antebrazo o el muslo, con la cabeza más baja que el pecho y sostenida de manera segura.
      .col-md-6.col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i6.svg" alt="" style="width: 60px")
          p.mb-0.mt-3 #[b Aplicar golpes en la espalda:] realizar cinco golpes firmes entre los omóplatos con el talón de la mano.
      .col-md-6.col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i7.svg" alt="" style="width: 60px")
          p.mb-0.mt-3 #[b Girar al lactante:] colocarlo boca arriba, manteniendo la cabeza más baja que el pecho.
      .col-md-6.col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i8.svg" alt="" style="width: 60px")
          p.mb-0.mt-3 #[b Realizar compresiones torácicas:] aplicar cinco compresiones en el centro del pecho, sobre el esternón.
      .col-md-6.col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure
            img(src="@/assets/curso/temas/t3/i9.svg" alt="" style="width: 60px")
          p.mb-0.mt-3 #[b Repetir la secuencia:] alternar cinco golpes en la espalda y cinco compresiones torácicas hasta que el objeto sea expulsado, el lactante respire o pierda la respuesta.

    p.mt-4(data-aos="fade-down") No se deben realizar compresiones abdominales en lactantes, debido al riesgo de causar lesiones en los órganos internos.

    h3.titulo-tercero.mt-5(data-aos="fade-down")
      i.fas.fa-house-medical
      span Actuación ante una obstrucción en niñas y niños

    p(data-aos="fade-down") Si la niña o el niño está consciente y no puede respirar, hablar, llorar o toser eficazmente, se deben aplicar estas acciones:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4.p-md-5(data-aos="fade-down")
          .row.align-items-center
            .col-lg-7.mb-4.mb-lg-0
              ul.lista-ul--color.mb-0
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
            .col-lg-5
              figure.m-0
                img(src="@/assets/curso/temas/t3/f4.png" alt="").w-100

    p.mt-4(data-aos="fade-down") Las maniobras deben ajustarse al tamaño y a las condiciones físicas de la niña o del niño, evitando aplicar una fuerza desproporcionada.

    .row.justify-content-center.mt-4
      .col-lg-10
        .cajon.color1.p-4(data-aos="fade-down")
          p.mb-0 Después de reconocer las acciones para atender una obstrucción de la vía aérea, es importante abordar el uso del desfibrilador externo automático como apoyo durante la reanimación cardiopulmonar. En el siguiente apartado, se explica su función y las principales recomendaciones para utilizarlo de manera segura en lactantes, niñas y niños.

    Separador

    #t_3_4.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 3.4 Uso del desfibrilador externo automático (DEA)

    .row.align-items-start
      .col-lg-8
        p(data-aos="fade-down") El desfibrilador externo automático (DEA) es un dispositivo portátil que analiza el ritmo cardíaco y determina si es necesario aplicar una descarga eléctrica. Su uso durante un paro cardiorrespiratorio complementa la reanimación cardiopulmonar (RCP), pero no reemplaza las compresiones ni las ventilaciones.
        .cajon.color1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 En lactantes, niñas y niños, el DEA debe utilizarse tan pronto como esté disponible. Para menores de ocho años, se emplean preferiblemente parches pediátricos o un sistema reductor de energía. Si estos elementos no están disponibles, puede utilizarse un DEA con parches para personas adultas, siguiendo las instrucciones del dispositivo.
      .col-lg-4.mt-4.mt-lg-0
        figure.m-0
          img(src="@/assets/curso/temas/t3/f5.png" alt="").w-100

    p.mt-4(data-aos="fade-down") Mientras una persona realiza la RCP, otra debe activar el sistema de emergencias mediante la línea 123 y buscar el DEA. Para utilizarlo de manera organizada y segura, se deben seguir estas acciones:

    //- Ocho pasos en el slider. El XD sólo dibuja las tres tarjetas de la ventana visible y
    //- sólo trae esos tres iconos: las cinco restantes van sin icono en vez de repetirlos.
    SlyderF.slyder--principios.mt-4(columnas="col-md-6 col-lg-4")
      .tarjeta.bg-4.r-20.p-4.h-100
        figure
          img(src="@/assets/curso/temas/t3/i10.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Encender el DEA
        p.text-center.mb-0 activar el dispositivo y escuchar atentamente las instrucciones visuales o de voz.
      .tarjeta.bg-4.r-20.p-4.h-100
        figure
          img(src="@/assets/curso/temas/t3/i11.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Descubrir el pecho
        p.text-center.mb-0 retirar las prendas que impidan la colocación de los parches y secar la piel si se encuentra húmeda.
      .tarjeta.bg-4.r-20.p-4.h-100
        figure
          img(src="@/assets/curso/temas/t3/i12.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Seleccionar los parches
        p.text-center.mb-0 utilizar parches pediátricos o un sistema reductor de energía cuando estén disponibles para lactantes y menores de ocho años.
      .tarjeta.bg-4.r-20.p-4.h-100
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Colocar los parches
        p.text-center.mb-0 adherirlos sobre el pecho desnudo, de acuerdo con las imágenes indicadas en el dispositivo. Si los parches pueden tocarse entre sí, se debe colocar uno en el centro del pecho y otro en la espalda.
      .tarjeta.bg-4.r-20.p-4.h-100
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Permitir el análisis
        p.text-center.mb-0 suspender momentáneamente las compresiones y verificar que ninguna persona toque al lactante, la niña o el niño mientras el DEA analiza el ritmo cardíaco.
      .tarjeta.bg-4.r-20.p-4.h-100
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Aplicar la descarga
        p.text-center.mb-0 si el dispositivo la recomienda, comprobar que nadie esté en contacto con la persona y seguir la indicación para administrarla.
      .tarjeta.bg-4.r-20.p-4.h-100
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Reanudar la RCP
        p.text-center.mb-0 reiniciar inmediatamente las compresiones y las ventilaciones después de la descarga o cuando el DEA indique que esta no es necesaria.
      .tarjeta.bg-4.r-20.p-4.h-100
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b Seguir las instrucciones
        p.text-center.mb-0 continuar la RCP y atender las indicaciones del dispositivo hasta que se evidencien signos de respuesta o llegue el personal especializado.

    p.mt-5(data-aos="fade-down") Durante el uso del DEA, se deben tener en cuenta las siguientes precauciones:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4.p-md-5(data-aos="fade-down")
          .row.align-items-center
            .col-lg-8.mb-4.mb-lg-0
              //- Las precauciones NO van en negrilla: el DOCX no las lleva, aunque el XD las pinte así.
              ul.lista-ol--cuadro.mb-0
                li
                  .lista-ol--cuadro__vineta
                    span A
                  | No colocar los parches sobre ropa, piel mojada ni objetos metálicos.
                li
                  .lista-ol--cuadro__vineta
                    span B
                  | No permitir que los parches se toquen o se superpongan.
                li
                  .lista-ol--cuadro__vineta
                    span C
                  | No tocar al lactante, la niña o el niño durante el análisis ni al aplicar la descarga.
                li
                  .lista-ol--cuadro__vineta
                    span D
                  | No retirar los parches ni apagar el dispositivo mientras continúa la atención.
                li.mb-0
                  .lista-ol--cuadro__vineta
                    span E
                  | Reducir al mínimo las interrupciones de las compresiones torácicas.
            .col-lg-4
              figure.m-0
                img(src="@/assets/curso/temas/t3/ilus2.svg" alt="" style="width: 222px").m-auto

    .row.align-items-start.mt-4
      .col-auto.mb-3.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t3/ic2.svg" alt="" style="width: 84px")
      .col
        p(data-aos="fade-down") El uso oportuno del DEA, combinado con una RCP de calidad, fortalece la respuesta ante un paro cardiorrespiratorio. Mantener la calma, seguir las instrucciones del dispositivo y continuar las maniobras contribuye a brindar una atención inicial segura mientras llega el personal especializado.
        p.mb-0(data-aos="fade-down") Después de reconocer las acciones de soporte vital básico, es necesario abordar otras situaciones que también pueden afectar la salud y la integridad de lactantes, niñas y niños. En el siguiente apartado, se presentan las medidas de atención inicial ante lesiones, traumatismos y situaciones que requieren una movilización segura.

</template>

<script>
export default {
  name: 'Tema3',
}
</script>

