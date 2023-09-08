import sys
from collections import deque

def bfs(srt, end, weight):
    queue = deque()
    visited = [False] * (N + 1)
    
    queue.append((srt, 0))
    visited[srt] = True

    while queue:
        cur_node, cur_weight = queue.popleft()

        if cur_node == end:
            return True

        for linked_node, required_weight in adj[cur_node]:
            if not visited[linked_node] and required_weight >= weight:
                visited[linked_node] = True
                queue.append((linked_node, required_weight))            
    
    return False

if __name__ == "__main__":
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y, weight = map(int, input().split())

        adj[x].append((y, weight))
        adj[y].append((x, weight))

    srt, end = map(int, input().split())

    left, right = 1, 1000000000
    max_weight = 0

    while left <= right:
        mid = (left + right) // 2
        print(left, "    ", mid, "    ", right)

        if bfs(srt, end, mid):
            max_weight = max(mid, max_weight)
            left = mid + 1
        else:
            right = mid -1

    print(max_weight)