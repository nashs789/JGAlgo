import sys
sys.setrecursionlimit(2000 * 1000)

def sol(n, cnt):
    if dp[1] <= cnt or n < 1:
        return

    dp[n] = cnt
    cnt = cnt + 1

    if n % 3 == 0:
        sol(n // 3, cnt)
    
    if n % 2 == 0:
        sol(n // 2, cnt)
    
    sol(n - 1, cnt)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    dp = [sys.maxsize for _ in range(N + 1)]

    sol(N, 0)
    print(dp[1])