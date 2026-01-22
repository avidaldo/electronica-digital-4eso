# Tema 2: Sistemas de Numeración

## 🎯 Objetivos de Aprendizaje
Al finalizar este tema, serás capaz de:
- Comprender el funcionamiento del sistema binario y hexadecimal
- Convertir números entre sistemas decimal, binario y hexadecimal
- Realizar operaciones aritméticas básicas en binario
- Aplicar estos conocimientos al diseño de circuitos digitales

---

## 1. ¿Por Qué Diferentes Sistemas de Numeración?

En electrónica digital trabajamos con **dos estados** (encendido/apagado, alto/bajo), por eso el **sistema binario** (base 2) es el lenguaje natural de los circuitos digitales.

El **sistema hexadecimal** (base 16) se usa como "atajo" para representar grandes números binarios de forma más compacta.

---

## 2. Sistema Decimal (Base 10)

Es el sistema que usamos habitualmente. Tiene **10 símbolos**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9.

### 2.1. Valor Posicional

Cada posición representa una potencia de 10:

$$
325_{10} = 3 \times 10^2 + 2 \times 10^1 + 5 \times 10^0 = 300 + 20 + 5
$$

---

## 3. Sistema Binario (Base 2)

Solo tiene **2 símbolos**: 0 y 1 (llamados **bits**).

### 3.1. Valor Posicional en Binario

Cada posición representa una potencia de 2:

| Posición | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|----------|---|---|---|---|---|---|---|---|
| Potencia | $2^7$ | $2^6$ | $2^5$ | $2^4$ | $2^3$ | $2^2$ | $2^1$ | $2^0$ |
| Valor | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

#### Ejemplo:
$$
10110101_2 = 1\times128 + 0\times64 + 1\times32 + 1\times16 + 0\times8 + 1\times4 + 0\times2 + 1\times1
$$
$$
= 128 + 32 + 16 + 4 + 1 = 181_{10}
$$

### 3.2. Conversión: Decimal → Binario

**Método de las divisiones sucesivas:**

Convertir $25_{10}$ a binario:

```
25 ÷ 2 = 12  resto 1  ↑ (LSB - bit menos significativo)
12 ÷ 2 = 6   resto 0  │
6  ÷ 2 = 3   resto 0  │
3  ÷ 2 = 1   resto 1  │
1  ÷ 2 = 0   resto 1  ↓ (MSB - bit más significativo)

Resultado: 25₁₀ = 11001₂
```

**Comprobación:** $16 + 8 + 1 = 25$ ✓

### 3.3. Conversión: Binario → Decimal

Multiplica cada bit por su peso (potencia de 2) y suma:

$$
1101_2 = 1\times8 + 1\times4 + 0\times2 + 1\times1 = 8 + 4 + 1 = 13_{10}
$$

---

## 4. Sistema Hexadecimal (Base 16)

Tiene **16 símbolos**: 0-9 y A-F (donde A=10, B=11, C=12, D=13, E=14, F=15).

### 4.1. ¿Por Qué Hexadecimal?

Porque **4 bits = 1 dígito hexadecimal**, lo que hace muy sencilla la conversión:

| Binario | Hexadecimal | Decimal |
|---------|-------------|---------|
| 0000 | 0 | 0 |
| 0001 | 1 | 1 |
| 0010 | 2 | 2 |
| 0011 | 3 | 3 |
| 0100 | 4 | 4 |
| 0101 | 5 | 5 |
| 0110 | 6 | 6 |
| 0111 | 7 | 7 |
| 1000 | 8 | 8 |
| 1001 | 9 | 9 |
| 1010 | A | 10 |
| 1011 | B | 11 |
| 1100 | C | 12 |
| 1101 | D | 13 |
| 1110 | E | 14 |
| 1111 | F | 15 |

### 4.2. Conversión: Binario ↔ Hexadecimal

#### Binario → Hexadecimal:
Agrupa de 4 en 4 bits (empezando por la derecha) y convierte cada grupo:

```
Binario:  11010110₂
Grupos:   1101  0110
Hex:        D     6

Resultado: 11010110₂ = D6₁₆
```

#### Hexadecimal → Binario:
Convierte cada dígito hex a 4 bits:

```
3A₁₆
3 = 0011
A = 1010

Resultado: 3A₁₆ = 00111010₂
```

### 4.3. Conversión: Hexadecimal ↔ Decimal

#### Hexadecimal → Decimal:
$$
2F_{16} = 2 \times 16^1 + F \times 16^0 = 2 \times 16 + 15 \times 1 = 32 + 15 = 47_{10}
$$

#### Decimal → Hexadecimal:
Divisiones sucesivas entre 16:

```
255 ÷ 16 = 15  resto 15 (F)  ↑
15  ÷ 16 = 0   resto 15 (F)  ↓

Resultado: 255₁₀ = FF₁₆
```

---

## 5. Operaciones Aritméticas en Binario

### 5.1. Suma Binaria

**Reglas básicas:**
- 0 + 0 = 0
- 0 + 1 = 1
- 1 + 0 = 1
- 1 + 1 = 10 (0 y me llevo 1)

#### Ejemplo:
```
    1011₂  (11₁₀)
  +  110₂  ( 6₁₀)
  -------
   10001₂  (17₁₀)
  
   ¹¹      (acarreos)
```

### 5.2. Resta Binaria

**Reglas básicas:**
- 0 - 0 = 0
- 1 - 0 = 1
- 1 - 1 = 0
- 0 - 1 = 1 (y pido prestado 1)

#### Ejemplo:
```
   1101₂  (13₁₀)
  - 101₂  ( 5₁₀)
  ------
   1000₂  ( 8₁₀)
```

---

## 6. Aplicaciones en Electrónica Digital

### 6.1. Direcciones de Memoria

Los microprocesadores usan **direcciones hexadecimales**:
- Arduino Uno: memoria RAM de `0x0000` a `0x08FF`
- El prefijo `0x` indica hexadecimal

### 6.2. Códigos de Color RGB

Los colores en pantallas se representan en hexadecimal:
- Rojo puro: `#FF0000` = (255, 0, 0)
- Verde: `#00FF00`
- Azul: `#0000FF`
- Blanco: `#FFFFFF` = (255, 255, 255)

### 6.3. Puertos de E/S

Si un puerto de 8 bits (1 byte) tiene el valor `10110010₂`:
- En binario: `10110010`
- En hexadecimal: `B2` (más compacto)
- En decimal: 178

---

## 7. Tabla Resumen de Conversiones

| Decimal | Binario | Hexadecimal |
|---------|---------|-------------|
| 0 | 0000 | 0 |
| 5 | 0101 | 5 |
| 10 | 1010 | A |
| 15 | 1111 | F |
| 16 | 00010000 | 10 |
| 255 | 11111111 | FF |

---

## 📝 Actividades

### Actividad 1: Conversión Decimal → Binario
Convierte a binario: 42, 100, 127, 200

### Actividad 2: Conversión Binario → Decimal
Convierte a decimal: `11001`, `10101010`, `11111111`

### Actividad 3: Conversión Binario ↔ Hexadecimal
1. Binario → Hex: `11010110`, `10011111`
2. Hex → Binario: `3F`, `A5`, `FF`

### Actividad 4: Suma Binaria
Resuelve:
1. `1010₂ + 0111₂`
2. `1101₂ + 1011₂`

### Actividad 5: Aplicación Práctica
Un LED RGB se controla con 3 bytes (8 bits cada uno) para R, G, B. Si queremos un color naranja `#FF6600`:
1. Convierte cada valor a binario
2. ¿Cuántos bits en total necesitas?

---

## ❓ Preguntas de Repaso

1. ¿Cuántos símbolos tiene el sistema binario?
2. ¿Cuál es el equivalente decimal de `1111₂`?
3. ¿Por qué se usa el sistema hexadecimal en informática?
4. Convierte `10101010₂` a hexadecimal sin pasar por decimal.
5. ¿Cuántos bits se necesitan para representar 256 valores diferentes?

---

## 🔗 Recursos Adicionales

- **Calculadora online:** [RapidTables - Binary Converter](https://www.rapidtables.com/convert/number/binary-to-decimal.html)
- **Práctica interactiva:** [Cisco Binary Game](https://learningnetwork.cisco.com/s/binary-game)

---

**Tema anterior:** [Introducción a la Electrónica Digital](01_introduccion.md)  
**Siguiente tema:** [Álgebra de Boole](03_algebra_boole.md)
