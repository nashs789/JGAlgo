#include <stdio.h> 

void Sum(int, int);
extern int result;

int main(void){
    Sum(5, 3);
    printf("5 + 3 = %d\n", result);
}