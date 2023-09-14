#include <stdio.h>
#include <stdlib.h>

typedef unsigned char uch;

int main(void){
    uch *p_limit_table, **p; 
    int age, age_step, member, temp, sum;

    printf("20대부터 시작해서 연령층이 몇 개인가요? : ");
    scanf("%d", &age_step);

    p_limit_table = (uch *) malloc(age_step);
    p = (uch *) malloc(sizeof(uch *) * age_step);

    for(age = 0; age < age_step; age++){
        printf("\n%d0대 연령의 윗몸 일으키기 횟수\n", age + 2);
        printf("이 연령대는 몇 명입니까? : ");
        scanf("%d", &temp);

        *(p_limit_table + age) = temp; // (uch) temp;
        *(p + age) = (uch *) malloc(temp);

        for(member = 0; member < *(p_limit_table + age); member++){
            printf("%dth : ", member + 1);
            scanf("%d", &temp);
            *(*(p + age) + member) = (uch) temp;
        }
    }

    printf("\n\n 연령별 평균 윗몸 일으키기 횟수\n");

    for(age = 0; age < age_step; age++){
        sum = 0;

        printf("%d0대", age + 2);

        for(member = 0; member < *(p_limit_table + age); member++){
            sum += *(*(p + age) + member);
        }

        printf("%5.2f\n", (double) sum / *(p_limit_table + age));
    }   

    free(p);
    free(p_limit_table);

    return 0;
}