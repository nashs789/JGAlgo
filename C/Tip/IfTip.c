#include <stdio.h>

int main(void){
    int A = 5;
    int B = 0;

    if(A == 5){
        A += 2;
    }

    printf("A = %d\n", A);

    A = 5;
    A = A + 2 * (A == 5);
    printf("A = %d\n", A);

    // ============================
    
    // case 1
    int step, i;

    for(step = 0; step < 2; step++){
        for(i = 0; i < 5; i++){
            printf("%d, ", i);    
        }
    }
    printf("\n");
    // case 2
    int count = 0;

    for(i = 0; i < 10; i++){
        if(count == 5){
            count = 0;
        }

        printf("%d, ",i % 5);
    }
    printf("\n");
    // case 3 - best
    for(i = 0; i < 10; i++){
        printf("%d, ",i % 5);
    }
    printf("\n");

    // ============================
    // case 1
    if (A != 0){
        // A가 참인경우
    }

    if(A){
        // A가 참인경우
    }

    // case 2
    if(!(A == 0 && B == 0)){

    }

    if(A != 0 || B != 0){

    }

    if(A || B){
        
    }
}