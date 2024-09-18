#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int i, j, fd;
    int dato;
    fd = open("prueba", O_RDONLY);
    if (fd == -1) {
        perror("Error al abrir el archivo");
        return 1;
    }

    if (fork() != 0) {
        while (read(fd, &dato, sizeof(int)) > 0) {
            for (j = 0; j < 100000; j++); /*espera*/
            printf("Proceso padre. Dato = %d\n", dato);
        }
    } else {
        while (read(fd, &dato, sizeof(int)) > 0) {
            for (j = 0; j < 100000; j++); /*espera*/
            printf("Proceso hijo. Dato = %d\n", dato);
        }
    }

    close(fd);
    return 0;
}
