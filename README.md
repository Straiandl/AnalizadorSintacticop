# Analizador Sintáctico

Este repositorio contiene la implementación en **Python** de un **Analizador Sintáctico** utilizando una pila de enteros para el manejo de estados y símbolos.

---

## Contenido de la Práctica

La práctica se divide en ejemplos demostrativos y dos ejercicios iterativos principales:

1. **Ejemplo 1:** Manipulación de la pila de enteros (`push`, `pop`, `top`).
2. **Ejemplo 2:** Lectura y tokenización básica con la clase `Lexico`.
3. **Ejercicio 1:** Análisis sintáctico para la gramática $E \rightarrow id + id$.
4. **Ejercicio 2:** Análisis sintáctico iterativo con reducción para la gramática recursiva $E \rightarrow id + E \mid id$.

---

## Mapeo de Símbolos y Matriz de Acciones

### Identificadores de Símbolos (Terminales y No Terminales)

Para el índice de columnas en la matriz de parseo $LR(1)$, se utilizan los siguientes enteros:

| ID Numérico | Símbolo | Categoría |
| :---: | :---: | :---: |
| **0** | `id` | Identificador (Terminal) |
| **1** | `+` | Operador de adición (Terminal) |
| **2** | `$` | Fin de cadena / Pesos (Terminal) |
| **3** | $E$ | Variable No Terminal |

### Convención de Valores en la Tabla $LR(1)$

* **Valores Positivos ($n > 0$):** Representan **Desplazamientos** (*Shift*) al estado $n$.
* **Valores Negativos ($n < 0$):** Representan **Reducciones** (*Reduce*):
  * `-1`: Aceptación de la cadena ($r_0$).
  * `-2`: Reducción por la **Regla 1** ($r_1$).
  * `-3`: Reducción por la **Regla 2** ($r_2$).
* **Valor Cero (`0`):** Error sintáctico (celda vacía en la tabla).

---

## Gramáticas y Tablas LR(1)

### Ejercicio 1: Gramática $E \rightarrow id + id$

#### Tabla de Parseo LR(1)

| Estado | `id` (0) | `+` (1) | `$` (2) | $E$ (3) |
| :---: | :---: | :---: | :---: | :---: |
| **0** | $d_2$ | | | 1 |
| **1** | | | $r_0$ (Aceptación) | |
| **2** | | $d_3$ | | |
| **3** | $d_4$ | | | |
| **4** | | | $r_1$ | |

---

### Ejercicio 2: Gramática $E \rightarrow id + E \mid id$

#### Reglas de Producción
* **Regla 1:** $E \rightarrow id + E$ (Longitud del lado derecho = 3, No terminal = $E$)
* **Regla 2:** $E \rightarrow id$ (Longitud del lado derecho = 1, No terminal = $E$)

#### Tabla de Parseo LR(1)

| Estado | `id` (0) | `+` (1) | `$` (2) | $E$ (3) |
| :---: | :---: | :---: | :---: | :---: |
| **0** | $d_2$ | | | 1 |
| **1** | | | $r_0$ (Aceptación) | |
| **2** | | $d_3$ | $r_2$ | |
| **3** | $d_2$ | | | 4 |
| **4** | | | $r_1$ | |

---

## Algoritmo de Reducción e Iteración

Para automatizar las reducciones en el ciclo principal, se utilizan dos arreglos auxiliares con la información de las reglas:

```python
# Identificador del No Terminal a la izquierda de la regla (3 representa a E)
idReglas = [3, 3]

# Cantidad de símbolos en el lado derecho de cada regla
lonReglas = [3, 1]
```

Al ejecutarse una reducción $r_k$:
1. Se determina el número de regla: `num_regla = abs(accion) - 2`.
2. Se extraen de la pila $2 \times \text{longitud}$ elementos (por cada símbolo se almacena el par `[Símbolo, Estado]`).
3. Se obtiene el estado en el nuevo tope de la pila.
4. Se consulta la transición de la matriz `tablaLR[estado][no_terminal]` y se inserta el no terminal junto con el nuevo estado.

---

## Requisitos y Ejecución

### Requisitos

* Python 3.8 o superior.

### Ejecución

Puedes ejecutar el script directamente desde la terminal:

```bash
python analizador_LR1.py
```

---

##  Ejemplo de Salida en Consola (Prueba con `"a+b"`)
![Salida Consola ejercicio 1](https://github.com/Straiandl/AnalizadorSintacticop/blob/037173398d73537ae80a2e310e01acf13d2225fb/Sintactico1.png)

![Salida Consola ejercicio 2]()

```

---

## Estructura del Proyecto

```text
.
├── analizador_LR1.py    # Script principal con la clase Lexico y algoritmos LR(1)
└── README.md            # Documentación del proyecto y explicación sintáctica
```

---
