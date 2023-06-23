#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
  int i, fd, vector[10];
  fd = creat("prueba", 0600);
  for (i = 0; i < 10; i++)
    vector[i] = i;
  write(fd, vector, sizeof(vector));
  close(fd);
  return 0;
}

