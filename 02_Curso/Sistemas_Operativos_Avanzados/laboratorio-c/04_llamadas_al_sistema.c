#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
  int i, fd;
  fd = creat("prueba", 0600);
  if (fd == -1) {
    perror("Error al abrir el archivo");
    return 1;
  }
  for (i = 0; i < 10; i++) {
    if (write(fd, &i, sizeof(i)) == -1) {
      perror("Error al escribir en el archivo");
      return 1;
    }
  }
  close(fd);
  return 0;
}
