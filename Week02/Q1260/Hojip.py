import sys
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())

givenGraph = [[] for _ in range(N+1)]

for i in range(N+1) :
    A, B = map(int,sys.stdin.readline().split())
    givenGraph[A].append(B)
    givenGraph[B].append(A)


def DFS(start) :
    visit[start] = True
    print(start, end=" ")
    
    for i in givenGraph[start] :
        if visit[i] == False :
            DFS(i)

def BFS(start) :
    q

for i in givenGraph :
    i.sort()
    
visit = [False] * (N+1)
DFS(V)
print()

