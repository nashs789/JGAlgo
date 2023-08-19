import sys
import heapq

givenNum = int(sys.stdin.readline())

List = list()
for i in range(givenNum) :
    A = int(sys.stdin.readline()) * (-1)
    if A == 0 and len(List) == 0 :
        print(0)
    elif A == 0 and len(List) != 0 :
        print(heapq.heappop(List)*(-1))
    elif A != 0 :
        heapq.heappush(List, A)
    