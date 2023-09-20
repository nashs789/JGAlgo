#include <stdio.h>
#include <arpa/inet.h>

void printBinaryIP(const struct in_addr *addr) {
    unsigned char *bytes = (unsigned char *)&(addr->s_addr);
    printf("Binary IP Address: ");
    for (int i = 0; i < 4; i++) {
        printf("%02X", bytes[i]); // 2자리 16진수로 출력
        if (i < 3) {
            printf(":"); // 바이트 사이에 콜론으로 구분
        }
    }
    printf("\n");
}

int main() {
    const char *ip_address = "192.168.1.1";
    struct in_addr addr;

    int result = inet_pton(AF_INET, ip_address, &addr);
    if (result == 1) {
        printBinaryIP(&addr);
    } else if (result == 0) {
        printf("Invalid IP Address Format\n");
    } else {
        perror("inet_pton");
    }

    return 0;
}
