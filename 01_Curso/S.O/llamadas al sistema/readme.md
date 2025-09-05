# 📂 Llamadas al Sistema y Planificación de Procesos

## 💡 Introducción

Este repositorio contiene material de estudio y ejemplos prácticos sobre la **Planificación de Procesos** en Sistemas Operativos. La planificación es crucial para la gestión de los recursos de la CPU.

Se exploran y demuestran tres algoritmos clave: **FIFO** (First In First Out), **Prioridades** y **Round Robin**, con sus respectivos ejemplos, cálculos de rendimiento y código fuente.

---

## 📺 Recursos Audiovisuales

| Título del Video | Enlace |
| :--- | :--- |
| **Planificación de Procesos en Python: Domina las Llamadas al Sistema con 2 Algoritmos Clave** | [🖥️ Ver en YouTube](https://youtu.be/QlMv7Pj1pk8) |



---

## 🔄 Algoritmos de Planificación de Procesos

### 1. Algoritmo FIFO (First In First Out)

También conocido como FCFS (First Come, First Served). Los procesos se ejecutan en el orden estricto de su tiempo de llegada.

#### 📝 Ejemplo de Procesos (FIFO)

| Proceso | Tiempo de Llegada (TL) | Ráfaga de CPU (R) |
| :---: | :---: | :---: |
| `#1 Chrome` | 0 | 10 |
| `#2 Vs Code` | 2 | 12 |
| `#3 Excel` | 4 | 5 |
| `#4 Git` | 3 | 6 |
| `#5 Word` | 1 | 24 |

#### 📊 Diagrama de Gantt (FIFO)

| `Chrome` (0-10) | `Word` (10-34) | `Vs Code` (34-46) | `Git` (46-52) | `Excel` (52-57) |
| :---: | :---: | :---: | :---: | :---: |
| **10** | **34** | **46** | **52** | **57** |

#### ⏱️ Cálculos de Tiempos (FIFO)

* **Fórmulas:**
    * **Tiempo de Espera (TE):** Tiempo de Inicio - Tiempo de Llegada
    * **Tiempo de Respuesta (TR):** Tiempo de Finalización

| Proceso | TE (Cálculo) | TE (Resultado) | TR (Cálculo) | TR (Resultado) |
| :---: | :---: | :---: | :---: | :---: |
| **Chrome** | $0 - 0$ | 0 | $10$ | 10 |
| **Word** | $10 - 1$ | 9 | $34$ | 34 |
| **Vs Code** | $34 - 2$ | 32 | $46$ | 46 |
| **Git** | $46 - 3$ | 43 | $52$ | 52 |
| **Excel** | $52 - 4$ | 48 | $57$ | 57 |
| **---** | **Promedio** | **26.4 ut** | **Promedio** | **39.8 ut** |

#### 💻 Código Fuente (FIFO)

* **Python:** [algoritmo_planificacion_fifo.py](https://github.com/JimcostDev/python_programming_fundamentals/tree/master/exercises/alg-planif-proc)
* **Java:** [Main.java](https://github.com/Leila-Bula/algoritmo-planificacion-fcfs/blob/master/src/main/java/Main.java)
* **Resultados PDF:** [fcfs.pdf](https://github.com/JimcostDev/Mis_Apuntes_Unir/blob/master/01_Curso/S.O/llamadas%20al%20sistema/fcfs.pdf)

### 2. Algoritmo de Planificación Basado en Prioridades

Los procesos se ejecutan según un valor de prioridad asignado. En este ejemplo, se asume que un número de prioridad **menor** significa **mayor** prioridad.

#### 📝 Ejemplo de Procesos (Prioridades)

| Proceso | Prioridad (P) | Ráfaga de CPU (R) |
| :---: | :---: | :---: |
| `#1 Chrome` | 3 | 10 |
| `#2 Vs Code` | 1 | 1 |
| `#3 Excel` | 5 | 2 |
| `#4 Git` | 4 | 1 |
| `#5 Word` | 2 | 5 |

#### 📊 Diagrama de Gantt (Prioridades)

| `Vs Code` (0-1) | `Word` (1-6) | `Chrome` (6-16) | `Git` (16-17) | `Excel` (17-19) |
| :---: | :---: | :---: | :---: | :---: |
| **1** | **6** | **16** | **17** | **19** |

#### ⏱️ Cálculos de Tiempos (Prioridades)

| Proceso | TE (Cálculo) | TE (Resultado) | TR (Cálculo) | TR (Resultado) |
| :---: | :---: | :---: | :---: | :---: |
| **Vs Code** | $0 - 0$ | 0 | $1$ | 1 |
| **Word** | $1 - 0$ | 1 | $6$ | 6 |
| **Chrome** | $6 - 0$ | 6 | $16$ | 16 |
| **Git** | $16 - 0$ | 16 | $17$ | 17 |
| **Excel** | $17 - 0$ | 17 | $19$ | 19 |
| **---** | **Promedio** | **8 ut** | **Promedio** | **11.8 ut** |

#### 💻 Código Fuente (Prioridades)

* **Python:** [algoritmo_planificacion_x_prioridades.py](https://github.com/JimcostDev/python_programming_fundamentals/tree/master/exercises/alg-planif-proc)

### 3. Algoritmo de Planificación Round Robin (RR)

Algoritmo de planificación preventivo que asigna a cada proceso una porción de tiempo de CPU llamada **Quantum** (Q).

#### 📝 Ejemplo de Procesos (Round Robin)

| Proceso | Ráfaga de CPU (R) |
| :---: | :---: |
| `#1 Chrome` | 10 |
| `#2 Vs Code` | 4 |
| `#3 Excel` | 8 |
| `#4 Git` | 5 |
| `#5 Word` | 12 |

**Quantum (Q) = 5 ut**

#### ⏱️ Tiempos Promedio (Round Robin)

* **Tiempo de Espera Promedio:** **15.8 ut**
* **Tiempo de Respuesta Promedio:** **23.6 ut**

*(Nota: Los cálculos detallados del Diagrama de Gantt para Round Robin están incluidos en el código fuente.)*

#### 💻 Código Fuente y Video (Round Robin)

* **Python:** [round_robin.py](https://github.com/JimcostDev/python_programming_fundamentals/tree/master/exercises/alg-planif-proc)
* **Video Complementario:** [🔁 Round Robin en Python y Java: Implementación Práctica para Sistemas Operativos 🖥️](https://youtu.be/xVzgQukMcVE)

---

## 🔗 Referencias y Créditos

* **MasterHeHeGar:** [Canal de YouTube](https://www.youtube.com/user/MasterHeHeGar)
