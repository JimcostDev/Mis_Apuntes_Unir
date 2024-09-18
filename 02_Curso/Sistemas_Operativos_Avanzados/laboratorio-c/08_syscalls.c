#include <stdio.h>
#include <unistd.h>

int main() {
  printf("Inicio Test\n");
  if (fork() == 0)
    printf("Yo soy el hijo\n");
  else
    printf("Yo soy el padre\n");

  int i, j;

  for (i = 0; i < 100; i++) {
    for (j = 0; j < 10000; j++)
      printf("Proceso padre, indice i=%d\n", i);
  }

  for (i = 0; i < 100; i++) {
    for (j = 0; j < 10000; j++)
      printf("Proceso hijo, indice i=%d\n", i);
  }

  return 0;
}
