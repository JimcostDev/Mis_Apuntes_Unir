#include <stdio.h>

enum champions
{
  real_madrid = 14, 
  milan = 7, 
  liverpool = 6, 
  bayern_munich = 6, 
  barcelona = 5,
} quantity;

int main(){
  quantity = liverpool;
  printf("Liverpool ha ganado: %d champions", quantity);
  return 0;
}