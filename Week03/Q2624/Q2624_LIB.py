import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    k = int(input())
    dp = [0 for _ in range(T + 1)]
    dp[0] = 1

    for _ in range(k):
        coin, n = map(int, input().split())
        
        for won in range(T, 0, -1):
            for coin_count in range(1, n + 1):
                target = won - coin * coin_count

                if target < 0:
                    break
                
                dp[won] += dp[target]

    print(dp[T])