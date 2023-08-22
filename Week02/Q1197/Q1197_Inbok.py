import sys
import heapq

def search():
    visited = [False] * (V + 1)
    acc = 0
    cnt = 0

    pQueue = [(0, 1)]

    while V != cnt:
        dist, cur_node = heapq.heappop(pQueue)

        if visited[cur_node]:
            continue

        visited[cur_node] = True
        acc += dist
        cnt += 1

        for linked_node, next_dist in adj[cur_node]:
            heapq.heappush(pQueue, (next_dist, linked_node))

    print(acc)

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        x, y, c = map(int, sys.stdin.readline().split())

        adj[x].append((y, c))
        adj[y].append((x, c))

    search()