import javax.swing.*;
import java.awt.*;

public class Hello extends JFrame {
    public Hello() {
        setTitle("Bienvenido a mi aplicación"); 
        setSize(300, 200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout());

        // Crear componentes
        JLabel lblNombre = new JLabel("Ingrese su nombre:");
        JTextField txtNombre = new JTextField(20);
        JButton btnSaludar = new JButton("Saludar");

        // Agregar componentes a la ventana
        add(lblNombre); add(txtNombre);
        add(btnSaludar); add(new JLabel()); // Espacio vacío

        // Crear listener para el botón
        btnSaludar.addActionListener(e -> {
            String nombre = txtNombre.getText();
            JOptionPane.showMessageDialog(this, "¡Hola, " + nombre + "!");
        });

        // hacer visible la ventana
        setVisible(true);
    }

    public static void main(String[] args) {
        new Hello();
    }
}