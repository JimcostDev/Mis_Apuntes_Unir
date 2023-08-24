# Documentación Técnica - Implementación de la Clase `Teams`

**Autor :** *Ronaldo Jimenez* 

**Web :** www.jimcostdev.com

## Introducción

La clase `Teams` implementa una lista doblemente enlazada genérica en Java. Esta estructura de datos permite almacenar elementos (en este ejemplo, equipos de futbol) en una secuencia ordenada, y proporciona métodos para agregar, borrar, reemplazar, mostrar y realizar otras operaciones sobre los elementos de la lista.

Decidí hacer este ejemplo con equipos de futbol, ya que es un tema que me gusta y además me facilita la comprensión de los conceptos.

## Diseño de la Clase `Teams`

### Atributos

- `cabeza`: Representa el primer nodo de la lista.
- `cola`: Representa el último nodo de la lista.
- `cantidad`: Almacena la cantidad de elementos en la lista.

### Clase Interna `Nodo`

La clase interna `Nodo` se utiliza para representar cada elemento en la lista. Cada nodo contiene tres atributos:
- `valor`: Almacena el valor del elemento.
- `siguiente`: Apunta al siguiente nodo en la lista.
- `anterior`: Apunta al nodo anterior en la lista.

### Métodos Principales

#### `agregar(T elemento)`

- Descripción: Agrega un elemento al final de la lista.
- Implementación: Se crea un nuevo nodo con el elemento proporcionado. Si la lista está vacía, la cabeza y la cola apuntan al nuevo nodo. Si no está vacía, se actualiza el enlace del nodo anterior y se establece la cola en el nuevo nodo.

#### `borrar(T elemento)`

- Descripción: Elimina un elemento específico de la lista.
- Implementación: Se recorre la lista para encontrar el nodo con el valor especificado. Se actualizan los enlaces de los nodos adyacentes para eliminar el nodo seleccionado.

#### `reemplazar(T elementoViejo, T elementoNuevo)`

- Descripción: Reemplaza un elemento específico en la lista.
- Implementación: Se recorre la lista para encontrar el nodo con el valor a reemplazar. Se actualiza el valor del nodo encontrado con el nuevo valor.

#### `concatenar(Teams<T> otraLista)`

- Descripción: Concatena dos listas en una sola.
- Implementación: Si la segunda lista no está vacía, se actualizan los enlaces de los nodos para conectar la cola de la primera lista con la cabeza de la segunda lista. Luego se actualiza la cola y la cantidad.

#### `obtenerElemento(int posicion)`

- Descripción: Obtiene el elemento en una posición específica.
- Implementación: Se recorre la lista hasta llegar a la posición deseada y se devuelve el valor del nodo en esa posición.

#### `sacarElemento(T elemento)`

- Descripción: Elimina un elemento específico de la lista.
- Implementación: Similar al método `borrar`, recorre la lista para encontrar el nodo con el valor especificado y actualiza los enlaces adyacentes para eliminarlo.

#### `sacarEnPosicion(int posicion)`

- Descripción: Elimina el elemento en una posición específica.
- Implementación: Similar al método `borrar`, recorre la lista hasta llegar a la posición deseada y actualiza los enlaces adyacentes para eliminar el nodo en esa posición.

#### `contiene(T elemento)`

- Descripción: Verifica si un elemento existe en la lista.
- Implementación: Recorre la lista para verificar si alguno de los nodos tiene el valor especificado.

## Conclusión

La implementación de la clase `Teams` proporciona una estructura de datos para manipular listas doblemente enlazadas genéricas. Los métodos implementados permiten realizar operaciones comunes sobre la lista, como agregar, borrar, reemplazar y concatenar elementos, así como verificar la existencia de un elemento en la lista.


