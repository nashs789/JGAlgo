import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = []
    dp = [0] * (k + 1)
    dp[0] = 1

    for _ in range(n):
        coins.append(int(input()))

    for coin in coins:
        for idx in range(coin, k + 1):
            if idx - coin >= 0:
                dp[idx] += dp[idx - coin]

    print(dp[k])