import sys
from collections import deque

def bfs(srt):
    queue = deque()
    visited = [False] * (N + 1)

    queue.append((srt, 0))    # node, dist
    visited[srt] = True

    while queue:
        cur_node, cur_dist = queue.popleft()

        if cur_dist == K:
            answer.append(cur_node)
            continue

        for linked_node in adj[cur_node]:
            if not visited[linked_node]:
                visited[linked_node] = True
                queue.append((linked_node, cur_dist + 1))

if __name__ == "__main__":
    N, M, K, X = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(N + 1)] 
    answer = []

    for _ in range(M):
        srt, end = map(int, sys.stdin.readline().split())

        adj[srt].append(end)
    
    bfs(X)

    answer.sort()
    
    if len(answer) == 0:
        print(-1)
        sys.exit()

    for node in answer:
        print(node)