export default {
  global: {
    Name: 'Técnicas de primeros auxilios en primera infancia',
    Description:
      'Este componente desarrolla las técnicas de primeros auxilios en primera infancia, así como la valoración inicial y la atención de emergencias. Integra técnicas de soporte vital básico, manejo de lesiones, movilización, comunicación y articulación con el sistema de salud, fortaleciendo la capacidad de respuesta oportuna y segura.',
    imagenBannerPrincipal: '@/assets/curso/portada/ilustracion.png',
    fondoBannerPrincipal: '@/assets/curso/portada/fondo-banner.png',
    imagenesDecorativasBanner: [
      {
        clases: ['banner-principal-decorativo-1', 'd-none', 'd-lg-block'],
        imagen: '@/assets/curso/portada/decorativo-1.png',
      },
      {
        clases: ['banner-principal-decorativo-2', 'd-none', 'd-lg-block'],
        imagen: '@/assets/curso/portada/decorativo-2.png',
      },
    ],
  },
  menuPrincipal: {
    menu: [
      {
        nombreRuta: 'inicio',
        icono: 'fas fa-home',
        titulo: 'Volver al inicio',
      },
      {
        nombreRuta: 'introduccion',
        icono: 'fas fa-info-circle',
        titulo: 'Introducción',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'tema1',
        numero: '1',
        titulo: 'Anatomía y fisiología básica',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '1.1',
            titulo: 'Sistema circulatorio',
            hash: 't_1_1',
          },
          {
            numero: '1.2',
            titulo: 'Sistema respiratorio',
            hash: 't_1_2',
          },
          {
            numero: '1.3',
            titulo: 'Sistema tegumentario',
            hash: 't_1_3',
          },
          {
            numero: '1.4',
            titulo: 'Sistema musculoesquelético',
            hash: 't_1_4',
          },
          {
            numero: '1.5',
            titulo: 'Relación con la atención de emergencias',
            hash: 't_1_5',
          },
        ],
      },
      {
        nombreRuta: 'tema2',
        numero: '2',
        titulo: 'Evaluación inicial del lesionado',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '2.1',
            titulo: 'Nivel de conciencia',
            hash: 't_2_1',
          },
          {
            numero: '2.2',
            titulo: 'Valoración de la respiración',
            hash: 't_2_2',
          },
          {
            numero: '2.3',
            titulo: 'Valoración del pulso',
            hash: 't_2_3',
          },
          {
            numero: '2.4',
            titulo: 'Identificación de signos de alarma',
            hash: 't_2_4',
          },
        ],
      },
      {
        nombreRuta: 'tema3',
        numero: '3',
        titulo: 'Soporte vital básico en primera infancia',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '3.1',
            titulo: 'RCP en lactantes',
            hash: 't_3_1',
          },
          {
            numero: '3.2',
            titulo: 'Obstrucción de la vía aérea por cuerpo extraño (OVACE)',
            hash: 't_3_2',
          },
          {
            numero: '3.3',
            titulo: 'Uso del desfibrilador externo automático (DEA)',
            hash: 't_3_3',
          },
        ],
      },
      {
        nombreRuta: 'tema4',
        numero: '4',
        titulo: 'Lesiones, traumatismos y movilización',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '4.1',
            titulo: 'Atención de lesiones en primeros auxilios',
            hash: 't_4_1',
          },
          {
            numero: '4.2',
            titulo: 'Manejo de lesiones osteomusculares',
            hash: 't_4_2',
          },
          {
            numero: '4.3',
            titulo: 'Manejo de traumas',
            hash: 't_4_3',
          },
          {
            numero: '4.4',
            titulo: 'Movilización y traslado del lesionado',
            hash: 't_4_4',
          },
          {
            numero: '4.5',
            titulo: 'Principios de la movilización segura',
            hash: 't_4_5',
          },
          {
            numero: '4.6',
            titulo: 'Tipos de movilización',
            hash: 't_4_6',
          },
          {
            numero: '4.7',
            titulo: 'Técnicas de traslado',
            hash: 't_4_7',
          },
        ],
      },
      {
        nombreRuta: 'tema5',
        numero: '5',
        titulo: 'Situaciones específicas y enfermedades prevalentes',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '5.1',
            titulo: 'Atención de situaciones específicas',
            hash: 't_5_1',
          },
          {
            numero: '5.2',
            titulo: 'Principales enfermedades prevalentes',
            hash: 't_5_2',
          },
          {
            numero: '5.3',
            titulo: 'Signos de alarma',
            hash: 't_5_3',
          },
        ],
      },
      {
        nombreRuta: 'tema6',
        numero: '6',
        titulo: 'Comunicación, emergencias y cadena de custodia',
        desarrolloContenidos: true,
        subMenu: [
          {
            numero: '6.1',
            titulo: 'Primeros auxilios psicológicos y comunicación',
            hash: 't_6_1',
          },
          {
            numero: '6.2',
            titulo: 'Articulación con el sistema de emergencias',
            hash: 't_6_2',
          },
          {
            numero: '6.3',
            titulo: 'Cadena de custodia',
            hash: 't_6_3',
          },
        ],
      },
    ],
    subMenu: [
      {
        icono: 'fas fa-sitemap',
        titulo: 'Síntesis',
        nombreRuta: 'sintesis',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'actividad',
        icono: 'far fa-question-circle',
        titulo: 'Actividad didáctica',
        desarrolloContenidos: true,
      },
      {
        nombreRuta: 'glosario',
        icono: 'fas fa-sort-alpha-down',
        titulo: 'Glosario',
      },
      {
        icono: 'fas fa-book',
        titulo: 'Referencias bibliográficas',
        nombreRuta: 'referencias',
      },
      {
        icono: 'fas fa-file-pdf',
        titulo: 'Descargar PDF',
        download: 'downloads/63720048_CF02_CFA_DU.pdf',
      },
      {
        icono: 'fas fa-download',
        titulo: 'Descargar material',
        download: 'downloads/material.zip',
      },
      {
        icono: 'far fa-registered',
        titulo: 'Créditos',
        nombreRuta: 'creditos',
      },
    ],
  },
  glosario: [
    {
      termino: 'Anatomía',
      significado:
        'ciencia que estudia la estructura y la organización de las partes del cuerpo humano, base para comprender su funcionamiento en la atención de primeros auxilios.',
    },
    {
      termino: 'Bioseguridad',
      significado:
        'conjunto de medidas y prácticas orientadas a prevenir riesgos biológicos y proteger la salud del primer respondiente y de la niña o el niño durante la atención de una emergencia.',
    },
    {
      termino: 'Cadena de custodia',
      significado:
        'conjunto de procedimientos que garantizan la integridad, el manejo adecuado y la trazabilidad de la evidencia relacionada con un evento que pueda tener implicaciones legales.',
    },
    {
      termino: 'Convulsión',
      significado:
        'alteración neurológica súbita, producida por una actividad eléctrica anormal del cerebro, que se manifiesta con movimientos involuntarios y pérdida temporal del control corporal.',
    },
    {
      termino: 'Desfibrilador externo automático (DEA)',
      significado:
        'dispositivo portátil que analiza el ritmo cardíaco de una persona en paro y, si es necesario, administra una descarga eléctrica para restablecer un ritmo cardíaco normal.',
    },
    {
      termino: 'Deshidratación',
      significado:
        'pérdida excesiva de agua y electrolitos en el organismo, frecuente en la primera infancia, que puede afectar el estado general de la niña o el niño.',
    },
    {
      termino: 'Esguince',
      significado:
        'lesión de los ligamentos de una articulación, causada por un estiramiento o desgarro brusco, que produce dolor e inflamación.',
    },
    {
      termino: 'Hemorragia',
      significado:
        'pérdida de sangre causada por la ruptura de uno o varios vasos sanguíneos, que puede ser interna o externa.',
    },
    {
      termino: 'Luxación',
      significado:
        'desplazamiento de un hueso fuera de su articulación, que produce dolor intenso, deformidad e imposibilidad de movimiento.',
    },
    {
      termino: 'OVACE',
      significado:
        'obstrucción de la vía aérea por un cuerpo extraño que impide el paso del aire hacia los pulmones y requiere maniobras de desobstrucción inmediatas.',
    },
    {
      termino: 'Reanimación cardiopulmonar (RCP)',
      significado:
        'conjunto de maniobras de compresiones torácicas y ventilaciones, dirigidas a restablecer la respiración y la circulación en una persona en paro cardiorrespiratorio.',
    },
  ],
  referencias: [
    {
      referencia:
        'American Heart Association. (2020). <em>Guidelines for cardiopulmonary resuscitation and emergency cardiovascular care</em>.',
      link: '',
    },
    {
      referencia:
        'European Resuscitation Council. (2021). <em>European Resuscitation Council guidelines 2021</em>.',
      link: '',
    },
    {
      referencia:
        'Fiscalía General de la Nación (Colombia). (s.f.). <em>Manual de cadena de custodia</em>.',
      link: '',
    },
    {
      referencia:
        'International Federation of Red Cross and Red Crescent Societies. (2020). <em>International first aid, resuscitation and education guidelines</em>.',
      link: '',
    },
    {
      referencia:
        'International Liaison Committee on Resuscitation (ILCOR). (2020). <em>Consensus on science with treatment recommendations (CoSTR)</em>.',
      link: '',
    },
    {
      referencia:
        'Ministerio de Salud y Protección Social. (2018). <em>Ruta integral de atención en salud para la promoción y mantenimiento de la salud</em>.',
      link: '',
    },
    {
      referencia:
        'MSD Manual. (2023). <em>Cómo tratar al lactante consciente que se asfixia</em>.',
      link: '',
    },
    {
      referencia:
        'Organización Mundial de la Salud. (2020). <em>Emergency care systems for universal health coverage: Ensuring timely care for the acutely ill and injured</em>.',
      link: '',
    },
    {
      referencia:
        'Osakidetza. (2022). <em>Manual de reanimación cardiopulmonar básica y avanzada en pediatría</em>.',
      link: '',
    },
    {
      referencia:
        'Tortora, G. J., &amp; Derrickson, B. (2021). <em>Principles of anatomy and physiology</em> (16.ª ed.). John Wiley &amp; Sons.',
      link: '',
    },
  ],
  creditos: [
    {
      titulo: 'ECOSISTEMA DE RECURSOS EDUCATIVOS DIGITALES',
      autores: [
        {
          nombre: 'Claudia Johanna Gómez Pérez ',
          cargo:
            'Profesional G06. Responsable Ecosistema Virtual de Recursos Educativos Digitales',
          centro: 'Centro Agroturístico - Regional Santander',
        },
        {
          nombre: 'Diana Rocío Possos Beltrán',
          cargo: 'Responsable de línea de producción ',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'CONTENIDO INSTRUCCIONAL',
      autores: [
        {
          nombre: 'Laura Briguitte Perea Possos',
          cargo: 'Experta temática',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Gloria Lida Alzate Suárez',
          cargo: 'Evaluadora instruccional',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'DISEÑO Y DESARROLLO DE RECURSOS EDUCATIVOS DIGITALES',
      autores: [
        {
          nombre: 'Juan Daniel Polanco Muñoz',
          cargo: 'Diseñador de contenidos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Manuel Felipe Echavarria Orozco',
          cargo: 'Desarrollador <em>full stack</em>',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Gilberto Junior Rodríguez Rodríguez',
          cargo: 'Animador y productor audiovisual',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
    {
      titulo: 'VALIDACIÓN RECURSO EDUCATIVO DIGITAL',
      autores: [
        {
          nombre: 'María Fernanda Pineda Mora',
          cargo: 'Evaluadora de contenidos inclusivos y accesibles',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
        {
          nombre: 'Javier Mauricio Oviedo',
          cargo: 'Validador y vinculador de recursos educativos digitales',
          centro: 'Centro de Comercio y Servicios - Regional Tolima',
        },
      ],
    },
  ],
  creditosAdicionales: {
    imagenes:
      'Fotografías y vectores tomados de <a href="https://www.freepik.es/" target="_blank">www.freepik.es</a>, <a href="https://www.shutterstock.com/" target="_blank">www.shutterstock.com</a>, <a href="https://unsplash.com/" target="_blank">unsplash.com </a>y <a href="https://www.flaticon.com/" target="_blank">www.flaticon.com</a>',
    creativeCommons:
      'Licencia creative commons CC BY-NC-SA<br><a href="https://creativecommons.org/licenses/by-nc-sa/2.0/" target="_blank">ver licencia</a>',
  },
}
