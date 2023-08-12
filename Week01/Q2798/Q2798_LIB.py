# 숫자가 M과 같다면 바로 종료할 것
# 같은 숫자가 안나온다면 모든 조합 확인할 것
import sys

N, M = map(int, sys.stdin.readline().split())
card_list = list(map(int, sys.stdin.readline().split()))
visited = [False] * len(card_list)
comb = [0] * 3
gapMin = sys.maxsize
answer = 0

def backTracking(listIdx, combIdx):
    global gapMin
    global answer

    if combIdx == 3:
        sumCom = sum(comb)
        gap = M - sumCom

        if gap == 0:
            print(M)
            sys.exit()

        if M > sumCom and gapMin > abs(gap):
            gapMin = abs(gap)
            answer = sumCom

        return

    for idx in range(listIdx, len(card_list)):
        if not visited[idx]:
            visited[idx] = True
            comb[combIdx] = card_list[idx]
            backTracking(listIdx + 1, combIdx + 1)
            visited[idx] = False
        

backTracking(0, 0)
print(answer)