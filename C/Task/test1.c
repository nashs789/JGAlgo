#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAXLINE 10000

void parse_uri(char *uri, char *hostname, char *path, int *port) {
    // uri = "http://example.com/path/to/resource"
    char *pos = strstr(uri, "//");
    // uri = "//example.com/path/to/resource"

    *port = 80;
    pos = pos != NULL ? pos + 2 : uri;

    char *pos2 = strstr(pos, ":");
    printf("pos = %s\n", pos);
    printf("pos2 = %s\n", pos2);

    // sscanf 에서 %s는 '\0'을 구분으로 읽기 때문에 넣어줌
    if(pos2 != NULL) {
        *pos2 = '\0';                            // 1. pos, pos2를 ':' 기준으로 분리 hostname:port
        sscanf(pos, "%s", hostname);             // 2. pos: ':' 앞에 있는 hostname
        sscanf(pos2 + 1, "%d%s", port, path);    // 3. pos2: ':' 뒤에 있는 port번호, 그리고 뒤에 있는 path
    } else {
        pos2 = strstr(pos, "/");
        printf("pos2 = %s\n", pos2);
        
        if(pos2 != NULL) {
            sscanf(pos2, "%s", path);
            *pos2 = '\0';                        // 1. pos, pos2를 ':' 기준으로 분리 hostname/{path}
            sscanf(pos, "%s", hostname);         // 2. pos: '/' 앞에 있는 hostname
            //*pos2 = '/';                       // 3. pos2: '/'뒤에 있는 path
            //sscanf(pos2, "%s", path);
        } else {
            sscanf(pos, "%s", hostname);
        }
    }
    return;
}

int main(void){
    int port = 8000;
    //char uri[MAXLINE] = "http://localhost:8000/";
    char uri[MAXLINE] = "http://example.com/path/to/resource";
    char hostname[MAXLINE] = "localhost";
    char path[MAXLINE] = "/";

    parse_uri(uri, hostname, path, &port);
    printf("uri = %s\n", uri);
    printf("hostname = %s\n", hostname);
    printf("path = %s\n", path);
    printf("port = %d\n", port);

    return 0;
}