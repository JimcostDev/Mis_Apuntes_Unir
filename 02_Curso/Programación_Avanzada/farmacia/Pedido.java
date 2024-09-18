public class Pedido {
    private String medicamento;
    private String tipo;
    private int cantidad;
    private String distribuidor;
    private boolean principal, secundaria;

    // Constructor
    public Pedido(String medicamento, String tipo, int cantidad, String distribuidor, boolean principal, boolean secundaria) {
        this.medicamento = medicamento;
        this.tipo = tipo;
        this.cantidad = cantidad;
        this.distribuidor = distribuidor;
        this.principal = principal;
        this.secundaria = secundaria;
    }

    // Getters y setters
    public String getMedicamento() {
        return medicamento;
    }

    public void setMedicamento(String medicamento) {
        this.medicamento = medicamento;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    public String getDistribuidor() {
        return distribuidor;
    }

    public void setDistribuidor(String distribuidor) {
        this.distribuidor = distribuidor;
    }

    public boolean isPrincipal() {
        return principal;
    }

    public void setPrincipal(boolean principal) {
        this.principal = principal;
    }

    public boolean isSecundaria() {
        return secundaria;
    }

    public void setSecundaria(boolean secundaria) {
        this.secundaria = secundaria;
    }

    // Método para obtener el resumen del pedido
    public String getResumen() {
        String direccion = "";
        if (principal) {
            direccion += "Calle de la Rosa n. 28";
        }
        if (secundaria) {
            if (!direccion.isEmpty()) {
                direccion += " y ";
            }
            direccion += "Calle Alcazabilla n. 3";
        }

        // Usar etiquetas HTML y <br> para los saltos de línea
        return "<html>Pedido al distribuidor " + distribuidor + "<br>" +
        cantidad + " unidades del " + tipo + " " + medicamento + "<br>" +
        "Para la farmacia situada en " + direccion + "</html>";
    }
}