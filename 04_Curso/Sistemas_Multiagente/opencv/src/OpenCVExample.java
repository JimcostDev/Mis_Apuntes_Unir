import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.CvType;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.highgui.HighGui;

public class OpenCVExample {
    public static void main(String[] args) {
        // Cargar la biblioteca de OpenCV
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);

        // Crea una imagen en blanco (Mat de 400x400, tipo 8UC3 para color)
        Mat image = Mat.zeros(400, 400, CvType.CV_8UC3);

        // Dibujar un círculo en la imagen
        Imgproc.circle(image, new org.opencv.core.Point(200, 200), 100, new Scalar(0, 0, 255), -1);

        // Guardar la imagen en el sistema
        Imgcodecs.imwrite("output.jpg", image);

        // Mostrar la imagen en una ventana
        HighGui.imshow("Imagen de prueba", image);
        HighGui.waitKey();
    }
}
