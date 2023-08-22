import sys
from collections import deque

givenNum = int(sys.stdin.readline())

givenTF = sys.stdin.readline().strip()
visited = []
visited.append('0')
for i in range(len(givenTF)) :
    visited.append(givenTF[i])

for i in range(len(visited)) :
    if visited[i] == '0' :
        visited[i] = False 
    else :
        visited[i] = True

graph = [[] for _ in range(givenNum+1)]
for _ in range(givenNum-1) :
    A, B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

cnt = 0
def BFS(start) :
    global cnt
    q = deque()
    
    while q :
        tmp = q.popleft()
        for i in tmp :
            if visited[tmp] == False :
                cnt+= 1  
            else :
                visited[i] = True
                q.append(i)
            

print(visited)
print(graph)