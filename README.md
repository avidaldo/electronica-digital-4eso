# Electrónica Digital - 4º ESO

Materiales didácticos para la Unidad Didáctica de **Electrónica Digital** de la asignatura de Tecnología de 4º ESO, siguiendo el currículum de la Comunidad Autónoma de Galicia (Decreto 156/2022).

## 📚 Contenido

| Tema | Título | Descripción |
|------|--------|-------------|
| 1 | [Introducción](docs/apuntes/01_introduccion.md) | Historia, señales analógicas vs digitales |
| 2 | [Sistemas de Numeración](docs/apuntes/02_sistemas_numeracion.md) | Binario, hexadecimal, conversiones |
| 3 | [Álgebra de Boole](docs/apuntes/03_algebra_boole.md) | AND, OR, NOT, De Morgan |
| 4 | [Puertas Lógicas](docs/apuntes/04_puertas_logicas.md) | Puertas básicas y universales |
| 5 | [Diseño de Circuitos](docs/apuntes/05_diseno_circuitos.md) | Tablas de verdad, Karnaugh |
| 6 | [Circuitos Combinacionales](docs/apuntes/06_circuitos_combinacionales.md) | Codificadores, displays, MUX |
| 7 | [Prácticas de Taller](docs/apuntes/07_practicas_taller.md) | Protoboard, CIs, simuladores |

## 🌐 Web Online

La documentación se despliega automáticamente en GitHub Pages:

**🔗 [https://tu-usuario.github.io/electronica-digital-4eso/](https://tu-usuario.github.io/electronica-digital-4eso/)**

## 🎬 Presentaciones

Las presentaciones interactivas en Reveal.js están disponibles en la carpeta `presentacion/`:

- [Índice de presentaciones](presentacion/index.html)
- Tema 1 a 7: Una presentación por tema

## 📥 Descargas

| Recurso | Formato | Descripción |
|---------|---------|-------------|
| Apuntes completos | PDF | Todos los temas en un documento |
| Presentaciones | HTML | Slides interactivos (Reveal.js) |

## 🛠️ Desarrollo Local

### Requisitos previos

- **Node.js** 18+ (para Docusaurus)
- **Python** 3.8+ (para generar figuras y PDF)
- **Pandoc** + **LaTeX** (para PDF, opcional)

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/electronica-digital-4eso.git
cd electronica-digital-4eso

# Instalar dependencias Node.js
npm install

# Instalar dependencias Python
pip install -r requirements.txt
```

### Comandos disponibles

```bash
# Desarrollo: servidor local con hot-reload
npm start

# Construir web para producción
npm run build

# Generar PDF de apuntes
npm run build:pdf
# o directamente:
python scripts/build-pdf.py

# Servidor local para presentaciones
npm run slides:dev

# Construir todo (web + PDF + slides)
npm run build:all
```

### Generar figuras

Las imágenes de los apuntes se generan con matplotlib:

```bash
python recursos/generar_figuras.py
```

## 📁 Estructura del Proyecto

```
electronica-digital-4eso/
├── apuntes/                 # Markdown original (fuente)
├── docs/                    # Documentación para Docusaurus
│   ├── apuntes/             # Apuntes adaptados con frontmatter
│   ├── legislacion/         # Marco legal
│   └── protocolos/          # Protocolos de atención
├── presentacion/            # Presentaciones Reveal.js
│   ├── tema1.html           # Una por cada tema
│   ├── ...
│   └── index.html           # Índice de presentaciones
├── recursos/
│   ├── imagenes/            # Figuras generadas
│   └── generar_figuras.py   # Script Python para gráficos
├── scripts/
│   └── build-pdf.py         # Generador de PDF con Pandoc
├── src/
│   └── css/custom.css       # Estilos personalizados
├── static/                  # Archivos estáticos (se copian al build)
├── .github/
│   └── workflows/
│       └── deploy.yml       # GitHub Actions para CI/CD
├── docusaurus.config.js     # Configuración de Docusaurus
├── sidebars.js              # Configuración del sidebar
├── package.json             # Dependencias Node.js
└── requirements.txt         # Dependencias Python
```

## 🚀 Despliegue Automático

Cada push a la rama `main` dispara automáticamente:

1. **Generación de figuras** con Python/matplotlib
2. **Construcción del PDF** con Pandoc (si está configurado)
3. **Build de Docusaurus** con las imágenes y presentaciones
4. **Despliegue a GitHub Pages**

Ver el workflow en [.github/workflows/deploy.yml](.github/workflows/deploy.yml).

### Configurar GitHub Pages

1. Ve a **Settings** → **Pages** del repositorio
2. En "Build and deployment", selecciona **GitHub Actions**
3. El workflow se encargará del resto

### Personalizar URLs

Edita `docusaurus.config.js` y cambia:
- `url`: Tu URL de GitHub Pages
- `organizationName`: Tu usuario de GitHub
- `projectName`: Nombre del repositorio

## 📖 Legislación

Los contenidos siguen:
- **Decreto 156/2022** (currículum ESO en Galicia)
- **LOMLOE** (Ley Orgánica 3/2020)
- Principios de **Diseño Universal para el Aprendizaje (DUA)**

Ver carpeta [legislacion/](legislacion/) para detalles.

## ✏️ Contribuir

1. Fork del repositorio
2. Crea una rama (`git checkout -b feature/mejora`)
3. Commit de cambios (`git commit -am 'Añade nueva actividad'`)
4. Push a la rama (`git push origin feature/mejora`)
5. Abre un Pull Request

## 📄 Licencia

Contenido bajo licencia **CC BY-SA 4.0** (Creative Commons Atribución-CompartirIgual).

Puedes:
- ✅ Compartir y adaptar el material
- ✅ Uso comercial permitido

Debes:
- 📝 Dar crédito apropiado
- 🔄 Compartir con la misma licencia

---

Desarrollado para el Departamento de Tecnología 🔧
