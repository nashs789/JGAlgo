import sys
from collections import deque

def bfs(node):
    queue = deque()

    queue.append(node)
    visited[node] = True

    while len(queue) != 0:
        cur_node = queue.popleft()

        for linked_node in adj[cur_node]:
            if not visited[linked_node]:
                visited[linked_node] = True
                queue.append(linked_node)

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        srt, end = map(int, sys.stdin.readline().split())

        adj[srt].append(end)
        adj[end].append(srt)
    
    cnt = 0

    for node in range(1, N + 1):
        if not visited[node]:
            bfs(node)
            cnt += 1

    print(cnt)