# Tema 3: Álgebra de Boole

## 🎯 Objetivos de Aprendizaje
Al finalizar este tema, serás capaz de:
- Comprender los fundamentos del álgebra de Boole
- Aplicar las operaciones lógicas básicas (AND, OR, NOT)
- Utilizar las leyes y teoremas fundamentales para simplificar expresiones
- Traducir problemas lógicos a expresiones booleanas

---

## 1. ¿Qué es el Álgebra de Boole?

Es un sistema matemático creado por **George Boole** (1854) que trabaja con variables que solo pueden tomar **dos valores**: 
- **VERDADERO / FALSO**
- **1 / 0**
- **ALTO / BAJO**
- **SÍ / NO**

Es la base matemática de toda la electrónica digital y la informática.

---

## 2. Variables y Funciones Lógicas

### 2.1. Variables Booleanas

Se representan con letras mayúsculas: $A$, $B$, $C$, etc.

**Ejemplo:** 
- $A = 1$ → El interruptor A está cerrado
- $A = 0$ → El interruptor A está abierto

### 2.2. Funciones Lógicas

Una función lógica $F$ relaciona una o más variables de entrada con una salida:

$$
F = f(A, B, C, ...)
$$

**Ejemplo:** $F = A \cdot B$ significa que $F$ vale 1 solo si $A$ **y** $B$ valen 1.

---

## 3. Operaciones Lógicas Básicas

### 3.1. Operación NOT (Negación)

**Símbolo:** $\overline{A}$ o $A'$ o $\neg A$

**Definición:** Invierte el valor de la variable.

**Tabla de verdad:**

| $A$ | $\overline{A}$ |
|-----|----------------|
| 0   | 1              |
| 1   | 0              |

**Ejemplo:** Si $A$ = "está lloviendo", entonces $\overline{A}$ = "NO está lloviendo"

---

### 3.2. Operación AND (Producto Lógico)

**Símbolo:** $A \cdot B$ o $A \land B$ o $AB$

**Definición:** Vale 1 **solo si todas** las entradas valen 1.

**Tabla de verdad:**

| $A$ | $B$ | $A \cdot B$ |
|-----|-----|-------------|
| 0   | 0   | 0           |
| 0   | 1   | 0           |
| 1   | 0   | 0           |
| 1   | 1   | 1           |

**Analogía eléctrica:** Dos interruptores en **serie**:
```
  ─[A]─[B]─   → Solo pasa corriente si A Y B están cerrados
```

**Ejemplo:** "Para encender el ordenador, debe haber corriente (A=1) Y el botón estar pulsado (B=1)"

---

### 3.3. Operación OR (Suma Lógica)

**Símbolo:** $A + B$ o $A \lor B$

**Definición:** Vale 1 **si al menos una** entrada vale 1.

**Tabla de verdad:**

| $A$ | $B$ | $A + B$ |
|-----|-----|---------|
| 0   | 0   | 0       |
| 0   | 1   | 1       |
| 1   | 0   | 1       |
| 1   | 1   | 1       |

**Analogía eléctrica:** Dos interruptores en **paralelo**:
```
     ┌─[A]─┐
  ───┤     ├───   → Pasa corriente si A O B están cerrados
     └─[B]─┘
```

**Ejemplo:** "La alarma suena si detecta humo (A=1) O si detecta movimiento (B=1)"

---

## 4. Propiedades Fundamentales

### 4.1. Identidad

$$
A \cdot 1 = A \quad \quad A + 0 = A
$$

### 4.2. Elemento Absorbente (Dominante)

$$
A \cdot 0 = 0 \quad \quad A + 1 = 1
$$

### 4.3. Idempotencia

$$
A \cdot A = A \quad \quad A + A = A
$$

### 4.4. Complementariedad

$$
A \cdot \overline{A} = 0 \quad \quad A + \overline{A} = 1
$$

### 4.5. Doble Negación

$$
\overline{\overline{A}} = A
$$

---

## 5. Leyes Fundamentales

### 5.1. Conmutativa

$$
A \cdot B = B \cdot A \quad \quad A + B = B + A
$$

El orden de los factores no altera el resultado.

---

### 5.2. Asociativa

$$
(A \cdot B) \cdot C = A \cdot (B \cdot C) \quad \quad (A + B) + C = A + (B + C)
$$

Permite agrupar las operaciones como queramos.

---

### 5.3. Distributiva

$$
A \cdot (B + C) = A \cdot B + A \cdot C
$$

El producto se distribuye sobre la suma (igual que en álgebra normal).

**Ejemplo práctico:**
$$
A(B + C) = AB + AC
$$

---

## 6. Teoremas de De Morgan

Son **fundamentales** para simplificar circuitos. Permiten convertir productos en sumas y viceversa:

### Primer Teorema:
$$
\overline{A \cdot B} = \overline{A} + \overline{B}
$$

"La negación de un producto es la suma de las negaciones"

### Segundo Teorema:
$$
\overline{A + B} = \overline{A} \cdot \overline{B}
$$

"La negación de una suma es el producto de las negaciones"

### Ejemplo de Aplicación:
Simplificar: $\overline{A \cdot B \cdot C}$

Aplicando De Morgan:
$$
\overline{A \cdot B \cdot C} = \overline{A} + \overline{B} + \overline{C}
$$

---

## 7. Simplificación de Expresiones

### Ejemplo 1: Usar Idempotencia
$$
F = A + A + B = A + B
$$

### Ejemplo 2: Usar Absorción
$$
F = A + A \cdot B = A \quad \text{(porque si } A=1 \text{, } F=1 \text{ independientemente de } B\text{)}
$$

### Ejemplo 3: Usar Complementariedad
$$
F = A \cdot B + A \cdot \overline{B} = A(B + \overline{B}) = A \cdot 1 = A
$$

### Ejemplo 4: Usar De Morgan
$$
F = \overline{A + B} \quad \Rightarrow \quad F = \overline{A} \cdot \overline{B}
$$

---

## 8. Aplicación: Problemas Verbales

### Problema 1: Sistema de Seguridad
*Una puerta se abre si:*
- *Hay tarjeta válida (A=1) Y el PIN es correcto (B=1)*
- *O si hay emergencia (C=1)*

**Expresión booleana:**
$$
F = A \cdot B + C
$$

**Tabla de verdad:**

| $A$ | $B$ | $C$ | $F$ | Interpretación |
|-----|-----|-----|-----|----------------|
| 0   | 0   | 0   | 0   | No se abre |
| 0   | 0   | 1   | 1   | Emergencia → Abre |
| 0   | 1   | 0   | 0   | PIN sin tarjeta → No abre |
| 1   | 0   | 0   | 0   | Tarjeta sin PIN → No abre |
| 1   | 1   | 0   | 1   | Tarjeta + PIN → Abre |
| 1   | 1   | 1   | 1   | Todo correcto + emergencia → Abre |

---

### Problema 2: Control de Riego
*El riego se activa si:*
- *El sensor de humedad indica seco (H=0)*
- *Y NO está lloviendo (L=0)*
- *Y es de día (D=1)*

**Expresión booleana:**
$$
F = \overline{H} \cdot \overline{L} \cdot D
$$

---

## 9. Formas Canónicas

### 9.1. Suma de Productos (SOP)

**Forma estándar:** $F = AB + \overline{A}C + BC$

Cada término es un "minitérmino" (producto de variables).

### 9.2. Producto de Sumas (POS)

**Forma estándar:** $F = (A+B)(A+\overline{C})(\overline{B}+C)$

Cada término es un "maxitérmino" (suma de variables).

**Nota:** En el Tema 5 aprenderemos a simplificar estas expresiones con **Mapas de Karnaugh**.

---

## 📝 Actividades

### Actividad 1: Completar Tablas de Verdad
Completa las tablas para:
1. $F = A \cdot \overline{B}$
2. $F = \overline{A} + B$
3. $F = A \cdot B + \overline{B}$

### Actividad 2: Simplificación Algebraica
Simplifica usando las leyes de Boole:
1. $F = A \cdot 0 + B$
2. $F = A + A \cdot B$
3. $F = (A + B)(A + \overline{B})$
4. $F = \overline{A \cdot B} \cdot \overline{A + B}$

### Actividad 3: Aplicación Práctica
Un sistema de calefacción se enciende si:
- La temperatura es baja (T=1)
- Y hay alguien en casa (P=1)
- O si hay riesgo de helada (H=1)

1. Escribe la expresión booleana
2. Crea la tabla de verdad

### Actividad 4: De Morgan
Aplica De Morgan para transformar:
1. $\overline{A + B + C}$
2. $\overline{(A \cdot B) + C}$

---

## ❓ Preguntas de Repaso

1. ¿Cuál es el resultado de $1 \cdot 0$?
2. ¿Cuál es el resultado de $1 + 0$?
3. ¿Qué dice la ley de idempotencia para la suma?
4. Enuncia el primer teorema de De Morgan.
5. Si $A=1$ y $B=0$, ¿cuánto vale $\overline{A} + B$?

---

## 🔗 Recursos Adicionales

- **Simulador online:** [Boolean Algebra Calculator](https://www.boolean-algebra.com/)
- **Video explicativo:** [Álgebra de Boole - Khan Academy](https://www.khanacademy.org/)

---

**Tema anterior:** [Sistemas de Numeración](02_sistemas_numeracion.md)  
**Siguiente tema:** [Puertas Lógicas](04_puertas_logicas.md)
