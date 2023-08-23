import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
dp = [10001] * (k + 1)
dp[0] = 0

for _ in range(n):
    coins.append(int(input()))

for coin in coins:
    for idx in range(coin, k + 1):
        dp[idx] = min(dp[idx], dp[idx - coin] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])