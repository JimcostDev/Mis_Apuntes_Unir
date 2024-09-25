public class Cancion {
    private String titulo;
    private String artista;
    private double duracion; // Duración en minutos

    // Constructor
    public Cancion(String titulo, String artista, double duracion) {
        this.titulo = titulo;
        this.artista = artista;
        this.duracion = duracion;
    }

    // Getters
    public String getTitulo() {
        return titulo;
    }

    public String getArtista() {
        return artista;
    }

    public double getDuracion() {
        return duracion;
    }

    // Método para representar la información de la canción en formato de cadena
    @Override
    public String toString() {
        return "Título: " + titulo + ", Artista: " + artista + ", Duración: " + duracion + " min";
    }
}
