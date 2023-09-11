#include <stdio.h>

typedef unsigned char uchar;

uchar SetBit(uchar dest_data, uchar bit_num){
    if(bit_num < 8){
        dest_data |= (0x01 << bit_num);
    }

    return dest_data;
}

int main(void){
    uchar lamp_state = 0x77;

    printf("%X -> ", lamp_state);

    lamp_state = SetBit(lamp_state, 3);

    printf("%X\n", lamp_state);
}