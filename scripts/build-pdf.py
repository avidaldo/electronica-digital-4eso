#!/usr/bin/env python3
"""
Script para generar PDF de los apuntes de Electrónica Digital.
Combina todos los archivos Markdown en un único PDF usando Pandoc.

Requisitos:
- Python 3.8+
- Pandoc (https://pandoc.org/installing.html)
- Motor LaTeX: TeX Live o MiKTeX con xelatex

Uso:
    python scripts/build-pdf.py
    python scripts/build-pdf.py --output apuntes_electronica.pdf
"""

import subprocess
import sys
import argparse
from pathlib import Path
from datetime import datetime

# Configuración
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
APUNTES_DIR = PROJECT_ROOT / "apuntes"
OUTPUT_DIR = PROJECT_ROOT / "dist"
RECURSOS_DIR = PROJECT_ROOT / "recursos"

# Orden de los archivos (sin el índice, se genera automáticamente)
ARCHIVOS_ORDEN = [
    "01_introduccion.md",
    "02_sistemas_numeracion.md",
    "03_algebra_boole.md",
    "04_puertas_logicas.md",
    "05_diseno_circuitos.md",
    "06_circuitos_combinacionales.md",
    "07_practicas_taller.md",
]

# Metadatos del documento
METADATA = {
    "title": "Electrónica Digital",
    "subtitle": "Apuntes de Tecnología 4º ESO",
    "author": "Departamento de Tecnología",
    "date": datetime.now().strftime("%d de %B de %Y"),
    "lang": "es-ES",
}


def check_dependencies():
    """Verifica que Pandoc esté instalado."""
    try:
        result = subprocess.run(
            ["pandoc", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        version = result.stdout.split("\n")[0]
        print(f"✓ {version}")
        return True
    except FileNotFoundError:
        print("✗ Error: Pandoc no está instalado.")
        print("  Instálalo desde: https://pandoc.org/installing.html")
        return False
    except subprocess.CalledProcessError as e:
        print(f"✗ Error al ejecutar Pandoc: {e}")
        return False


def check_latex():
    """Verifica que xelatex esté disponible."""
    try:
        subprocess.run(
            ["xelatex", "--version"],
            capture_output=True,
            check=True
        )
        print("✓ XeLaTeX disponible")
        return True
    except FileNotFoundError:
        print("⚠ XeLaTeX no encontrado. Intentando con pdflatex...")
        try:
            subprocess.run(
                ["pdflatex", "--version"],
                capture_output=True,
                check=True
            )
            print("✓ pdfLaTeX disponible (alternativo)")
            return True
        except FileNotFoundError:
            print("✗ Error: No se encontró ningún motor LaTeX.")
            print("  Instala TeX Live o MiKTeX.")
            return False


def create_metadata_file():
    """Crea archivo YAML temporal con metadatos."""
    metadata_content = f"""---
title: "{METADATA['title']}"
subtitle: "{METADATA['subtitle']}"
author: "{METADATA['author']}"
date: "{METADATA['date']}"
lang: {METADATA['lang']}
documentclass: report
geometry:
  - margin=2.5cm
  - a4paper
fontsize: 11pt
linestretch: 1.15
toc: true
toc-depth: 3
numbersections: true
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - \\usepackage{{fancyhdr}}
  - \\pagestyle{{fancy}}
  - \\fancyhead[L]{{Electrónica Digital}}
  - \\fancyhead[R]{{4º ESO}}
  - \\fancyfoot[C]{{\\thepage}}
  - \\usepackage{{tcolorbox}}
---

"""
    metadata_file = OUTPUT_DIR / "metadata.yaml"
    metadata_file.write_text(metadata_content, encoding="utf-8")
    return metadata_file


def preprocess_markdown(content: str, source_file: Path) -> str:
    """
    Preprocesa el contenido Markdown para compatibilidad con Pandoc.
    - Ajusta rutas de imágenes
    - Elimina emojis problemáticos o los convierte
    """
    # Ajustar rutas de imágenes relativas
    content = content.replace("../recursos/imagenes/", str(RECURSOS_DIR / "imagenes") + "/")
    content = content.replace("../recursos/", str(RECURSOS_DIR) + "/")
    
    # Mapa de emojis a texto (para compatibilidad LaTeX básica)
    emoji_map = {
        "🎯": "**[Objetivo]**",
        "📚": "**[Contenido]**",
        "🔧": "**[Recurso]**",
        "📝": "**[Actividad]**",
        "❓": "**[Pregunta]**",
        "💡": "**[Nota]**",
        "♻️": "[Reciclar]",
        "🔌": "[Eléctrico]",
        "⚡": "[Energía]",
        "📦": "[Paquete]",
        "🏠": "[Casa]",
        "📱": "[Móvil]",
        "🚗": "[Coche]",
        "🎮": "[Juego]",
        "🏥": "[Salud]",
        "🏭": "[Industria]",
    }
    
    for emoji, replacement in emoji_map.items():
        content = content.replace(emoji, replacement)
    
    return content


def combine_markdown_files():
    """Combina todos los archivos Markdown en uno solo."""
    combined_content = []
    
    for filename in ARCHIVOS_ORDEN:
        filepath = APUNTES_DIR / filename
        if filepath.exists():
            print(f"  Procesando: {filename}")
            content = filepath.read_text(encoding="utf-8")
            processed = preprocess_markdown(content, filepath)
            combined_content.append(processed)
            combined_content.append("\n\\newpage\n\n")  # Salto de página entre temas
        else:
            print(f"  ⚠ Archivo no encontrado: {filename}")
    
    combined_file = OUTPUT_DIR / "combined_apuntes.md"
    combined_file.write_text("\n".join(combined_content), encoding="utf-8")
    return combined_file


def build_pdf(output_filename: str):
    """Ejecuta Pandoc para generar el PDF."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print("\n📄 Generando PDF de apuntes...")
    print("-" * 40)
    
    # Crear archivo combinado
    print("1. Combinando archivos Markdown...")
    combined_file = combine_markdown_files()
    
    # Crear metadatos
    print("\n2. Configurando metadatos...")
    metadata_file = create_metadata_file()
    
    # Construir comando Pandoc
    output_path = OUTPUT_DIR / output_filename
    
    cmd = [
        "pandoc",
        str(combined_file),
        str(metadata_file),
        "-o", str(output_path),
        "--pdf-engine=xelatex",
        "--highlight-style=tango",
        "--standalone",
        "-V", "mainfont=DejaVu Sans",
        "-V", "monofont=DejaVu Sans Mono",
        "--resource-path", str(RECURSOS_DIR),
        "--resource-path", str(APUNTES_DIR),
    ]
    
    print(f"\n3. Ejecutando Pandoc...")
    print(f"   Comando: {' '.join(cmd[:5])}...")
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )
        
        if result.returncode == 0:
            print(f"\n✅ PDF generado correctamente: {output_path}")
            print(f"   Tamaño: {output_path.stat().st_size / 1024:.1f} KB")
            return True
        else:
            print(f"\n❌ Error al generar PDF:")
            print(result.stderr)
            
            # Intentar con pdflatex como alternativa
            print("\n🔄 Intentando con pdflatex...")
            cmd[cmd.index("--pdf-engine=xelatex")] = "--pdf-engine=pdflatex"
            # Quitar fuentes personalizadas para pdflatex
            cmd = [c for c in cmd if not c.startswith("-V") or "font" not in c]
            
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=PROJECT_ROOT)
            if result.returncode == 0:
                print(f"\n✅ PDF generado con pdflatex: {output_path}")
                return True
            else:
                print(f"❌ También falló con pdflatex:\n{result.stderr}")
                return False
                
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        return False
    finally:
        # Limpieza de archivos temporales
        for temp_file in OUTPUT_DIR.glob("*.aux"):
            temp_file.unlink()
        for temp_file in OUTPUT_DIR.glob("*.log"):
            temp_file.unlink()


def main():
    parser = argparse.ArgumentParser(
        description="Genera PDF de los apuntes de Electrónica Digital"
    )
    parser.add_argument(
        "-o", "--output",
        default="apuntes_electronica_digital.pdf",
        help="Nombre del archivo PDF de salida (default: apuntes_electronica_digital.pdf)"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Solo verificar dependencias sin generar PDF"
    )
    
    args = parser.parse_args()
    
    print("=" * 50)
    print("  Generador de PDF - Electrónica Digital 4º ESO")
    print("=" * 50)
    
    print("\n🔍 Verificando dependencias...")
    pandoc_ok = check_dependencies()
    latex_ok = check_latex()
    
    if args.check:
        if pandoc_ok and latex_ok:
            print("\n✅ Todas las dependencias están instaladas.")
            sys.exit(0)
        else:
            print("\n❌ Faltan dependencias.")
            sys.exit(1)
    
    if not pandoc_ok:
        sys.exit(1)
    
    success = build_pdf(args.output)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
