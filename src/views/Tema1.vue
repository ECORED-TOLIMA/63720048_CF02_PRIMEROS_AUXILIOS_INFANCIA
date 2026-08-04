<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 1
      h1 Anatomía y fisiología básica

    //- Composición del XD: foto (186,316) 614x339 al ras del borde izquierdo, panel #8EC5FC
    //- (495,316) 919x339 y caja blanca (685,360) 685x250 montada sobre las dos.
    .row.g-0.mt-4(data-aos="fade-down")
      .col-lg-6
        figure.m-0.h-100
          img.w-100.h-100.object-fit-cover(src="@/assets/curso/temas/t1/f1.png" alt="")
      .col-lg-6.bg-4.d-flex.align-items-center
        .bg-white.p-4.caja-sobre-panel
          p.mb-0 La anatomía y la fisiología constituyen la base para comprender el funcionamiento del cuerpo humano y su relación con la atención de emergencias. La anatomía estudia las estructuras corporales, mientras que la fisiología explica el funcionamiento de los órganos y sistemas (Tortora y Derrickson, 2021). En la primera infancia, este conocimiento adquiere especial importancia debido a las características propias del desarrollo, como la mayor frecuencia respiratoria y cardíaca, el menor tamaño de las vías aéreas y el crecimiento continuo de las estructuras corporales. Estas condiciones requieren una actuación cuidadosa y adaptada a las necesidades de la población infantil.

    p.mt-4(data-aos="fade-down") Los sistemas corporales actúan de manera coordinada para mantener la vida, proteger el organismo y permitir el movimiento. Su reconocimiento facilita la valoración inicial y la identificación de alteraciones durante una emergencia. Para comprender sus funciones principales, se describen los siguientes sistemas:

    //- SIN `.h-100`: `.tarjeta--icono-arriba` ya iguala los altos con `height: calc(100% - 75px)`,
    //- que descuenta los 75 px que el círculo del icono saca por arriba. La utilidad de Bootstrap
    //- es `height: 100% !important` y pisa ese calc, así que la tarjeta acaba midiendo la columna
    //- ENTERA más los 75 px de margen y se sale 75 px por abajo, encima del bloque siguiente.
    .row.mt-5.bg-fondo-t1-sistemas
      .col-lg-3.mb-4.mb-lg-0(data-aos="fade-down")
        .tarjeta.bg-4.r-20.tarjeta--icono-arriba
          figure
            img(src="@/assets/curso/temas/t1/i1.svg" alt="")
          h4.text-center Sistema circulatorio
          p.text-center.mb-0 Transporta la sangre, el oxígeno y los nutrientes por todo el organismo. Su reconocimiento permite valorar el pulso e identificar alteraciones de la circulación.
      .col-lg-3.mb-4.mb-lg-0(data-aos="fade-down")
        .tarjeta.bg-4.r-20.tarjeta--icono-arriba
          figure
            img(src="@/assets/curso/temas/t1/i2.svg" alt="")
          h4.text-center Sistema respiratorio
          p.text-center.mb-0 Permite el intercambio de oxígeno y dióxido de carbono. Su funcionamiento orienta la identificación de dificultades respiratorias o de una obstrucción de la vía aérea.
      .col-lg-3.mb-4.mb-lg-0(data-aos="fade-down")
        .tarjeta.bg-4.r-20.tarjeta--icono-arriba
          figure
            img(src="@/assets/curso/temas/t1/i3.svg" alt="")
          h4.text-center Sistema tegumentario
          p.text-center.mb-0 Protege el cuerpo mediante la piel y contribuye a regular la temperatura. Su valoración permite identificar heridas, quemaduras y signos de infección.
      .col-lg-3(data-aos="fade-down")
        .tarjeta.bg-4.r-20.tarjeta--icono-arriba
          figure
            img(src="@/assets/curso/temas/t1/i4.svg" alt="")
          h4.text-center Sistema musculoesquelético
          p.text-center.mb-0 Brinda soporte al cuerpo y permite el movimiento. Su reconocimiento facilita la identificación de fracturas, esguinces y luxaciones.

    //- El bloque del XD va inset: la nota ocupa (290,1351) 708x150 y la foto (1018,1240) 292x261,
    //- o sea 1020 px centrados en los 1228 útiles.
    .row.justify-content-center.mt-5
      .col-lg-10
        .row.align-items-start.justify-content-between
          .col-lg-8
            p(data-aos="fade-down") La comprensión integrada de estos sistemas favorece una valoración inicial adecuada, la identificación de riesgos y la aplicación segura de las técnicas de primeros auxilios. En la primera infancia, una intervención oportuna puede contribuir favorablemente a la evolución de la persona afectada (Ministerio de Salud y Protección Social, 2018).
            .bg-1.p-4.mt-4(data-aos="fade-down")
              p.mb-0 Para valorar adecuadamente una emergencia, es necesario reconocer cómo actúan los sistemas corporales y qué signos pueden indicar una alteración en su funcionamiento. Este proceso comienza con el sistema circulatorio, cuya evaluación permite identificar posibles riesgos para la vida.
          .col-auto.d-none.d-lg-block
            figure
              img(src="@/assets/curso/temas/t1/f3.png" alt="" style="width: 292px").m-auto

    Separador

    #t_1_1.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 1.1 Sistema circulatorio

    .row.align-items-start
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t1/f2.png" alt="" style="width: 292px").m-auto
      .col-lg-9
        p(data-aos="fade-down") El sistema circulatorio transporta la sangre por todo el organismo y permite que las células reciban el oxígeno y los nutrientes necesarios para su funcionamiento. También recoge dióxido de carbono y otras sustancias de desecho para facilitar su eliminación. Está conformado por el corazón, los vasos sanguíneos y la sangre, elementos que actúan de manera coordinada para conservar el equilibrio del organismo (Tortora y Derrickson, 2021).
        .cajon.color1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 La circulación sanguínea comprende dos recorridos relacionados. En la circulación pulmonar, la sangre se desplaza desde el corazón hacia los pulmones, donde libera dióxido de carbono y recibe oxígeno antes de regresar al corazón. En la circulación sistémica, la sangre oxigenada sale del corazón, llega a los diferentes órganos y tejidos y retorna con menor cantidad de oxígeno (Tortora y Derrickson, 2021).

    p.mt-4(data-aos="fade-down") Durante la primera infancia, la valoración de la circulación permite reconocer signos que pueden indicar una alteración y requerir atención prioritaria. La frecuencia y la calidad del pulso, el color y la temperatura de la piel, así como el tiempo de llenado capilar, aportan información sobre el flujo sanguíneo. Estos signos deben interpretarse de manera conjunta y teniendo en cuenta el estado general de la persona afectada.

    p(data-aos="fade-down") Cada estructura del sistema circulatorio cumple una función específica en el recorrido y la distribución de la sangre. El reconocimiento de estas funciones facilita la comprensión del proceso circulatorio y de las alteraciones que pueden presentarse durante una emergencia. Sus principales componentes son los siguientes:

    .row.mt-4
      .col-sm-6.col-lg-3.mb-4.mb-lg-0(data-aos="fade-down")
        .tarjeta--boton.color-1.p-4(style="min-height: 449px")
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t1/i5.svg" alt="")
                img.icono-hover(src="@/assets/curso/temas/t1/i5-h.svg" alt="")
          h3.text-center Corazón
          p.text-small.text-center.mb-0 Órgano muscular que impulsa la sangre mediante contracciones rítmicas y mantiene su circulación hacia los pulmones y el resto del organismo. Durante una emergencia, la valoración del pulso contribuye a reconocer posibles alteraciones de la actividad cardíaca.
      .col-sm-6.col-lg-3.mb-4.mb-lg-0(data-aos="fade-down")
        .tarjeta--boton.color-1.p-4(style="min-height: 449px")
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t1/i6.svg" alt="")
                img.icono-hover(src="@/assets/curso/temas/t1/i6-h.svg" alt="")
          h3.text-center Arterias
          p.text-small.text-center.mb-0 Vasos sanguíneos que conducen la sangre desde el corazón hacia los órganos y tejidos. En los lactantes, la arteria braquial constituye uno de los puntos utilizados para verificar el pulso durante la valoración de la circulación.
      .col-sm-6.col-lg-3.mb-4.mb-sm-0(data-aos="fade-down")
        .tarjeta--boton.color-1.p-4(style="min-height: 449px")
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t1/i7.svg" alt="")
                img.icono-hover(src="@/assets/curso/temas/t1/i7-h.svg" alt="")
          h3.text-center Venas
          p.text-small.text-center.mb-0 Vasos sanguíneos que retornan la sangre desde los tejidos hacia el corazón. Este recorrido permite que la sangre con menor cantidad de oxígeno sea dirigida posteriormente hacia los pulmones para participar nuevamente en el proceso de oxigenación.
      .col-sm-6.col-lg-3(data-aos="fade-down")
        .tarjeta--boton.color-1.p-4(style="min-height: 449px")
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t1/i8.svg" alt="")
                img.icono-hover(src="@/assets/curso/temas/t1/i8-h.svg" alt="")
          h3.text-center Capilares
          p.text-small.text-center.mb-0 Vasos sanguíneos microscópicos que conectan las ramificaciones más pequeñas de las arterias y las venas. En ellos se produce el intercambio de oxígeno, nutrientes y sustancias de desecho entre la sangre y los diferentes tejidos.

    .row.justify-content-center.mt-5
      .col-lg-10
        p(data-aos="fade-down") El reconocimiento de estas estructuras permite relacionar el funcionamiento circulatorio con signos como palidez, piel fría, sangrado, pulso débil o llenado capilar prolongado. Durante una emergencia, estos hallazgos deben valorarse de forma conjunta para identificar oportunamente un posible compromiso de la circulación y solicitar la atención correspondiente.

    .row.justify-content-center
      .col-lg-11
        .bg-2.r-10.p-4(data-aos="fade-down")
          p.mb-0 La siguiente figura representa la ubicación del corazón y la distribución general de los principales vasos sanguíneos. Su observación permite comprender cómo estas estructuras conforman una red que mantiene el recorrido de la sangre por el organismo.

    .titulo-sexto.color-acento-contenido.mb-3.mt-5
      h5 Figura 1.
      span Sistema circulatorio en la primera infancia

    .row.justify-content-center.bg-fondo-t1-figura
      .col-lg-10
        figure(data-aos="fade-down")
          img(src="@/assets/curso/temas/t1/fig1.png" alt="Figura 1. Sistema circulatorio en la primera infancia. La ilustración representa la ubicación del corazón y el recorrido de los principales vasos sanguíneos en el cuerpo de una niña y un niño. Permite reconocer cómo estas estructuras conforman una red que distribuye la sangre por todo el organismo.").w-100

    p.mt-4(data-aos="fade-down") El adecuado funcionamiento del organismo depende de la acción coordinada de sus diferentes sistemas. En este proceso, la respiración cumple una función esencial al permitir la incorporación del oxígeno necesario para la vida y la eliminación del dióxido de carbono, aspectos que se abordan en el sistema respiratorio.

    Separador

    #t_1_2.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 1.2 Sistema respiratorio

    .row.align-items-start
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t1/f4.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p(data-aos="fade-down") La respiración es un proceso esencial para mantener el funcionamiento del organismo, ya que permite incorporar el oxígeno que requieren las células y eliminar el dióxido de carbono que producen. En este proceso intervienen diferentes estructuras encargadas de conducir el aire y realizar el intercambio gaseoso. Durante la primera infancia, las vías aéreas son más estrechas y la frecuencia respiratoria es mayor; por ello, existe mayor riesgo de obstrucción y dificultad respiratoria (Tortora y Derrickson, 2021).
        .bg-2.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Las estructuras respiratorias actúan de manera coordinada durante la entrada y salida del aire. Reconocer su función permite comprender el proceso respiratorio e identificar oportunamente posibles alteraciones. Sus principales componentes son los siguientes:

    //- Tres paneles pegados: #8EC5FC r=[20,0,0,20] (186,4180) 405x461, #DBC2FA sin radio
    //- (591,4180) 419x461 y #FFE6DE (1009,4180) 405x461 redondeado por la derecha.
    .row.g-0.mt-5
      .col-lg-4
        .bg-4.r-izq-20.p-4.tarjeta--icono-arriba(data-aos="fade-down")
          figure
            img(src="@/assets/curso/temas/t1/i9.svg" alt="")
          h4.text-center Vías respiratorias
          p.text-center.mb-0 Conducen el aire desde la nariz o la boca hasta los pulmones, a través de la faringe, la laringe y la tráquea. Por ejemplo, un alimento o un objeto pequeño puede bloquear este recorrido y ocasionar una obstrucción de la vía aérea por cuerpo extraño (OVACE).
      .col-lg-4
        .bg-6.p-4.tarjeta--icono-arriba(data-aos="fade-down")
          figure
            img(src="@/assets/curso/temas/t1/i10.svg" alt="")
          h4.text-center Pulmones
          p.text-center.mb-0 Realizan el intercambio de oxígeno y dióxido de carbono entre el aire y la sangre. Por ejemplo, una alteración en este proceso puede manifestarse mediante dificultad para respirar, respiración acelerada o coloración azulada en los labios.
      .col-lg-4
        .bg-1.r-der-20.p-4.tarjeta--icono-arriba(data-aos="fade-down")
          figure
            img(src="@/assets/curso/temas/t1/i11.svg" alt="")
          h4.text-center Músculos respiratorios
          p.text-center.mb-0 Permiten los movimientos de inspiración y espiración mediante la acción del diafragma y los músculos intercostales. Por ejemplo, el hundimiento de la piel entre las costillas, denominado tiraje, puede indicar un aumento del esfuerzo respiratorio.

    p.mt-5(data-aos="fade-down") La observación de la respiración permite reconocer signos de alarma, como movimientos anormales del tórax, ruidos respiratorios, cambios en la coloración de la piel o dificultad para hablar, llorar o toser. Estas manifestaciones deben valorarse de manera conjunta, puesto que pueden indicar una disminución de la entrada de aire y requerir atención inmediata.

    .row.align-items-start.mt-4
      .col-lg-9
        .row.align-items-start
          .col-auto.mb-3.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t1/ic1.png" alt="" style="width: 84px")
          .col
            p.mb-0(data-aos="fade-down") El reconocimiento de las estructuras respiratorias orienta la apertura de la vía aérea, la valoración de la respiración y la aplicación de maniobras de desobstrucción en caso de OVACE. La identificación temprana de los signos de dificultad respiratoria y la actuación oportuna son fundamentales, debido a que estas alteraciones pueden evolucionar rápidamente durante la primera infancia (Ministerio de Salud y Protección Social, 2018).
        .bg-1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Además de incorporar el oxígeno necesario para el funcionamiento del organismo, el cuerpo requiere una barrera que lo proteja frente a lesiones, microorganismos y otros agentes externos. Esta función corresponde principalmente a la piel y a sus estructuras asociadas, las cuales conforman el sistema tegumentario.
      .col-lg-3.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t1/f5.png" alt="" style="width: 292px").m-auto

    Separador

    #t_1_3.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 1.3 Sistema tegumentario

    .row.align-items-start
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t1/ilus1.svg" alt="" style="width: 292px").m-auto
      .col-lg-9
        p(data-aos="fade-down") La protección del organismo depende, en gran medida, de la integridad de la piel. Esta estructura actúa como barrera frente a microorganismos, golpes, cambios de temperatura y otros agentes externos. Además, participa en la sensibilidad y en la regulación de la temperatura corporal.
        .bg-1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 El sistema tegumentario está conformado por la piel y sus estructuras asociadas, como el cabello, las uñas y las glándulas. La piel se organiza en tres capas principales: epidermis, dermis e hipodermis (Tortora y Derrickson, 2021). Durante la primera infancia, es más delgada, sensible y vulnerable, por lo que puede lesionarse con mayor facilidad.

    p.mt-4(data-aos="fade-down") La observación del color, la temperatura y la integridad de la piel permite reconocer alteraciones que requieren protección o atención inmediata. Entre las manifestaciones más frecuentes se encuentran las siguientes:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ul--color.mb-0
            li
              i.fas.fa-heart
              span.mb-0 #[b Heridas:] producen una pérdida de continuidad de la piel. Por ejemplo, un raspón durante el juego puede ocasionar dolor, sangrado y riesgo de infección.
            li
              i.fas.fa-heart
              span.mb-0 #[b Quemaduras:] lesionan la piel por acción del calor, la electricidad, sustancias químicas u otros agentes. Por ejemplo, pueden producirse por el contacto accidental con agua caliente.
            li
              i.fas.fa-heart
              span.mb-0 #[b Irritaciones:] generan enrojecimiento, picazón o inflamación por contacto con sustancias o materiales. Por ejemplo, algunos productos de limpieza pueden irritar la piel infantil.
            li.mb-0
              i.fas.fa-heart
              span.mb-0 #[b Coloración:] comprende cambios como palidez, enrojecimiento o cianosis. Por ejemplo, una tonalidad azulada en los labios puede indicar una alteración respiratoria.

    p.mt-5(data-aos="fade-down") El reconocimiento de estas manifestaciones permite establecer la posible gravedad de la lesión y evitar prácticas que puedan incrementar el daño. En la primera infancia, cualquier cambio significativo debe valorarse teniendo en cuenta su extensión, localización, causa y evolución.

    p(data-aos="fade-down") Ante una lesión de la piel, la actuación inicial debe desarrollarse de manera organizada. Para orientar este proceso, se presentan las siguientes acciones generales:

    SlyderF.slyder--principios.mt-4(columnas="col-md-6 col-lg-4")
      .tarjeta.bg-4.r-20.p-4(style="min-height: 476px")
        figure
          img(src="@/assets/curso/temas/t1/i16.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b 1. Verificar la seguridad del entorno
        p.text-center.mb-0 Identificar y controlar, cuando sea posible, el agente que ocasionó la lesión, sin poner en riesgo a la persona afectada ni al primer respondiente.
      .tarjeta.bg-4.r-20.p-4(style="min-height: 476px")
        figure
          img(src="@/assets/curso/temas/t1/i17.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b 2. Aplicar medidas de bioseguridad
        p.text-center.mb-0 Utilizar los elementos de protección disponibles para evitar el contacto directo con sangre, fluidos corporales o sustancias potencialmente peligrosas.
      .tarjeta.bg-4.r-20.p-4(style="min-height: 476px")
        figure
          img(src="@/assets/curso/temas/t1/i18.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b 3. Observar la lesión
        p.text-center.mb-0 Reconocer su localización, extensión, profundidad aparente y posibles signos de alarma, sin presionar ni manipular innecesariamente la zona afectada.
      .tarjeta.bg-4.r-20.p-4(style="min-height: 476px")
        figure
          img(src="@/assets/curso/temas/t1/i19.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b 4. Proporcionar la atención inicial
        p.text-center.mb-0 Limpiar y proteger las heridas superficiales o enfriar las quemaduras térmicas con agua corriente limpia, según el tipo de lesión.
      .tarjeta.bg-4.r-20.p-4(style="min-height: 476px")
        figure
          img(src="@/assets/curso/temas/t1/i20.svg" alt="" style="width: 128px").m-auto
        p.text-center.mt-3.mb-2(style="font-size:1.125em")
          b 5. Solicitar atención especializada
        p.text-center.mb-0 Activar el servicio de emergencias cuando existan sangrado abundante, quemaduras extensas, dificultad respiratoria, alteración de la conciencia u otros signos de gravedad.

    .row.align-items-start.mt-5
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t1/f6.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p(data-aos="fade-down") Estas acciones contribuyen a proteger la zona afectada, disminuir el riesgo de infección y prevenir complicaciones. No deben aplicarse sustancias caseras, cremas ni otros productos sobre una quemadura, salvo indicación del personal de salud.
        .bg-1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Además de proteger al organismo frente a los agentes externos, el cuerpo necesita estructuras que le proporcionen soporte, estabilidad y movimiento. Estas funciones dependen de la acción coordinada de los huesos, los músculos y las articulaciones, componentes del sistema musculoesquelético.

    Separador

    #t_1_4.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 1.4 Sistema musculoesquelético

    .row.align-items-start
      .col-lg-9
        p(data-aos="fade-down") El movimiento corporal requiere la participación coordinada de diferentes estructuras que proporcionan soporte, estabilidad y protección. Durante la primera infancia, estas estructuras se encuentran en crecimiento y favorecen el desarrollo de habilidades como caminar, correr, saltar y manipular objetos.
        .cajon.color1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 El sistema musculoesquelético está constituido por huesos, músculos, articulaciones, ligamentos y tendones. Los huesos brindan soporte y protegen los órganos internos, mientras que los músculos y las articulaciones permiten el movimiento (Tortora y Derrickson, 2021). Aunque los huesos infantiles presentan mayor flexibilidad, las caídas y los golpes pueden ocasionar lesiones.
      .col-lg-3.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t1/ilus2.png" alt="" style="width: 292px").m-auto

    p.mt-4(data-aos="fade-down") La valoración inicial permite reconocer alteraciones relacionadas con el dolor, la inflamación, la deformidad o la limitación del movimiento. Las lesiones musculoesqueléticas más frecuentes se describen a continuación:

    .row.mt-4
      .col-sm-6.col-lg-3.mb-4.mb-lg-0(data-aos="fade-down")
        .tarjeta--boton.color-1.p-4(style="min-height: 358px")
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t1/i12.svg" alt="")
                img.icono-hover(src="@/assets/curso/temas/t1/i12-h.svg" alt="")
          h3.text-center Esguince
          p.text-small.text-center.mb-0 Afecta un ligamento por estiramiento o desgarro. Por ejemplo, puede producirse cuando una niña o un niño se tuerce el tobillo durante el juego.
      .col-sm-6.col-lg-3.mb-4.mb-lg-0(data-aos="fade-down")
        .tarjeta--boton.color-1.p-4(style="min-height: 358px")
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t1/i13.svg" alt="")
                img.icono-hover(src="@/assets/curso/temas/t1/i13-h.svg" alt="")
          h3.text-center Luxación
          p.text-small.text-center.mb-0 Ocurre cuando un hueso se desplaza fuera de su articulación. Puede manifestarse mediante dolor intenso, deformidad visible y dificultad para mover la zona.
      .col-sm-6.col-lg-3.mb-4.mb-sm-0(data-aos="fade-down")
        .tarjeta--boton.color-1.p-4(style="min-height: 358px")
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t1/i14.svg" alt="")
                img.icono-hover(src="@/assets/curso/temas/t1/i14-h.svg" alt="")
          h3.text-center Fractura
          p.text-small.text-center.mb-0 Corresponde a la ruptura parcial o total de un hueso. Por ejemplo, puede presentarse después de una caída y causar dolor, inflamación o deformidad.
      .col-sm-6.col-lg-3(data-aos="fade-down")
        .tarjeta--boton.color-1.p-4(style="min-height: 358px")
          .row.justify-content-center.mb-3
            .col-7
              figure
                img.icono(src="@/assets/curso/temas/t1/i15.svg" alt="")
                img.icono-hover(src="@/assets/curso/temas/t1/i15-h.svg" alt="")
          h3.text-center Contusión
          p.text-small.text-center.mb-0 Se produce por un golpe que lesiona los tejidos sin romper la piel. Por ejemplo, puede ocasionar dolor, inflamación y cambio de coloración.

    p.mt-5(data-aos="fade-down") La presencia de dolor intenso, deformidad, inflamación progresiva o incapacidad para mover una extremidad puede indicar una lesión que requiere atención especializada. La zona afectada debe mantenerse en reposo y en la posición encontrada, evitando movimientos que puedan agravar el daño.

    p(data-aos="fade-down") Cuando se sospecha una lesión musculoesquelética, la atención inicial debe seguir una secuencia organizada y segura:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ol--cuadro.mb-0
            li
              span.lista-ol--cuadro__vineta 1
              |  #[b Comprobar la seguridad del lugar:] verificar que no persistan riesgos asociados con la caída, el golpe o el objeto que produjo la lesión.
            li
              span.lista-ol--cuadro__vineta 2
              |  #[b Observar la zona afectada:] identificar dolor, inflamación, heridas, deformidad, cambio de coloración o limitación del movimiento, sin forzar la extremidad.
            li
              span.lista-ol--cuadro__vineta 3
              |  #[b Evitar movimientos innecesarios:] mantener la zona en la posición encontrada y solicitar a la persona afectada que permanezca en reposo.
            li
              span.lista-ol--cuadro__vineta 4
              |  #[b Inmovilizar cuando sea necesario:] estabilizar la extremidad sin intentar enderezarla ni devolver los huesos o las articulaciones a su posición.
            li.mb-0
              span.lista-ol--cuadro__vineta 5
              |  #[b Solicitar atención especializada:] activar el servicio de emergencias ante deformidad, dolor intenso, sangrado, pérdida de sensibilidad o sospecha de lesión en la cabeza, el cuello o la columna.

    .row.align-items-start.mt-5
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t1/ilus3.png" alt="" style="width: 292px").m-auto
      .col-lg-9
        p(data-aos="fade-down") El manejo inicial busca disminuir el movimiento, evitar nuevas lesiones y facilitar un traslado seguro. No se debe intentar corregir una deformidad ni comprobar una posible fractura mediante movimientos, ya que estas prácticas pueden aumentar el dolor y afectar los tejidos cercanos.
        .cajon.color1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 El reconocimiento de las funciones y alteraciones de los sistemas circulatorio, respiratorio, tegumentario y musculoesquelético permite comprender su importancia durante una situación crítica. Esta integración facilita la identificación de signos de alarma y orienta la atención inicial de las emergencias en la primera infancia.

    Separador

    #t_1_5.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 1.5 Relación con la atención de emergencias

    .row.align-items-stretch.g-0
      .col-lg-3
        figure.m-0.h-100
          img.w-100.h-100.object-fit-cover(src="@/assets/curso/temas/t1/f7.png" alt="")
      .col-lg-9
        .bg-1.p-4.h-100
          .row.align-items-start
            .col-auto.mb-3
              figure
                img(src="@/assets/curso/temas/t1/ic2.png" alt="" style="width: 84px")
          p.mb-0 Durante una emergencia, los sistemas corporales pueden afectarse de manera simultánea. Una caída, por ejemplo, puede ocasionar una herida, una fractura y una alteración de la circulación. Por esta razón, la valoración no debe limitarse a la lesión visible, sino considerar el estado general de la persona afectada.

    p.mt-4(data-aos="fade-down") La comprensión integrada de los sistemas permite reconocer cambios que pueden comprometer la respiración, la circulación, la integridad de la piel o el movimiento. Esta relación ayuda al primer respondiente a establecer prioridades y a solicitar oportunamente la atención especializada.

    p(data-aos="fade-down") La valoración inicial permite identificar los sistemas corporales afectados y establecer las acciones prioritarias de atención. Para ello, se deben observar los signos presentes, relacionarlos con la posible lesión y determinar si existe riesgo para la vida de la niña o el niño. A continuación, se describen las principales alteraciones:

    .row.align-items-center.mt-4
      .col-lg-6.mb-4.mb-lg-0
        LineaTiempoD.linea-tiempo--caracteristicas.linea-bold
          .row(numero="1" titulo="Circulatorias")
            .col-12
              p.mb-0 Incluyen sangrado abundante, palidez, piel fría, pulso débil o ausencia de respuesta. Estos signos pueden indicar una alteración del flujo sanguíneo. Por ejemplo, ante una herida con hemorragia, se debe aplicar presión directa, comprobar el estado general y solicitar atención especializada para prevenir un posible choque circulatorio.
          .row(numero="2" titulo="Respiratorias")
            .col-12
              p.mb-0 Comprenden dificultad para respirar, respiración rápida, lenta o ausente, ruidos anormales y coloración azulada. Estas manifestaciones pueden indicar una alteración de la oxigenación. Por ejemplo, si un alimento obstruye la vía aérea, se debe aplicar de inmediato la técnica correspondiente para atender la obstrucción de la vía aérea por cuerpo extraño.
          .row(numero="3" titulo="Tegumentarias")
            .col-12
              p.mb-0 Incluyen heridas, quemaduras, irritaciones y cambios en la coloración o la temperatura de la piel. Estas lesiones pueden afectar la protección del organismo. Por ejemplo, ante una quemadura extensa, se debe enfriar la zona con agua corriente, cubrirla con material limpio y evitar la aplicación de sustancias caseras.
          .row(numero="4" titulo="Musculoesqueléticas")
            .col-12
              p.mb-0 Se manifiestan mediante dolor, inflamación, deformidad o limitación del movimiento y pueden afectar el soporte corporal. Por ejemplo, después de una caída que ocasione una posible fractura, se debe inmovilizar la zona, evitar movimientos innecesarios y realizar un traslado seguro, sin intentar acomodar el hueso afectado.
      .col-lg-4.offset-lg-1.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/t1/f8.png" alt="" style="width: 396px").m-auto

    p.mt-5(data-aos="fade-down") El reconocimiento conjunto de estos signos permite comprender que una lesión puede afectar varios sistemas corporales al mismo tiempo. Por esta razón, la atención debe priorizar las alteraciones que comprometan la conciencia, la respiración, la circulación o produzcan una hemorragia grave.

    p(data-aos="fade-down") Ante una situación de emergencia, la actuación inicial puede organizarse mediante la siguiente secuencia:

    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4.p-md-5(data-aos="fade-down")
          .row.align-items-center
            .col-lg-7
              ul.lista-ol--cuadro.mb-0
                li
                  span.lista-ol--cuadro__vineta A
                  |  #[b Proteger:] verificar la seguridad del lugar y evitar que la persona afectada, el primer respondiente u otras personas se expongan a nuevos riesgos.
                li
                  span.lista-ol--cuadro__vineta B
                  |  #[b Valorar:] comprobar la respuesta, la respiración, la presencia de hemorragias graves y otros signos visibles que puedan indicar una situación crítica.
                li
                  span.lista-ol--cuadro__vineta C
                  |  #[b Alertar:] comunicarse con el servicio de emergencias y proporcionar información clara sobre el lugar, la situación y el estado de la persona afectada.
                li
                  span.lista-ol--cuadro__vineta D
                  |  #[b Atender:] aplicar únicamente las técnicas de primeros auxilios conocidas, sin realizar procedimientos que superen la preparación del primer respondiente.
                li.mb-0
                  span.lista-ol--cuadro__vineta E
                  |  #[b Acompañar:] observar los cambios en el estado de la persona, conservar la calma y permanecer a su lado hasta la llegada del personal especializado.
            .col-lg-5.d-none.d-lg-block
              figure.m-0
                img(src="@/assets/curso/temas/t1/f9.png" alt="" style="width: 316px").m-auto

    .row.align-items-start.mt-5
      .col-auto.mb-3.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t1/ic3.png" alt="" style="width: 84px")
      .col
        p(data-aos="fade-down") Esta secuencia favorece una respuesta segura, ordenada y centrada en las necesidades prioritarias. En la primera infancia, la observación permanente es fundamental, ya que el estado de una niña o un niño puede cambiar rápidamente durante una emergencia.
        p.mb-0(data-aos="fade-down") La comprensión de la anatomía y la fisiología básicas proporciona los fundamentos para reconocer posibles alteraciones corporales. Estos conocimientos facilitan la evaluación inicial de la persona lesionada, permiten identificar su estado general y ayudan a establecer las prioridades de atención.

</template>

<script>
export default {
  name: 'Tema1',
}
</script>
