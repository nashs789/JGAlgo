import sys
from collections import deque

def bfs():
    queue = deque([])

    queue.append(V)
    visited[V] = True

    while len(queue) != 0:
        cur_node = queue.popleft()
        print(cur_node, end=" ")

        for linked_node in adj[cur_node]:
            if not visited[linked_node]:
                visited[linked_node] = True
                queue.append(linked_node)

def dfs(cur_node):
    print(cur_node, end=" ")
    visited[cur_node] = True

    for linked_node in adj[cur_node]:
        if not visited[linked_node]:
            dfs(linked_node)
                

if __name__ == "__main__":
    N, M, V = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        srt, end = map(int, sys.stdin.readline().split())
        
        adj[srt].append(end)
        adj[end].append(srt)

    for idx in range(N + 1):
        adj[idx].sort()

    visited = [False] * (N + 1)
    dfs(V)
    print()
    visited = [False] * (N + 1)
    bfs()