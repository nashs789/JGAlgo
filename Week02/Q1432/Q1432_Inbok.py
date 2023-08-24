import sys
from heapq import heappop, heappush

def topology_sort():
    seq_node = N

    while queue:
        cur_node = heappop(queue)[1]
        seq[cur_node] = seq_node
        seq_node -= 1

        for linked_node in adj[cur_node]:
            in_degree[linked_node] -= 1

            if in_degree[linked_node] == 0:
                heappush(queue, (-linked_node, linked_node))

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    queue = []
    seq = [0 for _ in range(N + 1)]
    adj = [[] for _ in range(N + 1)]
    in_degree = [0 for _ in range(N + 1)]

    for idx in range(N):
        temp = list(input().strip("\n"))

        for node, val in enumerate(temp):
            if val == "1":
                adj[node + 1].append(idx + 1)
                in_degree[idx + 1] += 1

    for node in range(1, N + 1):
        if in_degree[node] == 0:
            heappush(queue, (-node, node))

    if len(queue) == 0:
        print(-1)
        sys.exit()

    topology_sort()
    
    for node in range(1, N + 1):
        print(seq[node], end=" ")