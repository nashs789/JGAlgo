import sys
from collections import deque

N,M,V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
	a,b = map(int, input().split())
	graph[a][b] = True
	graph[b][a] = True

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

# dfs는 깊이우선으로 재귀를 통해 모든 방법을 찾아 들어간다
def dfs(V):
	visited1[V] = True	# 찾으러 들어가기 전에 현재위치를 방문햇다고 표시
	print(V, end=" ")
	for i in range(1, N+1):
		if not visited1[i] and graph[V][i]:
			dfs(i)	# 들어갈 수 있는 모든 부분에 재귀로 들어가기

# bfs는 넓이우선으로 해당 노드에 대한 모든 자손을 넣고 그 자손에 대해 차례대로 밑으로 내려간다.
def bfs(V):
	q = deque([V])			# root를 프린트
	visited2[V] = True	
	while q:			# q에 들어있는 갯수만큼 while문
		V = q.popleft()		# 찾을 노드에 대해 프린트 및 팝
		print(V, end=" ")	
		for i in range(1,N+1):	# 자손 노드에 대해 연결되는 부분이 있는지 graph를 통해 탐색
			if not visited2[i] and graph[V][i]:
				q.append(i)
				visited2[i] = True	# q에 넣었으면 들어갔으니까 visited찍기

dfs(V)
print()
bfs(V)