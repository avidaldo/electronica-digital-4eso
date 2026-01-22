---
sidebar_position: 7
title: Tema 7 - Prácticas de Taller
description: Uso de protoboard, CIs digitales, montaje y simuladores
---

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

:::warning IMPORTANTE
Pin 14 = +5V, Pin 7 = GND (común a casi todos los CIs de 14 pines)
:::

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

## 4. Simuladores de Electrónica Digital

### 4.1. Tinkercad Circuits

**URL:** [tinkercad.com/circuits](https://www.tinkercad.com/circuits)

**Ventajas:**
- Gratuito y online (no necesita instalación)
- Incluye componentes reales (CIs, protoboard)
- Simulación en tiempo real
- Permite código Arduino

**Cómo usarlo:**
1. Crear cuenta gratuita
2. Nuevo diseño → "Circuits"
3. Arrastrar componentes desde la barra lateral
4. Conectar con cables (clic y arrastrar)
5. Iniciar simulación

### 4.2. Falstad Circuit Simulator

**URL:** [falstad.com/circuit](https://falstad.com/circuit/)

**Ventajas:**
- Muy visual (muestra flujo de corriente)
- Incluye sección "Digital Logic"
- Sin registro

---

## 5. Diagnóstico de Fallos

### 5.1. Fallos Comunes

| Síntoma | Posible Causa | Solución |
|---------|---------------|----------|
| Nada funciona | Falta alimentación | Comprobar VCC y GND |
| LED siempre encendido | Cortocircuito a VCC | Revisar conexiones |
| LED siempre apagado | LED invertido o quemado | Verificar polaridad, probar LED |
| Comportamiento errático | Entradas flotantes | Añadir resistencias pull-down/up |
| CI muy caliente | Cortocircuito interno | Desconectar y revisar |

### 5.2. Herramientas de Diagnóstico

- **Multímetro:** Medir tensiones y continuidad
- **LED de prueba:** Verificar niveles lógicos
- **Cables de repuesto:** Sustituir cables sospechosos

---

## 6. Normas de Seguridad

:::danger Seguridad en el taller
1. **Trabajar sin tensión** al montar o modificar circuitos
2. **Nunca superar 5V** en circuitos TTL
3. **Descargar electricidad estática** antes de tocar CIs
4. **Guardar componentes** en bolsas antiestáticas
5. **No comer ni beber** en el taller
6. **Informar de averías** al profesor
:::

---

## 📝 Prácticas

### Práctica 1: Puerta AND
Monta el circuito del apartado 3 y verifica la tabla de verdad.

### Práctica 2: Puerta OR
Repite con el CI 7432 (puertas OR).

### Práctica 3: Sistema de Alarma
Diseña y monta: "La alarma suena si hay humo (S1) O si hay intrusión (S2) Y NO está desactivada (D)"

$$
F = S_1 + (S_2 \cdot \overline{D})
$$

### Práctica 4: Display 7 Segmentos
Monta un circuito con CI 7447 + display para mostrar los dígitos 0-9.

### Práctica 5: Votación
Implementa el sistema de voto por mayoría del Tema 5.

---

## ❓ Preguntas de Repaso

1. ¿Cómo se identifican las filas conectadas en una protoboard?
2. ¿Qué significa "74LS08"?
3. ¿Por qué necesitamos resistencias pull-down?
4. ¿Cuál es la función del pin 7 en un CI de 14 pines?
5. ¿Qué herramienta usarías para comprobar si hay 5V en un punto?

---

## 🔗 Recursos Adicionales

- **Video tutorial protoboard:** [YouTube - Cómo usar una protoboard](https://www.youtube.com/)
- **Pinouts de todos los CIs:** [Datasheet Catalog](https://www.datasheetcatalog.com/)
- **Tutoriales Tinkercad:** [learn.tinkercad.com](https://www.tinkercad.com/learn/circuits)
