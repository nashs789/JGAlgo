#include <stdio.h>
#include <string.h>

int main(void){
    // 문자형 정수를 정수로 변경하고 싶다면 아스키코드 '0'으로 빼준다.
    int pos_num = 100, num = 0, i, temp_num;
    char num_string[4] = "123";

    for(i = 0; i < 3; i++){
        temp_num = num_string[i] - '0';

        num += temp_num * pos_num;
        pos_num /= 10;
    }

    printf("%s -> %d\n", num_string, num);

    // m: my
    int answer = 0;
    char m_num[5] = "1234";
    unsigned char len = strlen(m_num);

    for(i = 0; i < len; i++){
        answer = answer * 10 + (m_num[i] - '0');
    }

    printf("%s -> %d\n", m_num, answer);

    return 0;
} 