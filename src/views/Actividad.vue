<template lang="pug">
.curso-main-container.pb-3
  BannerInterno(icono="far fa-question-circle" titulo="Actividad didáctica")
  .container.tarjeta.tarjeta--blanca.p-4.p-md-5
    #Actividad
    ActividadController(:cuestionario="cuestionario")

</template>

<script>
//- GENERADO por `scripts/gen_actividad.py` desde `63720048_CF02_AD.docx`.
//- No editar a mano: volver a correr el script si cambia el docx.
import ActividadController from '@ecored-sena/boulder-kit/plugin/components/actividad/ActividadController.vue'

export default {
  name: 'ActividadDidactica',
  components: {
    ActividadController,
  },
  data: () => ({
    cuestionario: {
      tema: 'Técnicas de primeros auxilios en primera infancia',
      titulo: 'Misión: salvar vidas',
      introduccion:
        '<b>Objetivo:</b> Aplicar los conocimientos y habilidades adquiridas para atender emergencias en la primera infancia, identificando situaciones de riesgo, evaluando al lesionado y ejecutando acciones de primeros auxilios de forma oportuna, segura y conforme a los protocolos establecidos.<br><br>Esta actividad le permitirá determinar el grado de apropiación de los contenidos del componente formativo Técnicas de primeros auxilios en primera infancia. Antes de su realización, se recomienda la lectura del componente formativo mencionado. Es opcional (no es calificable), y puede realizarse todas las veces que se desee. Lea la pregunta de cada ítem y seleccione la respuesta correcta.',
      // el kit sólo muestra 10 de las 20: barajar es OBLIGATORIO
      barajarPreguntas: true,
      titulo_aprobado: '¡BUEN TRABAJO!',
      titulo_reprobado: 'VUELVA A INTENTARLO',
      // `mensaje_final_*`, NO `mensaje_*`: es el nombre que lee
      // `actividadCuestionario/Actividad.vue` del kit (1.0.9). Con el nombre corto los dos
      // mensajes finales del docx no se pintan nunca y no salta ningún error.
      mensaje_final_aprobado: 'Felicitaciones. Ha superado satisfactoriamente la actividad. Los resultados obtenidos evidencian una comprensión adecuada de los conceptos y procedimientos relacionados con la atención de emergencias en la primera infancia. Se reconoce la capacidad para identificar situaciones de riesgo, interpretar signos de alarma y aplicar acciones básicas de primeros auxilios de manera segura y oportuna.',
      mensaje_final_reprobado: 'No ha superado la actividad. Le recomendamos volver a revisar el componente formativo e intentar nuevamente la actividad didáctica.',
      preguntas: [
        {
          id: 1,
          texto: '¿Cuál es el objetivo principal de los primeros auxilios?',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Reemplazar la atención médica.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Administrar medicamentos.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Estabilizar al paciente y evitar complicaciones.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Diagnosticar enfermedades.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Los primeros auxilios buscan estabilizar al paciente y prevenir el agravamiento mientras llega la atención especializada.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 2,
          texto: '¿Qué sistema transporta oxígeno y nutrientes en el cuerpo?',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Digestivo.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Circulatorio.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Respiratorio.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Nervioso.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'El sistema circulatorio transporta sangre, oxígeno y nutrientes a todo el organismo.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 3,
          texto: '¿Cuál es el primer paso en la atención de una emergencia?',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Evaluar el entorno.',
              esCorrecta: true,
            },
            {
              id: 'b',
              texto: 'Mover al paciente.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Llamar a emergencias.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Aplicar RCP.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Evaluar la seguridad del entorno es esencial antes de intervenir, para evitar nuevos riesgos.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 4,
          texto: '¿Qué indica la cianosis?',
          imagen: '@/assets/actividad/imagen1.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Falta de oxígeno.',
              esCorrecta: true,
            },
            {
              id: 'b',
              texto: 'Enrojecimiento de la piel.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Dolor.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Fiebre.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La coloración azulada de la piel (cianosis) indica un déficit de oxígeno en la sangre y constituye una urgencia.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 5,
          texto: '¿Qué se debe hacer ante una obstrucción leve de la vía aérea?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Dar agua.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Aplicar compresiones.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Permitir que tosa.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Introducir los dedos.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La tos es el mecanismo más eficaz para expulsar el objeto en una obstrucción leve de la vía aérea.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 6,
          texto: '¿Qué técnica se utiliza en lactantes para OVACE?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'RCP directa.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Solo ventilaciones.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Golpes interescapulares y compresiones torácicas.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Compresiones abdominales.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'En lactantes, se combinan golpes interescapulares y compresiones torácicas para desobstruir la vía aérea.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 7,
          texto: '¿Cuál es la profundidad adecuada de compresión en RCP pediátrica?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: '10 cm.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Un tercio del tórax.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: '1 cm.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: '5 cm.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La profundidad de compresión recomendada en RCP pediátrica es, aproximadamente, un tercio del diámetro del tórax.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 8,
          texto: '¿Cuál es la función del DEA?',
          imagen: '@/assets/actividad/imagen2.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Analizar el ritmo cardíaco y dar descarga.',
              esCorrecta: true,
            },
            {
              id: 'b',
              texto: 'Medir la presión arterial.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Administrar medicamentos.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Controlar la respiración.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'El DEA analiza el ritmo cardíaco y aplica una descarga cuando es necesario.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 9,
          texto: '¿Qué se debe evitar en una quemadura?',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Retirar ropa suelta.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Aplicar sustancias.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Aplicar agua.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Cubrir la herida.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Aplicar sustancias sobre una quemadura puede empeorar la lesión o causar infección.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 10,
          texto: '¿Cuál es la primera acción ante una hemorragia?',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Lavar la herida.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Presión directa.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Elevar al paciente.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Aplicar hielo.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La presión directa es la medida más efectiva para controlar una hemorragia.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 11,
          texto: '¿Qué se debe hacer ante una sospecha de fractura?',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Masajear.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Mover la zona.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Aplicar calor.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Inmovilizar.',
              esCorrecta: true,
            },
          ],
          mensaje_correcto: 'Inmovilizar la zona afectada evita que la fractura se agrave.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 12,
          texto: '¿Cuál es un signo de deshidratación?',
          imagen: '@/assets/actividad/imagen3.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Hambre.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Tos.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Sudoración.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Ojos hundidos.',
              esCorrecta: true,
            },
          ],
          mensaje_correcto: 'Los ojos hundidos son un signo típico de deshidratación.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 13,
          texto: '¿Qué hacer durante una convulsión?',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Dar agua.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Proteger y colocar de lado.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Sujetar al paciente.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Introducir objetos en la boca.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Durante una convulsión, se debe proteger al menor y colocarlo de lado para evitar lesiones y riesgo de aspiración.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 14,
          texto: '¿Qué caracteriza una emergencia?',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'No requiere atención.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Es leve.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Riesgo inmediato para la vida.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Es opcional.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Una emergencia implica un riesgo inmediato para la vida y exige intervención urgente.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 15,
          texto: '¿Qué se debe hacer ante una intoxicación?',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Inducir vómito.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Identificar una sustancia y no intervenir sin indicación.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Dar alimentos.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Ignorar síntomas.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Ante una intoxicación, es clave identificar la sustancia y no intervenir sin orientación médica.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 16,
          texto: '¿Cuál es un signo de alarma respiratorio?',
          imagen: '@/assets/actividad/imagen4.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Aleteo nasal.',
              esCorrecta: true,
            },
            {
              id: 'b',
              texto: 'Estornudo.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Bostezo.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Tos leve.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'El aleteo nasal es un signo de dificultad respiratoria que requiere atención.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 17,
          texto: '¿Qué principio es clave en la movilización?',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Velocidad.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Improvisación.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Alineación corporal.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Fuerza.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Mantener la alineación corporal evita lesiones adicionales durante la movilización.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 18,
          texto: '¿Qué caracteriza la comunicación en emergencias?',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Rápida sin explicación.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Clara y sencilla.',
              esCorrecta: true,
            },
            {
              id: 'c',
              texto: 'Compleja.',
              esCorrecta: false,
            },
            {
              id: 'd',
              texto: 'Técnica.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'En una emergencia, la comunicación debe ser clara y sencilla para reducir el estrés y facilitar la comprensión.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 19,
          texto: '¿Qué se debe hacer antes de movilizar a un lesionado?',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Levantarlo.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Sentarlo.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Evaluar su estado.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Mover inmediatamente.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'Evaluar el estado del lesionado antes de movilizarlo permite decidir la forma adecuada de hacerlo.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
        {
          id: 20,
          texto: '¿Qué implica la cadena de custodia?',
          imagen: '@/assets/actividad/imagen5.png',
          barajarRespuestas: true,
          opciones: [
            {
              id: 'a',
              texto: 'Mover al paciente.',
              esCorrecta: false,
            },
            {
              id: 'b',
              texto: 'Atender rápido.',
              esCorrecta: false,
            },
            {
              id: 'c',
              texto: 'Registrar y conservar la evidencia.',
              esCorrecta: true,
            },
            {
              id: 'd',
              texto: 'Llamar a emergencias.',
              esCorrecta: false,
            },
          ],
          mensaje_correcto: 'La cadena de custodia garantiza la integridad y la trazabilidad de la información o la evidencia.',
          mensaje_incorrecto: 'Revise nuevamente el contenido del componente formativo.',
        },
      ],
    },
  }),
}
</script>

<style lang="sass"></style>
