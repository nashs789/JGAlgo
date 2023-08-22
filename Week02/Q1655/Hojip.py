
from collections import deque
import sys
import heapq
givenNum = int(sys.stdin.readline())

listLeft = []
listRight = []

for i in range(givenNum) : 
    A = int(sys.stdin.readline()) # 
    
    if len(listLeft) == len(listRight) :
        heapq.heappush(listLeft, (-A, A))
    else :
        heapq.heappush(listRight, (A, A))
        
    if listRight and listLeft[0][1] > listRight[0][1] : #최대힙 > #최소힙
        a, b = heapq.heappop(listLeft)[1], heapq.heappop(listRight)[1]
        heapq.heappush(listLeft, (-b, b))
        heapq.heappush(listRight, (a, a))
    
    print(listLeft[0][1])