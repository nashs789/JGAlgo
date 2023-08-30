import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dp = [0]*(M+1)
bag = []
for i in range(1, N+1):
    V, C, K = map(int, input().split())
##비트마스크??
    while K > 0:
        cnt = min(i, K)
        bag.append((V*cnt, C*cnt))
        K -= i
        i *= 2
    print(bag)

for V, C in bag:
    for i in range(M, V-1, -1):
        dp[i] = max(dp[i], dp[i - V] + C)
    
    #print(dp)
print(dp[M])