#include <stdio.h>
#include <stdlib.h>

typedef unsigned char uch;

int main(void){
    uch limit_table[3], *p[3];
    int age, member, temp, sum;

    for(age = 0; age < 3; age++){
        printf("\n%d0대 연령의 윗몸 일으키기 횟수\n", age + 2);
        printf("이 연령대는 몇 명입니까? : ");
        scanf("%d", &temp);
        limit_table[age] = (uch) temp;
        
        p[age] = (uch *) malloc(limit_table[age]);

        for(member = 0; member < limit_table[age]; member++){
            printf("%dth : ", member + 1);
            scanf("%d", &temp);
            *(p[age] + member) = (uch) temp;
        }
    }

    printf("\n\n연령별 평균 윗몸 일으키기 횟수\n");

    for(age = 0; age < 3; age++){
        sum = 0;
        printf("%d0대: ", age + 2);
        
        for(member = 0; member < limit_table[age]; member++){
            sum += *(p[age] + member);
        }

        printf("%5.2f\n", (double) sum / limit_table[age]);
        free(p[age]);
    }

    return 0;
}