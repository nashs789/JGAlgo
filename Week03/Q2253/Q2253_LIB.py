import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    rocks = set()
    dp = [[sys.maxsize for _ in range(int((2 * N) ** 0.5) + 2)] for _ in range(N + 1)]
    dp[1][0] = 0

    for _ in range(M):
        rocks.add(int(input().strip()))

    for cur_rock in range(2, N + 1):
        if cur_rock in rocks:
            continue

        for speed in range(1, int((2 * cur_rock) ** 0.5) + 1):
            next_rock = dp[cur_rock - speed]
            dp[cur_rock][speed] = min(next_rock[speed - 1], next_rock[speed], next_rock[speed + 1]) + 1
        
    result = min(dp[N])

    if result == sys.maxsize:
        print(-1)
    else:
        print(result)