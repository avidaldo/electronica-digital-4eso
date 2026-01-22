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

**Contraparte:** Los **circuitos secuenciales** (tema de 1º Bachillerato) sí tienen memoria (flip-flops, contadores).

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

**Ejemplo:** Si se pulsan $I_2$ e $I_1$ simultáneamente, el codificador devuelve 2 (ignora $I_1$).

**CI comercial:** 74LS148 (codificador de prioridad de 8 a 3)

---

## 3. Decodificadores

### 3.1. Definición

Un **decodificador** hace la operación inversa: convierte $n$ entradas binarias en $2^n$ salidas (solo una activa).

**Ejemplo:** Decodificador de 2 a 4
- 2 entradas (código binario)
- 4 salidas (solo una a 1)

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

### 3.3. Decodificador de 3 a 8

**CI comercial:** 74LS138

**Aplicación:** Selección de memoria (direccionamiento de chips)

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

**Entrada:** BCD (Binary Coded Decimal) de 0 a 9
**Salida:** 7 señales (a, b, c, d, e, f, g)

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

### 4.3. Diseño de la Función para el Segmento "a"

**Tabla de verdad para "a":**

| D | C | B | A | a |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 0 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 1 |
| ... | ... | ... | ... | ... |

**Expresión (simplificada con Karnaugh):**
$$
a = \overline{D}\overline{C}\overline{B}\overline{A} + \overline{D}C + \text{(otros términos)}
$$

Este proceso se repite para cada segmento (b, c, d, e, f, g).

---

## 5. Multiplexores (MUX)

### 5.1. Definición

Un **multiplexor** selecciona una de entre $2^n$ entradas de datos y la dirige a la salida, controlado por $n$ señales de selección.

**Analogía:** Es como un interruptor rotativo que elige qué canal de entrada pasa a la salida.

### 5.2. Multiplexor de 2 a 1

**Entradas:**
- $D_0$, $D_1$ (datos)
- $S$ (selector)

**Salida:**
- $F$

**Tabla de verdad:**

| $S$ | $F$ |
|-----|-----|
| 0   | $D_0$ |
| 1   | $D_1$ |

**Expresión:**
$$
F = \overline{S} \cdot D_0 + S \cdot D_1
$$

**Circuito:**
```
          ┌───┐
 D₀ ──────┤   │
          │AND├──┐
 S̄  ──────┤   │  │  ┌───┐
          └───┘  ├──┤OR ├── F
          ┌───┐  │  └───┘
 D₁ ──────┤   │  │
          │AND├──┘
 S  ──────┤   │
          └───┘
```

### 5.3. Multiplexor de 4 a 1

**Entradas:**
- $D_0$, $D_1$, $D_2$, $D_3$ (datos)
- $S_1$, $S_0$ (selectores)

**Tabla de selección:**

| $S_1$ | $S_0$ | $F$ |
|-------|-------|-----|
| 0     | 0     | $D_0$ |
| 0     | 1     | $D_1$ |
| 1     | 0     | $D_2$ |
| 1     | 1     | $D_3$ |

**CI comercial:** 74LS153 (doble MUX 4 a 1)

**Aplicaciones:**
- Selección de fuentes de datos en microprocesadores
- Conversión de señales paralelas a serie
- Implementación de funciones lógicas complejas

### 5.4. Implementar Funciones con MUX

**Ventaja:** Cualquier función de $n$ variables puede implementarse con un MUX de $2^n$ entradas.

**Ejemplo:** Implementar $F(A,B) = A + \overline{B}$ con un MUX 4:1

**Paso 1:** Tabla de verdad:

| A | B | F |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

**Paso 2:** Conectar:
- $S_1 = A$, $S_0 = B$
- $D_0 = 1$ (fila 00)
- $D_1 = 0$ (fila 01)
- $D_2 = 1$ (fila 10)
- $D_3 = 1$ (fila 11)

---

## 6. Demultiplexores (DEMUX)

### 6.1. Definición

Un **demultiplexor** hace la operación inversa: dirige una entrada de datos a una de entre $2^n$ salidas, seleccionada por $n$ señales de control.

**Analogía:** Es como un interruptor que dirige el agua de una tubería a uno de varios destinos.

### 6.2. Demultiplexor de 1 a 4

**Entradas:**
- $D$ (dato)
- $S_1$, $S_0$ (selectores)

**Salidas:**
- $Y_0$, $Y_1$, $Y_2$, $Y_3$

**Tabla:**

| $S_1$ | $S_0$ | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
|-------|-------|-------|-------|-------|-------|
| 0     | 0     | $D$   | 0     | 0     | 0     |
| 0     | 1     | 0     | $D$   | 0     | 0     |
| 1     | 0     | 0     | 0     | $D$   | 0     |
| 1     | 1     | 0     | 0     | 0     | $D$   |

**Expresiones:**
$$
Y_0 = \overline{S_1} \cdot \overline{S_0} \cdot D
$$
$$
Y_1 = \overline{S_1} \cdot S_0 \cdot D
$$
$$
Y_2 = S_1 \cdot \overline{S_0} \cdot D
$$
$$
Y_3 = S_1 \cdot S_0 \cdot D
$$

**CI comercial:** 74LS138 (se puede usar como DEMUX 1 a 8)

**Aplicación:** Distribución de señales (ej. enviar datos a uno de varios dispositivos)

---

## 7. Comparadores

### 7.1. Comparador de 1 Bit

**Función:** Compara dos bits (A y B) y genera 3 salidas:
- $A > B$
- $A = B$
- $A < B$

**Tabla de verdad:**

| A | B | A>B | A=B | A<B |
|---|---|-----|-----|-----|
| 0 | 0 | 0   | 1   | 0   |
| 0 | 1 | 0   | 0   | 1   |
| 1 | 0 | 1   | 0   | 0   |
| 1 | 1 | 0   | 1   | 0   |

**Expresiones:**
$$
A > B = A \cdot \overline{B}
$$
$$
A = B = \overline{A \oplus B}
$$
$$
A < B = \overline{A} \cdot B
$$

### 7.2. Comparador de Magnitud de 4 Bits

**CI comercial:** 7485

**Función:** Compara dos números de 4 bits cada uno.

**Aplicación:** Control de procesos (ej. alarma si temperatura > umbral)

---

## 8. Sumadores

### 8.1. Semisumador (Half Adder)

**Función:** Suma 2 bits (A + B) sin acarreo de entrada.

**Tabla de verdad:**

| A | B | Suma (S) | Acarreo (C) |
|---|---|----------|-------------|
| 0 | 0 | 0        | 0           |
| 0 | 1 | 1        | 0           |
| 1 | 0 | 1        | 0           |
| 1 | 1 | 0        | 1           |

**Expresiones:**
$$
S = A \oplus B
$$
$$
C = A \cdot B
$$

**Circuito:** 1 XOR + 1 AND

---

### 8.2. Sumador Completo (Full Adder)

**Función:** Suma 3 bits (A + B + $C_{in}$), necesario para sumar números de varios bits.

**Tabla de verdad:**

| A | B | $C_{in}$ | Suma (S) | $C_{out}$ |
|---|---|----------|----------|-----------|
| 0 | 0 | 0        | 0        | 0         |
| 0 | 0 | 1        | 1        | 0         |
| 0 | 1 | 0        | 1        | 0         |
| 0 | 1 | 1        | 0        | 1         |
| 1 | 0 | 0        | 1        | 0         |
| 1 | 0 | 1        | 0        | 1         |
| 1 | 1 | 0        | 0        | 1         |
| 1 | 1 | 1        | 1        | 1         |

**Expresiones:**
$$
S = A \oplus B \oplus C_{in}
$$
$$
C_{out} = AB + AC_{in} + BC_{in}
$$

**CI comercial:** 7483 (sumador de 4 bits)

---

## 9. Resumen de CIs Combinacionales

| Función | CI TTL | Descripción |
|---------|--------|-------------|
| Codificador 8→3 | 74LS148 | Con prioridad |
| Decodificador 2→4 | 74LS139 | Doble |
| Decodificador 3→8 | 74LS138 | Enable activo |
| BCD a 7 seg | 7447/7448 | Ánodo/Cátodo común |
| Multiplexor 4→1 | 74LS153 | Doble |
| Multiplexor 8→1 | 74LS151 | Simple |
| Comparador 4 bits | 7485 | Con cascada |
| Sumador 4 bits | 7483 | Acarreo rápido |

---

## 📝 Actividades

### Actividad 1: Análisis de Codificador
Diseña un codificador de 8 a 3 que convierta las teclas de un teclado numérico (0-7) a binario.

### Actividad 2: Display de 7 Segmentos
Completa la tabla de verdad para el segmento "g" del display BCD a 7 segmentos.

### Actividad 3: Diseño con Multiplexor
Implementa la función $F(A,B,C) = A\overline{B} + BC$ usando un MUX 8:1.

### Actividad 4: Sumador de 2 Bits
Diseña un circuito que sume dos números de 2 bits cada uno (A1A0 + B1B0), usando semisumadores y sumadores completos.

### Actividad 5: Aplicación Práctica
Diseña un sistema que:
- Tenga 4 sensores de temperatura (entradas binarias)
- Use un codificador para identificar qué sensor está activo
- Muestre el número del sensor en un display de 7 segmentos

---

## ❓ Preguntas de Repaso

1. ¿Cuál es la diferencia entre un codificador y un decodificador?
2. ¿Cuántos segmentos tiene un display y cuál NO se usa para el dígito "1"?
3. ¿Qué hace un multiplexor?
4. ¿Cuántas entradas de selección necesita un MUX de 16 a 1?
5. ¿Qué puerta lógica se usa para la suma en un semisumador?

---

## 🔗 Recursos Adicionales

- **Simulador:** [Falstad - Digital Logic](https://www.falstad.com/circuit/)
- **Datasheets:** [74LS138](https://www.ti.com/lit/ds/symlink/sn74ls138.pdf), [7447](https://www.ti.com/lit/ds/symlink/sn7447a.pdf)
- **Video:** [Multiplexores y Demultiplexores - Electrónica Digital](https://www.youtube.com/watch?v=example)

---

**Tema anterior:** [Análisis y Diseño de Circuitos](05_diseno_circuitos.md)  
**Siguiente tema:** [Prácticas de Taller](07_practicas_taller.md)
