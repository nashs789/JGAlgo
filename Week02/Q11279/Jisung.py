import sys
#from collections import deque
import heapq as hq

input = sys.stdin.readline

N = int(input())
numbers = []

for i in range(N):
    temp = int(input())
    if temp == 0:
        if len(numbers)==0:
            print(0)
        else:
            print(-(hq.heappop(numbers)))
    else:
        hq.heappush(numbers, -temp)