import sys
import heapq

givenNum = int(sys.stdin.readline())

List = list()
for i in range(givenNum) :
    A = int(sys.stdin.readline())
    if A == 0 and len(List) == 0 :
        print(0)
    elif A == 0 and len(List) != 0 :
        print(max(List))
        List.pop(List.index(max(List)))
    elif A != 0 :
        heapq.heappush(List, A)
    