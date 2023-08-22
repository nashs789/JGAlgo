import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

K = int(input())

def dfs(v, group):
    global graph, visited, is_error
    if is_error:
        return

    visited[v] = group
    for i in graph[v]:
        if not visited[i]:
            dfs(i, -group)
            if is_error:
                return
        elif visited[v] == visited[i]:
            is_error = True
            return

for _ in range(K):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    is_error = False
    for _ in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i,1)
    if is_error:
        print("NO")
    else:
        print("YES")