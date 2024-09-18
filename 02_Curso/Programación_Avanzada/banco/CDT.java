package banco;

public class CDT {
    private Cliente cliente;
    private String numeroCDT;
    private String fechaApertura;
    private int plazoMeses;
    private double valor;
    private double porcentajeInteres;

    public CDT(Cliente cliente, String numeroCDT, String fechaApertura, int plazoMeses, double valor, double porcentajeInteres) {
        this.cliente = cliente;
        this.numeroCDT = numeroCDT;
        this.fechaApertura = fechaApertura;
        this.plazoMeses = plazoMeses;
        this.valor = valor;
        this.porcentajeInteres = porcentajeInteres;
    }

    public double calcularValorFinal() {
        double intereses = valor * (porcentajeInteres / 100) * plazoMeses;
        return valor + intereses;
    }

    // Getters y Setters

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public String getNumeroCDT() {
        return numeroCDT;
    }

    public void setNumeroCDT(String numeroCDT) {
        this.numeroCDT = numeroCDT;
    }

    public String getFechaApertura() {
        return fechaApertura;
    }

    public void setFechaApertura(String fechaApertura) {
        this.fechaApertura = fechaApertura;
    }

    public int getPlazoMeses() {
        return plazoMeses;
    }

    public void setPlazoMeses(int plazoMeses) {
        this.plazoMeses = plazoMeses;
    }

    public double getValor() {
        return valor;
    }

    public void setValor(double valor) {
        this.valor = valor;
    }

    public double getPorcentajeInteres() {
        return porcentajeInteres;
    }

    public void setPorcentajeInteres(double porcentajeInteres) {
        this.porcentajeInteres = porcentajeInteres;
    }
}
