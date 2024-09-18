import java.util.ArrayList;

public class Album {
    private String nombre;
    private String artista;
    private ArrayList<Cancion> canciones;

    public Album(String nombre, String artista) {
        this.nombre = nombre;
        this.artista = artista;
        this.canciones = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public String getArtista() {
        return artista;
    }

    public void agregarCancion(Cancion cancion) {
        canciones.add(cancion);
    }

    // Método único para obtener la lista de canciones
    public ArrayList<Cancion> getCanciones() {
        return canciones;
    }

    @Override
    public String toString() {
        return nombre + " - " + artista;
    }
}
