<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 6
      h1 Comunicación, emergencias y cadena de custodia

    //- Ficha: texto a col-9 · foto (1122,316) 292x271 -> col-3 · nota (186,437) 916x150 #F4EDFE r=10
    //- con el icono (215,470) 84x84 a la IZQUIERDA del texto (324,467)
    .row.align-items-start.mt-4
      .col-lg-9
        p(data-aos="fade-down") La atención inicial de una emergencia en la primera infancia también requiere acompañar emocionalmente a la niña o al niño, comunicar la situación con claridad y coordinar oportunamente la intervención de los servicios especializados. Estas acciones favorecen una respuesta organizada y permiten mantener informados a los familiares, cuidadores y profesionales que participan en la atención.
        .bg-2.r-10.p-4.mt-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t6/ic1.svg" alt="" style="width: 84px")
            .col
              p.mb-0 Cuando el evento puede tener implicaciones legales, también es necesario proteger la escena, evitar la manipulación de objetos y registrar únicamente la información observada. Estas actuaciones deben realizarse sin retrasar los primeros auxilios, debido a que la protección de la vida y la salud de la persona afectada constituye la prioridad.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f2.png" alt="" style="width: 292px").m-auto

    p.mt-4(data-aos="fade-down") Para comprender la relación entre estas acciones, se deben considerar los siguientes aspectos:

    //- Ficha: tres tarjetas visibles (290/637/983, 705) 327x400 #8EC5FC r=20 con su círculo #F6F0E8
    //- de 128 dentro, y chevrones verdes a los lados -> es un `SlyderF`. El DI lista CINCO aspectos:
    //- las dos que no se ven están en el pasteboard, en (6195,-10995) y (6547,-10995).
    SlyderF.slyder--principios.mt-4(columnas="col-md-6 col-lg-4")
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 400px")
        figure
          img(src="@/assets/curso/temas/t6/i1.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2
          b Acompañamiento emocional
        p.text-center.mb-0 Ayuda a disminuir el miedo, la angustia y la confusión que puede experimentar la niña o el niño.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 400px")
        figure
          img(src="@/assets/curso/temas/t6/i2.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2
          b Comunicación durante la atención
        p.text-center.mb-0 Permite explicar las acciones mediante palabras sencillas, frases breves y un tono tranquilo.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 400px")
        figure
          img(src="@/assets/curso/temas/t6/i3.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2
          b Activación del sistema de emergencias
        p.text-center.mb-0 Comunicarse con la línea de emergencias 123 para reportar con claridad la condición de la niña o del niño y su ubicación exacta.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 400px")
        figure
          img(src="@/assets/curso/temas/t6/i4.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2
          b Protección de la información
        p.text-center.mb-0 Evita divulgar datos personales, imágenes o detalles que puedan afectar la intimidad de la persona involucrada.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 400px")
        figure
          img(src="@/assets/curso/temas/t6/i5.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2
          b Preservación de la escena
        p.text-center.mb-0 Contribuye a evitar la alteración de objetos, rastros o elementos relacionados con una posible investigación.

    //- Ficha: foto (186,1230) 292x272 -> col-3 · texto y nota (498,1362) 916x140 #DBC2FA r=10 -> col-9
    .row.align-items-start.mt-5
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f3.png" alt="" style="width: 292px").m-auto
      .col-lg-9
        p(data-aos="fade-down") El desarrollo articulado de estos aspectos fortalece la actuación del primer respondiente. No obstante, cada acción debe aplicarse de acuerdo con las características del evento, el estado de la niña o del niño y las indicaciones de las autoridades competentes.
        .bg-6.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 La comunicación clara, el acompañamiento respetuoso y la coordinación oportuna complementan la atención física y contribuyen a proteger integralmente a la niña o al niño.

    p.mt-4(data-aos="fade-down") A continuación, se aborda el acompañamiento emocional durante una emergencia y la comunicación con la persona afectada, sus familiares y cuidadores.

    Separador

    #t_6_1.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 6.1 Primeros auxilios psicológicos y comunicación

    //- Ficha: texto a col-8 · foto (1018,1793) 396x211 -> col-4
    .row.align-items-start.mt-4
      .col-lg-8
        p(data-aos="fade-down") Una emergencia puede generar miedo, llanto, confusión, silencio o dificultad para seguir indicaciones. Los primeros auxilios psicológicos comprenden acciones inmediatas de apoyo que buscan brindar seguridad, disminuir la angustia y favorecer una respuesta emocional más estable mientras se desarrolla la atención.
        p(data-aos="fade-down") La reacción puede variar según la edad, el desarrollo, las experiencias previas y las características del evento. Por esta razón, se debe observar el comportamiento, respetar las manifestaciones emocionales y adaptar la comunicación a la capacidad de comprensión de cada niña o niño.
        p.mb-0(data-aos="fade-down") El acompañamiento inicial debe orientarse mediante las siguientes acciones:
      .col-lg-4.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f4.png" alt="" style="width: 396px").m-auto

    //- Ficha: rejilla de seis tarjetas (186/602/1018, 2034 y 2284) 396x230 #FFE6DE r=10, con su
    //- icono #8EC5FC de 60 dentro
    .row.mt-4
      .col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure.mb-3
            img(src="@/assets/curso/temas/t6/g1.svg" alt="" style="width: 60px")
          p.mb-0 #[b Acercarse de manera tranquila:] ubicarse a una distancia apropiada, presentarse y evitar movimientos que puedan generar mayor temor.
      .col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure.mb-3
            img(src="@/assets/curso/temas/t6/g2.svg" alt="" style="width: 60px")
          p.mb-0 #[b Escuchar con atención:] permitir que la niña o el niño exprese lo ocurrido, sin presionarlo, interrumpirlo ni formular preguntas repetitivas.
      .col-lg-4.mb-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure.mb-3
            img(src="@/assets/curso/temas/t6/g3.svg" alt="" style="width: 60px")
          p.mb-0 #[b Reconocer sus emociones:] aceptar el miedo, la tristeza o la confusión sin minimizar estas manifestaciones ni emitir juicios.
      .col-lg-4.mb-4.mb-lg-0(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure.mb-3
            img(src="@/assets/curso/temas/t6/g4.svg" alt="" style="width: 60px")
          p.mb-0 #[b Explicar las acciones:] informar de manera progresiva qué se va a realizar y emplear palabras comprensibles para su edad.
      .col-lg-4.mb-4.mb-lg-0(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure.mb-3
            img(src="@/assets/curso/temas/t6/g5.svg" alt="" style="width: 60px")
          p.mb-0 #[b Brindar seguridad:] permanecer cerca, mantener un tono sereno y comunicar que se está gestionando la ayuda necesaria.
      .col-lg-4(data-aos="fade-down")
        .bg-1.r-10.p-4.h-100
          figure.mb-3
            img(src="@/assets/curso/temas/t6/g6.svg" alt="" style="width: 60px")
          p.mb-0 #[b Favorecer el contacto protector:] facilitar el acompañamiento de una persona cuidadora conocida, siempre que su presencia sea segura y beneficiosa.

    p.mt-5(data-aos="fade-down") Estas acciones permiten establecer un entorno de confianza durante la atención. No se deben hacer promesas que no puedan cumplirse, exigir que la persona relate el evento ni utilizar expresiones que aumenten su preocupación.

    //- Ficha: pastilla (186,2647) 396x50 #FFC0AC r=25 con el icono `house-medical-solid-full`
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Comunicación con la niña o el niño

    p.mt-4(data-aos="fade-down") La comunicación debe adaptarse a la edad, el estado emocional y la capacidad de respuesta. Para facilitar la comprensión, se recomienda:

    //- Ficha: caja (186,2776) 916x320 #F4EDFE con la lista A-F -> col-9 · foto (1122,2776) 292x394 -> col-3
    .row.align-items-start.mt-4
      .col-lg-9
        .bg-2.p-4(data-aos="fade-down")
          ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
            li
              span.lista-ol--cuadro__vineta A
              |  Utilizar frases breves y palabras conocidas.
            li
              span.lista-ol--cuadro__vineta B
              |  Dar una indicación a la vez.
            li
              span.lista-ol--cuadro__vineta C
              |  Mantener un tono de voz calmado.
            li
              span.lista-ol--cuadro__vineta D
              |  Comprobar si la información fue comprendida.
            li
              span.lista-ol--cuadro__vineta E
              |  Evitar explicaciones alarmantes o innecesarias.
            li.mb-0
              span.lista-ol--cuadro__vineta F
              |  Respetar los silencios y el tiempo necesario para responder.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f5.png" alt="" style="width: 292px").m-auto

    p.mt-4(data-aos="fade-down") La comunicación no verbal también transmite seguridad. La postura corporal, la expresión facial, el contacto visual respetuoso y la distancia adecuada deben ser coherentes con el mensaje expresado.

    //- Ficha: pastilla (186,3214) 471x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Comunicación con familiares o cuidadores

    p.mt-4(data-aos="fade-down") Los familiares o cuidadores deben recibir información objetiva sobre el estado observado, las acciones realizadas y la ayuda solicitada. La comunicación debe evitar diagnósticos, afirmaciones sin confirmar o señalamientos sobre posibles responsabilidades. Para mantener una comunicación clara y respetuosa, es importante:

    //- Ficha: caja (290,3367) 1020x319 #DDEEFE con la lista A-F y la ilustración (914,3394) dentro
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-lg-8
              ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
                li
                  span.lista-ol--cuadro__vineta A
                  |  Informar qué ocurrió y en qué momento.
                li
                  span.lista-ol--cuadro__vineta B
                  |  Describir las manifestaciones observadas.
                li
                  span.lista-ol--cuadro__vineta C
                  |  Explicar las medidas de atención aplicadas.
                li
                  span.lista-ol--cuadro__vineta D
                  |  Comunicar si se solicitó ayuda especializada.
                li
                  span.lista-ol--cuadro__vineta E
                  |  Indicar las recomendaciones recibidas.
                li.mb-0
                  span.lista-ol--cuadro__vineta F
                  |  Evitar divulgar información frente a personas ajenas al evento.
            .col-lg-4.d-none.d-lg-block
              figure.m-0
                img(src="@/assets/curso/temas/t6/ilus2.svg" alt="").w-100

    p.mt-4(data-aos="fade-down") Una comunicación respetuosa ayuda a disminuir la incertidumbre y facilita la participación de la familia o del cuidador en la continuidad de la atención.

    //- Ficha: caja (290,3749) 1020x160 #F4EDFE con el icono (330,3787) 84x84 a la izquierda
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t6/ic2.svg" alt="" style="width: 84px")
            .col
              p.mb-0 Para fortalecer la comprensión de estos contenidos, se presenta un recurso de audio sobre el acompañamiento emocional del niño o la niña durante una emergencia. En este se explica en qué consisten los primeros auxilios psicológicos, la importancia de la calma y la palabra como herramienta del primer respondiente, y la forma de acompañar al menor sin generar más angustia mientras llega la ayuda especializada.

    //- Ficha: ilustración (290,3940) 1020x227 y debajo el panel (290,4166) 1020x160 #8EC5FC con la
    //- tarjeta blanca 972x110 `r=20` y la barra verde 930x60 `r=30`: es el `TarjetaAudio` del kit.
    //- ⚠️ No hay audio en ninguna fuente: el DI sólo da el NOMBRE del guion. Va un MP3 mudo.
    .row.justify-content-center.mt-4
      .col-lg-10
        figure.m-0
          img(src="@/assets/curso/temas/t6/f6.png" alt="").w-100
        .bg-4.p-4
          TarjetaAudio.tarjeta-audio--podcast(
            texto="Pódcast"
            tiempo
            :audio="require_src('@/assets/curso/temas/t6/audios/63720048_CF02_Guion_podcast.mp3')")

    p.mt-4(data-aos="fade-down") El acompañamiento emocional oportuno contribuye a reducir el impacto de la emergencia en la niña o el niño y facilita la atención física necesaria. Sin embargo, esta contención no reemplaza la atención especializada; por ello, a continuación, se presenta la articulación con el sistema de emergencias y su importancia para garantizar la continuidad del cuidado.

    Separador

    #t_6_2.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 6.2 Articulación con el sistema de emergencias

    //- Ficha: texto a col-8 · foto (1018,4666) 396x187 -> col-4
    .row.align-items-start.mt-4
      .col-lg-8
        p(data-aos="fade-down") La articulación con el sistema de emergencias permite solicitar ayuda especializada y garantizar la continuidad de la atención cuando una situación supera la capacidad de actuación del primer respondiente. Este proceso requiere identificar la necesidad de apoyo, comunicarse oportunamente con la línea de emergencias y proporcionar información clara sobre el estado de la niña o del niño.
        p.mb-0(data-aos="fade-down") En Colombia, la activación debe realizarse mediante la línea de emergencias 123. Durante la llamada, es importante mantener la calma, responder las preguntas del operador y seguir las indicaciones recibidas, sin interrumpir la comunicación hasta que se autorice finalizarla.
      .col-lg-4.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f7.png" alt="" style="width: 396px").m-auto

    //- Ficha: pastilla (186,4903) 446x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Activación del sistema de emergencias

    p.mt-4(data-aos="fade-down") Para realizar una activación organizada y facilitar la respuesta del personal especializado, se deben considerar las siguientes acciones:

    //- Ficha: caja (291,5023) 1020x410 #F4EDFE con la lista numerada 1-8 (viñetas en x=333)
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4(data-aos="fade-down")
          ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
            li
              span.lista-ol--cuadro__vineta 1
              |  #[b Reconocer la emergencia:] identificar los signos de alarma o las condiciones que requieren atención especializada.
            li
              span.lista-ol--cuadro__vineta 2
              |  #[b Comunicarse con la línea 123:] reportar con claridad la condición de la niña o del niño y su ubicación exacta.
            li
              span.lista-ol--cuadro__vineta 3
              |  #[b Informar la ubicación:] indicar el municipio, el barrio, la dirección, un punto de referencia y las condiciones de acceso al lugar.
            li
              span.lista-ol--cuadro__vineta 4
              |  #[b Describir lo ocurrido:] explicar brevemente el evento, el número de personas afectadas y las manifestaciones observadas.
            li
              span.lista-ol--cuadro__vineta 5
              |  #[b Comunicar las acciones realizadas:] informar los primeros auxilios brindados y los cambios identificados durante la atención.
            li
              span.lista-ol--cuadro__vineta 6
              |  #[b Seguir las indicaciones:] escuchar al operador y aplicar las orientaciones recibidas de acuerdo con las condiciones de seguridad.
            li
              span.lista-ol--cuadro__vineta 7
              |  #[b Facilitar el acceso:] despejar el recorrido y, cuando sea posible, asignar a una persona para orientar al equipo de emergencias.
            li.mb-0
              span.lista-ol--cuadro__vineta 8
              |  #[b Entregar la información:] comunicar al personal especializado la evolución de la niña o del niño y las acciones realizadas.

    p.mt-4(data-aos="fade-down") El cumplimiento ordenado de estas acciones facilita la comprensión del evento y permite que los organismos de respuesta determinen los recursos necesarios. La información suministrada debe ser concreta, verificable y limitada a los hechos observados.

    //- Ficha: pastilla (186,5566) 416x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Información que debe comunicarse

    p.mt-4(data-aos="fade-down") Durante la llamada, se deben proporcionar los datos esenciales para orientar la respuesta:

    //- Ficha: tres tarjetas (290/637/983, 5695) 327x347 #8EC5FC r=20 con chevrones -> `SlyderF`.
    //- El XD pone detrás una banda de 1328x254, pero envolver el slider en un contenedor con
    //- `margin-inline` negativo le ensancha el `__main` y asoman las tarjetas vecinas por los dos
    //- lados. Va como en los temas 1 y 3: al nivel de la tarjeta. La banda queda en los pendientes.
    SlyderF.slyder--principios.mt-4(columnas="col-md-6 col-lg-4")
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 347px")
        figure
          img(src="@/assets/curso/temas/t6/i6.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2
          b Situación presentada
        p.text-center.mb-0 Qué ocurrió y cómo sucedió, si esta información se conoce.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 347px")
        figure
          img(src="@/assets/curso/temas/t6/i7.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2
          b Ubicación exacta
        p.text-center.mb-0 Dirección, municipio, barrio, punto de referencia y condiciones de acceso.
      .tarjeta.bg-4.r-20.p-4.h-100(style="min-height: 347px")
        figure
          img(src="@/assets/curso/temas/t6/i8.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2
          b Persona afectada
        p.text-center.mb-0 Edad aproximada y estado actual de la niña o del niño.

    p.mt-4(data-aos="fade-down") Estos datos permiten que el operador comprenda la situación y proporcione instrucciones apropiadas. Si alguna información se desconoce, debe indicarse con claridad, sin realizar suposiciones ni emitir diagnósticos.

    //- Ficha: badge (765,6145) 70x70 #8EC5FC r=42 sobre la caja (290,6180) 1020x140 #DBC2FA r=10
    .row.justify-content-center.mt-5
      .col-lg-10
        .tarjeta--badge-arriba.bg-6(data-aos="fade-down")
          figure
            img(src="@/assets/curso/temas/t6/badge.svg" alt="")
          p.text-center.mb-0 Durante la llamada a la línea de emergencias 123, se debe informar qué ocurrió, dónde sucedió, cómo se encuentra la niña o el niño y cuáles acciones se han realizado.

    //- Ficha: pastilla (186,6380) 396x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Actuación mientras llega la ayuda

    p.mt-4(data-aos="fade-down") La atención no termina después de realizar la llamada. Mientras llega el personal especializado, el primer respondiente debe continuar con las siguientes acciones:

    //- Ficha: caja (290,6509) 1020x247 #DDEEFE con la lista y la ilustración (1018,6531) 272x204 dentro
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-lg-8
              ul.lista-ul.lista-ul--compacta.mb-0
                li
                  i.fas.fa-heart
                  span Mantener la vigilancia sobre la respiración, el estado de conciencia y la condición general.
                li
                  i.fas.fa-heart
                  span Aplicar las indicaciones proporcionadas por el operador de emergencias.
                li
                  i.fas.fa-heart
                  span Evitar movilizar a la niña o al niño, salvo que permanezca expuesto a un peligro inmediato.
                li
                  i.fas.fa-heart
                  span Mantener despejado y seguro el lugar de atención.
                li
                  i.fas.fa-heart
                  span Informar cualquier cambio significativo mediante la línea de emergencias.
                li.mb-0
                  i.fas.fa-heart
                  span.mb-0 Preparar la información necesaria para entregarla al personal especializado.
            .col-lg-4.d-none.d-lg-block
              figure.m-0
                img(src="@/assets/curso/temas/t6/ilus3.svg" alt="").w-100

    p.mt-4(data-aos="fade-down") La vigilancia continua permite reconocer cambios que puedan requerir nuevas acciones. En todo momento, se debe conservar la calma, proteger a la niña o al niño y evitar procedimientos que no hayan sido indicados por personal capacitado.

    //- Ficha: pastilla (186,6889) 396x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Entrega al personal especializado

    p.mt-4(data-aos="fade-down") Cuando llegue el equipo de emergencias, se debe realizar una entrega clara y ordenada de la información. Para ello, se debe comunicar:

    //- Ficha: lista A-F con divisores #AFAFAF de 604 de ancho (x=291) -> col-6 · foto (914,7010)
    //- 396x304 -> col-4
    .row.align-items-center.justify-content-center.mt-4
      .col-lg-6
        ol.lista-ol--cuadro.lista-numerada--clara.mb-0(data-aos="fade-down")
          li
            span.lista-ol--cuadro__vineta A
            |  Qué ocurrió y a qué hora aproximadamente.
          li
            span.lista-ol--cuadro__vineta B
            |  Cuáles manifestaciones se observaron inicialmente.
          li
            span.lista-ol--cuadro__vineta C
            |  Cómo evolucionó el estado de la niña o del niño.
          li
            span.lista-ol--cuadro__vineta D
            |  Qué primeros auxilios se realizaron.
          li
            span.lista-ol--cuadro__vineta E
            |  Qué indicaciones proporcionó el operador de la línea 123.
          li.mb-0
            span.lista-ol--cuadro__vineta F
            |  Si existen antecedentes relevantes informados por la familia o el cuidador.
      .col-lg-4.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f8.png" alt="" style="width: 396px").m-auto

    //- Ficha: foto (186,7362) 396x227 -> col-4 · texto y nota (602,7460) 812x130 #DBC2FA r=10 -> col-8
    .row.align-items-start.mt-5
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f9.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p(data-aos="fade-down") La entrega de esta información favorece la continuidad del cuidado y evita la pérdida de datos importantes. Una vez que el personal especializado asuma la atención, se deben seguir sus indicaciones y evitar interferir en los procedimientos.
        .bg-6.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 La articulación con el sistema de emergencias integra la solicitud de ayuda, la comunicación precisa, la vigilancia y la entrega responsable de la información. Cuando el evento también puede tener implicaciones legales, se deben proteger el lugar, los elementos relacionados y la intimidad de la niña o del niño, aspectos que se abordan en el siguiente numeral.

    Separador

    #t_6_3.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 6.3 Cadena de custodia

    //- Ficha: texto a col-9 · foto (1122,7832) 292x247 -> col-3 · nota (186,7929) 916x150 #DDEEFE
    .row.align-items-start.mt-4
      .col-lg-9
        p(data-aos="fade-down") Cuando una emergencia se relaciona con un accidente grave, una posible situación de violencia u otro hecho que requiera investigación, se debe proteger el lugar y evitar alteraciones innecesarias. Estas acciones contribuyen a conservar la información y los elementos que posteriormente pueden ser examinados por las autoridades competentes.
        //- (187,7929) lleva la pestaña de 25x8 #8EC5FC: es el ÚNICO `.cajon` del tema (check 4b)
        .cajon.color1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 La cadena de custodia es un procedimiento técnico que permite identificar, conservar, trasladar y entregar los elementos materiales probatorios y la evidencia física. Su aplicación corresponde a las autoridades y al personal legalmente facultado. Por tanto, el primer respondiente debe brindar la atención inicial, proteger el lugar y comunicar objetivamente lo observado, sin asumir funciones investigativas.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f10.png" alt="" style="width: 292px").m-auto

    //- Ficha: pastilla (186,8139) 353x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Prioridad durante la atención

    p.mt-4(data-aos="fade-down") La protección de la vida y la salud de la niña o del niño siempre es prioritaria. Si para brindar los primeros auxilios es indispensable ingresar al lugar, mover un objeto o modificar alguna condición del entorno, se debe realizar únicamente la acción necesaria e informar posteriormente a la autoridad.

    //- Ficha: pastilla (186,8312) 427x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Actuaciones del primer respondiente

    p.mt-4(data-aos="fade-down") Para proteger el lugar y apoyar la intervención de las autoridades, se deben aplicar las siguientes acciones:

    //- Ficha: caja (291,8441) 1020x485 #F4EDFE con la lista numerada 1-8 (viñetas en x=333)
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4(data-aos="fade-down")
          ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
            li
              span.lista-ol--cuadro__vineta 1
              |  #[b Verificar la seguridad:] identificar los riesgos para la niña, el niño y las demás personas presentes.
            li
              span.lista-ol--cuadro__vineta 2
              |  #[b Activar el sistema de emergencias:] comunicarse con la línea de emergencias 123 para reportar con claridad la condición de la niña o del niño y su ubicación exacta.
            li
              span.lista-ol--cuadro__vineta 3
              |  #[b Restringir el acceso:] evitar, cuando sea seguro, el ingreso de personas ajenas al evento.
            li
              span.lista-ol--cuadro__vineta 4
              |  #[b Conservar el lugar:] procurar que los objetos permanezcan en la posición y el estado en que fueron encontrados.
            li
              span.lista-ol--cuadro__vineta 5
              |  #[b Evitar manipulaciones:] no mover, limpiar, recoger, lavar, desechar ni trasladar objetos relacionados con el evento.
            li
              span.lista-ol--cuadro__vineta 6
              |  #[b Registrar los hechos:] anotar la fecha, la hora aproximada, el lugar, las condiciones observadas, los primeros auxilios brindados y las modificaciones realizadas.
            li
              span.lista-ol--cuadro__vineta 7
              |  #[b Proteger la intimidad:] impedir la toma o divulgación de fotografías, videos, audios y datos personales.
            li.mb-0
              span.lista-ol--cuadro__vineta 8
              |  #[b Entregar la información:] comunicar al personal especializado las actuaciones realizadas y los cambios indispensables efectuados durante la atención.

    p.mt-4(data-aos="fade-down") Estas acciones permiten apoyar la protección de la escena sin asumir procedimientos propios de las autoridades. El primer respondiente no debe recolectar, embalar, rotular ni trasladar posibles evidencias, salvo que reciba una instrucción expresa de la autoridad competente.

    //- Ficha: pastilla (186,9063) 325x50 #FFC0AC r=25
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Manejo de la información

    //- Ficha: foto (186,9143) 396x265 -> col-4 · nota (602,9143) 812x265 #FFE6DE r=10 con el icono
    //- (638,9179) 84x84 ENCIMA del texto (638,9293)
    .row.align-items-start.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t6/f11.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        .bg-1.r-10.p-4(data-aos="fade-down")
          figure.mb-3
            img(src="@/assets/curso/temas/t6/ic3.svg" alt="" style="width: 84px")
          p.mb-0 El registro debe limitarse a hechos observables, sin incluir acusaciones, interpretaciones ni conclusiones personales. Si la niña o el niño expresa espontáneamente información sobre lo ocurrido, sus palabras deben registrarse con fidelidad, sin completar el relato ni formular preguntas que sugieran respuestas.

    p.mt-4(data-aos="fade-down") La información debe compartirse únicamente con el personal de salud, los familiares o cuidadores responsables y las autoridades facultadas. No se deben divulgar nombres, imágenes ni detalles del evento mediante redes sociales u otros medios. Cuando existan indicios de violencia, maltrato o abuso, la situación debe informarse inmediatamente a las autoridades competentes.

    //- Ficha: caja (291,9532) 1019x150 #B8F4CE con la ilustración (324,9570), el texto en x=424 y el
    //- botón (1146,9585) 125x44 #16D95E. La URL del manual SÍ está en el DI, no se inventa.
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-5.r-10.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure.m-0
                img(src="@/assets/curso/temas/t6/ilus1.svg" alt="" style="width: 110px")
            .col-lg
              p.mb-1
                b Manual del Sistema de Cadena de Custodia
              p.mb-0 Para ampliar los conocimientos sobre los procedimientos relacionados con la protección de la escena y la cadena de custodia, se recomienda consultar el manual de la Fiscalía General de la Nación, disponible en el siguiente enlace.
            .col-lg-auto.mt-3.mt-lg-0
              a.boton.color-acento-botones(href="https://safgncacportalwebprod01.blob.core.windows.net/media-portalweb-prd/MANUAL-DEL-SISTEMA-DE-CADENA-DE-CUSTODIA.pdf" target="_blank")
                span Descargar
                i.fas.fa-file-arrow-down

    p.mt-5(data-aos="fade-down") La protección de la escena, el registro objetivo y el manejo reservado de la información contribuyen a preservar los elementos relacionados con el evento y a garantizar los derechos de la niña o del niño. La actuación del primer respondiente debe centrarse en priorizar la vida, evitar alteraciones innecesarias y facilitar la intervención de las entidades responsables.

    p.mb-0(data-aos="fade-down") Al finalizar este componente formativo, se reconoce que actuar ante una emergencia en la primera infancia requiere conocimientos, calma, responsabilidad y sensibilidad. Cada acción oportuna contribuye a proteger la vida, brindar un acompañamiento respetuoso y facilitar la atención especializada de la niña o del niño.

</template>

<script>
export default {
  name: 'Tema6',
}
</script>
