import sys

t = int(sys.stdin.readline())
k = int(sys.stdin.readline())
coins = []
dp=[0]*(t+1)
dp[0]=1


for _ in range(k):
    p, n = map(int, input().split())
    coins.append((p,n))

for coin,cnt in coins:
    for money in range(t,0,-1):
        for i in range(1,cnt+1):
            if money-coin*i>=0:
                dp[money]+=dp[money-coin*i]

print(dp[t])
