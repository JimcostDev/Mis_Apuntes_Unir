#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>

int main() {
  printf("Inicio Test\n");
  if (fork() == 0)
    printf("Yo soy el hijo\n");
  else
    printf("Yo soy el padre\n");
  return 0;
}