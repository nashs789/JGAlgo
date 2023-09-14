#include <stdio.h>
#include <stdlib.h>

int main(void){
    short data = 0;
    int my_ptr = (int) &data;

    printf("%lu, %lu\n", sizeof(data), sizeof(my_ptr));
    printf("%p, %p\n", &data, my_ptr);
    printf("%X, %X\n", &data, my_ptr);

    short **pp;
    short *p;
    short data1 = 3;

    printf("===================\n");
    printf("pp = %X\n", &pp);
    printf("p = %X\n", &p);
    printf("data1 = %X\n", &data1);

    p = &data1;
    pp = &p;

    printf("pp = %X\n", pp);
    printf("*pp = %X\n", *pp);
    printf("*pp = %X\n", &**pp);
    printf("*pp = %d\n", **pp);

    short **a;
    a = (short**)malloc((sizeof(int*)));
    *a = (int*)malloc(sizeof(int));
    **a = 1234;

    printf("%d\n", **a);
    printf("%lu\n", sizeof(int*));

    return 0; 
}