#include <stdio.h>
#include <stdlib.h>

void GetMyData(int **q){
    *q = (int *)malloc(8);
}

int main(void){
    int *p;
    GetMyData(&p);
    *p = 5;

    printf("%d\n", *p);
    free(p);

    return 0;
}