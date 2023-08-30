import heapq
import sys


input_ = sys.stdin.readline

n = int(input_())
array = []
for _ in range(n):
    deadline, num = map(int, input_().split())
    array.append((deadline, num))

array.sort()
print(array)
q = []
for deadline, num in array:
    heapq.heappush(q, num)
    #print(q)
    #print(len(q))
    # 힙 안의 작업 개수가 마감 기한보다 크다면,
    # 가장 작은 'num' 값을 가진 작업을 힙에서 제거합니다.
    if len(q) > deadline:
        heapq.heappop(q)
    #print(q)

print(sum(q))