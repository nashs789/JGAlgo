import sys

t = int(sys.stdin.readline())

for _ in range(t):

    n = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    dp = [0] * (m+1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, m+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[m])