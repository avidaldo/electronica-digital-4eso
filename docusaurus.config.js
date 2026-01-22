// @ts-check
// Docusaurus configuration for Electrónica Digital 4º ESO

import { themes as prismThemes } from 'prism-react-renderer';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Electrónica Digital',
  tagline: 'Apuntes de Tecnología 4º ESO',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  // Cambiar por tu usuario de GitHub
  url: 'https://avidaldo.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  baseUrl: '/electronica-digital-4eso/',

  // GitHub pages deployment config
  organizationName: 'avidaldo', // Cambiar por tu usuario de GitHub
  projectName: 'electronica-digital-4eso', // Nombre del repositorio
  trailingSlash: false,

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  // Soporte para matemáticas con KaTeX
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
      type: 'text/css',
      integrity: 'sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV',
      crossorigin: 'anonymous',
    },
  ],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          routeBasePath: '/', // Docs como página principal
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
          // Editar en GitHub
          editUrl: 'https://github.com/tu-usuario/electronica-digital-4eso/tree/main/',
        },
        blog: false, // Desactivar blog
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Imagen para redes sociales
      image: 'img/social-card.png',
      
      navbar: {
        title: 'Electrónica Digital',
        logo: {
          alt: 'Logo Electrónica Digital',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: '📚 Apuntes',
          },
          {
            to: '/presentaciones',
            label: '🎬 Presentaciones',
            position: 'left',
          },
          {
            href: 'https://www.tinkercad.com/circuits',
            label: '🔧 Simulador',
            position: 'right',
          },
          {
            href: 'https://github.com/tu-usuario/electronica-digital-4eso',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },

      footer: {
        style: 'dark',
        links: [
          {
            title: 'Contenido',
            items: [
              { label: 'Apuntes', to: '/' },
              { label: 'Presentaciones', to: '/presentaciones' },
            ],
          },
          {
            title: 'Herramientas',
            items: [
              { label: 'Tinkercad', href: 'https://www.tinkercad.com/circuits' },
              { label: 'Falstad Simulator', href: 'https://falstad.com/circuit/' },
            ],
          },
          {
            title: 'Más',
            items: [
              { label: 'Legislación', to: '/legislacion' },
              { label: 'GitHub', href: 'https://github.com/tu-usuario/electronica-digital-4eso' },
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} Electrónica Digital 4º ESO. Contenido bajo licencia CC BY-SA 4.0.`,
      },

      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['bash', 'python'],
      },

      // Búsqueda local
      algolia: undefined, // Desactivar Algolia, usar búsqueda local

      tableOfContents: {
        minHeadingLevel: 2,
        maxHeadingLevel: 4,
      },
    }),

  // Búsqueda local sin Algolia
  themes: [
    [
      require.resolve("@easyops-cn/docusaurus-search-local"),
      /** @type {import("@easyops-cn/docusaurus-search-local").PluginOptions} */
      ({
        hashed: true,
        language: ["es"],
        highlightSearchTermsOnTargetPage: true,
        explicitSearchResultPath: true,
      }),
    ],
  ],
};

export default config;
