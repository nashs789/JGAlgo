import sys
from collections import deque

givenNum = int(sys.stdin.readline())

List = deque()

for i in reversed(range(1,givenNum+1)) :
    List.append(i)


for i in range(givenNum-1) :
    List.pop()
    List.appendleft(List.pop())
    
print(List[0])