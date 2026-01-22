// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'index',
      label: '📚 Índice General',
    },
    {
      type: 'category',
      label: '📖 Apuntes',
      collapsed: false,
      items: [
        'apuntes/01_introduccion',
        'apuntes/02_sistemas_numeracion',
        'apuntes/03_algebra_boole',
        'apuntes/04_puertas_logicas',
        'apuntes/05_diseno_circuitos',
        'apuntes/06_circuitos_combinacionales',
        'apuntes/07_practicas_taller',
      ],
    },
    {
      type: 'category',
      label: '📜 Legislación',
      collapsed: true,
      items: [
        'legislacion/00_indice_normativa',
        'legislacion/01_marco_legal',
        'legislacion/02_competencias',
        'legislacion/03_saberes_basicos',
        'legislacion/04_evaluacion',
        'legislacion/05_inclusion',
      ],
    },
    {
      type: 'category',
      label: '📋 Protocolos',
      collapsed: true,
      items: [
        'protocolos/protocolo_tdah_dislexia',
      ],
    },
  ],
};

export default sidebars;
