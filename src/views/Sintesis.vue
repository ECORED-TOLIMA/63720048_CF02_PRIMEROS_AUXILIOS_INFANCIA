<template lang="pug">
.curso-main-container.pb-3
  BannerInterno(icono="fas fa-sitemap" titulo="Síntesis")
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5.mb-5

    p(data-aos="fade-down") El componente formativo desarrolla los fundamentos y procedimientos esenciales para la atención de emergencias en la primera infancia, integrando conocimientos de anatomía y fisiología básica, evaluación inicial del lesionado y aplicación del soporte vital básico. A partir de estos elementos, se fortalecen las capacidades para reconocer situaciones críticas, interpretar signos de alarma y ejecutar intervenciones oportunas y seguras.

    p.mt-4(data-aos="fade-down") De igual forma, se abordan las principales lesiones y situaciones específicas que pueden presentarse en esta etapa, así como la movilización del lesionado, la comunicación con el menor y la articulación con el sistema de emergencias. Todo ello con el propósito de garantizar una atención integral, segura y oportuna que proteja la vida y la salud de niñas y niños en las diferentes situaciones de emergencia.

    //- El mapa del XD mide 1228 px, que es justo el ancho útil de la tarjeta.
    figure.mt-4(data-aos="fade-down")
      img(src="@/assets/curso/sintesis.svg" alt="Mapa conceptual del componente Técnicas de primeros auxilios en primera infancia, organizado en seis ejes relacionados entre sí. Los tres primeros ejes desarrollan las bases técnicas: anatomía y fisiología, evaluación inicial del lesionado, y soporte vital básico con RCP, OVACE y desfibrilador. Los dos ejes siguientes abordan la atención práctica: lesiones y movilización segura, y las situaciones específicas más frecuentes en la primera infancia. El último eje reúne la comunicación con el menor y sus cuidadores, la articulación con el sistema de emergencias y la cadena de custodia." style="width: 1228px").m-auto

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
