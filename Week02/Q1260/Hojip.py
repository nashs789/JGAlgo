import sys
from collections import deque
N, M, V = map(int,sys.stdin.readline().split())

givenGraph = [[] for _ in range(N+1)]

for i in range(M) :
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
    queue = deque([start])
    visit2[start] = True
    
    while queue :
        start = queue.popleft()
        print(start, end=" ")
        for i in givenGraph[start] :
            if visit2[i] == False :
                queue.append(i)
                visit2[i] = True


for i in givenGraph :
    i.sort()
    
visit = [False] * (N+1)
DFS(V)
print()

visit2 = [False] * (N+1)
BFS(V)
print()

