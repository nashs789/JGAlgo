
import sys
input = sys.stdin.readline

t = int(input())
k = int(input())

coin = []
dp =[0] * (t+1)
dp[0] = 1

for i in range(k):
    p, n = map(int, input().split())
    # 이걸 그래프로 풀어?
    # ??????????
    coin.append((p, n))

coin.sort()

# for문의 특성상 회전 횟수를 미리 정해줘야 할 거 같은데
# 코인의 개수를 입력 시 세서 정해주자.
for coin, cnt in coin:
    # 금액이 많은 순서 부터 1원까지 계산을 하겠다.
    for money in range(t, 0, -1):
        # 동전 개수 만큼 계산
        # 그니까 위꺼는 크기 순으로 먼저 계산을 하고
        # 그 다음으로 입력 받은 n만큰 계산을 해주겠다.
        for i in range(1, cnt+1):
            if money - coin * i >= 0:
                dp[money] += dp[money - coin * i]

print(dp[t])





