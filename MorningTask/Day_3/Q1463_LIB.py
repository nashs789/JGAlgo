import sys

def sol(n, cnt):
    if dp[n] < cnt or n == 1:
        return
    
    dp[n] = cnt + 1

    if n % 3 == 0:
        sol(n // 3, cnt)
    elif n % 2 == 0:
        sol(n // 2, cnt)
    
    sol(n - 1, cnt)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    dp = [sys.maxsize for _ in range(N + 1)]

    sol(N, 0)
    print(dp)
    print(dp[1])