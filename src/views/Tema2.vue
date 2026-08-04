<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 2
      h1 Evaluación inicial del lesionado

    //- Ficha: icono (186,413) 84x84 #FFC0AC r=10 · nota (186,534) 812x120 #F4EDFE r=10 ·
    //- foto (1018,316) 396x338
    .row.align-items-start.mt-4
      .col-lg-8
        p(data-aos="fade-down") La respuesta de una niña o un niño ante la voz, el contacto y otros estímulos permite reconocer posibles cambios en su estado general. Esta observación debe compararse con su comportamiento habitual, debido a que cada persona puede reaccionar de manera diferente según su edad, condición de salud y circunstancias de la lesión.

        .row.align-items-start.mt-4(data-aos="fade-down")
          .col-auto.mb-3.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t2/ic1.png" alt="" style="width: 84px")
          .col
            p.mb-0 La somnolencia inusual, la desorientación o la ausencia de respuesta pueden indicar un deterioro que requiere atención inmediata. Por ello, también es necesario observar la respiración, la coloración de la piel y la capacidad para interactuar, seguir indicaciones o realizar movimientos habituales.

        .bg-2.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Para llevar a cabo esta valoración de forma rápida y organizada, se utiliza la escala AVPU. Esta herramienta clasifica el nivel de conciencia de acuerdo con cuatro tipos de respuesta: alerta, respuesta verbal, respuesta al dolor y ausencia de respuesta.
      .col-lg-4.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t2/f1.png" alt="" style="width: 396px").m-auto

    p.mt-4(data-aos="fade-down") A continuación, la siguiente figura presenta los cuatro niveles que conforman la escala AVPU y las respuestas asociadas a cada uno.

    .titulo-sexto.color-acento-contenido.mb-3.mt-5
      h5 Figura 2.
      span Escala AVPU para valorar el nivel de conciencia

    .row.justify-content-center
      .col-lg-10
        figure(data-aos="fade-down")
          img(src="@/assets/curso/temas/t2/fig2.png" alt="Figura 2. Escala AVPU para valorar el nivel de conciencia. Presenta los cuatro niveles de la escala —alerta, respuesta verbal, respuesta al dolor y ausencia de respuesta— con la reacción que describe el estado de la niña o el niño en cada uno.").w-100

    p.mt-4(data-aos="fade-down") Para dar continuidad a la evaluación inicial, se deben observar los movimientos del tórax y el abdomen, así como la frecuencia y el ritmo respiratorios. También es importante identificar sonidos anormales o señales de esfuerzo al respirar. Estos aspectos permiten reconocer posibles alteraciones y orientar adecuadamente la valoración de la respiración.

    Separador

    #t_2_2.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 2.2 Valoración de la respiración

    //- Ficha: foto (186,1748) 396x261 a la izquierda
    .row.align-items-start
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t2/f2.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p(data-aos="fade-down") Una vez valorado el nivel de conciencia, es necesario comprobar cómo respira la niña o el niño. Esta observación permite reconocer si el aire ingresa y sale adecuadamente, así como detectar cambios que puedan afectar la oxigenación. Debido a las características propias de la primera infancia, cualquier alteración respiratoria requiere una valoración cuidadosa y oportuna.
        .cajon.color1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Para realizar esta valoración, se deben observar los movimientos del tórax y el abdomen, contar las respiraciones durante un minuto e identificar el ritmo, la profundidad, los sonidos y el esfuerzo respiratorio. La observación debe efectuarse sin causar agitación, debido a que el llanto, el miedo, la actividad física o la fiebre pueden modificar temporalmente la forma de respirar.

    p.mt-4(data-aos="fade-down") Los principales aspectos que deben tenerse en cuenta son los siguientes:

    //- Ficha: panel abierto (290,2100) 1020x170 #F4EDFE r=20 y 4 filas cerradas 1020x90 #B8F4CE r=20
    .row.justify-content-center.mt-4
      .col-lg-10
        AcordionA.acordion--principios(tipo="b")
          .row(titulo="Frecuencia respiratoria")
            .col-12
              p.mb-0 Corresponde al número de respiraciones realizadas durante un minuto. Su valoración permite reconocer si la respiración se mantiene dentro de las características esperadas para la edad o presenta cambios que requieren atención.
          .row(titulo="Ritmo respiratorio")
            .col-12
              p.mb-0 Indica si las respiraciones se producen de manera regular o irregular. Se debe observar si los intervalos entre cada respiración son semejantes o si se presentan pausas, cambios repentinos o movimientos desorganizados.
          .row(titulo="Profundidad respiratoria")
            .col-12
              p.mb-0 Permite identificar la cantidad de aire movilizada durante cada respiración. Puede reconocerse mediante la amplitud de los movimientos del tórax y el abdomen, los cuales pueden ser normales, superficiales o más profundos de lo habitual.
          .row(titulo="Sonidos respiratorios")
            .col-12
              p.mb-0 Corresponden a los ruidos que acompañan la entrada y salida del aire. La presencia de silbidos, ronquidos, quejidos u otros sonidos inusuales puede relacionarse con una dificultad en el paso del aire.
          .row(titulo="Esfuerzo respiratorio")
            .col-12
              p.mb-0 Comprende las manifestaciones que evidencian dificultad para respirar. Entre ellas se encuentran el hundimiento de la piel entre las costillas, el movimiento exagerado del abdomen, la apertura de las fosas nasales y el uso marcado de los músculos del cuello.

    //- Ficha: nota (186,2837) 916x120 #FFE6DE sin radio · foto (1122,2740) 292x290
    .row.align-items-start.mt-5
      .col-lg-9
        p(data-aos="fade-down") La valoración conjunta de estos aspectos permite reconocer cómo se realiza la respiración y facilita la identificación de cambios relevantes. No debe interpretarse una característica de manera aislada, pues la edad, el llanto, la fiebre, la actividad física y el estado emocional pueden modificar temporalmente el patrón respiratorio.
        .bg-1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 En la primera infancia, las alteraciones respiratorias pueden presentarse de distintas formas según su causa y evolución. Por ello, no basta con comprobar que existe respiración; también se deben analizar sus características para determinar si la ventilación parece adecuada o si requiere una intervención oportuna.
        p.mt-4(data-aos="fade-down") La comparación de los patrones observados facilita la toma de decisiones durante la atención inicial. La siguiente tabla presenta los principales tipos de respiración, sus características y las acciones generales que deben considerarse.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t2/f3.png" alt="" style="width: 292px").m-auto

    .titulo-sexto.color-acento-contenido.mb-3.mt-5
      h5 Tabla 1.
      span Tipos de respiración y acciones iniciales

    .row.justify-content-center
      .col-lg-10
        .tabla-a.color-acento-contenido(data-aos="fade-down")
          table
            thead
              tr
                th Tipo de respiración
                th Características observables
                th Acción inicial
            tbody
              tr
                td Respiración normal
                td Presenta movimientos regulares del tórax y el abdomen, sin ruidos anormales ni esfuerzo evidente.
                td Mantener la observación y comprobar periódicamente que no se presentan cambios.
              tr
                td Respiración rápida
                td Se evidencia un aumento del número de respiraciones en comparación con el estado habitual de la niña o el niño.
                td Mantener en reposo, evitar la agitación y vigilar la evolución de la respiración.
              tr
                td Respiración lenta
                td Presenta una disminución evidente del número de respiraciones o pausas más prolongadas de lo habitual.
                td Solicitar atención especializada y observar permanentemente el nivel de respuesta.
              tr
                td Respiración irregular
                td Alterna respiraciones rápidas, lentas, superficiales o pausas sin un patrón constante.
                td Mantener la vigilancia y solicitar ayuda especializada si el cambio persiste o empeora.
              tr
                td Respiración con esfuerzo
                td Se observa hundimiento entre las costillas, apertura de las fosas nasales, movimientos exagerados o uso de los músculos del cuello.
                td Facilitar una posición cómoda, evitar movimientos innecesarios y activar el servicio de emergencias.
              tr
                td Respiración ruidosa
                td Presenta silbidos, ronquidos, quejidos u otros sonidos inusuales durante la entrada o salida del aire.
                td Verificar que la vía aérea permanezca despejada y solicitar valoración especializada.
              tr
                td Respiración ausente
                td No se observan movimientos del tórax ni del abdomen y no se percibe entrada o salida de aire.
                td Activar inmediatamente el servicio de emergencias e iniciar las maniobras correspondientes, si se cuenta con la preparación necesaria.

    p.mt-4(data-aos="fade-down") Las características respiratorias pueden modificarse en poco tiempo; por ello, la observación debe mantenerse durante toda la atención inicial. Si la respiración es ausente, irregular o se realiza con un esfuerzo evidente, se debe solicitar ayuda especializada y actuar únicamente de acuerdo con la preparación recibida.

    .row.justify-content-center.mt-4
      .col-lg-10
        .cajon.color1.p-4(data-aos="fade-down")
          p.mb-0 La respiración aporta información esencial sobre el funcionamiento del organismo; sin embargo, también es necesario comprobar cómo se mantiene la circulación. Esta valoración se complementa con la identificación del pulso y de sus principales características.

    Separador

    #t_2_3.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 2.3 Valoración del pulso

    p(data-aos="fade-down") Durante una emergencia, la observación del pulso ayuda a reconocer cómo se encuentra la actividad cardíaca y la circulación sanguínea. En la primera infancia, esta valoración debe realizarse con precisión, porque la frecuencia cardíaca suele ser mayor y cualquier alteración puede evolucionar rápidamente.

    p(data-aos="fade-down") Para realizar esta valoración de manera organizada, se recomienda seguir la siguiente secuencia:

    //- Ficha: banda (290,4147) 1020x380 #DDEEFE · foto (998,4171) 294x332
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4.p-md-5(data-aos="fade-down")
          .row.align-items-center
            .col-lg-7
              ul.lista-ol--cuadro.mb-0
                li
                  span.lista-ol--cuadro__vineta 1
                  |  #[b Localizar la arteria:] ubicar la arteria braquial en lactantes o la arteria carótida en niñas y niños mayores.
                li
                  span.lista-ol--cuadro__vineta 2
                  |  #[b Palpar suavemente:] colocar las yemas de los dedos índice y medio sobre la arteria, sin ejercer una presión excesiva.
                li
                  span.lista-ol--cuadro__vineta 3
                  |  #[b Comprobar la presencia:] verificar si el pulso se percibe con claridad durante un tiempo máximo de 10 segundos.
                li
                  span.lista-ol--cuadro__vineta 4
                  |  #[b Observar sus características:] identificar la frecuencia, el ritmo y la intensidad del pulso, teniendo en cuenta el estado general de la niña o el niño.
                li.mb-0
                  span.lista-ol--cuadro__vineta 5
                  |  #[b Relacionar los hallazgos:] valorar el pulso junto con la respiración, la coloración de la piel, el nivel de conciencia y otros signos observados.
            .col-lg-5.d-none.d-lg-block
              figure.m-0
                img(src="@/assets/curso/temas/t2/f4.png" alt="" style="width: 294px").m-auto

    //- Ficha: ilustración (186,4559) 292x194 · icono (498,4656) 84x84 #FFC0AC r=10
    .row.align-items-start.mt-5
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t2/ilus1.png" alt="" style="width: 292px").m-auto
      .col-lg-9
        p(data-aos="fade-down") Esta secuencia facilita la identificación de posibles alteraciones circulatorias y orienta la necesidad de solicitar atención especializada. Un pulso débil, irregular o ausente puede estar acompañado de otros signos de deterioro que requieren una actuación inmediata.
        .row.align-items-start.mt-4(data-aos="fade-down")
          .col-auto.mb-3.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t2/ic2.png" alt="" style="width: 84px")
          .col
            p.mb-0 Una vez comprobada la presencia del pulso, se deben observar sus características y relacionarlas con el estado general de la niña o el niño. La siguiente tabla sintetiza los principales hallazgos, su posible interpretación y la atención inicial correspondiente.

    .titulo-sexto.color-acento-contenido.mb-3.mt-5
      h5 Tabla 2.
      span Valoración del pulso en la evaluación inicial

    .row.justify-content-center
      .col-lg-10
        .tabla-a.color-acento-contenido(data-aos="fade-down")
          table
            thead
              tr
                th Pulso
                th Características
                th Posible interpretación
                th Atención inicial
            tbody
              tr
                td Normal
                td Presenta una frecuencia y un ritmo acordes con el estado general.
                td La circulación se encuentra conservada.
                td Continuar con la valoración y observar posibles cambios.
              tr
                td Rápido
                td La frecuencia se encuentra aumentada.
                td Puede relacionarse con dolor, fiebre, temor o pérdida de líquidos.
                td Observar otros signos y vigilar la evolución.
              tr
                td Lento
                td La frecuencia se encuentra disminuida.
                td Puede indicar un compromiso respiratorio, cardíaco o neurológico.
                td Solicitar atención especializada y vigilar el estado general.
              tr
                td Débil
                td El pulso es difícil de percibir.
                td Puede existir una circulación insuficiente.
                td Activar el servicio de emergencias y observar otros signos.
              tr
                td Ausente
                td No se percibe durante la evaluación realizada por una persona capacitada.
                td Puede indicar un paro cardiorrespiratorio.
                td Iniciar la RCP según el protocolo establecido.

    p.mt-4(data-aos="fade-down") De acuerdo con la información presentada, las características del pulso deben interpretarse junto con la respiración, el nivel de conciencia, la coloración y la temperatura de la piel. Esta valoración integral permite reconocer oportunamente un posible compromiso circulatorio y determinar la necesidad de atención inmediata.

    .row.justify-content-center.mt-4
      .col-lg-10
        .cajon.color1.p-4(data-aos="fade-down")
          p.mb-0 Además de los cambios en el pulso, pueden presentarse otras manifestaciones que indiquen un deterioro del estado general. Por esta razón, la evaluación inicial continúa con la identificación de los signos de alarma que requieren una actuación oportuna.

    Separador

    #t_2_4.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 2.4 Identificación de signos de alarma

    p(data-aos="fade-down") El estado de una niña o un niño puede cambiar rápidamente ante una lesión o alteración de la salud. Por esta razón, es necesario observar su respiración, nivel de conciencia, coloración de la piel, comportamiento y respuesta a los estímulos. Estos elementos permiten reconocer la gravedad de la situación y establecer prioridades durante la atención inicial.

    p(data-aos="fade-down") Según las manifestaciones observadas y la respuesta requerida, los signos pueden organizarse en tres niveles:

    //- Ficha: banda (137,5902) 1328x747, degradado lavanda #E3D7FF -> azul #97CBFF. El PDF la
    //- aplasta a violeta oscuro por el blendMode: es CLARA. La tarjeta del slider va encima.
    .row.bg-banda-t2-24.mt-4
      .col-12.p-4.p-md-5
        SlyderA.tarjeta.tarjeta--blanca.p-4.p-md-5(tipo="b")
          .row.align-items-center
            .col-lg-6.mb-4.mb-lg-0
              h4 Observación (Seguimiento)
              ul.lista-ul.mb-0
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Irritabilidad leve:] cambio moderado en el comportamiento que requiere acompañamiento y seguimiento.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Malestar general:] presencia de incomodidad, cansancio o disminución temporal del estado habitual.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Lesiones leves:] heridas superficiales, golpes menores o molestias que no comprometen el estado general.
                li.mb-0
                  span.lista-ul__vineta
                  span.mb-0 #[b Cambios leves en la actividad:] disminución moderada del juego, el movimiento o la interacción.
            .col-lg-6
              figure.m-0.marco-degradado
                img(src="@/assets/curso/temas/t2/f5.png" alt="")
          .row.align-items-center
            .col-12
              h4 Alerta (Valoración oportuna)
              ul.lista-ul.mb-0
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Respiración rápida o irregular:] cambio en la frecuencia o el ritmo respiratorio que requiere vigilancia.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Dolor intenso:] molestia que causa llanto persistente, limita el movimiento o altera el comportamiento.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Fiebre persistente:] aumento de la temperatura que se mantiene o se acompaña de decaimiento.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Debilidad o decaimiento:] disminución evidente de la energía, la actividad o la capacidad de respuesta.
                li.mb-0
                  span.lista-ul__vineta
                  span.mb-0 #[b Cambios importantes en el comportamiento:] somnolencia inusual, irritabilidad intensa, confusión o dificultad para interactuar.
          .row.align-items-center
            .col-12
              h4 Grave (Atención inmediata)
              ul.lista-ul.mb-0
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Ausencia de respiración:] falta de movimientos respiratorios y de entrada o salida de aire.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Dificultad respiratoria intensa:] esfuerzo evidente para respirar, hundimiento del pecho, ruidos anormales o coloración azulada.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Pérdida de la conciencia:] ausencia de respuesta ante la voz o los estímulos.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Convulsiones:] movimientos involuntarios, rigidez corporal o pérdida repentina de la respuesta.
                li
                  span.lista-ul__vineta
                  span.mb-0 #[b Sangrado abundante:] pérdida de sangre que no se controla mediante presión directa.
                li.mb-0
                  span.lista-ul__vineta
                  span.mb-0 #[b Cianosis:] coloración azulada o violácea en los labios, la piel o las uñas.

    p.mt-5(data-aos="fade-down") Esta clasificación orienta la observación y ayuda a reconocer cuándo se requiere seguimiento, valoración o atención inmediata. Los signos deben interpretarse de manera conjunta, ya que el estado general puede cambiar rápidamente y exigir la activación del servicio de emergencias.

    //- Ficha: ilustración (1122,6574) 292x167 #8EC5FC r=10
    .row.align-items-center.mt-4
      .col-lg-9
        .cajon.color1.p-4(data-aos="fade-down")
          p.mb-0 Una vez identificadas las manifestaciones que pueden comprometer la vida, es necesario conocer las acciones destinadas a mantener la respiración y la circulación. En el siguiente apartado, se presentan los procedimientos de soporte vital básico aplicados en la primera infancia.
      .col-lg-3.mt-4.mt-lg-0
        figure.m-0
          img(src="@/assets/curso/temas/t2/ilus2.png" alt="" style="width: 292px").m-auto

</template>

<script>
export default {
  name: 'Tema2',
}
</script>
