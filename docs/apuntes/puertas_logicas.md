---
sidebar_position: 4
title: Tema 4 - Puertas Lógicas
description: Puertas básicas AND, OR, NOT, puertas universales NAND, NOR y puerta XOR
---

# Tema 4: Puertas Lógicas

## 🎯 Objetivos de Aprendizaje
Al finalizar este tema, serás capaz de:
- Identificar los símbolos normalizados de las puertas lógicas
- Construir tablas de verdad para cada tipo de puerta
- Explicar el funcionamiento físico de una puerta lógica
- Diseñar circuitos simples combinando puertas

---

## 1. ¿Qué es una Puerta Lógica?

Una **puerta lógica** es un circuito electrónico que implementa una operación booleana. Es el componente básico de todos los circuitos digitales.

**Características:**
- **Entradas:** Variables booleanas (0 ó 1, representadas por niveles de tensión)
- **Salida:** Resultado de la operación lógica
- **Velocidad:** Retraso del orden de nanosegundos (10⁻⁹ s)

:::note Ejemplo físico
Un circuito integrado **74LS08** contiene 4 puertas AND en un chip de 14 pines.
:::

---

## 2. Puertas Lógicas Básicas

### 2.1. Puerta NOT (Inversor)

**Función:** Invierte la entrada ($F = \overline{A}$)

**Tabla de verdad:**

| $A$ | $F = \overline{A}$ |
|-----|---------------------|
| 0   | 1                   |
| 1   | 0                   |

**Características:**
- Es la única puerta con **1 entrada**

---

### 2.2. Puerta AND

**Función:** Producto lógico ($F = A \cdot B$)

**Tabla de verdad:**

| $A$ | $B$ | $F = A \cdot B$ |
|-----|-----|-----------------|
| 0   | 0   | 0               |
| 0   | 1   | 0               |
| 1   | 0   | 0               |
| 1   | 1   | 1               |

:::tip Regla mnemotécnica
"La salida es 1 **solo si TODAS** las entradas son 1"
:::

**Aplicación:** Control de seguridad (necesitas clave **Y** huella dactilar)

---

### 2.3. Puerta OR

**Función:** Suma lógica ($F = A + B$)

**Tabla de verdad:**

| $A$ | $B$ | $F = A + B$ |
|-----|-----|-------------|
| 0   | 0   | 0           |
| 0   | 1   | 1           |
| 1   | 0   | 1           |
| 1   | 1   | 1           |

:::tip Regla mnemotécnica
"La salida es 1 si **AL MENOS UNA** entrada es 1"
:::

**Aplicación:** Sensor de intrusión (alarma si detecta movimiento **O** rotura de cristal)

---

## 3. Puertas Lógicas Universales

Se llaman "universales" porque puedes construir **cualquier** otra puerta solo con ellas.

### 3.1. Puerta NAND (NOT-AND)

**Función:** AND negada ($F = \overline{A \cdot B}$)

**Tabla de verdad:**

| $A$ | $B$ | $F = \overline{A \cdot B}$ |
|-----|-----|----------------------------|
| 0   | 0   | 1                          |
| 0   | 1   | 1                          |
| 1   | 0   | 1                          |
| 1   | 1   | 0                          |

:::tip Regla mnemotécnica
"La salida es 0 **solo si TODAS** las entradas son 1"
:::

:::info Dato curioso
Los primeros ordenadores se construían solo con puertas NAND (más baratas de fabricar).
:::

---

### 3.2. Puerta NOR (NOT-OR)

**Función:** OR negada ($F = \overline{A + B}$)

**Tabla de verdad:**

| $A$ | $B$ | $F = \overline{A + B}$ |
|-----|-----|------------------------|
| 0   | 0   | 1                      |
| 0   | 1   | 0                      |
| 1   | 0   | 0                      |
| 1   | 1   | 0                      |

:::tip Regla mnemotécnica
"La salida es 1 **solo si TODAS** las entradas son 0"
:::

---

## 4. Puerta XOR (O-Exclusiva)

### 4.1. Puerta XOR

**Función:** OR exclusiva ($F = A \oplus B$)

**Tabla de verdad:**

| $A$ | $B$ | $F = A \oplus B$ |
|-----|-----|------------------|
| 0   | 0   | 0                |
| 0   | 1   | 1                |
| 1   | 0   | 1                |
| 1   | 1   | 0                |

:::tip Regla mnemotécnica
"La salida es 1 si las entradas son **diferentes**"
:::

**Expresión equivalente:**
$$
A \oplus B = A \cdot \overline{B} + \overline{A} \cdot B
$$

**Aplicaciones:**
- **Sumadores binarios** (el bit resultante de sumar 1+1 es 0 con acarreo)
- **Comparadores** (detectar si dos señales son iguales o diferentes)
- **Criptografía** (operación de cifrado básica)

---

### 4.2. Puerta XNOR (Equivalencia)

**Función:** XOR negada ($F = \overline{A \oplus B}$)

**Tabla de verdad:**

| $A$ | $B$ | $F = \overline{A \oplus B}$ |
|-----|-----|------------------------------|
| 0   | 0   | 1                            |
| 0   | 1   | 0                            |
| 1   | 0   | 0                            |
| 1   | 1   | 1                            |

:::tip Regla mnemotécnica
"La salida es 1 si las entradas son **iguales**"
:::

---

## 5. Resumen de Todas las Puertas

| Puerta | Función | Salida = 1 cuando... |
|--------|---------|----------------------|
| NOT    | $\overline{A}$ | A = 0 |
| AND    | $A \cdot B$ | Todas las entradas = 1 |
| OR     | $A + B$ | Al menos una entrada = 1 |
| NAND   | $\overline{A \cdot B}$ | Al menos una entrada = 0 |
| NOR    | $\overline{A + B}$ | Todas las entradas = 0 |
| XOR    | $A \oplus B$ | Entradas diferentes |
| XNOR   | $\overline{A \oplus B}$ | Entradas iguales |

---

## 6. Circuitos Integrados Comerciales

### 6.1. Familias Lógicas

**Serie 74xx (TTL - Transistor-Transistor Logic):**
- Alimentación: 5V
- Ejemplo: 74LS00 (4 puertas NAND), 74LS08 (4 puertas AND)

**Serie 40xx (CMOS - Complementary Metal-Oxide Semiconductor):**
- Alimentación: 3-15V (más flexible)
- Menor consumo energético
- Ejemplo: 4011 (4 puertas NAND)

### 6.2. Encapsulado DIP

Los CIs tienen forma rectangular con dos filas de pines:

```
    74LS08 (4 puertas AND)
    ┌──┐─┐
1A  │1 └┐│  14 VCC
1B  │2  ││  13 4B
1Y  │3  ││  12 4A
2A  │4  ││  11 4Y
2B  │5  ││  10 3B
2Y  │6  ││  9  3A
GND │7  ││  8  3Y
    └────┘
```

:::warning Importante
Pin 14 = VCC (+5V), Pin 7 = GND (masa)
:::

---

## 7. Construcción de Puertas con NAND

**Teorema:** NAND es universal → puedes construir cualquier puerta con NANDs.

### NOT con NAND:
```
  A ─┬─┤NAND├─── F = Ā
      │        
      └────────┘
```

### AND con NAND:
```
  A ──┐         ┌──┐
      ├─┤NAND├──┤NAND├─ F = A·B
  B ──┘         └──┘
```

---

## 📝 Actividades

### Actividad 1: Identificación de Puertas
Dada la siguiente tabla, identifica qué puerta corresponde:

| A | B | F |
|---|---|---|
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

### Actividad 2: Construcción de Tablas
Completa las tablas de verdad para:
1. $F = \overline{A} \cdot B$
2. $F = A + \overline{B}$
3. $F = \overline{A + B}$

### Actividad 3: Análisis de Circuito
Dibuja el circuito y obtén la tabla de verdad de:
$$
F = (A + B) \cdot \overline{C}
$$

### Actividad 4: Diseño con NAND
Diseña una puerta OR usando solo puertas NAND.

### Actividad 5: Aplicación Práctica
Diseña un circuito que active una alarma (F=1) si:
- Se detecta humo (S=1) **O**
- La temperatura es alta (T=1) **Y** NO está el sistema desactivado (D=0)

Expresión: $F = S + (T \cdot \overline{D})$

---

## ❓ Preguntas de Repaso

1. ¿Qué puerta tiene solo una entrada?
2. ¿Cuándo la salida de una puerta AND es 1?
3. ¿Cuál es la diferencia entre OR y XOR?
4. ¿Qué significa que NAND sea "universal"?
5. ¿Qué pines de un CI 74LS08 se conectan a alimentación?

---

## 🔗 Recursos Adicionales

- **Simulador online:** [Falstad Circuit Simulator](https://www.falstad.com/circuit/) (sección "Digital Logic")
- **Tinkercad Circuits:** Permite montar circuitos con CIs virtuales
- **Hoja de datos:** [74LS08 Datasheet](https://www.ti.com/lit/ds/symlink/sn74ls08.pdf)
