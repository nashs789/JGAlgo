#include <stdio.h>

int main(){
    int i_data;
    float f_data;

    scanf("%d", &i_data);
    scanf("%f", &f_data);

    printf("input: %d, %f\n", i_data, f_data);

    int num = 0;

    while(1){
        printf("input age: ");

        if(!scanf("%d", &num)){
            rewind(stdin);
            printf("[Enter]digit number!! \n");
        } else {
            if(num > 0 && num <= 130){
                break;
            } else {
                printf("Incorrect Age!! \n");
            }
        }
    }

    printf("your age: %d\n", num);

    return 0;
}