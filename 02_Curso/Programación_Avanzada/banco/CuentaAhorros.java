package banco;

public class CuentaAhorros extends Cuenta {

    public CuentaAhorros(Cliente cliente, String numeroCuenta, String fechaApertura, double saldo, double porcentajeInteres) {
        super(cliente, numeroCuenta, fechaApertura, saldo, porcentajeInteres);
    }

    @Override
    public void calcularInteresesMensuales() {
        double intereses = saldo * (porcentajeInteres / 100);
        saldo += intereses;
    }
}

