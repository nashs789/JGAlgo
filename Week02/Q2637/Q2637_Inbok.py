import sys
from collections import deque

def topology_sort():
    while queue:
        cur_node = queue.popleft()

        for linked_node, pieces in adj[cur_node]:
            indegree[linked_node] -= 1

            if len(parts[cur_node]) == 0:
                parts[linked_node][cur_node] = pieces
            else:
                for key in parts[cur_node]:
                    if key in parts[linked_node]:
                        parts[linked_node][key] += parts[cur_node][key] * pieces
                    else:
                        parts[linked_node][key] = parts[cur_node][key] * pieces

            if indegree[linked_node] == 0:
                queue.append(linked_node)

if __name__ == "__main__":
    input = sys.stdin.readline
    queue = deque()
    N = int(input())
    M = int(input())

    parts = [{} for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    adj = [[] for _ in range(N + 1)]

    for _ in range(M):
        X, Y, K = map(int, input().split())

        adj[Y].append((X, K))
        indegree[X] += 1

    for node in range(1, N):
        if indegree[node] == 0:
            queue.append(node)

    topology_sort()

    for key in sorted(parts[N].keys()):
        print(key, parts[N][key])