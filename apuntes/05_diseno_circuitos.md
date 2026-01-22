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

Esta expresión está **sin simplificar**. Funciona, pero usa demasiadas puertas.

---

## 4. Simplificación Algebraica

### Método: Aplicar las leyes de Boole

**Ejemplo:** Simplificar $F = \overline{A}BC + A\overline{B}C + AB\overline{C} + ABC$

**Paso 1:** Agrupar términos con factores comunes:
$$
F = \overline{A}BC + ABC + A\overline{B}C + AB\overline{C}
$$

**Paso 2:** Factorizar BC:
$$
F = BC(\overline{A} + A) + A\overline{B}C + AB\overline{C}
$$

**Paso 3:** Simplificar $\overline{A} + A = 1$:
$$
F = BC + A\overline{B}C + AB\overline{C}
$$

**Paso 4:** Factorizar $A$ en los dos últimos términos:
$$
F = BC + A(\overline{B}C + B\overline{C})
$$

**Paso 5:** Reconocer XOR: $\overline{B}C + B\overline{C} = B \oplus C$:
$$
F = BC + A(B \oplus C)
$$

**Resultado simplificado:**
$$
F = AB + AC + BC
$$

(También válida: $F = BC + A(B \oplus C)$)

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

Cada celda representa una combinación de A y B.

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

**IMPORTANTE:** El orden de las columnas es **00, 01, 11, 10** (código Gray), NO 00, 01, 10, 11. Esto asegura que solo cambia 1 bit entre celdas adyacentes.

---

### 5.3. Ejemplo: Sistema de Voto

**Tabla de verdad:**

| A | B | C | F |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 |

**Paso 1:** Rellenar el mapa con los valores de F:

```
         BC
       00  01  11  10
     ┌────────────────┐
   0 │ 0 │ 0 │ 1 │ 0 │
A    ├────────────────┤
   1 │ 0 │ 1 │ 1 │ 1 │
     └────────────────┘
```

**Paso 2:** Agrupar los 1's en rectángulos de tamaño 2ⁿ (1, 2, 4, 8...):

```
         BC
       00  01  11  10
     ┌────┬────┬────┬────┐
   0 │ 0 │ 0 │[1]│ 0 │  Grupo 1 (vertical)
A    ├────┼────┼────┼────┤
   1 │ 0 │[1]│[1]│[1]│  Grupo 2 (horizontal)
     └────┴────┴────┴────┘
```

**Grupo 1 (vertical):** Celdas 3 y 7 → A varía, BC=11 → $BC$

**Grupo 2 (horizontal):** Celdas 5, 7, 6 → B y C varían... 

Mejor: dividir en dos grupos de 2:
- Celdas 5 y 7: C varía, A=1 y B=1 → $AB$
- Celdas 6 y 7: B varía, A=1 y C=1 → $AC$

**Resultado:**
$$
F = AB + AC + BC
$$

(¡Mismo resultado que con simplificación algebraica!)

---

### 5.4. Reglas para Karnaugh

1. **Agrupa los 1's**, no los 0's
2. Los grupos deben ser **rectangulares** (no en "L" o diagonales)
3. Tamaño del grupo: **potencia de 2** (1, 2, 4, 8)
4. **Maximiza el tamaño** de los grupos (menos términos)
5. Un 1 puede pertenecer a **varios grupos**
6. Los bordes del mapa son **adyacentes** (se "enrolla")

---

### 5.5. Mapa para 4 Variables

```
          CD
        00  01  11  10
      ┌────────────────┐
   00 │ 0 │ 1 │ 3 │ 2 │
AB    ├────────────────┤
   01 │ 4 │ 5 │ 7 │ 6 │
      ├────────────────┤
   11 │12 │13 │15 │14 │
      ├────────────────┤
   10 │ 8 │ 9 │11 │10 │
      └────────────────┘
```

**Ejemplo:** $F(A,B,C,D) = \sum(0,1,2,5,6,7,8,9,10,14)$

(Los números indican las filas de la tabla donde F=1)

---

## 6. Implementación del Circuito

Una vez simplificada la expresión, diseñamos el circuito con puertas.

### Ejemplo: $F = AB + AC + BC$

**Circuito:**

```
      ┌───┐
  A ──┤   ├──┐
  B ──┤AND│  │
      └───┘  │
             │  ┌───┐
      ┌───┐  ├──┤   │
  A ──┤   ├──┤  │OR ├── F
  C ──┤AND│  │  │   │
      └───┘  │  └───┘
             │
      ┌───┐  │
  B ──┤   ├──┘
  C ──┤AND│
      └───┘
```

**Componentes necesarios:**
- 3 puertas AND (puedes usar 3/4 de un CI 74LS08)
- 1 puerta OR de 3 entradas (o 2 OR de 2 entradas)

---

## 7. Optimización del Diseño

### 7.1. Minimizar el Número de Chips

**Problema:** Cada CI cuesta dinero y ocupa espacio.

**Estrategia:**
1. Simplifica la expresión al máximo
2. Usa puertas universales (NAND/NOR) si reduces chips
3. Aprovecha todas las puertas de un CI (74LS08 tiene 4 AND)

### 7.2. Ejemplo: AND-OR vs NAND-NAND

La expresión $F = AB + CD$ puede implementarse:

**Opción 1:** 2 AND + 1 OR → 2 chips  
**Opción 2:** Solo NANDs → 1 chip (aplicando De Morgan)

---

## 8. Verificación del Diseño

### Paso 1: Simulación
Usa software (Tinkercad, Falstad) para probar todas las combinaciones.

### Paso 2: Montaje en Protoboard
Verifica físicamente con:
- Interruptores para las entradas
- LEDs para las salidas
- Multímetro para comprobar niveles de tensión

### Paso 3: Comparar con la Tabla
Comprueba que para cada combinación de entradas, la salida coincide con la tabla de verdad.

---

## 9. Caso Práctico Completo

### Problema: Alarma de Coche

**Especificaciones:**
- La alarma (F=1) suena si:
  - Las puertas están cerradas (P=1) **Y** detecta movimiento (M=1)
  - **O** si el cristal está roto (C=1)

**Paso 1: Tabla de verdad**

| P | M | C | F | Razón |
|---|---|---|---|-------|
| 0 | 0 | 0 | 0 | Puerta abierta, sin cristal roto |
| 0 | 0 | 1 | 1 | Cristal roto → alarma |
| 0 | 1 | 0 | 0 | Puerta abierta (movimiento normal) |
| 0 | 1 | 1 | 1 | Cristal roto → alarma |
| 1 | 0 | 0 | 0 | Puerta cerrada, sin movimiento |
| 1 | 0 | 1 | 1 | Cristal roto → alarma |
| 1 | 1 | 0 | 1 | Puerta cerrada + movimiento → alarma |
| 1 | 1 | 1 | 1 | Puerta cerrada + movimiento + cristal |

**Paso 2: Expresión (SOP)**
$$
F = \overline{P}\overline{M}C + \overline{P}MC + P\overline{M}C + PMC + PM\overline{C}
$$

**Paso 3: Karnaugh (3 variables)**

```
         MC
       00  01  11  10
     ┌────────────────┐
   0 │ 0 │ 1 │ 1 │ 0 │
P    ├────────────────┤
   1 │ 0 │ 1 │ 1 │ 1 │
     └────────────────┘
```

**Agrupaciones:**
- Columna C=1: $C$ (grupo de 4)
- Fila inferior: $PM$ (grupo de 2)

**Expresión simplificada:**
$$
F = C + PM
$$

**Paso 4: Circuito**

```
      ┌───┐
  P ──┤   ├──┐
  M ──┤AND│  │  ┌───┐
      └───┘  ├──┤OR ├── F
             │  └───┘
  C ─────────┘
```

**Componentes:** 1 AND + 1 OR → ¡Muy simple!

---

## 📝 Actividades

### Actividad 1: Tabla → Expresión
Dada esta tabla, obtén la expresión SOP:

| A | B | F |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Actividad 2: Simplificación Algebraica
Simplifica:
$$
F = ABC + AB\overline{C} + \overline{A}BC
$$

### Actividad 3: Karnaugh (3 variables)
Simplifica usando mapa de Karnaugh:
$$
F(A,B,C) = \sum(1,3,5,7)
$$

### Actividad 4: Diseño Completo
**Problema:** Un ascensor tiene 3 botones (A, B, C) correspondientes a 3 pisos. El ascensor se mueve (F=1) si se pulsa exactamente 1 botón.

1. Construye la tabla de verdad
2. Obtén la expresión
3. Simplifica con Karnaugh
4. Dibuja el circuito

### Actividad 5: Optimización
Implementa $F = AB + \overline{A}C$ usando:
1. Puertas AND y OR
2. Solo puertas NAND

---

## ❓ Preguntas de Repaso

1. ¿Qué es un minitérmino?
2. ¿Por qué en Karnaugh el orden de columnas es 00-01-11-10?
3. ¿Cuál es el tamaño máximo de grupo en un K-map de 3 variables?
4. Si simplificas una función y obtienes $F=A$, ¿cuántas puertas necesitas?
5. ¿Qué ventaja tiene NAND sobre AND+OR en diseño real?

---

## 🔗 Recursos Adicionales

- **Simulador de Karnaugh:** [K-map Solver](https://www.boolean-algebra.com/kmap/)
- **Video tutorial:** [Mapas de Karnaugh paso a paso](https://www.youtube.com/watch?v=PA0kBrpHLM4)
- **Práctica online:** [Interactive K-map](https://www.cs.umd.edu/~blj/kmaps/)

---

**Tema anterior:** [Puertas Lógicas](04_puertas_logicas.md)  
**Siguiente tema:** [Circuitos Combinacionales](06_circuitos_combinacionales.md)
