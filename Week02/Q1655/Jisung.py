import heapq
import sys
input = sys.stdin.readline

N = int(input())
left, right = [], []

for i in range(N):
    nums = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-nums, nums))
    else:
        heapq.heappush(right, (nums, nums))
    
    if right and left[0][1] > right[0][1]:
        a, b = heapq.heappop(left)[1], heapq.heappop(right)[1]
        heapq.heappush(left, (-b, b))
        heapq.heappush(right, (a, a))

    print(left[0][1])