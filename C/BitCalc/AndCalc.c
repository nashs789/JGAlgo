#include <stdio.h>

typedef unsigned char uchar;

uchar ResetBit(uchar dest_data, uchar bit_num){
    if(bit_num < 8){
        dest_data &= ~(0x01 << bit_num);
    }

    return dest_data;
}

uchar GetBit(uchar dest_data, uchar bit_num){
    uchar bit_state = 0;

    if(bit_num < 8) {
        bit_state = dest_data & (0x01 << bit_num);
        bit_state >>= bit_num;
    }

    return bit_state;
}

int main(){
    uchar lamp_state = 0x7F, bit_state;
    int i;
    
    printf("%X -> ", lamp_state);

    lamp_state = ResetBit(lamp_state, 3);

    printf("%X\n", lamp_state);

    lamp_state = 0x75;

    printf("%X -> ", lamp_state);

    for(int i = 0; i < 8; i++){
        bit_state = GetBit(lamp_state, 7 - i);
        printf("%d", bit_state);
    }
    printf("\n");
}