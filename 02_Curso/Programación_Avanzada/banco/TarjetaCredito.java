package banco;

public class TarjetaCredito {
    private Cliente cliente;
    private String numeroTarjeta;
    private String fechaApertura;
    private String fechaVencimiento;
    private double porcentajeInteres;
    private double cupo;
    private double valorUtilizado;

    public TarjetaCredito(Cliente cliente, String numeroTarjeta, String fechaApertura, String fechaVencimiento, double porcentajeInteres, double cupo, double valorUtilizado) {
        this.cliente = cliente;
        this.numeroTarjeta = numeroTarjeta;
        this.fechaApertura = fechaApertura;
        this.fechaVencimiento = fechaVencimiento;
        this.porcentajeInteres = porcentajeInteres;
        this.cupo = cupo;
        this.valorUtilizado = valorUtilizado;
    }

    public void calcularInteresesMensuales() {
        double intereses = valorUtilizado * (porcentajeInteres / 100);
        valorUtilizado += intereses;
    }

    // Getters y Setters

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public String getNumeroTarjeta() {
        return numeroTarjeta;
    }

    public void setNumeroTarjeta(String numeroTarjeta) {
        this.numeroTarjeta = numeroTarjeta;
    }

    public String getFechaApertura() {
        return fechaApertura;
    }

    public void setFechaApertura(String fechaApertura) {
        this.fechaApertura = fechaApertura;
    }

    public String getFechaVencimiento() {
        return fechaVencimiento;
    }

    public void setFechaVencimiento(String fechaVencimiento) {
        this.fechaVencimiento = fechaVencimiento;
    }

    public double getPorcentajeInteres() {
        return porcentajeInteres;
    }

    public void setPorcentajeInteres(double porcentajeInteres) {
        this.porcentajeInteres = porcentajeInteres;
    }

    public double getCupo() {
        return cupo;
    }

    public void setCupo(double cupo) {
        this.cupo = cupo;
    }

    public double getValorUtilizado() {
        return valorUtilizado;
    }

    public void setValorUtilizado(double valorUtilizado) {
        this.valorUtilizado = valorUtilizado;
    }
}

