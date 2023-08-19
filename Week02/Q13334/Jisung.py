import sys
from collections import deque
import heapq as hq

input = sys.stdin.readline

N = int(input().rstrip())
distance = []
road = [sorted(list(map(int,input().split()))) for x in range(N)]
d = int(input())

for h,o in road:
    if abs(o-h) <= d:
        hq.heappush(distance,(h,o))

distance.sort(key=lambda x:x[1])

hopeset = []
result = 0

for i in distance:
    if not hopeset:
        hq.heappush(hopeset, i)
    else:
        while hopeset[0][0] < i[1]-d:
            hq.heappop(hopeset)
            if not hopeset:
                break
        hq.heappush(hopeset,i)
    result = max(result, len(hopeset))
# 내가 생각한거
# - 뒷값을 기준으로 막대를 움직이다가 앞쪽값이 제일 작을때 빼준다.

# 찾은 정답
# - 비어있지않다면 제일 처음값이랑 들어올값의 범위를 비교한다.
# 그러면서 마지막 부분을 통해 하나씩 result값을 늘려나가다가 
# 시작하는 부분을 기준으로 이 범위를 벗어나게되면 벗어난 그 선로를 기준으로
# 그 선로의 시작점부터 다시 스택을 쌓는다.
print(result)