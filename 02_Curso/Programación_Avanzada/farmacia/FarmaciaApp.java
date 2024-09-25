import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class FarmaciaApp extends JFrame {
    private JTextField nombreMedicamentoField;
    private JComboBox<String> tipoMedicamentoComboBox;
    private JTextField cantidadField;
    private ButtonGroup distribuidorButtonGroup;
    private JRadioButton cofarmaButton, empsepharButton, cemefarButton;
    private JCheckBox principalCheckBox, secundariaCheckBox;
    private JButton confirmarButton, borrarButton;

    public FarmaciaApp() {
        super("Pedido de Medicamentos");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(480, 740);
        setLayout(new BorderLayout());

    
        // Panel principal para contener todo
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());

        // Panel superior con la imagen
        JPanel imagePanel = new JPanel(new FlowLayout(FlowLayout.CENTER));

        // Cargar la imagen y redimensionarla
        ImageIcon originalIcon = new ImageIcon("farmacia.jpg"); // Ruta de la imagen
        Image originalImage = originalIcon.getImage();
        Image scaledImage = originalImage.getScaledInstance(480, 200, Image.SCALE_SMOOTH); // Ajustar el tamaño 
        ImageIcon scaledIcon = new ImageIcon(scaledImage);
        JLabel imageLabel = new JLabel(scaledIcon);
        imagePanel.add(imageLabel);

        // Panel del título
        JPanel titlePanel = new JPanel();
        titlePanel.setLayout(new BorderLayout());
        JLabel titleLabel = new JLabel("CREAR PEDIDO", JLabel.CENTER);
        titleLabel.setFont(new Font("Arial", Font.BOLD, 24));
        titlePanel.add(titleLabel, BorderLayout.NORTH);

        // Subtítulo: Datos del medicamento
        JLabel datosMedicamentoLabel = new JLabel("DATOS DEL MEDICAMENTO", JLabel.LEFT);
        datosMedicamentoLabel.setFont(new Font("Arial", Font.BOLD, 18));

        // Panel para los datos del medicamento en un recuadro
        JPanel datosMedicamentoPanel = new JPanel();
        datosMedicamentoPanel.setLayout(new GridLayout(3, 2, 5, 5));
        datosMedicamentoPanel.setBorder(BorderFactory.createTitledBorder(""));

        JLabel nombreLabel = new JLabel("Nombre del medicamento:");
        nombreMedicamentoField = new JTextField(20);

        JLabel tipoLabel = new JLabel("Tipo de medicamento:");
        String[] tiposMedicamentos = { "Analgésico", "Analéptico", "Anestésico", "Antiácido", "Antidepresivo",
                "Antibiótico" };
        tipoMedicamentoComboBox = new JComboBox<>(tiposMedicamentos);

        JLabel cantidadLabel = new JLabel("Cantidad:");
        cantidadField = new JTextField(10);

        datosMedicamentoPanel.add(nombreLabel);
        datosMedicamentoPanel.add(nombreMedicamentoField);
        datosMedicamentoPanel.add(tipoLabel);
        datosMedicamentoPanel.add(tipoMedicamentoComboBox);
        datosMedicamentoPanel.add(cantidadLabel);
        datosMedicamentoPanel.add(cantidadField);

        // Subtítulo: Datos del distribuidor
        JLabel datosDistribuidorLabel = new JLabel("DATOS DEL DISTRIBUIDOR", JLabel.LEFT);
        datosDistribuidorLabel.setFont(new Font("Arial", Font.BOLD, 18));

        // Panel para los datos del distribuidor
        JPanel datosDistribuidorPanel = new JPanel();
        datosDistribuidorPanel.setLayout(new GridLayout(1, 2, 10, 10));
        datosDistribuidorPanel.setBorder(BorderFactory.createTitledBorder(""));

        // Columna 1: Distribuidor
        JPanel distribuidorPanel = new JPanel();
        distribuidorPanel.setLayout(new GridLayout(4, 1));
        distribuidorPanel.add(new JLabel("Distribuidor:"));
        cofarmaButton = new JRadioButton("Cofarma");
        empsepharButton = new JRadioButton("Empsephar");
        cemefarButton = new JRadioButton("Cemefar");
        distribuidorButtonGroup = new ButtonGroup();
        distribuidorButtonGroup.add(cofarmaButton);
        distribuidorButtonGroup.add(empsepharButton);
        distribuidorButtonGroup.add(cemefarButton);

        distribuidorPanel.add(cofarmaButton);
        distribuidorPanel.add(empsepharButton);
        distribuidorPanel.add(cemefarButton);

        // Columna 2: Sucursal
        JPanel sucursalPanel = new JPanel();
        sucursalPanel.setLayout(new GridLayout(3, 1));
        sucursalPanel.add(new JLabel("Sucursal:"));
        principalCheckBox = new JCheckBox("Principal");
        secundariaCheckBox = new JCheckBox("Secundaria");
        sucursalPanel.add(principalCheckBox);
        sucursalPanel.add(secundariaCheckBox);

        // Agregar las dos columnas al panel distribuidor
        datosDistribuidorPanel.add(distribuidorPanel);
        datosDistribuidorPanel.add(sucursalPanel);

        // Panel de botones
        JPanel buttonPanel = new JPanel();
        confirmarButton = new JButton("Confirmar");
        borrarButton = new JButton("Borrar");
        buttonPanel.add(confirmarButton);
        buttonPanel.add(borrarButton);

        // Agregar ActionListener al botón Confirmar
        confirmarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (validarDatos()) {
                    Pedido pedido = new Pedido(
                            nombreMedicamentoField.getText(),
                            (String) tipoMedicamentoComboBox.getSelectedItem(),
                            Integer.parseInt(cantidadField.getText()),
                            getDistribuidorSeleccionado(),
                            principalCheckBox.isSelected(),
                            secundariaCheckBox.isSelected());

                    // Mostrar el resumen usando getResumen
                    String resumen = pedido.getResumen();

                    JFrame resumenFrame = new JFrame("Resumen del Pedido");
                    resumenFrame.setSize(480, 200);
                    resumenFrame.setLayout(new BorderLayout()); // Cambiar a BorderLayout para más control

                    // Mostrar el resumen del pedido en la parte superior
                    JLabel resumenLabel = new JLabel(resumen);
                    resumenFrame.add(resumenLabel, BorderLayout.CENTER);

                    // Crear un panel para los botones y ajustar su tamaño
                    JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 10, 10)); // Botones centrados
                    JButton cancelarButton = new JButton("Cancelar");
                    JButton enviarButton = new JButton("Enviar");

                    cancelarButton.addActionListener(e1 -> resumenFrame.dispose());
                    enviarButton.addActionListener(e1 -> {
                        JOptionPane.showMessageDialog(null, "Pedido enviado");
                        resumenFrame.dispose();
                    });

                    // Agregar los botones al panel de botones
                    buttonPanel.add(cancelarButton);
                    buttonPanel.add(enviarButton);

                    // Agregar el panel de botones a la parte inferior del frame
                    resumenFrame.add(buttonPanel, BorderLayout.SOUTH);

                    resumenFrame.setVisible(true);
                } else {
                    JOptionPane.showMessageDialog(null, "Por favor, complete todos los campos correctamente.");
                }
            }
        });

        // Agregar ActionListener al botón Borrar
        borrarButton.addActionListener(e -> {
            nombreMedicamentoField.setText("");
            tipoMedicamentoComboBox.setSelectedIndex(0);
            cantidadField.setText("");
            distribuidorButtonGroup.clearSelection();
            principalCheckBox.setSelected(false);
            secundariaCheckBox.setSelected(false);
        });

        // Agregar todo al panel principal
        mainPanel.add(imagePanel, BorderLayout.NORTH);
        mainPanel.add(titlePanel, BorderLayout.CENTER);

        // Panel central para subtítulos y secciones
        JPanel centerPanel = new JPanel();
        centerPanel.setLayout(new GridLayout(6, 1, 5, 5));
        centerPanel.add(datosMedicamentoLabel);
        centerPanel.add(datosMedicamentoPanel);
        centerPanel.add(datosDistribuidorLabel);
        centerPanel.add(datosDistribuidorPanel);

        mainPanel.add(centerPanel, BorderLayout.CENTER);
        mainPanel.add(buttonPanel, BorderLayout.SOUTH);

        add(mainPanel);
        setVisible(true);
    }

    // Método para validar los datos
    private boolean validarDatos() {
        String nombre = nombreMedicamentoField.getText();
        String cantidadStr = cantidadField.getText();
        if (nombre.isEmpty() || cantidadStr.isEmpty() || !cantidadStr.matches("\\d+")) {
            return false;
        }
        return true;
    }

    // Método para obtener el distribuidor seleccionado
    private String getDistribuidorSeleccionado() {
        if (cofarmaButton.isSelected()) {
            return "Cofarma";
        } else if (empsepharButton.isSelected()) {
            return "Empsephar";
        } else {
            return "Cemefar";
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new FarmaciaApp());
    }
}
