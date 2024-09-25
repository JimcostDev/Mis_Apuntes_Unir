package banco;

public class CuentaCorriente extends Cuenta {
    private double valorSobregiro;

    public CuentaCorriente(Cliente cliente, String numeroCuenta, String fechaApertura, double saldo, double porcentajeInteres, double valorSobregiro) {
        super(cliente, numeroCuenta, fechaApertura, saldo, porcentajeInteres);
        this.valorSobregiro = valorSobregiro;
    }

    @Override
    public void calcularInteresesMensuales() {
        if (saldo > 0) {
            double intereses = saldo * (porcentajeInteres / 100);
            saldo += intereses;
        }
    }

    public double getValorSobregiro() {
        return valorSobregiro;
    }

    public void setValorSobregiro(double valorSobregiro) {
        this.valorSobregiro = valorSobregiro;
    }
}
