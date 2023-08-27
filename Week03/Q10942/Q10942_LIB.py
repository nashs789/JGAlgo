import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().strip().split()))
    M = int(input())
    dp = [[0 for _ in range(N)] for _ in range(N)]

    for len_N in range(N):
        for srt in range(N - len_N):
            end = srt + len_N

            if srt == end:    # 글자 수가 1개일 경우
                dp[srt][end] = 1
            elif arr[srt] == arr[end]:
                if srt + 1 == end:    # 문자열이 두 글자일 때 같다면
                    dp[srt][end] = 1
                elif dp[srt + 1][end - 1] == 1:
                    dp[srt][end] = 1

    for _ in range(M):
        S, E = map(int, input().split())

        print(dp[S - 1][E - 1])

    for a in dp:
        print(a)