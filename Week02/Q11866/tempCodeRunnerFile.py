import sys
from collections import deque

A, B = map(int,sys.stdin.readline().split())

List = list() # 1 4 5 7
for i in range(1, A+1) : 
    List.append(i)


resultList = list()
B -= 1 # 2
while True :
    if len(List) == 0 :
        break
    
    resultList.append(List.pop(B)) # 3 6 2 len 4
    B += B # 4
    B = (B-1) % len(resultList) # 3
    
    
print("<" + ", ".join(map(str, resultList)) + ">")