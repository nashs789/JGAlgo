import sys
from collections import deque

N, M, K, X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
distance = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(M) :
    A, B = map(int,sys.stdin.readline().split())
    graph[A].append(B) # A에서 B로만 가는 단방향 간선

def bfs(start) :
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q :
        now = q.popleft()
        for i in graph[now] :
            if not visited[i] :
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] +1
                if distance[i] == K :
                    answer.append(i)
    if len(answer) == 0 :
        print(-1)
    else :
        answer.sort()
        for i in answer :
            print(i)
    
bfs(X)

