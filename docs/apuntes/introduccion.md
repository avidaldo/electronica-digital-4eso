---
sidebar_position: 1
title: Tema 1 - Introducción a la Electrónica Digital
description: Historia, señales analógicas vs digitales y aplicaciones cotidianas
---

# Tema 1: Introducción a la Electrónica Digital

## 🎯 Objetivos de Aprendizaje
Al finalizar este tema, serás capaz de:
- Diferenciar entre señales analógicas y digitales
- Explicar las ventajas de los sistemas digitales
- Identificar aplicaciones de la electrónica digital en la vida cotidiana
- Conocer la evolución histórica de la electrónica

---

## 1. ¿Qué es la Electrónica Digital?

La **electrónica digital** es la rama de la electrónica que trabaja con señales que solo pueden tomar **valores discretos** (normalmente dos: 0 y 1), a diferencia de la electrónica analógica, donde las señales pueden tomar cualquier valor dentro de un rango continuo.

### 1.1. Señales Analógicas vs Digitales

| Característica | Analógica | Digital |
|----------------|-----------|---------|
| **Valores** | Continuos (infinitos) | Discretos (0 y 1) |
| **Representación** | Onda continua | Pulsos cuadrados |
| **Ejemplos** | Temperatura, voz | Interruptor, dato binario |
| **Ruido** | Muy sensible | Muy resistente |
| **Procesamiento** | Complejo | Sencillo con lógica |

#### Representación gráfica:

![Comparación entre señal analógica y digital](/img/señales_analogica_digital.png)

*Arriba: Señal analógica (valores continuos). Abajo: Señal digital (solo dos niveles posibles, resistente al ruido).*

:::tip Ventaja clave
Una señal digital degradada por ruido sigue siendo interpretable (el 1 sigue siendo 1), mientras que una señal analógica se distorsiona.
:::

#### ¿Por qué la señal digital es más resistente al ruido?

![Comparación de resistencia al ruido](/img/comparacion_ruido.png)

Como puedes ver en la imagen, aunque la señal digital se vea afectada por ruido eléctrico, mientras los valores estén por encima o por debajo del **umbral de decisión** (normalmente 2.5V en sistemas de 5V), el circuito puede interpretarlos correctamente como 0 o 1. En cambio, la señal analógica pierde su forma original.

---

## 2. Representación de la Información Digital

En electrónica digital, usamos **dos niveles de tensión** para representar la información:

- **Nivel ALTO (1, TRUE):** Normalmente 5V o 3.3V
- **Nivel BAJO (0, FALSE):** Normalmente 0V (masa)

Esta simplicidad permite construir circuitos lógicos basados en **álgebra de Boole** (Tema 3).

### 2.1. El Bit: Unidad Básica

Un **bit** (binary digit) es la unidad mínima de información: puede ser 0 o 1.

- **1 byte** = 8 bits
- **1 kilobyte (KB)** = 1024 bytes
- Ejemplo: La letra "A" en código ASCII se representa con 8 bits: `01000001`

---

## 3. Ventajas de los Sistemas Digitales

1. **Inmunidad al ruido:** Pequeñas perturbaciones no afectan al resultado.
2. **Facilidad de almacenamiento:** Se puede guardar información de forma permanente sin degradación.
3. **Procesamiento potente:** Operaciones lógicas y aritméticas muy rápidas.
4. **Reproducibilidad:** Los circuitos digitales se comportan siempre igual (fiabilidad).
5. **Miniaturización:** Los transistores digitales pueden ser microscópicos (chips con miles de millones).

---

## 4. Evolución Histórica

### 4.1. Cronología Básica

| Año | Hito |
|-----|------|
| **1904** | Tubo de vacío (Fleming) - Primera "válvula" electrónica |
| **1947** | Invención del **transistor** (Bardeen, Brattain, Shockley) - Nobel 1956 |
| **1958** | Primer **circuito integrado** (Jack Kilby) |
| **1971** | Intel 4004: Primer **microprocesador** comercial (2300 transistores) |
| **2020** | Apple M1: Chip con **16.000 millones** de transistores |

### 4.2. Ley de Moore

Gordon Moore (1965) predijo que el número de transistores en un chip se **duplicaría cada 18-24 meses**. Esta ley se ha cumplido durante décadas, permitiendo los smartphones y ordenadores actuales.

---

## 5. Aplicaciones Cotidianas

La electrónica digital está en **todos** los dispositivos tecnológicos:

### Ejemplos:
- **🏠 Hogar:** Lavadoras, microondas, termostatos inteligentes
- **📱 Comunicación:** Smartphones, routers, antenas 5G
- **🚗 Transporte:** Control de motor, ABS, GPS
- **🎮 Ocio:** Consolas, drones, cámaras digitales
- **🏥 Salud:** Marcapasos, escáneres TAC, termómetros digitales
- **🏭 Industria:** Autómatas (PLCs), robots, control de calidad

:::note Caso práctico
Un **semáforo** es un sistema digital simple:
- Entrada: Sensor de vehículo (0=no hay coche, 1=hay coche)
- Proceso: Circuito lógico decide qué luz encender
- Salida: LEDs rojo/ámbar/verde
:::

---

## 6. Electrónica Digital y Sostenibilidad

### 6.1. Impacto Ambiental

**Aspectos positivos:**
- Optimización del consumo energético (edificios inteligentes)
- Control de procesos industriales más eficientes

**Aspectos negativos:**
- **Residuos electrónicos (e-waste):** Componentes con metales pesados (plomo, mercurio)
- Consumo energético de centros de datos (nube)
- Obsolescencia programada

### 6.2. Buenas Prácticas

- ♻️ Reciclar dispositivos en puntos limpios
- 🔧 Reparar antes que sustituir
- ⚡ Usar modos de bajo consumo
- 📦 Elegir fabricantes comprometidos con el medio ambiente

---

## 📝 Actividades

### Actividad 1: Identifica Sistemas Digitales
Haz una lista de 10 dispositivos de tu casa que contengan electrónica digital. Clasifícalos por su función (control, comunicación, entretenimiento, etc.).

### Actividad 2: Analógico vs Digital
Busca un ejemplo de un dispositivo que haya pasado de ser analógico a digital (ej. teléfono de disco → smartphone) y explica las ventajas del cambio.

### Actividad 3: Investigación - Ley de Moore
Investiga si la Ley de Moore sigue vigente en 2026. ¿Cuáles son los límites físicos que se están alcanzando?

---

## ❓ Preguntas de Repaso

1. ¿Cuál es la principal diferencia entre una señal analógica y una digital?
2. ¿Qué niveles de tensión representan típicamente el 0 y el 1?
3. Nombra 3 ventajas de los sistemas digitales sobre los analógicos.
4. ¿Qué invento de 1947 revolucionó la electrónica?
5. Explica con un ejemplo cómo la electrónica digital puede ayudar al medio ambiente.
