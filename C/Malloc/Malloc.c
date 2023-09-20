#include <stdio.h>
#include <stdlib.h>

int main(){
    int *pList = NULL;

    pList = malloc(sizeof(int) * 3);
    
    printf("%lu\n", sizeof(pList));
    pList[0] = 10;
    pList[1] = 20;
    pList[2] = 30;
    pList[4] = 40;

    *(((char*)pList) + 13) = 'A';
    printf("%d\n", pList[4]);

    free(pList);

    return 0;
} 