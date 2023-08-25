import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        coins = list(map(int, input().split()))
        M = int(input())
        dp = [0 for _ in range(M + 1)]
        dp[0] = 1

        for coin in coins:
            for won in range(M, 0, -1):
                dp[won] = 