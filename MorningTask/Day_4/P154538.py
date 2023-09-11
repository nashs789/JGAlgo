import sys
from collections import deque

def solution(x, y, n):
    isout = 0
    stack = deque([])
    stack.append([x,0])
    while stack and isout<1000000:
        temp = stack.popleft()
        if temp[0]==y:
            print(temp[1])
            return temp[1]
        stack.append([temp[0]+n,temp[1]+1])
        stack.append([temp[0]*2,temp[1]+1])
        stack.append([temp[0]*3,temp[1]+1])
        isout = temp[0]*2
    return -1