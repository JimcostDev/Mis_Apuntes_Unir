package banco;
public class Cliente {
    private String documento;
    private String nombre;
    private String correo;
    private String numeroCelular;
    private String direccion;

    public Cliente(String documento, String nombre, String correo, String numeroCelular, String direccion) {
        this.documento = documento;
        this.nombre = nombre;
        this.correo = correo;
        this.numeroCelular = numeroCelular;
        this.direccion = direccion;
    }

    // Getters y Setters

    public String getDocumento() {
        return documento;
    }

    public void setDocumento(String documento) {
        this.documento = documento;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }

    public String getNumeroCelular() {
        return numeroCelular;
    }

    public void setNumeroCelular(String numeroCelular) {
        this.numeroCelular = numeroCelular;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
}
