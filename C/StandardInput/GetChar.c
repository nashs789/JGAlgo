#include <stdio.h> 

#define GET_CHAR() getchar(); \
                   rewind(stdin);

int main(void){
    int input_data;

    // getchar();를 한 번 더 호출해서 \n를 제거해주는 용도 (표준입력버퍼에서)
    // 하지만 한 번에 여러개 입력되면 막을 수 없다.
    // 따라서 rewind를 호출해서 버퍼의 모든 입력 값을 제거한다.

    input_data = GET_CHAR();
    printf("input: %c\n", input_data);
    input_data = GET_CHAR();
    printf("input: %c\n", input_data);
}