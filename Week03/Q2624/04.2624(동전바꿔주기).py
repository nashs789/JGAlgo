#모르겠어요

T = int(input())
K = int(input())
dp = [0] * (T+1)
dp[0] = 1

for _ in range(K):
    p, n = map(int, input().split())
    
    for i in range(T, -1, -1):
        j = 1
        while j <= n and i - p * j >= 0:
            dp[i] += dp[i- p * j]
            j+=1
print(dp[T])
