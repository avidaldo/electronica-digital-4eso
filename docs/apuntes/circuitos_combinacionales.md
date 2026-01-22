---
sidebar_position: 6
title: Tema 6 - Circuitos Combinacionales
description: Codificadores, decodificadores, display 7 segmentos, multiplexores
---

# Tema 6: Circuitos Combinacionales

## 🎯 Objetivos de Aprendizaje
Al finalizar este tema, serás capaz de:
- Comprender qué es un circuito combinacional
- Analizar y diseñar codificadores y decodificadores
- Controlar displays de 7 segmentos
- Utilizar multiplexores y demultiplexores
- Aplicar estos bloques a problemas prácticos

---

## 1. ¿Qué es un Circuito Combinacional?

**Definición:** Circuito cuya salida depende **exclusivamente** del estado actual de las entradas (sin memoria).

$$
\text{Salida} = f(\text{Entradas actuales})
$$

**Características:**
- No tiene realimentación (las salidas no vuelven a las entradas)
- No depende del tiempo ni del estado anterior
- Ejemplos: sumadores, comparadores, codificadores

:::info Contraparte
Los **circuitos secuenciales** (tema de 1º Bachillerato) sí tienen memoria (flip-flops, contadores).
:::

---

## 2. Codificadores

### 2.1. Definición

Un **codificador** convierte información de $2^n$ entradas a $n$ salidas en código binario.

**Ejemplo:** Codificador de 8 a 3
- 8 entradas (una por cada línea)
- 3 salidas (código binario de 0 a 7)

### 2.2. Codificador de 4 a 2

**Función:** Detecta cuál de las 4 entradas está activa y devuelve su número en binario.

**Tabla de verdad:**

| $I_3$ | $I_2$ | $I_1$ | $I_0$ | $S_1$ | $S_0$ | Decimal |
|-------|-------|-------|-------|-------|-------|---------|
| 0     | 0     | 0     | 1     | 0     | 0     | 0       |
| 0     | 0     | 1     | 0     | 0     | 1     | 1       |
| 0     | 1     | 0     | 0     | 1     | 0     | 2       |
| 1     | 0     | 0     | 0     | 1     | 1     | 3       |

**Expresiones:**
$$
S_1 = I_2 + I_3
$$
$$
S_0 = I_1 + I_3
$$

**Aplicación:** Teclados matriciales (detectar qué tecla se ha pulsado)

### 2.3. Codificador de Prioridad

**Problema del codificador simple:** Si se activan varias entradas a la vez, hay conflicto.

**Solución:** El codificador de prioridad asigna preferencia a la entrada más significativa.

**CI comercial:** 74LS148 (codificador de prioridad de 8 a 3)

---

## 3. Decodificadores

### 3.1. Definición

Un **decodificador** hace la operación inversa: convierte $n$ entradas binarias en $2^n$ salidas (solo una activa).

### 3.2. Decodificador de 2 a 4

**Tabla de verdad:**

| $A$ | $B$ | $S_0$ | $S_1$ | $S_2$ | $S_3$ |
|-----|-----|-------|-------|-------|-------|
| 0   | 0   | 1     | 0     | 0     | 0     |
| 0   | 1   | 0     | 1     | 0     | 0     |
| 1   | 0   | 0     | 0     | 1     | 0     |
| 1   | 1   | 0     | 0     | 0     | 1     |

**Expresiones:**
$$
S_0 = \overline{A} \cdot \overline{B}
$$
$$
S_1 = \overline{A} \cdot B
$$
$$
S_2 = A \cdot \overline{B}
$$
$$
S_3 = A \cdot B
$$

**Circuito:** 2 inversores + 4 puertas AND de 2 entradas

**CI comercial:** 74LS139 (doble decodificador 2 a 4)

---

## 4. Display de 7 Segmentos

### 4.1. Estructura

Un display de 7 segmentos tiene 7 LEDs (a, b, c, d, e, f, g) dispuestos en forma de "8":

```
     a
   ┌───┐
 f │   │ b
   ├─g─┤
 e │   │ c
   └───┘
     d
```

**Tipos:**
- **Ánodo común:** Todos los ánodos juntos a VCC (enciendes con 0)
- **Cátodo común:** Todos los cátodos a GND (enciendes con 1)

### 4.2. Decodificador BCD a 7 Segmentos

**Función:** Convierte un número en binario (4 bits) a las señales para mostrar el dígito decimal.

**Tabla parcial (para cátodo común):**

| Decimal | BCD (DCBA) | a | b | c | d | e | f | g | Display |
|---------|------------|---|---|---|---|---|---|---|---------|
| 0       | 0000       | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0       |
| 1       | 0001       | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1       |
| 2       | 0010       | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 2       |
| 3       | 0011       | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 3       |
| 4       | 0100       | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 4       |
| 5       | 0101       | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 5       |
| 6       | 0110       | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 6       |
| 7       | 0111       | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 7       |
| 8       | 1000       | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 8       |
| 9       | 1001       | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 9       |

**CI comercial:** 
- 7447 (para ánodo común)
- 7448 (para cátodo común)

---

## 5. Multiplexores (MUX)

### 5.1. Definición

Un **multiplexor** selecciona una de entre $2^n$ entradas de datos y la dirige a la salida, controlado por $n$ señales de selección.

**Analogía:** Es como un interruptor rotativo que elige qué canal de entrada pasa a la salida.

### 5.2. Multiplexor de 2 a 1

**Entradas:**
- $D_0$, $D_1$ (datos)
- $S$ (selector)

**Tabla de verdad:**

| $S$ | $Y$ |
|-----|-----|
| 0   | $D_0$ |
| 1   | $D_1$ |

**Expresión:**
$$
Y = \overline{S} \cdot D_0 + S \cdot D_1
$$

### 5.3. Multiplexor de 4 a 1

**Entradas:**
- $D_0$, $D_1$, $D_2$, $D_3$ (datos)
- $S_1$, $S_0$ (selectores)

**Expresión:**
$$
Y = \overline{S_1}\overline{S_0}D_0 + \overline{S_1}S_0 D_1 + S_1\overline{S_0}D_2 + S_1 S_0 D_3
$$

**CI comercial:** 74LS151 (MUX 8 a 1), 74LS153 (doble MUX 4 a 1)

### 5.4. Aplicaciones

- **Transmisión de datos:** Enviar 8 señales por 1 cable (multiplexación en tiempo)
- **Implementación de funciones:** Un MUX de 8:1 puede implementar cualquier función de 3 variables

---

## 6. Demultiplexores (DEMUX)

### 6.1. Definición

El **demultiplexor** hace la operación inversa: toma 1 entrada de datos y la dirige a una de las $2^n$ salidas según las señales de selección.

**Nota:** Un decodificador con entrada de habilitación funciona como DEMUX.

---

## 📝 Actividades

### Actividad 1: Codificador
Diseña un codificador de 4 a 2 con puertas OR.

### Actividad 2: Decodificador
Implementa un decodificador de 2 a 4 con puertas AND e inversores.

### Actividad 3: Display 7 Segmentos
Diseña la función booleana para el segmento "g" del display (se enciende para: 2, 3, 4, 5, 6, 8, 9).

### Actividad 4: Multiplexor
Usando un MUX de 4:1, implementa la función: $F(A,B) = \Sigma(1, 2, 3)$

### Actividad 5: Aplicación Práctica
Diseña un sistema que muestre en un display el número del interruptor que está pulsado (4 interruptores, numerados 0-3).

---

## ❓ Preguntas de Repaso

1. ¿Qué diferencia hay entre un circuito combinacional y uno secuencial?
2. ¿Cuántas salidas tiene un codificador de 16 a 4?
3. ¿Qué CI usarías para controlar un display de 7 segmentos de cátodo común?
4. ¿Cuántas señales de selección necesita un MUX de 8 a 1?
5. ¿Para qué sirve un demultiplexor?

---

## 🔗 Recursos Adicionales

- **Simulador:** Monta un contador de 0-9 con display en Tinkercad
- **Datasheet:** [74LS47 (BCD to 7-segment)](https://www.ti.com/lit/ds/symlink/sn74ls47.pdf)
