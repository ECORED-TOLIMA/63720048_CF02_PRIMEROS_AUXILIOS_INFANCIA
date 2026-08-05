<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 5
      h1 Situaciones específicas y enfermedades prevalentes

    //- Ficha: foto (186,316) 396x281 -> col-4 · texto en x=603 -> col-8, y dentro la nota
    //- (602,437) 812x160 #F4EDFE r=10
    .row.align-items-start.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t5/f2.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p(data-aos="fade-down") Durante la primera infancia pueden presentarse accidentes y alteraciones de salud que evolucionan rápidamente y requieren una respuesta oportuna. Entre estas situaciones se encuentran la presencia de cuerpos extraños, las picaduras, las mordeduras, las convulsiones y las intoxicaciones. También son frecuentes algunas enfermedades respiratorias, gastrointestinales, dermatológicas, nutricionales e inmunoprevenibles.
        .bg-2.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Aunque estas situaciones tienen causas y manifestaciones diferentes, su atención inicial parte de una actuación común: observar el estado general de la niña o del niño, reconocer los cambios que indican gravedad y aplicar únicamente las medidas que correspondan al nivel de formación del primer respondiente. Esta valoración permite decidir si se requiere vigilancia, consulta médica prioritaria o activación inmediata del sistema de emergencias.

    p.mt-4(data-aos="fade-down") En los hogares, jardines infantiles y demás espacios de cuidado pueden ocurrir situaciones cotidianas como las siguientes:

    //- Ficha: caja (290,679) 1020x180 #DDEEFE SIN radio, con la lista numerada 1-4 (viñetas en x=322)
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4(data-aos="fade-down")
          ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
            li
              span.lista-ol--cuadro__vineta 1
              |  Una niña introduce una semilla o un objeto pequeño en la nariz mientras juega.
            li
              span.lista-ol--cuadro__vineta 2
              |  Un niño presenta inflamación y dificultad respiratoria después de la picadura de un insecto.
            li
              span.lista-ol--cuadro__vineta 3
              |  Una niña desarrolla una convulsión asociada con fiebre alta.
            li.mb-0
              span.lista-ol--cuadro__vineta 4
              |  Un niño ingiere accidentalmente un medicamento o producto de limpieza almacenado a su alcance.

    p.mt-4(data-aos="fade-down") Estas situaciones muestran la importancia de conservar la calma, proteger a la niña o al niño y evitar procedimientos improvisados. La intervención debe centrarse en reconocer los signos presentes, prevenir nuevos riesgos y solicitar ayuda profesional cuando la condición supere la capacidad de respuesta disponible.

    //- Ficha: badge (765,965) 70x70 #8EC5FC r=42 sobre la caja (290,1000) 1020x140 #DBC2FA r=10
    .row.justify-content-center.mt-5
      .col-lg-10
        .tarjeta--badge-arriba.bg-6(data-aos="fade-down")
          figure
            img(src="@/assets/curso/temas/t5/badge.svg" alt="")
          p.text-center.mb-0 La atención oportuna comienza con una observación cuidadosa. Reconocer qué ocurrió, cómo responde la niña o el niño y cuáles cambios requieren ayuda inmediata permite actuar con mayor seguridad.

    p.mt-5(data-aos="fade-down") El reconocimiento inicial de estas condiciones facilita la selección de medidas acordes con cada evento. Por ello, el siguiente apartado presenta las situaciones específicas que requieren primeros auxilios y las acciones básicas que pueden aplicarse mientras se obtiene atención especializada.

    Separador

    #t_5_1.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 5.1 Atención de situaciones específicas

    //- Ficha: texto a col-9 · foto (1122,1455) 292x247 -> col-3 · nota (186,1552) 916x150 #DDEEFE
    .row.align-items-start.mt-4
      .col-lg-9
        p(data-aos="fade-down") La atención de situaciones específicas comprende las medidas iniciales aplicadas ante eventos que pueden afectar repentinamente la salud de una niña o un niño. Su propósito es proteger la vida, disminuir la exposición al peligro y evitar que la condición se agrave mientras se solicita orientación o atención profesional.
        .bg-3.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Para actuar de manera segura, el primer respondiente debe identificar el evento, reconocer sus manifestaciones y valorar los posibles riesgos. No se deben realizar maniobras invasivas, administrar sustancias ni aplicar tratamientos que correspondan al personal de salud. La intervención debe limitarse a las acciones básicas para las cuales se cuenta con preparación.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t5/f3.png" alt="" style="width: 292px").m-auto

    p.mt-4(data-aos="fade-down") Las principales situaciones que requieren atención inicial son:

    //- Ficha: 4 pestañas (186, 1792/1858/1925/1991) 295x50 `r=5` —#B8F4CE y la abierta #16D95E— con
    //- el panel (498,1793) 916x248 y su icono de 84 dentro. Es `TabsA` del kit: col-xl-3 + col-xl-9,
    //- que da justo 295 y 916. Los TRES paneles que no se ven están en el pasteboard, en x=3035.
    TabsA.tabs--situaciones.mt-4
      .p-4(titulo="Cuerpos extraños")
        figure.mb-3
          img(src="@/assets/curso/temas/t5/ic1.svg" alt="" style="width: 84px")
        p.mb-0 Se presentan cuando un objeto ingresa en los ojos, la nariz, los oídos o la vía aérea. Pueden causar dolor, irritación, secreción, tos o dificultad respiratoria. No se debe manipular ni introducir otro elemento para extraerlo. Si el objeto no es visible, existe sangrado o se compromete la respiración, se requiere atención inmediata.
      .p-4(titulo="Picaduras y mordeduras")
        figure.mb-3
          img(src="@/assets/curso/temas/t5/ic2.svg" alt="" style="width: 84px")
        p.mb-0 Pueden ocasionar dolor, enrojecimiento, inflamación, prurito, infección o reacción alérgica. Se debe limpiar la zona, aplicar frío local protegido y observar la evolución. Ante hinchazón generalizada, dificultad respiratoria, alteración de la conciencia o mordedura de un animal desconocido, se debe solicitar atención médica inmediata.
      .p-4(titulo="Convulsiones")
        figure.mb-3
          img(src="@/assets/curso/temas/t5/ic3.svg" alt="" style="width: 84px")
        p.mb-0 Se manifiestan mediante movimientos involuntarios, rigidez, pérdida de respuesta o alteración de la conciencia. Se debe proteger a la niña o al niño de golpes, retirar los objetos cercanos y colocarlo de lado cuando sea posible. No se deben sujetar sus movimientos ni introducir objetos en la boca. Es importante controlar la duración del episodio.
      .p-4(titulo="Intoxicaciones")
        figure.mb-3
          img(src="@/assets/curso/temas/t5/ic4.svg" alt="" style="width: 84px")
        p.mb-0 Ocurren por contacto, inhalación o ingestión de medicamentos, sustancias químicas, productos de limpieza u otros elementos tóxicos. Se debe identificar el producto, conservar su envase y solicitar orientación especializada. No se debe inducir el vómito, ofrecer alimentos ni administrar remedios caseros, porque estas acciones pueden aumentar el daño.

    p.mt-4(data-aos="fade-down") El reconocimiento de estas situaciones permite aplicar medidas diferentes de acuerdo con el tipo de evento. En todos los casos, la observación continua resulta indispensable para detectar cambios en la respiración, la conciencia, la coloración de la piel o el comportamiento.

    //- Ficha: badge (765,2155) + caja (290,2190) 1020x140 #DBC2FA r=10
    .row.justify-content-center.mt-5
      .col-lg-10
        .tarjeta--badge-arriba.bg-6(data-aos="fade-down")
          figure
            img(src="@/assets/curso/temas/t5/badge.svg" alt="")
          p.text-center.mb-0 Ante una situación específica, intervenir de forma segura significa realizar solamente las acciones necesarias, evitar maniobras improvisadas y solicitar ayuda cuando aparezcan signos de gravedad.

    p.mt-5(data-aos="fade-down") Una vez atendido el evento inmediato, es necesario considerar otras alteraciones de salud que pueden manifestarse de manera progresiva. Entre ellas se encuentran las enfermedades prevalentes, cuyo reconocimiento favorece la consulta temprana y la prevención de complicaciones.

    //- Ficha: pastilla (186,2456) 520x50 #FFC0AC r=25 con el icono (201,2467) 28x28, que el XD llama
    //- `house-medical-solid-full`: el mismo `fa-house-medical` del Tema 3, con su asset ya exportado.
    .titulo-pastilla.mt-5(data-aos="fade-down")
      img(src="@/assets/curso/temas/ic-pastilla.png" alt="")
      span Enfermedades prevalentes en la primera infancia

    //- Ficha: texto a col-8 · foto (1018,2526) 396x261 -> col-4 · nota (186,2647) 812x140 #FFE6DE
    .row.align-items-start.mt-4
      .col-lg-8
        p(data-aos="fade-down") Las enfermedades prevalentes son condiciones de salud que se presentan con mayor frecuencia durante los primeros años de vida. Su aparición puede relacionarse con la inmadurez del sistema inmunológico, las condiciones del entorno, el acceso al agua segura, la alimentación, la higiene, la vacunación y la exposición a agentes infecciosos.
        .bg-1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 El primer respondiente no tiene la función de diagnosticar ni tratar estas enfermedades. Su responsabilidad consiste en reconocer cambios que puedan indicar deterioro, brindar una atención inicial segura y orientar a la familia o al cuidador sobre la necesidad de acudir a los servicios de salud.
      .col-lg-4.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t5/f4.png" alt="" style="width: 396px").m-auto

    p.mt-4(data-aos="fade-down") En el contexto colombiano, algunas condiciones ambientales, sociales y sanitarias pueden aumentar la aparición de enfermedades durante la primera infancia. Entre ellas se encuentran:

    //- Ficha: caja (290,2890) 1020x467 #DDEEFE SIN radio, padding 20/30/45/36
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ul.lista-ul--compacta
            li
              i.fas.fa-heart
              span #[b Temporadas de lluvia:] durante las lluvias aumenta la exposición a humedad, aguas estancadas y vectores, lo cual favorece enfermedades respiratorias, gastrointestinales e infecciosas.
            li
              i.fas.fa-heart
              span #[b Cambios de temperatura:] los cambios de temperatura pueden debilitar las defensas y favorecer tos, congestión, fiebre o dificultad respiratoria en niñas y niños.
            li
              i.fas.fa-heart
              span #[b Espacios comunitarios:] la permanencia en jardines, hogares comunitarios u otros espacios compartidos facilita el contacto con personas enfermas y agentes infecciosos circulantes.
            li
              i.fas.fa-heart
              span #[b Agua o alimentos contaminados:] el consumo de agua o alimentos contaminados puede causar diarrea, vómito, dolor abdominal y deshidratación, especialmente durante la primera infancia.
            li
              i.fas.fa-heart
              span #[b Vacunación incompleta:] los esquemas de vacunación incompletos reducen la protección frente a enfermedades prevenibles y aumentan el riesgo de complicaciones graves posteriores.
            li.mb-0
              i.fas.fa-heart
              span.mb-0 #[b Dificultades de acceso:] las dificultades para acceder a controles médicos retrasan la detección de alteraciones y el inicio oportuno del tratamiento profesional requerido.

    p.mt-4(data-aos="fade-down") El reconocimiento de estas condiciones permite fortalecer las acciones preventivas en el hogar y orientar oportunamente la consulta ante cambios en la salud.

    p(data-aos="fade-down") Antes de describir las principales patologías, es importante reconocer que cada una presenta manifestaciones particulares y puede afectar de manera diferente el bienestar de las niñas y los niños. Su clasificación facilita la comprensión de los síntomas más frecuentes y orienta la identificación oportuna de los cambios que requieren valoración por parte del personal de salud.

    Separador

    #t_5_2.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 5.2 Principales enfermedades prevalentes

    //- Ficha: foto (186,3745) 292x416 -> col-3 · texto y caja (498,3842) 916x320 #F4EDFE -> col-9,
    //- con la lista de letras A-F (viñetas en x=540)
    .row.align-items-start.mt-4
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t5/f5.png" alt="" style="width: 292px").m-auto
      .col-lg-9
        p(data-aos="fade-down") Durante la primera infancia, algunas enfermedades pueden iniciar con manifestaciones leves y evolucionar rápidamente. Por ello, es fundamental observar de manera continua el estado general de la niña o del niño e identificar cambios que indiquen la necesidad de una valoración profesional. Para orientar esta observación, se deben considerar los siguientes aspectos:
        .bg-2.p-4.mt-4(data-aos="fade-down")
          ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
            li
              span.lista-ol--cuadro__vineta A
              |  #[b Respiración:] identificar dificultad, sonidos inusuales o cambios en el ritmo respiratorio.
            li
              span.lista-ol--cuadro__vineta B
              |  #[b Hidratación:] observar sequedad en la boca, ausencia de lágrimas o disminución de la orina.
            li
              span.lista-ol--cuadro__vineta C
              |  #[b Temperatura corporal:] reconocer fiebre persistente, temperatura baja o variaciones repentinas.
            li
              span.lista-ol--cuadro__vineta D
              |  #[b Piel:] verificar cambios de coloración, erupciones, inflamación o aparición de lesiones.
            li
              span.lista-ol--cuadro__vineta E
              |  #[b Alimentación:] prestar atención al rechazo de alimentos o líquidos y a la pérdida del apetito.
            li.mb-0
              span.lista-ol--cuadro__vineta F
              |  #[b Comportamiento:] reconocer somnolencia excesiva, irritabilidad, debilidad o menor respuesta a los estímulos.

    p.mt-4(data-aos="fade-down") La observación conjunta de estos aspectos permite detectar oportunamente un posible deterioro de la salud y solicitar la atención necesaria, sin establecer diagnósticos ni administrar tratamientos por iniciativa propia.

    p(data-aos="fade-down") Antes de explorar las principales enfermedades prevalentes, es importante reconocer que cada una puede afectar de manera diferente la salud de las niñas y los niños. El siguiente recurso interactivo permite conocer sus características, manifestaciones y principales medidas de prevención, así como identificar los cambios que requieren valoración oportuna por parte del personal de salud.

    //- Ficha: el bloque (289,4399) 1020x590 #FFE6DE con seis píldoras #8EC5FC 153x60 y seis «+».
    //- El XD lo rotula `INFOGRAFIA PUNTOS CALIENTES` en el pasteboard (2982,-7967) y debajo trae los
    //- SEIS textos. La imagen base va sin las píldoras ni los «+»: los pinta el componente. Los x/y
    //- son % del contenedor, medidos sobre los nodos «+» y confirmados en la propia base.
    .row.justify-content-center.mt-4
      .col-lg-10
        ImagenInfografica.color-acento-botones.d-none.d-md-block
          template(v-slot:imagen)
            figure
              img(src="@/assets/curso/temas/t5/info.svg" alt="").w-100
          .tarjeta.color-primario.p-3(x="11.5%" y="39%" numero="+")
            .h5.mb-2 Enfermedades respiratorias
            p.mb-0 Son una de las principales causas de consulta y hospitalización en la primera infancia; incluyen resfriado común, bronquiolitis y neumonía, causa importante de mortalidad infantil mundial.
          .tarjeta.color-primario.p-3(x="27%" y="71%" numero="+")
            .h5.mb-2 Enfermedades gastrointestinales
            p.mb-0 Las enfermedades diarreicas agudas son frecuentes en la infancia y se asocian a infecciones virales, bacterianas o parasitarias; su riesgo principal es la deshidratación por pérdida de líquidos y electrolitos.
          .tarjeta.color-primario.p-3(x="42.5%" y="39%" numero="+")
            .h5.mb-2 Alteraciones nutricionales
            p.mb-0 La desnutrición y la anemia constituyen un problema de salud pública en la primera infancia; la desnutrición afecta el crecimiento y el desarrollo cognitivo, y la anemia afecta el aprendizaje.
          .tarjeta.color-primario.p-3(x="58%" y="71%" numero="+")
            .h5.mb-2 Enfermedades parasitarias
            p.mb-0 Las parasitosis intestinales son frecuentes donde existen deficiencias en saneamiento básico e higiene; generan síntomas como dolor abdominal, diarrea, pérdida de peso y alteraciones nutricionales en la infancia.
          .tarjeta.color-primario.p-3(x="73.4%" y="39%" numero="+")
            .h5.mb-2 Enfermedades dermatológicas
            p.mb-0 Las afecciones de la piel en la primera infancia incluyen dermatitis e infecciones bacterianas o micóticas, asociadas a condiciones de higiene, humedad o irritación, frecuentes en jardines infantiles.
          .tarjeta.color-primario.p-3(x="89%" y="71%" numero="+")
            .h5.mb-2 Enfermedades inmunoprevenibles
            p.mb-0 Enfermedades como sarampión, tosferina y varicela siguen representando un riesgo en poblaciones infantiles con esquemas de inmunización incompletos o atrasados en Colombia.
        figure.d-md-none
          img(src="@/assets/curso/temas/t5/1.svg" alt="").w-100


    //- Ficha: icono (186,5167) 84x84 con el texto en x=290 · ilustración (1122,5072) 292x185 -> col-3
    .row.align-items-center.mt-4
      .col-lg-9
        p(data-aos="fade-down") El reconocimiento de las enfermedades prevalentes en la primera infancia favorece la prevención y la detección temprana de cambios en el estado de salud. La observación de signos y síntomas, junto con el acceso oportuno a los servicios de salud, permite orientar una atención adecuada y reducir el riesgo de complicaciones.
        .row.align-items-start
          .col-auto.mb-3.mb-lg-0
            figure
              img(src="@/assets/curso/temas/t5/ic5.svg" alt="" style="width: 84px")
          .col
            p.mb-0(data-aos="fade-down") Además de identificar las manifestaciones de estas enfermedades, es fundamental reconocer aquellas señales que pueden indicar un deterioro de la salud. A continuación, se abordan los principales signos de alarma y las acciones iniciales que deben realizarse ante su aparición.
      .col-lg-3.mt-4.mt-lg-0
        figure.m-0
          img(src="@/assets/curso/temas/t5/ilus1.svg" alt="").w-100

    Separador

    #t_5_3.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 5.3 Signos de alarma

    //- Ficha: texto a col-9 · foto (1122,5493) 292x357 -> col-3 · nota (186,5590) 916x260 #DDEEFE
    //- con el icono (226,5620) 84x84 ENCIMA del texto (226,5734)
    .row.align-items-start.mt-4
      .col-lg-9
        p(data-aos="fade-down") Durante la primera infancia, algunas alteraciones de salud pueden evolucionar rápidamente y comprometer el bienestar de la niña o del niño. Los signos de alarma son manifestaciones que permiten reconocer un posible deterioro y orientan la necesidad de solicitar atención profesional prioritaria o activar inmediatamente el sistema de emergencias.
        .bg-3.p-4.mt-4(data-aos="fade-down")
          figure.mb-3
            img(src="@/assets/curso/temas/t5/ic6.svg" alt="" style="width: 84px")
          p.mb-0 La observación debe centrarse en los cambios relacionados con la respiración, el estado de conciencia, la hidratación, la temperatura corporal, la circulación, la alimentación y el comportamiento. Para reconocer una situación que requiere atención, no es necesario establecer un diagnóstico; se debe identificar cualquier manifestación inusual y valorar su evolución.
      .col-lg-3.mt-4.mt-lg-0
        figure
          img(src="@/assets/curso/temas/t5/f6.png" alt="" style="width: 292px").m-auto

    //- Ficha: badge (765,5880) + caja (290,5915) 1020x160 #DBC2FA r=10
    .row.justify-content-center.mt-5
      .col-lg-10
        .tarjeta--badge-arriba.bg-6(data-aos="fade-down")
          figure
            img(src="@/assets/curso/temas/t5/badge.svg" alt="")
          p.text-center.mb-0 El reconocimiento temprano de los signos de alarma permite solicitar atención oportuna y reducir el riesgo de complicaciones. Estas manifestaciones no deben minimizarse ni tratarse mediante medicamentos o procedimientos sin orientación profesional.

    p.mt-5(data-aos="fade-down") Los principales signos de alarma y las conductas iniciales que deben aplicarse son:

    //- Ficha: banda (136,6171) 1328x747 · tarjeta blanca 1263x585 · foto de cada slide 560x309 con el
    //- marco de 12px. Los SEIS estados que no se ven están en el pasteboard, en x=3537.
    .row.bg-banda-t5-53.mt-4
      .col-12
        .tarjeta.tarjeta--blanca.p-4.p-md-5
          SlyderA.slyder-a--curso(tipo="b")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Dificultad respiratoria:] la respiración rápida, el hundimiento entre las costillas, el aleteo nasal, los sonidos inusuales o la coloración azulada pueden indicar falta de oxígeno. Se debe mantener despejada la vía aérea, ubicar a la niña o al niño en una posición que facilite la respiración y evitar ofrecer alimentos o bebidas. Es necesario activar inmediatamente el sistema de emergencias y observar cualquier cambio mientras llega el personal especializado.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t5/f8.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Alteraciones neurológicas:] las convulsiones, la somnolencia excesiva, la irritabilidad persistente o la falta de respuesta pueden relacionarse con fiebre, infección, traumatismo u otra alteración grave. Se debe proteger a la niña o al niño de posibles golpes, retirar los objetos cercanos y colocarlo de lado cuando sea posible. No se deben sujetar sus movimientos ni introducir elementos en la boca. También es necesario controlar la duración del episodio y solicitar atención inmediata.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t5/s2.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Deshidratación:] el vómito persistente, la diarrea frecuente, el rechazo de líquidos, la boca seca, los ojos hundidos o la ausencia de lágrimas pueden indicar pérdida importante de líquidos. Si la niña o el niño está consciente y puede beber, se deben ofrecer pequeñas cantidades de solución de rehidratación oral. No se deben administrar medicamentos ni preparaciones caseras sin orientación profesional. Si las manifestaciones persisten o empeoran, se requiere valoración médica inmediata.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t5/s3.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Alteraciones de la temperatura:] la fiebre persistente, la temperatura corporal baja o el decaimiento general pueden indicar una infección u otra condición que requiere valoración. Se debe comprobar la temperatura, retirar el exceso de abrigo y mantener un ambiente ventilado. No se recomienda aplicar alcohol, hielo ni baños con agua fría. Si aparecen convulsiones, somnolencia, dificultad respiratoria o deterioro progresivo, se debe solicitar atención profesional de inmediato.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t5/s4.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Alteraciones circulatorias:] la palidez marcada, la piel fría, el pulso débil o la recuperación lenta del color de la piel pueden indicar una alteración de la circulación. La niña o el niño debe permanecer en reposo, abrigado y bajo vigilancia continua. No se deben ofrecer alimentos ni bebidas. Se debe activar el sistema de emergencias y observar permanentemente la respiración, el estado de conciencia y la coloración mientras llega el personal especializado.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t5/s5.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Alteraciones nutricionales:] la pérdida de peso, la falta de crecimiento, la debilidad o el rechazo persistente de los alimentos pueden relacionarse con una alteración nutricional u otra enfermedad. Se debe observar cuánto tiempo lleva la dificultad, registrar los cambios en el apetito e informar a la familia o al cuidador. No se debe forzar la alimentación. La valoración médica y nutricional permitirá identificar la causa y establecer el seguimiento correspondiente.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t5/s6.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Cambios de comportamiento:] el llanto inconsolable, la debilidad extrema, la irritabilidad o una conducta diferente de la habitual pueden indicar dolor o enfermedad. Se debe identificar cuándo comenzaron los cambios y observar si están acompañados de fiebre, golpes, dificultad respiratoria u otras manifestaciones. No se deben atribuir únicamente al cansancio. Si persisten, empeoran o se acompañan de menor respuesta a los estímulos, se requiere atención médica inmediata.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t5/s7.png" alt="")

    //- Ficha: foto (186,6782) 292x247 -> col-3 · nota (498,6782) 916x247 #FFE6DE r=10 con el icono
    //- (534,6818) 84x84 ENCIMA del texto (534,6932)
    .row.align-items-start.mt-5
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t5/f9.png" alt="" style="width: 292px").m-auto
      .col-lg-9
        .bg-1.r-10.p-4(data-aos="fade-down")
          figure.mb-3
            img(src="@/assets/curso/temas/t5/ic7.svg" alt="" style="width: 84px")
          p.mb-0 La valoración conjunta de estas manifestaciones permite determinar la urgencia de la atención. Al comunicarse con el personal de salud, se debe informar claramente qué ocurrió, cuándo comenzaron los signos, cómo han evolucionado y qué medidas iniciales se aplicaron.

    p.mt-4(data-aos="fade-down") Ante cualquier signo de alarma, se debe mantener la calma, vigilar permanentemente el estado de la niña o del niño y solicitar ayuda. La actuación oportuna debe proteger su salud sin reemplazar la valoración del personal especializado.

    //- Ficha: caja (290,7132) 1020x120 #DDEEFE con la pestaña de 25x8 #8EC5FC encima a la izquierda
    //- -> es el ÚNICO `.cajon` del tema. Lo cazó el check 4b: 1 pestaña en el XD, 0 maquetados.
    .row.justify-content-center.mt-4
      .col-lg-10
        .cajon.color1.p-4(data-aos="fade-down")
          p.mb-0 El reconocimiento de los signos de alarma debe complementarse con una comunicación clara y oportuna. Informar adecuadamente la situación, acompañar emocionalmente a la niña o al niño y seguir las indicaciones del sistema de emergencias contribuye a brindar una atención inicial segura.

</template>

<script>
export default {
  name: 'Tema5',
}
</script>
