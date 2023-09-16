#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>

int main(void){
    FILE *fp = fopen("test.txt", "r");

    if(fp == NULL){
        perror("File Read Failed...");
        return 1;
    }

    char line[100];
    
    while(fgets(line, sizeof(line), fp) != NULL){
        printf("%s", line);
    }

    fclose(fp);
    
    return 0;
}