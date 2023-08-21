import sys
from collections import deque

def DFS(start) :
    visited[start] = True
    
    for i in givenList[start] :
        if i == False :
            DFS(i)


K = int(sys.stdin.readline())
answer = [False] * K
for i in range(K) :
    V, E = map(int,sys.stdin.readline().split())
    givenList = [[] for _ in range(V+1)]
    for _ in range(E) :
        a, b = map(int,sys.stdin.readline().split())
        givenList[a].append(b)
        givenList[b].append(a)
    visited = [False] * (V+1)
    DFS(1)
    for j in range(1, len(visited)) :
        if visited[j] == False :
            answer[i] = False
            break

for i in range(len(answer)) :
    if answer[i] == False :
        print("NO")
    else :
        print("YES")