# Better Fitness Production Optimization

Este proyecto modela y resuelve el problema de producción de Better Fitness, Inc. utilizando Programación Lineal. Se determinan las cantidades óptimas de producción para las máquinas BodyPlus 100 y BodyPlus 200, considerando restricciones de recursos y políticas de mezcla.

## Herramientas y Tecnologías

- **GeoGebra**: Para representar gráficamente la región factible y visualizar las restricciones del modelo.
- **Python y PuLP**: Para formular y resolver el modelo de Programación Lineal.

## Descripción

El modelo optimiza la utilidad total, maximizando la producción de BodyPlus 100 y BodyPlus 200 bajo restricciones de:
- Horas disponibles de mecanizado, pintura y ensamblaje.
- Políticas de mezcla (proporción mínima de BodyPlus 200 en la producción total).

## Uso

1. Clona el repositorio.
2. Instala las dependencias con:
   ```bash
   pip install pulp
   ```
3. Ejecuta el script principal:
 ```bash
   python main.py
   ```

