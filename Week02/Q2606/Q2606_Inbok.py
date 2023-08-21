import sys
from collections import deque

def bfs():
    queue = deque()

    queue.append(1)
    visited[1] = True
    cnt = -1

    while len(queue) != 0:
        cur_node = queue.popleft()
        cnt += 1

        for linked_node in adj[cur_node]:
            if not visited[linked_node]:
                visited[linked_node] = True
                queue.append(linked_node)

    print(cnt)

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    adj = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)

    for _ in range(M):
        srt, end = map(int, sys.stdin.readline().split())
        
        adj[srt].append(end)
        adj[end].append(srt)

    bfs()