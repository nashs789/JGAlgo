import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def topology_sort():
    while queue:
        cur_node = queue.popleft()

        for linked_node in graph[cur_node]:
            indegree[linked_node] -= 1
            ans[linked_node] = max(ans[cur_node] + time[linked_node], ans[linked_node])

            if indegree[linked_node] == 0:
                queue.append(linked_node)
        

for _ in range(T):
    N, K = map(int, input().strip().split())
    time = [0] + list(map(int, input().strip().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    ans = [0 for _ in range(N + 1)]
    queue = deque()

    for _ in range(K):
        X, Y = map(int, input().strip().split())

        graph[X].append(Y)
        indegree[Y] += 1

    for idx in range(1, N + 1):
        if indegree[idx] == 0:
            queue.append(idx)
            ans[idx] = time[idx]

    topology_sort()
    target = int(input())
    print(ans[target])