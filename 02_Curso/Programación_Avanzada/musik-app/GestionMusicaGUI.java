import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;

public class GestionMusicaGUI extends JFrame {
    private JTextField txtNombreAlbum, txtArtistaAlbum, txtTituloCancion, txtArtistaCancion, txtDuracion;
    private JButton btnCrearAlbum, btnAgregarCancion, btnListarCanciones;
    private JComboBox<String> comboAlbumes; // Para seleccionar un álbum
    private JTextArea areaResultados; // Área para mostrar las canciones
    private ArrayList<Album> albumes; // Lista de álbumes

    public GestionMusicaGUI() {
        albumes = new ArrayList<>(); // Inicializamos la lista de álbumes

        // Configuración de la ventana principal
        setTitle("Gestión de Música");
        setSize(600, 500);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(10, 2));

        // Componentes para crear un álbum
        JLabel lblNombreAlbum = new JLabel("Nombre del Álbum:");
        txtNombreAlbum = new JTextField();
        
        JLabel lblArtistaAlbum = new JLabel("Artista del Álbum:");
        txtArtistaAlbum = new JTextField();
        
        btnCrearAlbum = new JButton("Crear Álbum");

        // Componentes para agregar una canción a un álbum
        JLabel lblTituloCancion = new JLabel("Título de la Canción:");
        txtTituloCancion = new JTextField();
        
        JLabel lblArtistaCancion = new JLabel("Artista de la Canción:");
        txtArtistaCancion = new JTextField();
        
        JLabel lblDuracion = new JLabel("Duración (min):");
        txtDuracion = new JTextField();
        
        btnAgregarCancion = new JButton("Agregar Canción al Álbum");

        // Dropdown para seleccionar álbum
        JLabel lblAlbumes = new JLabel("Seleccionar Álbum:");
        comboAlbumes = new JComboBox<>();
        
        // Botón para listar canciones
        btnListarCanciones = new JButton("Listar Canciones del Álbum");

        // Área de resultados
        areaResultados = new JTextArea();
        areaResultados.setEditable(false); // No se puede editar
        
        // Añadimos los componentes a la ventana
        add(lblNombreAlbum); add(txtNombreAlbum);
        add(lblArtistaAlbum); add(txtArtistaAlbum);
        add(btnCrearAlbum); add(new JLabel()); // Espacio vacío

        add(lblTituloCancion); add(txtTituloCancion);
        add(lblArtistaCancion); add(txtArtistaCancion);
        add(lblDuracion); add(txtDuracion);
        add(lblAlbumes); add(comboAlbumes);
        
        add(btnAgregarCancion); add(btnListarCanciones);
        add(new JLabel("Canciones del Álbum:")); add(new JScrollPane(areaResultados));

        // Acción al crear un álbum
        btnCrearAlbum.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                crearAlbum();
            }
        });

        // Acción al agregar una canción a un álbum
        btnAgregarCancion.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                agregarCancionAlAlbum();
            }
        });

        // Acción al listar canciones del álbum
        btnListarCanciones.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                listarCanciones();
            }
        });

        setVisible(true); // Mostrar la ventana
    }

    // Método para crear un álbum
    private void crearAlbum() {
        String nombre = txtNombreAlbum.getText();
        String artista = txtArtistaAlbum.getText();
        if (!nombre.isEmpty() && !artista.isEmpty()) {
            Album album = new Album(nombre, artista);
            albumes.add(album);
            comboAlbumes.addItem(album.toString()); // Añadimos el álbum al combo box
            txtNombreAlbum.setText("");
            txtArtistaAlbum.setText("");
            areaResultados.setText("Álbum '" + nombre + "' creado exitosamente.\n");
        } else {
            JOptionPane.showMessageDialog(this, "Por favor, ingresa el nombre y el artista del álbum.");
        }
    }

    // Método para agregar una canción a un álbum
    private void agregarCancionAlAlbum() {
        if (comboAlbumes.getSelectedItem() == null) {
            JOptionPane.showMessageDialog(this, "Por favor, selecciona un álbum.");
            return;
        }

        String titulo = txtTituloCancion.getText();
        String artista = txtArtistaCancion.getText();
        double duracion;

        try {
            duracion = Double.parseDouble(txtDuracion.getText());
            if (!titulo.isEmpty() && !artista.isEmpty()) {
                Cancion nuevaCancion = new Cancion(titulo, artista, duracion);
                int albumIndex = comboAlbumes.getSelectedIndex();
                Album albumSeleccionado = albumes.get(albumIndex);
                albumSeleccionado.agregarCancion(nuevaCancion);
                areaResultados.setText("Canción '" + nuevaCancion.getTitulo() + "' agregada al álbum '" + albumSeleccionado.getNombre() + "'.\n");
                // Limpiar los campos
                txtTituloCancion.setText("");
                txtArtistaCancion.setText("");
                txtDuracion.setText("");
            } else {
                JOptionPane.showMessageDialog(this, "Por favor, ingresa el título y el artista de la canción.");
            }
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "La duración debe ser un número válido.");
        }
    }

    // Método para listar canciones de un álbum
    private void listarCanciones() {
        if (comboAlbumes.getSelectedItem() == null) {
            JOptionPane.showMessageDialog(this, "Por favor, selecciona un álbum.");
            return;
        }

        int albumIndex = comboAlbumes.getSelectedIndex();
        Album albumSeleccionado = albumes.get(albumIndex);

        areaResultados.setText("Canciones del álbum '" + albumSeleccionado.getNombre() + "':\n");
        for (Cancion cancion : albumSeleccionado.getCanciones()) {
            areaResultados.append(cancion.toString() + "\n");
        }
    }

    // Método principal para ejecutar el programa
    public static void main(String[] args) {
        new GestionMusicaGUI();
    }
}
