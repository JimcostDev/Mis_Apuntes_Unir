# Llamadas al sistema

---

**Asignatura:** Sistemas operativos

**Presentado por:** *Ronaldo Jimenéz Acosta y Leila Bula*

--- 

### 1. Algoritmo de planificación FIFO (First In First Out)
**Ejemplo:**
Proceso | Tiempo de llegada | Ráfaga de CPU
--|--|--
```#1 Chrome``` | 0 | 10 
```#2 Vs Code``` | 2 | 12 
```#3 Excel``` | 4 | 5 
```#4 Git``` | 3 | 6 
```#5 Word``` | 1 | 24 

**Diagrama de Grantt:**
 ```Chrome``` | ```Word```  | ```Vs Code```  | ```Git``` |```Excel``` 
--|--|--|--|--
10 | 34 | 46 | 52 | 57

>**Tiempo de espera =** Tiempo ejecución - tiempo llegada
>
>**Chrome =** 0 - 0 = 0
>
>**Word =** 10 - 1 = 9
>
>**Vs Code =** 34 - 2 = 32
>
>**Git =** 46 - 3 = 43
>
>**Excel =** 52 - 4 = 48
>
>**Tiempo de espera promedio =** (0+9+32+43+48) / 5 = 26,4 ut.

>**Tiempo de respuesta =** Tiempo ráfaga + tiempo ráfaga anterior
>
>**Chrome =** 10 + 0 = 10
>
>**Word =** 24 + 10 = 34
>
>**Vs Code =** 12 + 34 = 46
>
>**Git =** 6 + 46 = 52
>
>**Excel =** 5 + 52 = 57
>
>**Tiempo de espera promedio =** (10+34+46+52+57) / 5 = 39,8 ut.

**Ejemplo en Python:**
>[algoritmo_planificacion_fifo.py](https://github.com/JimcostDev/Python_Ejercicios/blob/master/algoritmo_planificacion_fifo.py)

**Ejemplo en Java:**
>[Main.java](https://github.com/Leila-Bula/fcfs/blob/master/src/main/java/Main.java)


### 2. Algoritmo de planificación basado en prioridades
**Ejemplo:**
Proceso | Prioridad | Ráfaga de CPU
--|--|--
```#1 Chrome``` | 3 | 10 
```#2 Vs Code``` | 1 | 1 
```#3 Excel``` | 5 | 2 
```#4 Git``` | 4 | 1 
```#5 Word``` | 2 | 5 

**Diagrama de Grantt:**
 ```Vs Code``` | ```Word```  | ```Chrome```  | ```Git``` |```Excel``` 
--|--|--|--|--
1 | 6 | 16 | 17 | 19

>**Tiempo de espera =** Tiempo ejecución - tiempo llegada
>
>**Vs Code =** 0 - 0 = 0
>
>**Word =** 1 - 0 = 1
>
>**Chrome =** 6 - 0 = 6
>
>**Git =** 16 - 0 = 16
>
>**Excel =** 17 - 0 = 17
>
>**Tiempo de espera promedio =** (0+1+6+16+17) / 5 = 8 ut.

>**Tiempo de respuesta =** Tiempo ráfaga + tiempo ráfaga anterior
>
>**Vs Code =** 1 + 0 = 1
>
>**Word =** 5 + 1 = 6
>
>**Chrome =** 10 + 6 = 16
>
>**Git =** 1 + 16 = 17
>
>**Excel =** 2 + 17 = 19
>
>**Tiempo de espera promedio =** (1+6+16+17+19) / 5 = 11,8 ut.

**Ejemplo en Python:**
>[algoritmo_planificacion_x_prioridades.py](https://github.com/JimcostDev/Python_Ejercicios/blob/master/algoritmo_planificacion_x_prioridades.py)

### 3. Algoritmo de planificación Round Robin
**Ejemplo:**
Proceso |  Ráfaga de CPU
--|--
```#1 Chrome``` | 10 
```#2 Vs Code``` | 4
```#3 Excel``` | 8
```#4 Git``` | 5
```#5 Word``` | 12 

Quantum = 5

**Diagrama de Grantt:**
 ```Chrome``` | ```Vs Code```  | ```Excel```  | ```Git``` |```Word``` | ```Chrome``` | ```Excel```  |```Word``` |```Word```
--|--|--|--|--
5 | 9 | 14 | 19 | 24 | 29 | 32 | 37 | 39

>**Tiempo de espera promedio =** (19+5+24+14+27) / 5 = 17,8 ut.
>
>**Tiempo de espera promedio =** (29+9+32+19+39) / 5 = 25,6 ut.

**Ejemplo en Python:**
>[round_robin.py](https://github.com/JimcostDev/Python_Ejercicios/blob/master/round_robin.py)

