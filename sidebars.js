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
        'apuntes/introduccion',
        'apuntes/sistemas_numeracion',
        'apuntes/algebra_boole',
        'apuntes/puertas_logicas',
        'apuntes/diseno_circuitos',
        'apuntes/circuitos_combinacionales',
        'apuntes/practicas_taller',
      ],
    },
    {
      type: 'doc',
      id: 'presentaciones',
      label: '🎬 Presentaciones',
    },
  ],
};

export default sidebars;
