# Tema 7: Prácticas de Taller

## 🎯 Objetivos de Aprendizaje
Al finalizar este tema, serás capaz de:
- Utilizar correctamente una protoboard (placa de prototipado)
- Identificar y manejar circuitos integrados digitales
- Montar y verificar circuitos lógicos básicos
- Usar simuladores de electrónica digital
- Diagnosticar fallos comunes en montajes

---

## 1. La Protoboard (Breadboard)

### 1.1. Estructura

Una protoboard permite montar circuitos **sin soldadura**, mediante conexiones internas.

**Diagrama de conexiones:**

```
    BUSES DE ALIMENTACIÓN (horizontales)
    ┌────────────────────────────────────┐
    │ + + + + + + + + + + + + + + + + +  │  ← VCC (Rojo)
    │ - - - - - - - - - - - - - - - - -  │  ← GND (Negro/Azul)
    ├────────────────────────────────────┤
    │ a b c d e   f g h i j              │
    │ ○ ○ ○ ○ ○   ○ ○ ○ ○ ○  1           │
    │ ○ ○ ○ ○ ○   ○ ○ ○ ○ ○  2           │
    │ ○ ○ ○ ○ ○   ○ ○ ○ ○ ○  3           │
    │    ...     Canal ...               │
    │ ○ ○ ○ ○ ○   ○ ○ ○ ○ ○  30          │
    ├────────────────────────────────────┤
    │ - - - - - - - - - - - - - - - - -  │  ← GND
    │ + + + + + + + + + + + + + + + + +  │  ← VCC
    └────────────────────────────────────┘
```

**Conexiones internas:**
- **Buses laterales:** Conectados horizontalmente (toda la fila)
- **Filas centrales:** Conectadas verticalmente (a-e juntos, f-j juntos)
- **Canal central:** Separación para insertar CIs

---

### 1.2. Reglas de Uso

✅ **Hacer:**
- Insertar componentes con cuidado (sin forzar)
- Usar cables de colores (Rojo=+5V, Negro=GND, otros=señales)
- Mantener el montaje ordenado y limpio

❌ **NO hacer:**
- Insertar componentes con la alimentación conectada
- Forzar componentes (puedes doblar pines)
- Crear cortocircuitos directos entre VCC y GND
- Tocar los pines de los CIs con los dedos (electricidad estática)

---

## 2. Circuitos Integrados (CIs) Digitales

### 2.1. Identificación de un CI

**Información en el chip:**

```
    74LS08N
    ────────
    │o      │  ← Muesca (indica pin 1)
    │1    14│
    │2    13│
    │...    │
    │7     8│
    └───────┘
```

**Nomenclatura:** 74LS08
- **74:** Familia TTL estándar
- **LS:** Low-power Schottky (bajo consumo)
- **08:** Función (4 puertas AND)
- **N:** Encapsulado (DIP plástico)

**Pin 1:** Marcado con muesca, punto o círculo. Se cuenta en sentido **antihorario**.

---

### 2.2. Familias Lógicas

| Familia | Alimentación | Velocidad | Consumo | Observaciones |
|---------|--------------|-----------|---------|---------------|
| **TTL (74xx)** | 5V ±0.25V | Rápida | Alto | Estándar industrial |
| **LS (74LSxx)** | 5V | Media | Bajo | Más usada en educación |
| **CMOS (40xx)** | 3-15V | Lenta | Muy bajo | Más versátil en tensión |
| **HC (74HCxx)** | 5V | Rápida | Bajo | CMOS compatible con TTL |

**Niveles lógicos TTL:**
- **Nivel ALTO (1):** 2.0V - 5V
- **Nivel BAJO (0):** 0V - 0.8V
- **Zona prohibida:** 0.8V - 2.0V (indefinido)

---

### 2.3. Pinout de CIs Comunes

#### CI 7408 (4 puertas AND)

```
     7408
    ┌──┐─┐
1A  │1 └┐│ 14 VCC
1B  │2  ││ 13 4B
1Y  │3  ││ 12 4A
2A  │4  ││ 11 4Y
2B  │5  ││ 10 3B
2Y  │6  ││  9 3A
GND │7  ││  8 3Y
    └────┘
```

**IMPORTANTE:** Pin 14 = +5V, Pin 7 = GND (común a casi todos los CIs de 14 pines)

#### CI 7404 (6 inversores NOT)

```
     7404
    ┌──┐─┐
1A  │1 └┐│ 14 VCC
1Y  │2  ││ 13 6A
2A  │3  ││ 12 6Y
2Y  │4  ││ 11 5A
3A  │5  ││ 10 5Y
3Y  │6  ││  9 4A
GND │7  ││  8 4Y
    └────┘
```

---

## 3. Montaje Básico: Puerta AND con LED

### 3.1. Componentes Necesarios

- 1x CI 7408 (puertas AND)
- 2x Interruptores o pulsadores
- 1x LED (rojo, verde, etc.)
- 1x Resistencia 330Ω (para proteger el LED)
- 2x Resistencias 10kΩ (pull-down para las entradas)
- Fuente de alimentación 5V
- Cables de conexión

### 3.2. Esquema del Circuito

```
       +5V
        │
        ├──[Interruptor A]──┬──[10kΩ]──GND
        │                   │
        │                   ├─→ Pin 1 (1A)
        │                   
        ├──[Interruptor B]──┬──[10kΩ]──GND
        │                   │
        │                   ├─→ Pin 2 (1B)
        │
       Pin 14 (VCC)
        
       Pin 7 (GND) ──→ GND
       
       Pin 3 (1Y) ──→ [330Ω] ──→ [LED+] ──→ GND
```

### 3.3. Pasos de Montaje

1. **Desconectar la alimentación**
2. Insertar el CI 7408 atravesando el canal central
3. Conectar Pin 14 al bus +5V (cable rojo)
4. Conectar Pin 7 al bus GND (cable negro)
5. Montar los interruptores con resistencias pull-down
6. Conectar las salidas de los interruptores a pines 1 y 2
7. Conectar Pin 3 → Resistencia 330Ω → LED (ánodo)
8. Conectar cátodo del LED a GND
9. **Revisar conexiones** (comprobar que no hay cortos)
10. Conectar la alimentación

### 3.4. Verificación

Probar las 4 combinaciones:

| A | B | LED |
|---|---|-----|
| 0 | 0 | Apagado |
| 0 | 1 | Apagado |
| 1 | 0 | Apagado |
| 1 | 1 | **Encendido** |

---

## 4. Componentes Auxiliares

### 4.1. Resistencias

**Función:** Limitar corriente, pull-up/pull-down

**Código de colores:**

| Color | Valor |
|-------|-------|
| Marrón | 1 |
| Rojo | 2 |
| Naranja | 3 |
| Amarillo | 4 |
| Verde | 5 |
| Azul | 6 |
| Violeta | 7 |
| Gris | 8 |
| Blanco | 9 |

**Ejemplo:** 330Ω = **Naranja-Naranja-Marrón** (33 × 10¹)

**Valores comunes:**
- 330Ω: Protección de LEDs (5V)
- 1kΩ: Limitación de corriente general
- 10kΩ: Pull-down/pull-up

### 4.2. LEDs

**Polaridad:**
- **Ánodo (+):** Patilla larga
- **Cátodo (-):** Patilla corta, lado plano

**Caída de tensión típica:**
- Rojo: 1.8V
- Verde: 2.0V
- Azul/Blanco: 3.0V

**Cálculo de resistencia limitadora:**
$$
R = \frac{V_{fuente} - V_{LED}}{I_{LED}}
$$

Ejemplo (LED rojo, 5V, 10mA):
$$
R = \frac{5V - 1.8V}{0.01A} = 320\Omega \approx 330\Omega
$$

### 4.3. Interruptores y Pulsadores

**Tipos:**
- **SPST:** Simple, 2 pines
- **SPDT:** Doble posición, 3 pines
- **Pulsador NA (Normalmente Abierto):** Cierra al pulsar
- **Pulsador NC (Normalmente Cerrado):** Abre al pulsar

**Resistencias pull-down/pull-up:**
- **Pull-down:** Entrada → GND con 10kΩ → Interruptor a VCC
- **Pull-up:** Entrada → VCC con 10kΩ → Interruptor a GND

---

## 5. Uso de Multímetro

### 5.1. Medición de Tensión (Voltaje)

1. Selector en "V─" (voltaje DC)
2. Cable negro a COM
3. Cable rojo a V/Ω
4. Tocar con las puntas el punto a medir (relativo a GND)

**Valores esperados:**
- VCC: 5V ±0.25V
- Entrada alta: > 2.0V
- Entrada baja: < 0.8V

### 5.2. Comprobación de Continuidad

1. Selector en símbolo "•)))" (continuidad)
2. Tocar dos puntos → Si hay conexión, pita

**Uso:** Verificar que las conexiones internas de la protoboard funcionan.

---

## 6. Simuladores de Electrónica Digital

### 6.1. Tinkercad Circuits

**URL:** [https://www.tinkercad.com/circuits](https://www.tinkercad.com/circuits)

**Ventajas:**
- Interfaz visual muy intuitiva
- Biblioteca de CIs TTL (74xx)
- Simulación en tiempo real
- Montaje tipo protoboard

**Pasos básicos:**
1. Crear cuenta gratuita
2. "Crear nuevo circuito"
3. Arrastrar componentes (CIs, LEDs, interruptores)
4. Conectar con clics
5. "Iniciar simulación"

**Práctica recomendada:** Montar primero en Tinkercad antes de pasar a la protoboard física.

---

### 6.2. Falstad Circuit Simulator

**URL:** [https://www.falstad.com/circuit/](https://www.falstad.com/circuit/)

**Ventajas:**
- Simulación en tiempo real muy rápida
- Visualización del flujo de corriente (colores)
- No requiere registro
- Sección específica de lógica digital

**Limitaciones:**
- Interfaz menos intuitiva
- No modela CIs reales (solo funciones lógicas)

**Uso:** Ideal para verificar la lógica de un circuito antes de implementarlo.

---

### 6.3. Logisim (Evolution)

**Tipo:** Aplicación de escritorio (Windows/Mac/Linux)

**Ventajas:**
- Diseño de circuitos complejos (CPUs completas)
- Jerarquía de subcircuitos
- Análisis cronograma (timing)

**Descargar:** [GitHub - Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution)

**Uso:** Proyectos avanzados, simulación de sistemas completos.

---

## 7. Diagnóstico de Fallos

### 7.1. El Circuito No Funciona

**Checklist de verificación:**

1. ☐ ¿Está conectada la alimentación?
2. ☐ ¿El CI tiene alimentación? (Medir VCC en pin 14 y GND en pin 7)
3. ☐ ¿Los cables están bien insertados? (probar continuidad)
4. ☐ ¿El LED está bien polarizado? (ánodo a positivo)
5. ☐ ¿Hay resistencia limitadora en el LED?
6. ☐ ¿Las entradas están definidas? (no flotantes)
7. ☐ ¿El CI está insertado correctamente? (pin 1 en su sitio)

---

### 7.2. Problemas Comunes

| Síntoma | Causa Probable | Solución |
|---------|----------------|----------|
| LED siempre encendido | Cortocircuito en salida | Revisar conexiones |
| LED siempre apagado | Entrada flotante o sin alimentación | Añadir pull-down, verificar VCC |
| LED muy tenue | Resistencia demasiado alta | Usar 330Ω en lugar de 1kΩ |
| CI se calienta | Cortocircuito VCC-GND | ¡Desconectar inmediatamente! |
| Funciona a veces | Contactos flojos en protoboard | Reinsertar componentes |
| No pasa nada | CI quemado | Reemplazar chip |

---

### 7.3. Entradas Flotantes

**Problema:** Una entrada digital sin conectar puede "flotar" entre 0 y 1, dando resultados impredecibles.

**Solución:**
- **Entradas no usadas de puertas AND/NAND:** Conectar a VCC (=1)
- **Entradas no usadas de puertas OR/NOR:** Conectar a GND (=0)
- **Mejor:** Usar siempre resistencias pull-down (10kΩ a GND) en las entradas

---

## 8. Prácticas Propuestas

### Práctica 1: Puerta OR con LED
Montar un circuito con CI 7432 (OR) que encienda un LED si **al menos uno** de dos interruptores está cerrado.

### Práctica 2: Circuito con NOT
Usar un 7404 (NOT) para hacer que un LED se encienda cuando el interruptor está **abierto**.

### Práctica 3: Combinación AND-OR
Implementar: $F = AB + C$
- Usar 7408 (AND) y 7432 (OR)
- 3 interruptores de entrada
- 1 LED de salida

### Práctica 4: Decodificador 2 a 4
Construir un decodificador con puertas lógicas básicas (sin usar CI 74LS139):
- 2 entradas (A, B)
- 4 LEDs de salida (solo uno encendido según A-B)

### Práctica 5: Display de 7 Segmentos
- Conectar un display de cátodo común
- Usar resistencias de 330Ω en cada segmento
- Probar a encender cada dígito (0-9) manualmente con interruptores

---

## 9. Normas de Seguridad

### 9.1. Seguridad Eléctrica

⚠️ **Precauciones:**
- Trabajamos con **5V** (voltaje seguro), pero la corriente puede dañar componentes
- Nunca tocar circuitos en funcionamiento con objetos metálicos
- Desconectar la alimentación **antes** de modificar el circuito
- No forzar componentes (los pines se doblan o rompen)

### 9.2. Protección de Componentes

- **Electricidad estática:** Puede destruir CIs CMOS. Tocar una superficie metálica conectada a tierra antes de manipular chips.
- **Polaridad:** LEDs, condensadores electrolíticos y algunos CIs tienen polaridad. Verificar siempre.
- **Corriente máxima:** Los CIs TTL pueden suministrar 8-16mA por salida. No conectar motores o cargas grandes directamente.

### 9.3. Orden en el Taller

- Mantener el área de trabajo limpia
- Guardar componentes en cajas organizadas
- Etiquetar los cables de alimentación
- No comer ni beber cerca de los circuitos

---

## 10. Proyecto Final: Semáforo

### 10.1. Especificaciones

**Diseñar un semáforo de 2 fases:**
- Fase A: Verde A + Rojo B
- Fase B: Rojo A + Verde B
- Cambio manual con un pulsador

**Componentes:**
- 1x CI 7404 (NOT)
- 4x LEDs (2 rojos, 2 verdes)
- 1x Pulsador
- Resistencias 330Ω
- Protoboard y cables

### 10.2. Diseño

**Lógica:**
- Entrada: Pulsador (P)
- Salidas: Verde_A, Rojo_A, Verde_B, Rojo_B

**Expresiones:**
$$
Verde_A = P
$$
$$
Rojo_A = \overline{P}
$$
$$
Verde_B = \overline{P}
$$
$$
Rojo_B = P
$$

**Circuito:** Un inversor (NOT) permite obtener las señales complementarias.

---

## 📝 Actividades

### Actividad 1: Identificación de Componentes
Dado un CI 74LS08, identifica:
1. ¿Dónde está el pin 1?
2. ¿Qué pines son VCC y GND?
3. ¿Cuántas puertas lógicas contiene?

### Actividad 2: Montaje Virtual
Reproduce el circuito AND con LED en Tinkercad y comprueba su tabla de verdad.

### Actividad 3: Cálculo de Resistencia
Calcula la resistencia necesaria para un LED azul (3.0V, 15mA) con fuente de 5V.

### Actividad 4: Diagnóstico
Un circuito con una puerta OR no funciona. El LED está siempre apagado. Lista 5 posibles causas.

### Actividad 5: Proyecto Libre
Diseña y monta un circuito que resuelva un problema de tu elección (alarma, votación, control de acceso, etc.).

---

## ❓ Preguntas de Repaso

1. ¿Por qué es importante no forzar los componentes en la protoboard?
2. ¿Qué pines se conectan a alimentación en un CI de 14 pines?
3. ¿Qué es una entrada flotante y por qué es problemática?
4. ¿Qué mide un multímetro en modo continuidad?
5. Nombra 2 ventajas de simular antes de montar físicamente.

---

## 🔗 Recursos Adicionales

- **Video:** [Cómo usar una protoboard](https://www.youtube.com/watch?v=example)
- **Datasheets:** [All 74xx ICs](http://www.skot9000.com/ttl/)
- **Calculadora de LEDs:** [LED Resistor Calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-led-series-resistor)

---

## 📦 Lista de Materiales Recomendada (Kit de Prácticas)

### Componentes Digitales
- CIs: 7408 (AND), 7432 (OR), 7404 (NOT), 7486 (XOR)
- Display 7 segmentos (cátodo común)
- Protoboard 830 puntos

### Componentes Pasivos
- LEDs: 10 rojos, 5 verdes, 5 amarillos
- Resistencias: 330Ω (10x), 1kΩ (10x), 10kΩ (10x)
- Pulsadores NA (5x)

### Herramientas
- Multímetro digital
- Fuente de alimentación 5V (USB o adaptador)
- Cables jumper (macho-macho)
- Alicates de punta fina

---

**Tema anterior:** [Circuitos Combinacionales](06_circuitos_combinacionales.md)  
**Volver al índice:** [Índice de Apuntes](00_indice.md)
