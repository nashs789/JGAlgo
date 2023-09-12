#include <stdio.h>

int main(void){
    char input_string[10];

    gets(input_string);

    printf("input = %s\n", input_string);
}