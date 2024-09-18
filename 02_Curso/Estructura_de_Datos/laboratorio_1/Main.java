public class Main {
    public static void main(String[] args) {
        Teams<String> premier = new Teams<>();
      Teams<String> seria_a = new Teams<>();
        
        // Agregar algunos elementos a la lista
        premier.agregar("Liverpool");
        premier.agregar("Chelsea");
        premier.agregar("Man United");
        premier.agregar("Arsenal");
        premier.agregar("Man City");
        premier.agregar("Aston Villa");
        seria_a.agregar("Milan");
        
        // Mostrar la lista
        System.out.println("Elementos de la lista:");
        premier.mostrarElementos();
        System.out.println();
        
        // Eliminar un elemento
        premier.borrar("Man United");
        
        // Mostrar la lista de nuevo
        System.out.println("Elementos de la lista después de borrar 'Man United':");
        premier.mostrarElementos();
        System.out.println();
        
        // Reemplazar un elemento
        premier.reemplazar("Aston Villa", "Wolves");
        
        // Mostrar la lista de nuevo
        System.out.println("Elementos de la lista después de reemplazar 'Aston Villa' por 'Wolves':");
        premier.mostrarElementos();
        System.out.println();

        // Concatenar listas
        System.out.println("Elementos de la lista después de concatenar listas: ");
        premier.concatenar(seria_a);
        premier.mostrarElementos();
        System.out.println();

        //Comprobar si un elemento existe
        System.out.println("Comprobar si un elemento existe: ");
        boolean elemento = premier.contiene("Wolves");
        System.out.println(elemento);
        System.out.println();
  
        // Mostrar un elemento en una posición concreta
        int posicion = 1;
        System.out.println("Elemento en la posición " + posicion + ": " + premier.obtenerElemento(posicion));
        System.out.println();
      
          
        // Sacar un elemento concreto
        String elementoASacar = "Chelsea";
        premier.sacarElemento(elementoASacar);
        System.out.println("Elementos de la lista después de sacar '" + elementoASacar + "':");
        premier.mostrarElementos();
        System.out.println();
          
        // Sacar el elemento en una posición concreta
        int posicionASacar = 2;
        String elementoSacado = premier.sacarEnPosicion(posicionASacar);
        System.out.println("Elemento sacado de la posición " + posicionASacar + ": " + elementoSacado);
        System.out.println("Elementos de la lista después de sacar en posición " + posicionASacar + ":");
        premier.mostrarElementos();
        System.out.println();

        // Mostrar cantidad de elementos de la lista
        System.out.println("Cantidad de elementos en la lista: ");
        int cantidad = premier.obtenerCantidad();
        System.out.println(cantidad);
        
      }
}
