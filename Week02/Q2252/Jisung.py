import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    indegree[y] += 1



result = []
def topolgy_sort():
    q = deque()
    for idx in range(1, N+1) :
        if indegree[idx] == 0:
            q.append(idx)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

topolgy_sort()
print(' '.join(map(str,result)))