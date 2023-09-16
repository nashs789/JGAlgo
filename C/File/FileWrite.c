#include <stdio.h>
#include <stdlib.h>

int main(void){
    FILE *fp = (FILE *) fopen("./example.txt", "w");
    // /User/inbok/fileopentest.txt
    int num;

    if(fp == NULL){
        printf("File open failed...");
        exit(1);
    }

    printf("데아터를 입력하세요 : ");
    scanf("%d", &num);

    fprintf(fp, "%d", num);
    fclose(fp);

    return 0;
}