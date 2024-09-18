package banco;
// clase abstracta que representa una cuenta bancaria genérica.
public abstract class Cuenta {
    protected Cliente cliente;
    protected String numeroCuenta;
    protected String fechaApertura;
    protected double saldo;
    protected double porcentajeInteres;

    public Cuenta(Cliente cliente, String numeroCuenta, String fechaApertura, double saldo, double porcentajeInteres) {
        this.cliente = cliente;
        this.numeroCuenta = numeroCuenta;
        this.fechaApertura = fechaApertura;
        this.saldo = saldo;
        this.porcentajeInteres = porcentajeInteres;
    }

    // Método abstracto para el cálculo de intereses
    public abstract void calcularInteresesMensuales();

    // Getters y Setters

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public String getNumeroCuenta() {
        return numeroCuenta;
    }

    public void setNumeroCuenta(String numeroCuenta) {
        this.numeroCuenta = numeroCuenta;
    }

    public String getFechaApertura() {
        return fechaApertura;
    }

    public void setFechaApertura(String fechaApertura) {
        this.fechaApertura = fechaApertura;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getPorcentajeInteres() {
        return porcentajeInteres;
    }

    public void setPorcentajeInteres(double porcentajeInteres) {
        this.porcentajeInteres = porcentajeInteres;
    }
}
