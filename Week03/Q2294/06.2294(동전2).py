import sys

N,K = map(int,input().split())

sset = set() #같은 동전값 여러개 가능-> 중복제거
for _ in range(N):
    sset.add(int(input()))

#dp테이블 생성
INF = K+1
dp =[INF]*(K+1)
dp[0]=0

for coin in sset:
    for j in range(1,K+1):
        if j-coin>=0:
            dp[j] = min(dp[j],dp[j-coin]+1)

ans = dp[K]
if ans==INF:
    ans=-1
print(ans)