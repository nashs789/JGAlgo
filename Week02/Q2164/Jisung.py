import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
q = deque([x for x in range(1,N+1)])
sign = True
temp = 0
for _ in range(2*N-3):
    if sign:
        q.popleft()
        sign = False
    else:
        temp = q.popleft()
        q.append(temp)
        sign = True
print(q[-1])
