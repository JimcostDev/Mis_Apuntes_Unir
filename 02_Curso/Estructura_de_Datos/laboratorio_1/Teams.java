public class Teams<T> {

    private Nodo<T> cabeza;
    private Nodo<T> cola;
    private int cantidad;
  
    // Constructor de la lista
    public Teams() {
      this.cabeza = null;
      this.cola = null;
      this.cantidad = 0;
    }
  
    // Nodo interno para la lista
    private static class Nodo<T> {
      private T valor;
      private Nodo<T> siguiente;
      private Nodo<T> anterior;
  
      public Nodo(T valor) {
        this.valor = valor;
        this.siguiente = null;
        this.anterior = null;
      }
    }
  
    // Agregar un elemento a la lista al final
    public void agregar(T elemento) {
      Nodo<T> nuevoNodo = new Nodo<>(elemento);
      if (this.cabeza == null) {
        this.cabeza = nuevoNodo;
        this.cola = nuevoNodo;
      } else {
        nuevoNodo.anterior = this.cola;
        this.cola.siguiente = nuevoNodo;
        this.cola = nuevoNodo;
      }
      this.cantidad++;
    }
  
    // Concatenar dos listas
    public void concatenar(Teams<T> otraLista) {
      if (otraLista.cabeza == null) {
        return;
      }
      if (this.cabeza == null) {
        this.cabeza = otraLista.cabeza;
        this.cola = otraLista.cola;
        this.cantidad = otraLista.cantidad;
        return;
      }
      this.cola.siguiente = otraLista.cabeza;
      otraLista.cabeza.anterior = this.cola;
      this.cola = otraLista.cola;
      this.cantidad += otraLista.cantidad;
    }
  
    // Borrar un elemento de la lista
    public void borrar(T elemento) {
      Nodo<T> actual = this.cabeza;
      while (actual != null) {
        if (actual.valor.equals(elemento)) {
          if (actual.anterior == null) {
            this.cabeza = actual.siguiente;
          } else {
            actual.anterior.siguiente = actual.siguiente;
          }
          if (actual.siguiente == null) {
            this.cola = actual.anterior;
          } else {
            actual.siguiente.anterior = actual.anterior;
          }
          this.cantidad--;
          return;
        }
        actual = actual.siguiente;
      }
    }
  
    // Mostrar los elementos de la lista
    public void mostrarElementos() {
      Nodo<T> actual = this.cabeza;
      while (actual != null) {
        System.out.println(actual.valor);
        actual = actual.siguiente;
      }
    }
  
    // Reemplazar un elemento de la lista
    public void reemplazar(T elementoViejo, T elementoNuevo) {
      Nodo<T> actual = this.cabeza;
      while (actual != null) {
        if (actual.valor.equals(elementoViejo)) {
          actual.valor = elementoNuevo;
          return;
        }
        actual = actual.siguiente;
      }
    }
  
    // Obtener el cantidad de la lista
    public int obtenerCantidad() {
      return this.cantidad;
    }
  
    //Comprobar si un elemento existe
    public boolean contiene(T elemento) {
      Nodo<T> actual = this.cabeza;
      while (actual != null) {
          if (actual.valor.equals(elemento)) {
              return true;
          }
          actual = actual.siguiente;
      }
      return false;
  }

  // Mostrar el elemento en una posición concreta de la lista
  public T obtenerElemento(int posicion) {
    if (posicion < 0 || posicion >= cantidad) {
      throw new IndexOutOfBoundsException("Posición fuera de rango");
    }
  
    Nodo<T> actual = cabeza;
    for (int i = 0; i < posicion; i++) {
      actual = actual.siguiente;
    }
  
    return actual.valor;
  }
  
  // Sacar un elemento concreto de la lista
  public void sacarElemento(T elemento) {
    Nodo<T> actual = cabeza;
    while (actual != null) {
      if (actual.valor.equals(elemento)) {
        if (actual.anterior == null) {
          cabeza = actual.siguiente;
        } else {
          actual.anterior.siguiente = actual.siguiente;
        }
        if (actual.siguiente == null) {
          cola = actual.anterior;
        } else {
          actual.siguiente.anterior = actual.anterior;
        }
        cantidad--;
        return;
      }
      actual = actual.siguiente;
    }
  }
  
  // Sacar el elemento en una posición concreta de la lista
  public T sacarEnPosicion(int posicion) {
    if (posicion < 0 || posicion >= cantidad) {
      throw new IndexOutOfBoundsException("Posición fuera de rango");
    }
  
    Nodo<T> actual = cabeza;
    for (int i = 0; i < posicion; i++) {
      actual = actual.siguiente;
    }
  
    if (actual.anterior == null) {
      cabeza = actual.siguiente;
    } else {
      actual.anterior.siguiente = actual.siguiente;
    }
    if (actual.siguiente == null) {
      cola = actual.anterior;
    } else {
      actual.siguiente.anterior = actual.anterior;
    }
  
    cantidad--;
    return actual.valor;
  }
   
}
  