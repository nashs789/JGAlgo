import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def topology_sort():
    spend = [0 for _ in range(N + 1)]
    while queue:
        cur_node = queue.popleft()

        for linked_node in graph[cur_node]:
            indegree[linked_node] -= 1
        

for _ in range(T):
    N, K = map(int, input().strip().split())
    graph = [[] for _ in range(N + 1)]
    time = list(map(int, input().strip().split()))
    indegree = [0 for _ in range(K + 1)]
    queue = deque()

    for _ in range(K):
        X, Y = map(int, input().strip().split())

        graph[X].append(Y)
        indegree[Y] += 1

    target = int(input())

    for idx in range(1, N + 1):
        if indegree[idx] == 0:
            queue.append(idx)

    print("[==============]")
    print(graph)
    print(indegree)
    print(queue)
    print("[==============]")

    topology_sort()