"""
Script para generar figuras educativas de señales analógicas y digitales
Unidad Didáctica de Electrónica Digital - 4º ESO
"""

import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo para uso educativo
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16

# Crear figura con dos subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# === SEÑAL ANALÓGICA ===
t = np.linspace(0, 4*np.pi, 1000)
señal_analogica = np.sin(t) + 0.3*np.sin(3*t)  # Señal compuesta más realista

ax1.plot(t, señal_analogica, 'b-', linewidth=2.5)
ax1.set_title('SEÑAL ANALÓGICA', fontweight='bold', pad=15)
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Tensión (V)')
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-2, 2)
ax1.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax1.text(0.5, -1.5, '✓ Valores continuos\n✓ Infinitos niveles posibles', 
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7),
         fontsize=11)

# === SEÑAL DIGITAL ===
t_digital = np.array([0, 0, 1, 1, 2, 2, 2.5, 2.5, 3.5, 3.5, 5, 5, 6.5, 6.5, 8, 8, 9, 9, 10, 10, 11, 11, 12.5])
señal_digital = np.array([0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1])

ax2.plot(t_digital, señal_digital, 'r-', linewidth=2.5, drawstyle='steps-post')
ax2.fill_between(t_digital, señal_digital, step='post', alpha=0.3, color='red')
ax2.set_title('SEÑAL DIGITAL', fontweight='bold', pad=15)
ax2.set_xlabel('Tiempo')
ax2.set_ylabel('Tensión (V)')
ax2.set_ylim(-0.3, 1.5)
ax2.set_yticks([0, 1])
ax2.set_yticklabels(['0V (BAJO)', '5V (ALTO)'])
ax2.grid(True, alpha=0.3)
ax2.axhline(y=0, color='k', linestyle='-', linewidth=0.5)
ax2.axhline(y=1, color='k', linestyle='--', linewidth=0.5, alpha=0.5)
ax2.text(0.5, 1.2, '✓ Solo dos valores: 0 y 1\n✓ Resistente al ruido', 
         bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7),
         fontsize=11)

plt.tight_layout()
plt.savefig('recursos/imagenes/señales_analogica_digital.png', dpi=300, bbox_inches='tight')
print("✓ Figura generada: señales_analogica_digital.png")

# === FIGURA 2: COMPARACIÓN CON RUIDO ===
fig2, ((ax3, ax4), (ax5, ax6)) = plt.subplots(2, 2, figsize=(14, 10))

# Señal analógica limpia
t2 = np.linspace(0, 2*np.pi, 500)
señal_limpia = np.sin(2*t2)
ax3.plot(t2, señal_limpia, 'b-', linewidth=2)
ax3.set_title('Señal Analógica LIMPIA', fontweight='bold')
ax3.set_ylim(-2, 2)
ax3.grid(True, alpha=0.3)

# Señal analógica con ruido
ruido = np.random.normal(0, 0.3, len(t2))
señal_ruidosa = señal_limpia + ruido
ax4.plot(t2, señal_ruidosa, 'orange', linewidth=2)
ax4.set_title('Señal Analógica CON RUIDO ⚠️', fontweight='bold', color='red')
ax4.set_ylim(-2, 2)
ax4.grid(True, alpha=0.3)
ax4.text(3, 1.5, '¡Distorsionada!\nDifícil de interpretar', 
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.8))

# Señal digital limpia
t3 = np.array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
señal_dig = np.array([0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1])
ax5.plot(t3, señal_dig, 'g-', linewidth=2.5, drawstyle='steps-post')
ax5.fill_between(t3, señal_dig, step='post', alpha=0.3, color='green')
ax5.set_title('Señal Digital LIMPIA', fontweight='bold')
ax5.set_ylim(-0.3, 1.5)
ax5.set_yticks([0, 1])
ax5.grid(True, alpha=0.3)

# Señal digital con ruido (pero aún interpretable)
ruido_digital = np.random.normal(0, 0.15, len(t3))
señal_dig_ruido = señal_dig + ruido_digital
ax6.plot(t3, señal_dig_ruido, 'darkgreen', linewidth=2, drawstyle='steps-post', alpha=0.7)
ax6.axhline(y=0.5, color='purple', linestyle='--', linewidth=2, label='Umbral de decisión')
ax6.fill_between(t3, señal_dig_ruido, step='post', alpha=0.2, color='green')
ax6.set_title('Señal Digital CON RUIDO ✓', fontweight='bold', color='green')
ax6.set_ylim(-0.3, 1.5)
ax6.set_yticks([0, 0.5, 1])
ax6.set_yticklabels(['0 (BAJO)', 'Umbral', '1 (ALTO)'])
ax6.grid(True, alpha=0.3)
ax6.legend()
ax6.text(0.3, 1.2, '¡Sigue siendo interpretable!\n0 sigue siendo 0\n1 sigue siendo 1', 
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

plt.suptitle('VENTAJA DIGITAL: INMUNIDAD AL RUIDO', fontsize=18, fontweight='bold', y=1.00)
plt.tight_layout()
plt.savefig('recursos/imagenes/comparacion_ruido.png', dpi=300, bbox_inches='tight')
print("✓ Figura generada: comparacion_ruido.png")

print("\n✅ Todas las figuras generadas correctamente")
print("📁 Ubicación: recursos/imagenes/")
