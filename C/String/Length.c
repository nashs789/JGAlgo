#include <stdio.h>
#include <string.h>

int GetStringLength(char data[]){
    int count = 0;
    
    while(data[count]){
        count++;
    }

    return count;
}

int main(void){
    int data_length;
    char data[10] = "Happy!!";
    data_length = GetStringLength(data);

    printf("data length = %d\n", data_length);
    printf("data length = %lu\n", strlen(data));
}