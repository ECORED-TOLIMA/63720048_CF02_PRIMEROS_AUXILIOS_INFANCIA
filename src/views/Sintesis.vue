<template lang="pug">
.curso-main-container.pb-3
  BannerInterno(icono="fas fa-sitemap" titulo="Síntesis")
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    p(data-aos="fade-down") El componente formativo desarrolla los fundamentos y procedimientos esenciales para la atención de emergencias en la primera infancia, integrando conocimientos de anatomía y fisiología básica, evaluación inicial del lesionado y aplicación del soporte vital básico. A partir de estos elementos, se fortalecen las capacidades para reconocer situaciones críticas, interpretar signos de alarma y ejecutar intervenciones oportunas y seguras.

    p.mt-4(data-aos="fade-down") De igual forma, se abordan las principales lesiones y situaciones específicas que pueden presentarse en esta etapa, así como la movilización del lesionado, la comunicación con el menor y la articulación con el sistema de emergencias. Todo ello con el propósito de garantizar una atención integral, segura y oportuna que proteja la vida y la salud de niñas y niños en las diferentes situaciones de emergencia.

    p.mt-4.mb-0(data-aos="fade-down") A continuación, el mapa conceptual organiza de manera visual los ejes temáticos del componente formativo y las relaciones que los articulan.

    //- El mapa del XD mide 1228 px, que es justo el ancho útil de la tarjeta.
    figure.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/sintesis.svg" alt="Técnicas de primeros auxilios en primera infancia organiza el componente en seis ejes: anatomía y fisiología básica, evaluación inicial del lesionado, soporte vital básico, lesiones y movilización, situaciones específicas y enfermedades prevalentes, y comunicación, emergencias y cadena de custodia, con sus subtemas. Así, evidencia que atender una emergencia es un proceso integral, del reconocimiento de los signos de alarma a la movilización segura y la articulación con el sistema de salud." style="width: 1228px").m-auto

    .row.justify-content-center.mt-5
      .col-auto
        a.anexo(:href="obtenerLink('/downloads/Sintesis.pdf')" target="_blank")
          .anexo__icono
            img(src="@/assets/bullets/icono-pdf.svg")
          .anexo__texto
            p Anexo. Síntesis
</template>

<script>
export default {
  name: 'Sintesis',
  mounted() {
    this.$nextTick(() => {
      this.$aosRefresh()
    })
  },
  updated() {
    this.$aosRefresh()
  },
}
</script>

<style lang="sass"></style>
