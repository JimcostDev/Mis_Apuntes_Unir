# Documentación Técnica del Proyecto: Árbol Binario de Búsqueda (ABB) para Equipos de la Premier League en Java

**Autor :** *Ronaldo Jimenez* 

**Web :** www.jimcostdev.com

## Introducción

El proyecto consiste en la implementación de un Árbol Binario de Búsqueda (ABB) en Java para almacenar y gestionar información sobre equipos de la Premier League. El ABB permite realizar operaciones de inserción, borrado y recorridos en el árbol. Este documento proporciona una visión general de la implementación y cómo utilizarla.

## Estructura del Proyecto

El proyecto se divide en tres archivos Java principales:

1. **PremierLeagueTeam.java**: Este archivo define la clase `PremierLeagueTeam`, que representa un equipo de la Premier League con propiedades como nombre y puntos. Además, incluye un método `toString()` para facilitar la visualización.

2. **BinarySearchTree.java**: Este archivo contiene la implementación del Árbol Binario de Búsqueda (ABB) utilizando nodos `TreeNode` y proporciona métodos para insertar, borrar y realizar recorridos en el árbol. También incluye un método para imprimir el árbol.

3. **Main.java**: Este archivo es la clase principal que contiene el método `main()`. Aquí se crea una instancia del ABB, se insertan equipos de la Premier League, se realizan recorridos en el árbol, se borra un equipo y se imprime el árbol resultante.

## Uso del Proyecto

1. **Inserción de Equipos**: Puedes insertar equipos en el árbol utilizando el método `insert(PremierLeagueTeam team)` en `BinarySearchTree.java`. Los equipos se insertan según su puntaje.

2. **Recorridos en el Árbol**:
   - Para realizar un recorrido en preorden, utiliza el método `preOrderTraversal()`.
   - Para realizar un recorrido en inorden, utiliza el método `inOrderTraversal()`.
   - Para realizar un recorrido en posorden, utiliza el método `postOrderTraversal()`.

3. **Borrado de Equipos**: Puedes borrar un equipo del árbol utilizando el método `delete(PremierLeagueTeam team)` en `BinarySearchTree.java`. El equipo se borra según su puntaje.

4. **Impresión del Árbol**: Puedes imprimir el árbol en orden utilizando el método `printTree()` en `BinarySearchTree.java`. Esto mostrará los equipos ordenados por puntaje.

## Ejemplo de Uso

```java
public class Main {
    public static void main(String[] args) {
        BinarySearchTree premierLeagueTree = new BinarySearchTree();

        // Insertar equipos
        premierLeagueTree.insert(new PremierLeagueTeam("Manchester City", 76));
        premierLeagueTree.insert(new PremierLeagueTeam("Liverpool", 74));
        premierLeagueTree.insert(new PremierLeagueTeam("Chelsea", 70));
        premierLeagueTree.insert(new PremierLeagueTeam("Manchester United", 68));
        premierLeagueTree.insert(new PremierLeagueTeam("Arsenal", 66));

        // Realizar recorridos
        System.out.println("Recorrido en preorden:");
        premierLeagueTree.preOrderTraversal();

        System.out.println("\nRecorrido en inorden:");
        premierLeagueTree.inOrderTraversal();

        System.out.println("\nRecorrido en posorden:");
        premierLeagueTree.postOrderTraversal();
        System.out.println();

        // Borrar un equipo
        premierLeagueTree.delete(new PremierLeagueTeam("Chelsea", 70));

        // Imprimir el árbol después de borrar
        System.out.println("\nEquipo borrado:");
        premierLeagueTree.printTree();
    }
}
