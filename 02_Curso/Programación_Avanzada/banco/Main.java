package banco;

public class Main {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("123456789", "Ronaldo Jiménez", "rj@mail.com", "987654321", "Calle Falsa 123");

        // Cuenta de Ahorros
        CuentaAhorros cuentaAhorros = new CuentaAhorros(cliente, "AHO123", "2024-01-01", 1000.0, 1.5);
        cuentaAhorros.calcularInteresesMensuales();
        System.out.println("Saldo Cuenta de Ahorros: " + cuentaAhorros.getSaldo());

        // Cuenta Corriente
        CuentaCorriente cuentaCorriente = new CuentaCorriente(cliente, "COR123", "2024-01-01", 5000.0, 1.0, 500.0);
        cuentaCorriente.calcularInteresesMensuales();
        System.out.println("Saldo Cuenta Corriente: " + cuentaCorriente.getSaldo());

        // CDT
        CDT cdt = new CDT(cliente, "CDT123", "2024-01-01", 12, 5000.0, 2.0);
        double valorFinalCDT = cdt.calcularValorFinal();
        System.out.println("Valor final CDT: " + valorFinalCDT);

        // Tarjeta de Crédito
        TarjetaCredito tarjetaCredito = new TarjetaCredito(cliente, "TC123", "2024-01-01", "2025-01-01", 3.0, 10000.0, 5000.0);
        tarjetaCredito.calcularInteresesMensuales();
        System.out.println("Valor utilizado Tarjeta de Crédito: " + tarjetaCredito.getValorUtilizado());

        // Calcular intereses y mostrar el saldo actualizado
        cuentaAhorros.calcularInteresesMensuales();
        System.out.println("Saldo Cuenta de Ahorros después de calcular intereses: " + cuentaAhorros.getSaldo());

        // for para calcular intereses mensuales de la cuenta de ahorros
        System.out.println();
        for (int i = 0; i < 12; i++) {  // Simular 12 meses
            cuentaAhorros.calcularInteresesMensuales();
            System.out.println("Mes " + (i + 1) + " - Saldo: " + cuentaAhorros.getSaldo());
        }

        // mostar datos del cliente
        System.out.println();
        System.out.println("Datos del cliente: " + cliente.getNombre() + " - " + cliente.getCorreo());
        System.out.println("Dirección: " + cliente.getDireccion());
        System.out.println("Teléfono: " + cliente.getNumeroCelular());

    }
}
