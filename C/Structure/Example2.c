#include <stdio.h>

typedef struct {
    char name[12];
    unsigned short int age;
    float height;
    float weight;
} people;

int main(void){
    people p;
    p.age = 21;
    p.height = 178.3;

    printf("%lu\n", sizeof(p));
    printf("%hu\n", p.age);

    return 0;
}