import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())

graph = [[] for x in range(N+1)]
visited = [False for x in range(N+1)]

for _ in range(N-1):
	x,y = map(int, input().split())
	graph[x].append(y)
	graph[y].append(x)

def dfs(root):
	global graph, visited
	for i in graph[root]:
		if not visited[i]:
			visited[i] = root
			dfs(i)

dfs(1)

for i in range(2,N+1):
	print(visited[i])