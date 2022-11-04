# Llamadas al sistema

---

**Asignatura:** Sistemas operativos

**Presentado por:** *Ronaldo Jimenéz Acosta y Leila Bulla*

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

**Ejemplo en python:**
>[algoritmo_planificacion_fifo.py](https://github.com/JimcostDev/Python_Ejercicios/blob/master/algoritmo_planificacion_fifo.py)
