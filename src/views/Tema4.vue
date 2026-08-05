<template lang="pug">
.curso-main-container.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5
    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span 4
      h1 Lesiones, traumatismos y movilización

    p(data-aos="fade-down") Este eje temático aborda la atención inicial de heridas, hemorragias y quemaduras; el manejo de lesiones osteomusculares y traumatismos; y las técnicas para movilizar y trasladar de manera segura a la niña o al niño que presenta una lesión. Según las características del evento, estos procedimientos pueden complementarse para brindar una respuesta organizada y prevenir complicaciones.

    //- Ficha: ilustración (185,410) 292x245 -> col-3 · caja (497,410) 916x245 #FFE6DE r=10 -> col-9,
    //- con el icono (533,446) 84x84 ENCIMA del texto (533,560), no al lado.
    .row.align-items-center.mt-4
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t4/ilus1.svg" alt="").w-100
      .col-lg-9
        .bg-1.r-10.p-4(data-aos="fade-down")
          figure.mb-3
            img(src="@/assets/curso/temas/t4/ic1.svg" alt="" style="width: 84px")
          p.mb-0 Ante estas situaciones, el primer respondiente debe conservar la calma, identificar el tipo de lesión y aplicar las medidas iniciales pertinentes. Una actuación oportuna contribuye a evitar el agravamiento de la condición de la niña o del niño mientras se gestiona la ayuda necesaria.

    p.mt-4(data-aos="fade-down") Asimismo, es fundamental valorar el estado general de la niña o del niño, observar la zona afectada y evitar movimientos que puedan agravar la lesión. Esta valoración permite reconocer señales de alarma y determinar la necesidad de recibir atención especializada.

    p(data-aos="fade-down") Estas situaciones pueden presentarse con frecuencia en los entornos cotidianos de la primera infancia. Algunos ejemplos son los siguientes:

    //- Ficha: tres paneles PEGADOS (187,804) 405x413 #8EC5FC r=[20,0,0,20], (592,804) 419x413
    //- #DBC2FA sin radio y (1010,804) 405x413 #FFE6DE redondeado por la derecha. El icono va DENTRO
    //- de la tarjeta, en su círculo blanco de 150 (`Grupo 1177470..72`), no montado sobre el borde.
    .tarjeta--container.row.mt-4
      .col-md.tarjeta.bg-4.p-5
        .row.justify-content-center.mb-4
          .col-6
            figure
              img(src="@/assets/curso/temas/t4/i1.svg" alt="").w-100
        h4.text-center Caídas durante el juego
        p.mb-0 Pueden ocurrir en el parque o en el patio de un hogar comunitario y ocasionar heridas, golpes o lesiones que requieren valoración inicial.
      .col-md.tarjeta.bg-6.p-5
        .row.justify-content-center.mb-4
          .col-6
            figure
              img(src="@/assets/curso/temas/t4/i2.svg" alt="").w-100
        h4.text-center Contacto con líquidos calientes
        p.mb-0 Puede producir quemaduras en la cocina u otros espacios del hogar y requiere una actuación inmediata para disminuir el daño.
      .col-md.tarjeta.bg-1.p-5
        .row.justify-content-center.mb-4
          .col-6
            figure
              img(src="@/assets/curso/temas/t4/i3.svg" alt="").w-100
        h4.text-center Torceduras durante las actividades recreativas
        p.mb-0 Pueden afectar las articulaciones y exigir la inmovilización de la zona lesionada y un traslado seguro para evitar complicaciones.

    p.mt-5(data-aos="fade-down") Reconocer estos eventos permite identificar los posibles riesgos y aplicar las medidas iniciales correspondientes. En el siguiente apartado, se presentan las características de las heridas, las hemorragias y las quemaduras, junto con las acciones básicas para brindar una atención segura.

    Separador

    #t_4_1.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 4.1 Atención de lesiones en primeros auxilios

    p(data-aos="fade-down") Las heridas, las hemorragias y las quemaduras pueden afectar la piel y otros tejidos. Reconocer sus características permite brindar una atención inicial segura, prevenir complicaciones y solicitar ayuda especializada cuando sea necesario.

    p(data-aos="fade-down") Las principales lesiones y sus medidas de atención inicial son las siguientes:

    //- Ficha: abierto (290,1654) 1020x190 #F4EDFE r=20 y dos cerrados 1020x90 #B8F4CE r=20, con el
    //- botón circular verde #16D95E r=24 a la derecha -> es la `.acordion--principios` que ya existe.
    .row.justify-content-center.mt-4
      .col-lg-10
        AcordionA.acordion--principios(tipo="b")
          .row(titulo="Heridas")
            .col-12
              p.mb-0 Son lesiones que afectan la piel o los tejidos y pueden producir cortes, raspaduras, dolor o sangrado. Por ejemplo, una niña puede rasparse la rodilla al caer en el parque. Se debe limpiar la zona con agua, cubrirla con una gasa o material limpio y evitar su manipulación. Si la herida es profunda, contiene un objeto incrustado o continúa sangrando, se debe solicitar atención médica.
          .row(titulo="Hemorragias")
            .col-12
              p.mb-0 Corresponden a la pérdida de sangre ocasionada por la ruptura de uno o varios vasos sanguíneos. Por ejemplo, un niño puede presentar un sangrado abundante después de cortarse con un objeto afilado. Se debe ejercer presión directa sobre la herida con una gasa o tela limpia. Si existe un objeto incrustado, no debe retirarse; la presión se aplica alrededor de este.
          .row(titulo="Quemaduras")
            .col-12
              p.mb-0 Son lesiones causadas por el calor, las sustancias químicas, la electricidad o la radiación. Por ejemplo, un lactante puede quemarse al entrar en contacto con un líquido caliente. Se debe retirar la fuente que ocasionó la lesión y enfriar la zona con agua corriente fresca durante 20 minutos. No se deben aplicar hielo, cremas ni remedios caseros, ni romper las ampollas. Posteriormente, la zona se cubre suavemente con una gasa o material limpio.

    p.mt-5(data-aos="fade-down") Durante la atención, se debe conservar la calma y observar señales de alarma, como sangrado que no se detiene, dolor intenso, dificultad para respirar, pérdida de respuesta o quemaduras extensas. Ante estas manifestaciones, se debe activar el sistema de emergencias mediante la línea 123.

    //- Ficha: nota (185,2181) 916x130 #F4EDFE r=10 -> col-9 · ilustración (1121,2084) 292x227 -> col-3
    .row.align-items-center.mt-4
      .col-lg-9.mb-4.mb-lg-0
        .bg-2.r-10.p-4(data-aos="fade-down")
          p.mb-0 La aplicación adecuada de estas medidas contribuye a controlar la lesión y prevenir complicaciones. En el siguiente apartado, se presentan las acciones iniciales para reconocer y manejar las lesiones osteomusculares ocasionadas por caídas, golpes u otros traumatismos.
      .col-lg-3
        figure
          img(src="@/assets/curso/temas/t4/ilus2.svg" alt="").w-100

    Separador

    #t_4_2.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 4.2 Manejo de lesiones osteomusculares

    //- Ficha: foto (185,2553) 396x281 -> col-4 · nota (601,2674) 812x160 #DDEEFE r=10 con el icono
    //- (631,2712) 84x84 a la IZQUIERDA del texto (743,2697)
    .row.align-items-start.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t4/f2.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p(data-aos="fade-down") El manejo de lesiones en la primera infancia comprende las acciones orientadas a estabilizar, proteger y evitar el agravamiento de lesiones que comprometen estructuras como huesos, articulaciones, tejidos blandos y sistema neurológico. Estas lesiones pueden derivarse de caídas, golpes, accidentes o situaciones de riesgo en el entorno, siendo frecuentes en esta etapa del desarrollo (Organización Mundial de la Salud, 2020).
        .bg-3.r-10.p-4.mt-4(data-aos="fade-down")
          .row.align-items-start
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t4/ic2.svg" alt="" style="width: 84px")
            .col
              p.mb-0 La intervención del primer respondiente debe centrarse en la identificación de signos de gravedad, la limitación del movimiento, la protección de la zona afectada y la preparación para un traslado seguro, evitando maniobras que puedan generar daño adicional. La actuación oportuna permite disminuir complicaciones y favorecer la recuperación de la niña o del niño.

    p.mt-4(data-aos="fade-down") Para facilitar la comprensión y orientar la toma de decisiones, la siguiente tabla presenta las principales lesiones osteomusculares y traumáticas, su definición, los signos principales, el manejo inicial y las acciones que deben evitarse en cada caso.

    //- Ficha: encabezado (290,3001) 1020x52 #FFC0AC y 5 filas de 78/58 alternando #F6F6F6 y blanco.
    //- Divisores del PDF en 498, 706, 913 y 1101 -> ver `.tabla--traslado` en _custom.sass.
    .row.justify-content-center.mt-4
      .col-lg-10
        .titulo-sexto.color-acento-contenido.mb-3
          h5 Tabla 3.
          span Manejo inicial de esguinces, luxaciones, fracturas y trauma
        .tabla-a.tabla--traslado.color-acento-contenido(data-aos="fade-down")
          table
            thead
              tr
                th Tipo de lesión
                th Definición
                th Signos principales
                th Manejo inicial
                th Acción que debe evitarse
            tbody
              tr
                td Esguince
                td Lesión de los ligamentos causada por un estiramiento o desgarro.
                td Dolor, inflamación y dificultad para mover o apoyar la articulación.
                td Mantener la zona en reposo e inmovilizarla para evitar el agravamiento de la lesión.
                td No masajear ni forzar el movimiento de la articulación.
              tr
                td Luxación
                td Desplazamiento de un hueso fuera de su posición normal en una articulación.
                td Dolor intenso, deformidad visible e imposibilidad para mover la articulación.
                td Inmovilizar la zona en la posición encontrada y solicitar atención médica.
                td No recolocar el hueso ni corregir la deformidad.
              tr
                td Fractura
                td Ruptura parcial o total de un hueso.
                td Dolor intenso, inflamación, deformidad y dificultad para mover la zona afectada.
                td Inmovilizar la extremidad, evitar movimientos innecesarios y gestionar el traslado a un servicio de salud.
                td No enderezar la extremidad ni presionar directamente sobre el hueso lesionado.
              tr
                td Trauma craneoencefálico
                td Lesión en la cabeza que puede comprometer el cerebro.
                td Pérdida de conciencia, vómito, somnolencia, irritabilidad o cambios en el comportamiento.
                td Mantener a la niña o al niño en reposo, vigilar su respuesta y activar el sistema de emergencias.
                td No moverlo ni suministrarle alimentos, bebidas o medicamentos.
              tr
                td Traumatismo cervical
                td Lesión en la región del cuello que puede comprometer la médula espinal.
                td Dolor, limitación del movimiento, pérdida de sensibilidad o alteraciones en las extremidades.
                td Mantener alineadas la cabeza y el cuello, evitar la movilización y solicitar atención especializada.
                td No girar, levantar ni sentar a la niña o al niño.

    p.mt-4(data-aos="fade-down") Las medidas descritas permiten proteger la zona afectada mientras llega la atención especializada. Durante la valoración, se debe evitar cualquier maniobra que aumente el dolor o pueda agravar la lesión.

    p(data-aos="fade-down") Además del manejo específico de cada lesión, se deben considerar las siguientes recomendaciones generales:

    //- Ficha: caja (290,3575) 1020x317 #DDEEFE SIN radio, padding 20/30/40/30
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4.p-md-5(data-aos="fade-down")
          ul.lista-ul.lista-ul--compacta
            li
              i.fas.fa-heart
              span #[b Conservar la calma:] brindar seguridad a la niña o al niño y explicarle, con palabras sencillas, que recibirá ayuda.
            li
              i.fas.fa-heart
              span #[b Evitar movimientos innecesarios:] mantener la zona lesionada en la posición encontrada y no intentar corregir deformidades.
            li
              i.fas.fa-heart
              span #[b Inmovilizar la lesión:] utilizar elementos adecuados para limitar el movimiento, sin ejercer una presión excesiva ni afectar la circulación.
            li
              i.fas.fa-heart
              span #[b Observar las señales de alarma:] identificar dolor intenso, deformidad, pérdida de conciencia, vómito persistente, dificultad para respirar o alteraciones del movimiento.
            li.mb-0
              i.fas.fa-heart
              span.mb-0 #[b Solicitar atención especializada:] activar el sistema de emergencias mediante la línea 123 cuando se presenten signos de gravedad.

    .row.justify-content-center.mt-4
      .col-lg-10
        p(data-aos="fade-down") La aplicación adecuada de estas recomendaciones ayuda a prevenir complicaciones y protege a la niña o al niño mientras recibe atención especializada. No se deben enderezar extremidades, recolocar articulaciones ni efectuar traslados innecesarios.
        p.mb-0(data-aos="fade-down") Después de reconocer el manejo inicial de las lesiones osteomusculares, es necesario comprender cómo actuar ante otros traumatismos que pueden comprometer diferentes partes del cuerpo. En el siguiente apartado, se presentan las medidas correspondientes.

    Separador

    #t_4_3.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 4.3 Manejo de traumas

    //- Ficha: foto (185,4287) 292x227 -> col-3 · nota (497,4384) 916x130 #FFE6DE r=10 -> col-9
    .row.align-items-start.mt-4
      .col-lg-3.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t4/f3.png" alt="" style="width: 292px").m-auto
      .col-lg-9
        p(data-aos="fade-down") El manejo de traumas en la primera infancia reúne las acciones iniciales destinadas a atender lesiones causadas por caídas, golpes, accidentes u otras fuerzas externas. Estas situaciones pueden afectar distintas partes del cuerpo y requieren una intervención oportuna para disminuir el riesgo de agravamiento y prevenir posibles complicaciones.
        .bg-1.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 Debido a las características físicas propias de esta etapa, las niñas y los niños pueden presentar mayor vulnerabilidad ante algunas lesiones. Por ello, la atención debe realizarse con cuidado, evitando movimientos innecesarios y observando permanentemente cualquier cambio en su estado general.

    //- Ficha: icono (185,4544) 84x84 SUELTO, sin caja detrás: el SVG ya trae su cuadro salmón.
    .row.align-items-start.mt-4
      .col-auto.mb-3.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t4/ic3.svg" alt="" style="width: 84px")
      .col
        p.mb-0(data-aos="fade-down") El primer respondiente debe identificar el tipo de trauma, valorar la gravedad de la lesión y actuar de manera segura, priorizando la inmovilización, la protección de la zona afectada y la estabilidad de la niña o del niño. La intervención debe evitar movimientos innecesarios que puedan agravar el daño, especialmente en casos de compromiso de cabeza, cuello o columna.

    p.mt-4(data-aos="fade-down") Para orientar una atención segura, es necesario reconocer las características de la lesión y la zona del cuerpo comprometida. En la primera infancia, los golpes o las caídas pueden afectar especialmente la cabeza y el cuello; por ello, resulta fundamental diferenciar los tipos de trauma, reconocer sus signos de alarma y aplicar las medidas iniciales correspondientes, sin realizar movimientos que puedan agravar el daño. Con este propósito, se presentan las características y las medidas de atención inicial de los siguientes traumas:

    //- Ficha: (289,4779) y (289,4929) 1020x150 — son `Trazado`, no `rect`, y por eso no salían en la
    //- ficha hasta arreglar `mapa_bloques.py`. #DDEEFE y #F4EDFE, con el círculo lila de 84 a la izq.
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t4/i4.svg" alt="" style="width: 84px")
            .col
              p.mb-0 #[b Trauma craneoencefálico:] corresponde a una lesión en la cabeza que puede afectar el cerebro y alterar el estado general de la niña o el niño. Por ejemplo, después de una caída desde una cama, si presenta vómito repetido, somnolencia, convulsiones o cambios en el comportamiento, se deben evitar movimientos bruscos, vigilar su estado y solicitar atención especializada.
        .bg-2.p-4.mt-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t4/i5.svg" alt="" style="width: 84px")
            .col
              p.mb-0 #[b Trauma cervical:] corresponde a una lesión que puede comprometer las estructuras del cuello y la parte superior de la columna vertebral. Por ejemplo, si después de una caída la niña o el niño manifiesta dolor cervical, dificultad para mover el cuello, debilidad o pérdida de sensibilidad, se debe mantener la cabeza inmóvil y solicitar ayuda especializada, sin intentar cambiar su posición.

    p.mt-4(data-aos="fade-down") El reconocimiento de estos traumatismos permite identificar oportunamente los signos de alarma y aplicar medidas iniciales que reduzcan el riesgo de agravar la lesión. Sin embargo, cuando sea indispensable desplazar a la niña o al niño, se deben emplear técnicas seguras que protejan las zonas afectadas y mantengan la estabilidad corporal durante la movilización y el traslado.

    Separador

    #t_4_4.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 4.4 Movilización y traslado del lesionado

    //- Ficha: foto (185,5426) 396x261 -> col-4 · nota (601,5426) 812x140 #DDEEFE r=10 con el icono
    //- (631,5454) 84x84 a la izquierda
    .row.align-items-start.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t4/f4.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        .bg-3.r-10.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t4/ic4.svg" alt="" style="width: 84px")
            .col
              p.mb-0 La movilización y el traslado comprenden las acciones utilizadas para desplazar de forma segura a una persona lesionada. En la primera infancia, estas intervenciones requieren de especial cuidado, debido a que un movimiento inadecuado puede agravar la lesión, afectar otras zonas del cuerpo o generar complicaciones durante la atención inicial.
        p.mt-4.mb-0(data-aos="fade-down") Antes de movilizar a la niña o al niño, se debe valorar la seguridad del entorno, el tipo de lesión y la necesidad real del desplazamiento. Cuando el lugar no representa un peligro, se recomienda mantener a la persona en una posición estable, evitar movimientos innecesarios y esperar la llegada del personal especializado. Según las condiciones identificadas, pueden presentarse las siguientes situaciones:

    //- Ficha: (289,5717) #DDEEFE y (289,5847) #F4EDFE, 1020x130, con el círculo lila de 84
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-3.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t4/i6.svg" alt="" style="width: 84px")
            .col
              p.mb-0 #[b Movilización de emergencia:] se realiza cuando permanecer en el lugar representa un riesgo mayor que mover a la niña o al niño. Por ejemplo, si ocurre un incendio o una fuga de gas en la vivienda, se debe trasladar a un sitio seguro, protegiendo cabeza, cuello y cuerpo durante el desplazamiento.
        .bg-2.p-4.mt-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t4/i7.svg" alt="" style="width: 84px")
            .col
              p.mb-0 #[b Movilización no urgente:] se efectúa cuando el entorno es seguro y no existe amenaza inmediata. Por ejemplo, si una niña cae mientras juega en la sala y presenta dolor en una pierna, se debe evitar moverla, inmovilizar la zona, acompañarla y esperar la llegada del personal especializado antes de trasladarla.

    p.mt-4(data-aos="fade-down") La identificación adecuada de cada situación permite evitar desplazamientos innecesarios y seleccionar una actuación acorde con el riesgo presente. En los hogares colombianos, mantener despejadas las rutas de salida, conservar la calma y solicitar apoyo especializado contribuye a proteger a la niña o al niño durante una emergencia.

    //- Ficha: (289,6080) 1020x100 #DDEEFE con la pestaña de 25x8 #8EC5FC -> el ÚNICO `.cajon` del tema
    .row.justify-content-center.mt-4
      .col-lg-10
        .cajon.color1.p-4(data-aos="fade-down")
          p.mb-0 Para efectuar cualquier desplazamiento indispensable, se deben aplicar criterios que reduzcan el riesgo de movimientos bruscos y protejan las zonas lesionadas. Estos criterios constituyen la base de los principios de la movilización segura.

    Separador

    #t_4_5.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 4.5 Principios de la movilización segura

    //- Ficha: foto (185,6422) 614x257 · panel (494,6422) 919x257 #8EC5FC · tarjeta blanca
    //- (684,6467) 685x168 montada encima -> es el `.bloque-texto-g` del kit, no se arma a mano.
    .bloque-texto-g.color-primario.p-3.p-sm-4.p-md-5.mt-4
      .bloque-texto-g__img(:style="{'background-image': `url(${require_src('@/assets/curso/temas/t4/f5.png')})`}")
      .bloque-texto-g__texto.p-4
        p.mb-0 La movilización segura se fundamenta en principios orientados a proteger a la niña o al niño lesionado durante un desplazamiento indispensable. Su aplicación permite reducir el riesgo de agravar las lesiones, especialmente cuando existe una posible afectación en la cabeza, el cuello, la columna vertebral o las extremidades.

    p.mt-4(data-aos="fade-down") Antes de iniciar cualquier movimiento, se deben valorar las condiciones del entorno, el estado general de la persona lesionada y la necesidad real de trasladarla. Asimismo, es fundamental actuar con calma, solicitar apoyo cuando sea necesario y mantener una comunicación clara entre quienes participan. Para orientar esta actuación, se consideran los siguientes principios:

    //- Ficha: banda (136,6807) 1328x747 · tarjeta blanca 1263x585 · foto de cada slide 560x309 con el
    //- marco de 12px (#8EC5FC 584x330 + #DBC2FA 214x330). Los 4 estados que no se ven están en el
    //- PASTEBOARD, en x=521 y=-4808/-4448/-4088/-3728, con su foto.
    .row.bg-banda-t4-45.mt-4
      .col-12.p-4.p-md-5
        .tarjeta.tarjeta--blanca.p-4.p-md-5
          SlyderA.slyder-a--curso(tipo="b")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Evaluar la situación:] consiste en valorar el estado de la niña o del niño, identificar la lesión y comprobar los riesgos del entorno antes de intervenir. Por ejemplo, si cae cerca de una escalera, primero se debe asegurar el lugar, observar su respuesta y determinar si resulta indispensable moverlo de inmediato.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t4/f7.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Asegurar la alineación corporal:] implica mantener la cabeza, el cuello y la columna en una posición estable durante el desplazamiento. Por ejemplo, si una niña cae de una cama y manifiesta dolor cervical, se deben evitar giros, flexiones o cambios de postura que puedan aumentar el daño mientras llega la ayuda especializada.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t4/s2.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Inmovilizar la zona lesionada:] consiste en limitar el movimiento de la parte afectada antes de realizar un desplazamiento indispensable. Por ejemplo, si un niño se golpea el brazo al caer en el patio, puede sostenerse la extremidad con una prenda doblada, sin intentar enderezarla ni ejercer presión sobre la lesión.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t4/s3.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Realizar movimientos controlados:] requiere desplazar a la persona lesionada de manera lenta, coordinada y sin movimientos bruscos. Por ejemplo, ante una fuga de gas en la vivienda, dos adultos pueden trasladar a la niña hacia un lugar seguro, manteniendo alineados la cabeza, el cuello y el tronco durante todo el recorrido.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t4/s4.png" alt="")
            .row.align-items-center
              .col-lg-6.mb-4.mb-lg-0
                p.mb-0 #[b Reevaluar el estado general:] implica observar permanentemente la conciencia, la respiración, la coloración de la piel y otras manifestaciones durante el traslado. Por ejemplo, si el niño se torna somnoliento, respira con dificultad o presenta vómito, se debe detener el desplazamiento, solicitar ayuda especializada y vigilar su estado hasta recibir orientación.
              .col-lg-6
                figure.m-0.marco-degradado
                  img(src="@/assets/curso/temas/t4/s5.png" alt="")

    //- Ficha: foto (186,7414) 396x261 -> col-4 · nota (602,7535) 812x140 #DDEEFE r=10 con el icono
    //- (628,7563) 84x84 a la izquierda
    .row.align-items-start.mt-5
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t4/f8.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        p(data-aos="fade-down") La aplicación conjunta de estos principios permite realizar desplazamientos más seguros y responder de acuerdo con las condiciones de la emergencia. En la primera infancia, la vigilancia permanente resulta esencial, debido a que el estado de la niña o del niño puede cambiar rápidamente durante la atención y requerir apoyo especializado.
        .bg-3.r-10.p-4.mt-4(data-aos="fade-down")
          .row.align-items-center
            .col-auto.mb-3.mb-lg-0
              figure
                img(src="@/assets/curso/temas/t4/ic5.svg" alt="" style="width: 84px")
            .col
              p.mb-0 La necesidad y la urgencia del desplazamiento determinan la forma más adecuada de movilizar a la persona lesionada. Por ello, es importante diferenciar los tipos de movilización y reconocer en qué situaciones puede aplicarse cada uno sin aumentar el riesgo de lesión.

    Separador

    #t_4_6.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 4.6 Tipos de movilización

    //- Ficha: texto y nota (185,8014) 812x140 #FFE6DE SIN radio -> col-8 · foto (1017,7917) 396x310 -> col-4
    .row.align-items-start.mt-4
      .col-lg-8.mb-4.mb-lg-0
        p(data-aos="fade-down") La movilización debe responder a una necesidad concreta de protección o atención. Para tomar una decisión adecuada, se deben diferenciar las situaciones que exigen retirar inmediatamente a la niña o al niño de aquellas que permiten preparar el desplazamiento con mayor precaución y disponer de los apoyos necesarios.
        .bg-1.p-4.mt-4(data-aos="fade-down")
          p.mb-0 La decisión también depende de la evolución del estado de la persona lesionada, las condiciones del recorrido y la posibilidad de acceder oportunamente a los servicios de salud. El análisis conjunto de estos factores permite anticipar dificultades, organizar los recursos disponibles y evitar que el desplazamiento ocasione nuevos riesgos.
      .col-lg-4
        figure
          img(src="@/assets/curso/temas/t4/f9.png" alt="" style="width: 396px").m-auto

    p.mt-4(data-aos="fade-down") Cada tipo de movilización presenta características particulares relacionadas con la urgencia y los recursos disponibles. Esta clasificación facilita la identificación de la alternativa más apropiada para cada situación:

    //- Ficha: abierto (290,8257) 1020x190 #F4EDFE r=20 y dos cerrados 1020x90 #B8F4CE r=20
    .row.justify-content-center.mt-4
      .col-lg-10
        AcordionA.acordion--principios(tipo="b")
          .row(titulo="1. Movilización de emergencia")
            .col-12
              p.mb-0 Se emplea cuando existe una amenaza inmediata que impide permanecer en el lugar. Por ejemplo, si durante una inundación el agua comienza a ingresar rápidamente a la vivienda, la niña o el niño debe ser llevado a una zona segura. El desplazamiento se realiza solamente hasta eliminar la exposición al peligro y facilitar la atención requerida.
          .row(titulo="2. Movilización no urgente")
            .col-12
              p.mb-0 Corresponde al desplazamiento que puede planificarse porque las condiciones del lugar permanecen controladas. Por ejemplo, si un niño presenta una lesión después de caer en el jardín y requiere valoración médica, se conserva su posición mientras se organiza el traslado con orientación profesional, sin apresurarlo ni obligarlo a caminar para llegar al medio de transporte.
          .row(titulo="3. Movilización asistida")
            .col-12
              p.mb-0 Se utiliza cuando la persona lesionada necesita ayuda para desplazarse debido a su estado físico o a las características del recorrido. Por ejemplo, si una niña se lesiona en una zona rural de difícil acceso, las personas capacitadas pueden emplear un recurso de traslado apropiado y distribuir responsabilidades para acompañarla hasta el punto donde será recibida por el personal especializado.

    p.mt-5(data-aos="fade-down") La clasificación presentada permite comprender que no todos los desplazamientos responden a las mismas circunstancias. Una vez identificado el tipo de movilización requerido, se seleccionan las técnicas de traslado acordes con el estado de la persona lesionada, el lugar y los recursos disponibles.

    Separador

    #t_4_7.titulo-segundo.color-acento-contenido(data-aos="fade-down")
      h2 4.7 Técnicas de traslado

    //- Ficha: foto (185,8978) 396x275 -> col-4 · nota (601,8978) 812x275 #FFE6DE r=10 con el icono
    //- (637,9014) 84x84 ENCIMA del texto (637,9128)
    .row.align-items-start.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t4/f10.png" alt="" style="width: 396px").m-auto
      .col-lg-8
        .bg-1.r-10.p-4(data-aos="fade-down")
          figure.mb-3
            img(src="@/assets/curso/temas/t4/ic6.svg" alt="" style="width: 84px")
          p.mb-0 Las técnicas de traslado corresponden a las formas de desplazar a una niña o un niño lesionado cuando esta acción resulta necesaria. La elección debe considerar su edad, tamaño, capacidad para colaborar, zona afectada y estado general. También se debe verificar que la técnica seleccionada pueda aplicarse con seguridad y con los apoyos disponibles.

    p.mt-4(data-aos="fade-down") Antes de realizar el traslado, es necesario organizar la intervención para evitar improvisaciones. Para ello, se deben tener en cuenta los siguientes aspectos:

    //- Ficha: caja (290,9340) 1020x210 #F4EDFE SIN radio, con la lista A-E y la ilustración
    //- (1068,9351) 222x178 dentro, a la derecha.
    .row.justify-content-center.mt-4
      .col-lg-10
        .bg-2.p-4(data-aos="fade-down")
          .row.align-items-center
            .col-lg-8
              ol.lista-ol--cuadro.lista-numerada--cuadro.mb-0
                li
                  span.lista-ol--cuadro__vineta A
                  |  Comprobar el estado general de la niña o del niño.
                li
                  span.lista-ol--cuadro__vineta B
                  |  Identificar las zonas lesionadas que requieren protección.
                li
                  span.lista-ol--cuadro__vineta C
                  |  Verificar que el recorrido esté libre de obstáculos.
                li
                  span.lista-ol--cuadro__vineta D
                  |  Definir las funciones de las personas que prestarán ayuda.
                li.mb-0
                  span.lista-ol--cuadro__vineta E
                  |  Preparar los elementos necesarios para el desplazamiento.
            .col-lg-4.d-none.d-lg-block
              figure.m-0
                img(src="@/assets/curso/temas/t4/ilus3.svg" alt="" style="width: 222px").m-auto

    p.mt-4(data-aos="fade-down") Una vez verificadas estas condiciones, se puede seleccionar la técnica que responda a las características de la situación:

    //- Ficha: composición (269,9631) 396x391 —foto recortada + panel #8EC5FC 357x367 + adorno
    //- #FFC0AC 91x91— y las barras del acordeón (765,9629) 544x190/38 con `r=5` -> `LineaTiempoD`.
    .row.align-items-center.justify-content-center.mt-4
      .col-lg-4.mb-4.mb-lg-0
        figure
          img(src="@/assets/curso/temas/t4/comp47.png" alt="" style="width: 396px").m-auto
      .col-lg-5.offset-lg-1
        LineaTiempoD.linea-tiempo--caracteristicas.linea-bold
          .row(numero="1" titulo="Cargue en brazos")
            .col-12
              p.mb-0 Se emplea con lactantes o niñas y niños pequeños que, por su edad o condición, no pueden desplazarse. La persona que brinda ayuda debe sostener la cabeza, el cuello, la espalda y las piernas. Esta técnica no debe aplicarse cuando existan señales de lesión en la columna vertebral, excepto ante un peligro inmediato.
          .row(numero="2" titulo="Arrastre de emergencia")
            .col-12
              p.mb-0 Permite retirar a la persona lesionada de un lugar que representa una amenaza inmediata, como un incendio, una fuga de gas o el riesgo de derrumbe. El desplazamiento debe limitarse hasta alcanzar una zona segura, procurando mantener el cuerpo alineado y evitar que la cabeza o las extremidades golpeen contra el suelo u otros objetos.
          .row(numero="3" titulo="Traslado con apoyo")
            .col-12
              p.mb-0 Se utiliza cuando la niña o el niño permanece consciente, puede seguir indicaciones y conserva parcialmente la capacidad para caminar. La persona auxiliadora se ubica al lado afectado para proporcionar estabilidad. Esta técnica puede aplicarse ante una molestia leve, siempre que no existan mareo, dolor intenso o sospecha de lesión grave.
          .row(numero="4" titulo="Traslado asistido por dos personas")
            .col-12
              p.mb-0 Se aplica cuando el peso, el estado físico o las condiciones del recorrido requieren ayuda adicional. Las personas encargadas deben acordar quién dirigirá la maniobra, distribuir los puntos de apoyo y realizar el desplazamiento de manera coordinada. No se debe levantar a la niña o al niño sujetándolo únicamente por los brazos o las piernas.

    p.mt-5(data-aos="fade-down") La técnica seleccionada debe modificarse o suspenderse si durante el recorrido aparecen dificultad para respirar, pérdida de respuesta, dolor intenso, vómito o cambios en la coloración de la piel. En estas situaciones, se debe ubicar a la persona lesionada en un lugar seguro, solicitar atención especializada y mantener la vigilancia de su estado general.

    //- Ficha: caja (290,10174) 1020x140 #DBC2FA r=10 con el badge del corazón (765,10139) 70x70
    //- centrado y montado 35px por encima -> `.tarjeta--badge-arriba`, que ya existe.
    .row.justify-content-center.mt-5
      .col-lg-10
        .tarjeta--badge-arriba.bg-6.p-4(data-aos="fade-down")
          figure
            img(src="@/assets/curso/temas/t4/badge.svg" alt="")
          p.text-center.mb-0 El traslado no consiste únicamente en cambiar de lugar a la persona lesionada. Su propósito es protegerla durante un desplazamiento indispensable, sin aumentar el dolor ni agravar las lesiones existentes.

    p.mt-5.mb-0(data-aos="fade-down") El conocimiento de estas técnicas fortalece la capacidad de respuesta ante lesiones y traumatismos en la primera infancia. Asimismo, permite actuar con mayor seguridad frente a otras situaciones específicas que requieren observación, reconocimiento de signos de alarma y atención inicial oportuna.

</template>

<script>
export default {
  name: 'Tema4',
}
</script>
