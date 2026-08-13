<template lang="pug">
.curso-main-container.introduccion.pb-3
  BannerInterno
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    .titulo-principal.color-acento-contenido
      .titulo-principal__numero
        span
          i.fas.fa-info
      h1 Introducción

    .row
      .col-lg-3.d-none.d-lg-block
        figure
          img(src="@/assets/curso/temas/intro/foto.png" alt="" style="width: 297px").m-auto
      .col-lg-9
        p(data-aos="fade-down") Las técnicas de primeros auxilios en la primera infancia representan una herramienta esencial para proteger la vida y la integridad de un niño o una niña ante una situación de emergencia. Sin embargo, su aplicación efectiva no depende únicamente de conocer los procedimientos, sino de comprender el funcionamiento del cuerpo en esta etapa de la vida, reconocer los signos de alarma y actuar con calma y seguridad mientras llega la atención especializada.

        .bg-2.r-10.p-4.mt-4(data-aos="fade-down")
          p.mb-0 En este componente formativo se desarrollan las bases necesarias para adquirir estas competencias, permitiendo al talento humano en formación intervenir de manera oportuna y responsable ante una emergencia en la primera infancia, contribuyendo a salvar vidas y a reducir las consecuencias de una lesión mientras se activa el sistema de emergencias.

        .row.align-items-start.mt-4(data-aos="fade-down")
          .col-auto.mb-3.mb-lg-0
            figure
              img(src="@/assets/curso/temas/intro/icono.png" alt="" style="width: 84px")
          .col
            p.mb-0 El desarrollo de los contenidos se presenta de manera progresiva: inicia con la anatomía y fisiología básica y la evaluación inicial del lesionado; continúa con el soporte vital básico y el manejo de lesiones y traumatismos; y finaliza con la atención de situaciones específicas y la comunicación con el niño, la niña y sus cuidadores durante la emergencia. Para ampliar la información, se recomienda consultar el material audiovisual que acompaña esta sección.

    //- El XD deja este espacio como marcador («ESPACIO PARA VIDEO») y ni el .xd ni el DI traen la
    //- URL del vídeo: se queda el iframe del scaffold hasta que llegue el enlace real.
    .row.justify-content-center.align-items-center.mt-5
      .col-lg-12
        figure
          .video
            iframe(width="1331" height="749" src="https://www.youtube.com/embed/zpLeFDlZnMI" title="First Aid Techniques for Early Childhood" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen)

</template>

<script>
export default {
  name: 'Introduccion',
}
</script>
