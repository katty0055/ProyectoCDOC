#include <stdio.h>
/**
* @name division Divide como enteros los parámetros recibidos
* @param a Dividendo a utilizar, tipo int
* @param b Divisor a utilizar, tipo int
* @return División entera entre a y b
* @error Si el divisor es cero, hay error y se retorna 0
**/
int division(int a, int b) {
 if (b == 0) {
 printf(“Error de division entre cero”);
 return 0;
 } else {
 return a / b;
 }
}
/**
* @name main Programa principal
* @param argc Cantidad de parámetros recibidos
* @param argv Valores de parámetros recibidos
* @return void
* @extra Programa principal que calcula la división e imprime su resultado
en pantalla
**/
void main(int argc, char* argv) {
printf(“El resultado de la división es %d\n”, division(4,2));
}