#include <stdio.h>

typedef unsigned short int us;
typedef int ARR[5];

int main(void){
    us a = 3;
    ARR b = {1, 2, 3, 4, 5};

    printf("%d\n", a);

    for(int i = 0; i < 5; i++){
        printf("%d\n", b[i]);
    }

    int *p[5];
    
    *(p + 0) = 1;
    *(p + 1) = 2;
    *(p + 2) = 3;
    *(p + 3) = 4;
    *(p + 4) = 5;

    for(int i = 0; i < 5; i++){
        printf("%d\n", *(p + i));
    }

    ARR *pp;

    printf("%d\n", pp[0]);
    printf("%d\n", pp[1]);
    printf("%d\n", pp[3]);
    printf("%d\n", pp[4]);
    printf("%d\n", pp[5]);

    // *(pp[0]) = 3;

    return 0;
}