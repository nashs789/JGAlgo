import sys
from collections import deque

def bfs(node):
    queue = deque()

    queue.append(node)
    visited[node] = True
    is_ok = True
    blue.add(node)

    while len(queue) != 0:
        cur_node = queue.popleft()

        for linked_node in adj[cur_node]:
            if (cur_node in blue and linked_node in blue) or (cur_node in red and linked_node in red):
                is_ok = False
            
            if not visited[linked_node]:
                visited[linked_node] = True
                queue.append(linked_node)

                if cur_node in red:
                    blue.add(linked_node)
                else:
                    red.add(linked_node)
    
    return is_ok

if __name__ == "__main__":
    K = int(sys.stdin.readline())

    for _ in range(K):
        N, M = map(int, sys.stdin.readline().split())
        adj = [[] for _ in range(N + 1)]

        for _ in range(M):
            srt, end = map(int, sys.stdin.readline().split())

            adj[srt].append(end)
            adj[end].append(srt)
    
        visited = [False] * (N + 1)
        blue, red = set(), set()
        answer = True

        for node in range(1, N + 1):
            if not visited[node]:
                if not bfs(node):
                    answer = False

        if answer:
            print("YES")
        else:
            print("NO")