#include <stdio.h>
#include <stdlib.h>

int main(void){
    short **pp;
    //pp = (short**) malloc(sizeof(short *));

    printf("%lu\n", sizeof(short));
    printf("%lu\n", sizeof(short *));
    printf("%lu\n", sizeof(char));
    printf("%lu\n", sizeof(char *));
    printf("%lu\n", sizeof(int));
    printf("%lu\n", sizeof(int *));
    printf("%lu\n", sizeof(double));
    printf("%lu\n", sizeof(double *));
    
    return 0;
} 