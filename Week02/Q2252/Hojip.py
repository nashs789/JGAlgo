import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

givenList = [[] for _ in range(N+1)]

parents = [0] * (N+1)

for i in range(M) :
    A, B = map(int,sys.stdin.readline().split())
    givenList[A].append(B)
    parents[B] += 1

q = deque()
for i in range(1, N+1) :
    if parents[i] == 0 :
        q.append(i)

def BFS() :
    global q
    while q :
        cur = q.popleft() # 3
        print(cur) # 3
        for i in givenList[cur] : # 3
            parents[i] -= 1 # 부모가 하나 사라짐
            if parents[i] == 0 : # 
                q.append(i)

BFS()