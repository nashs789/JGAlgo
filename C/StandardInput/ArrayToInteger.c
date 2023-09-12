#include <stdio.h>
#include <stdlib.h>

int ArrayToInteger(char string[]){
    int cnt = 0, num = 0;

    while(string[cnt] != 0){ // fgets 사용시 && string[cnt] != '\n' 추가
        num = num * 10 + string[cnt++] - '0';
    }

    return num;
}

int main(){
    int first_num, second_num;
    char first_string[16], second_string[16];

    printf("input first number: ");
    gets(first_string);
    printf("second first number: ");
    gets(second_string);

    first_num = atoi(first_string); //ArrayToInteger(first_string);
    second_num = atoi(second_string); //ArrayToInteger(second_string);

    printf("%d + %d = %d\n", first_num, second_num, first_num + second_num);

    return 0; 
} 