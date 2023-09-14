#include <stdio.h>
#include <stdlib.h>

int main(){
    void* p = malloc(4);

    printf("%p\n", p);
    printf("%p\n", (char*) p + 1);
    printf("%p\n", (char*) p + 2);
    printf("%p\n", (char*) p + 3);
    printf("%p\n", (int*) p + 1);
    printf("%p\n", (int*) p + 2);
    printf("%p\n", (int*) p + 3);
    printf("%p\n", (int*) p + 4);

    printf("%d\n", sizeof(p));
}