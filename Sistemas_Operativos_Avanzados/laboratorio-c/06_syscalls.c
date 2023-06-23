#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
  int i, fd, vector[10];
  ssize_t leidos;
  int dato;

  fd = creat("prueba", 0600);
  for (i = 0; i < 10; i++)
    vector[i] = i;
  write(fd, vector, sizeof(vector));
  close(fd);

  fd = open("prueba", O_RDONLY);
  while ((leidos = read(fd, &dato, sizeof(int))) > 0) {
    printf("leido el número %d\n", dato);
  }
  close(fd);
  return 0;
}
