
import heapq
import sys
import math
givenNum = int(sys.stdin.readline())

heap = []

maxNum = math.inf

for i in range(givenNum) : 
    A = int(sys.stdin.readline()) # 
    heapq.heappush(heap, A)
    maxNum = min(maxNum, A) # 10
    while True :
        half = (heap[0] + maxNum) // 2 # 6
        if A <= half : # -99 >= 6
            print(heap[0])
            break
        else :
            heapq.heappop(heap)
            maxNum = A
