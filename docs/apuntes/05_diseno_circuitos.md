---
sidebar_position: 5
title: Tema 5 - Análisis y Diseño de Circuitos Lógicos
description: Tablas de verdad, expresiones booleanas, simplificación y Mapas de Karnaugh
---

# Tema 5: Análisis y Diseño de Circuitos Lógicos

## 🎯 Objetivos de Aprendizaje
Al finalizar este tema, serás capaz de:
- Obtener la tabla de verdad de un circuito o problema lógico
- Escribir la expresión booleana a partir de una tabla
- Simplificar funciones usando álgebra de Boole y Mapas de Karnaugh
- Implementar un circuito lógico con puertas comerciales

---

## 1. Proceso Completo de Diseño

El diseño de un circuito digital sigue estos pasos:

```
1. PROBLEMA VERBAL
        ↓
2. TABLA DE VERDAD
        ↓
3. EXPRESIÓN BOOLEANA
        ↓
4. SIMPLIFICACIÓN
        ↓
5. IMPLEMENTACIÓN CON PUERTAS
        ↓
6. MONTAJE Y VERIFICACIÓN
```

---

## 2. Del Problema a la Tabla de Verdad

### Ejemplo 1: Sistema de Voto por Mayoría

**Problema:** Tres personas (A, B, C) votan. La propuesta se aprueba si **al menos 2 votan SÍ** (=1).

**Paso 1:** Identificar entradas y salida
- Entradas: A, B, C (0=NO, 1=SÍ)
- Salida: F (0=rechazada, 1=aprobada)

**Paso 2:** Construir la tabla analizando todos los casos:

| $A$ | $B$ | $C$ | Votos SÍ | $F$ | Interpretación |
|-----|-----|-----|----------|-----|----------------|
| 0   | 0   | 0   | 0        | 0   | Rechazada |
| 0   | 0   | 1   | 1        | 0   | Rechazada |
| 0   | 1   | 0   | 1        | 0   | Rechazada |
| 0   | 1   | 1   | 2        | 1   | **Aprobada** |
| 1   | 0   | 0   | 1        | 0   | Rechazada |
| 1   | 0   | 1   | 2        | 1   | **Aprobada** |
| 1   | 1   | 0   | 2        | 1   | **Aprobada** |
| 1   | 1   | 1   | 3        | 1   | **Aprobada** |

---

## 3. De la Tabla a la Expresión Booleana

### 3.1. Suma de Minitérminos (SOP)

**Regla:** Para cada fila donde $F=1$, escribe el producto de las variables:
- Si la variable es 1 → aparece normal
- Si la variable es 0 → aparece negada

**Aplicando al ejemplo:**

Filas con $F=1$:
- Fila 3: $A=0, B=1, C=1$ → $\overline{A} \cdot B \cdot C$
- Fila 5: $A=1, B=0, C=1$ → $A \cdot \overline{B} \cdot C$
- Fila 6: $A=1, B=1, C=0$ → $A \cdot B \cdot \overline{C}$
- Fila 7: $A=1, B=1, C=1$ → $A \cdot B \cdot C$

**Expresión completa:**
$$
F = \overline{A}BC + A\overline{B}C + AB\overline{C} + ABC
$$

---

## 4. Simplificación Algebraica

### Método: Aplicar las leyes de Boole

**Resultado simplificado:**
$$
F = AB + AC + BC
$$

Esta expresión significa: "F vale 1 si al menos dos de las tres variables valen 1"

---

## 5. Mapas de Karnaugh (K-map)

Es un método **visual y sistemático** para simplificar funciones. Especialmente útil para 3 o 4 variables.

### 5.1. Mapa para 2 Variables

```
      B
    0   1
  ┌───┬───┐
A │   │   │
0 │ 0 │ 1 │
  ├───┼───┤
1 │ 2 │ 3 │
  └───┴───┘
```

---

### 5.2. Mapa para 3 Variables

**Formato estándar:**

```
         BC
       00  01  11  10
     ┌────────────────┐
   0 │ 0 │ 1 │ 3 │ 2 │
A    ├────────────────┤
   1 │ 4 │ 5 │ 7 │ 6 │
     └────────────────┘
```

:::warning IMPORTANTE
El orden de las columnas es **00, 01, 11, 10** (código Gray), NO 00, 01, 10, 11. Esto asegura que solo cambia 1 bit entre celdas adyacentes.
:::

---

### 5.3. Reglas de Agrupación

1. **Agrupar solo 1's** (o solo 0's si usamos POS)
2. **Tamaño de grupos:** Potencias de 2 (1, 2, 4, 8...)
3. **Forma:** Rectangular (incluye cuadrados)
4. **Los bordes conectan:** La primera fila es adyacente a la última
5. **Maximizar tamaño:** Grupos más grandes = expresión más simple
6. **Cubrir todos los 1's:** Pueden solaparse grupos

---

### 5.4. Ejemplo: Sistema de Voto

**Paso 1:** Rellenar el mapa con los valores de F:

```
         BC
       00  01  11  10
     ┌────┬────┬────┬────┐
   0 │ 0 │ 0 │ 1 │ 0 │
A    ├────┼────┼────┼────┤
   1 │ 0 │ 1 │ 1 │ 1 │
     └────┴────┴────┴────┘
```

**Paso 2:** Agrupar los 1's

- Grupo 1 (vertical): BC=11 → $BC$
- Grupo 2: A=1, C=1 → $AC$
- Grupo 3: A=1, B=1 → $AB$

**Resultado:**
$$
F = AB + AC + BC
$$

---

## 6. Mapa de Karnaugh para 4 Variables

```
          CD
        00  01  11  10
      ┌────────────────┐
   00 │ 0 │ 1 │ 3 │ 2 │
      ├────────────────┤
   01 │ 4 │ 5 │ 7 │ 6 │
AB    ├────────────────┤
   11 │12 │13 │15 │14 │
      ├────────────────┤
   10 │ 8 │ 9 │11 │10 │
      └────────────────┘
```

---

## 7. Implementación con Puertas

Una vez simplificada, la expresión $F = AB + AC + BC$ se implementa con:
- 3 puertas AND de 2 entradas
- 1 puerta OR de 3 entradas

**CIs necesarios:**
- 1x 74LS08 (4 puertas AND) - usamos 3
- 1x 74LS32 (4 puertas OR) - usamos 1 (conectando 2 en cascada)

---

## 📝 Actividades

### Actividad 1: Tabla de Verdad
Crea la tabla de verdad para: "Un sistema de riego se activa (F=1) si el sensor indica seco (S=0) Y es de noche (N=1)"

### Actividad 2: Expresión a partir de Tabla
Dada esta tabla, obtén la expresión SOP y simplifícala:

| A | B | F |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### Actividad 3: Karnaugh 3 variables
Simplifica con Karnaugh: $F(A,B,C) = \Sigma(0, 2, 4, 6)$

### Actividad 4: Karnaugh 4 variables
Simplifica: $F(A,B,C,D) = \Sigma(0, 1, 2, 3, 4, 5, 14, 15)$

### Actividad 5: Diseño completo
Diseña un circuito para: "La luz del pasillo (L) se enciende si el sensor de movimiento detecta presencia (M=1) Y es de noche (N=1), O si se pulsa el interruptor manual (I=1)"

---

## ❓ Preguntas de Repaso

1. ¿Qué significa SOP?
2. ¿Por qué el orden de las columnas en Karnaugh es 00, 01, 11, 10?
3. ¿Cuántas celdas tiene un mapa de Karnaugh de 4 variables?
4. ¿Por qué preferimos expresiones simplificadas?
5. ¿Cuántas puertas AND necesitas para implementar $F = ABC + \overline{A}BC$?

---

## 🔗 Recursos Adicionales

- **Calculadora Karnaugh online:** [Karnaugh Map Solver](https://www.charlie-coleman.com/experiments/kmap/)
- **Video tutorial:** [Karnaugh Maps - Ben Eater](https://www.youtube.com/watch?v=RO5alU6PpSU)
