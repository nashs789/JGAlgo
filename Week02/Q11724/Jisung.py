import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
visited = [False] * (N+1)
graph = [ [] for x in range(N+1)]

for i in range(M):
	u,v = map(int,input().split())
	graph[u].append(v)
	graph[v].append(u)

cycle = 0
# def bfs(v):
# 	queue = deque()
# 	queue.append(v)
# 	visited[v] = True
# 	while queue:
# 		k = queue.popleft()
# 		for i in graph[k]:
# 			if not visited[i]:
# 				queue.append(i)
# 				visited[i] = True

def dfs(v):
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			dfs(i)

for i in range(1,1+N):
	if not visited[i]:
		dfs(i)
		cycle += 1
print(cycle)