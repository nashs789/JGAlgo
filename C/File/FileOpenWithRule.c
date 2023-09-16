#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main(void){
    int fd; // 파일 디스크립터

    // 파일을 쓰기 전용으로 열고, 기존 파일 끝에 데이터를 추가
    fd = open("example.txt", O_CREAT | O_WRONLY | O_APPEND, S_IRUSR | S_IWUSR);

    if (fd == -1) {
        perror("파일 열기 실패");
        return 1;
    }

    // 파일 끝에 데이터를 추가
    const char *data = "추가할 데이터\n";
    ssize_t bytes_written = write(fd, data, strlen(data));

    if (bytes_written == -1) {
        perror("파일 쓰기 실패");
        close(fd);
        return 1;
    }

    printf("파일에 데이터 추가 완료.\n");

    // 파일 닫기
    close(fd);

    return 0;
}